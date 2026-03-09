from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CopyResult:
    src: Path
    dst: Path
    action: str  # copied | skipped | overwritten
    note: str = ""


def _overlay_root() -> Path:
    # Package data lives at src/prodkit/overlay/ in this repo and is included in builds.
    # Hidden directories (.specify, .claude) are stored without leading dots inside the
    # package (as specify/ and claude/) so setuptools doesn't silently exclude them.
    # The CLI maps them back to dot-prefixed names in the target repo.
    return Path(__file__).resolve().parent / "overlay"


def _pkg_src(rel_dst: Path) -> Path:
    """Convert a target-repo relative path (e.g. .specify/...) to its package-internal path.

    Hidden top-level dirs (.specify, .claude) are stored without the leading dot inside the
    package so setuptools doesn't silently exclude them during packaging.
    """
    parts = list(rel_dst.parts)
    # Strip the leading dot from the first component: .specify → specify, .claude → claude.
    parts[0] = parts[0].lstrip(".")
    return Path(*parts)


def _copy_file(src: Path, dst: Path, *, force: bool) -> CopyResult:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        if not force:
            return CopyResult(src=src, dst=dst, action="skipped", note="exists (use --force to overwrite)")
        shutil.copy2(src, dst)
        return CopyResult(src=src, dst=dst, action="overwritten")
    shutil.copy2(src, dst)
    return CopyResult(src=src, dst=dst, action="copied")


# Destination paths in the target repo (dot-prefixed).
def _rel_paths_required() -> list[Path]:
    return [
        Path(".specify/memory/constitution.md"),
        Path(".specify/templates/spec-template.md"),
        Path(".specify/templates/plan-template.md"),
        Path(".specify/templates/tasks-template.md"),
    ]


def _optional_dir_dst() -> Path:
    """Destination dir in the target repo for optional Claude command docs."""
    return Path(".claude/commands")


def _copy_tree(src_dir: Path, dst_dir: Path, *, force: bool) -> list[CopyResult]:
    results: list[CopyResult] = []
    for src in sorted(p for p in src_dir.rglob("*") if p.is_file()):
        rel = src.relative_to(src_dir)
        dst = dst_dir / rel
        results.append(_copy_file(src, dst, force=force))
    return results


def cmd_overlay(argv: list[str]) -> int:
    p = argparse.ArgumentParser(
        prog="prodkit overlay",
        description="Apply/upgrade the Prod‑Kit overlay files into a Spec‑Kit repo (current directory by default).",
    )
    p.add_argument(
        "--target",
        default=".",
        help="Target repository root (default: current directory).",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing overlay files (except constitution, see --force-constitution).",
    )
    p.add_argument(
        "--force-constitution",
        action="store_true",
        help="Also overwrite `.specify/memory/constitution.md` if it exists (DANGEROUS).",
    )
    p.add_argument(
        "--with-claude-commands",
        action="store_true",
        help="Also overlay `.claude/commands/*` guidance docs.",
    )
    args = p.parse_args(argv)

    overlay = _overlay_root()
    if not overlay.exists():
        print("ERROR: overlay data not found in installed package.", file=sys.stderr)
        return 2

    target = Path(args.target).expanduser().resolve()
    if not target.exists():
        print(f"ERROR: target path does not exist: {target}", file=sys.stderr)
        return 2

    results: list[CopyResult] = []

    for rel_dst in _rel_paths_required():
        # Source inside the package uses no leading dot.
        rel_src = _pkg_src(rel_dst)
        src = overlay / rel_src
        if not src.exists():
            print(f"ERROR: missing overlay file in package: {rel_src}", file=sys.stderr)
            return 2

        dst = target / rel_dst

        # Constitution is special: skip by default so users can merge manually.
        if rel_dst.as_posix() == ".specify/memory/constitution.md":
            force_constitution = bool(args.force_constitution)
            if dst.exists() and not force_constitution:
                results.append(
                    CopyResult(
                        src=src,
                        dst=dst,
                        action="skipped",
                        note="exists (merge manually; use --force-constitution to overwrite)",
                    )
                )
                continue
            results.append(_copy_file(src, dst, force=force_constitution))
            continue

        results.append(_copy_file(src, dst, force=bool(args.force)))

    if args.with_claude_commands:
        rel_dst_dir = _optional_dir_dst()
        rel_src_dir = _pkg_src(rel_dst_dir)
        src_dir = overlay / rel_src_dir
        if not src_dir.exists():
            print("ERROR: missing overlay directory in package: claude/commands", file=sys.stderr)
            return 2
        dst_dir = target / rel_dst_dir
        results.extend(_copy_tree(src_dir, dst_dir, force=bool(args.force)))

    copied = sum(1 for r in results if r.action in {"copied", "overwritten"})
    skipped = sum(1 for r in results if r.action == "skipped")

    print(f"Applied Prod‑Kit overlay to: {target}")
    print(f"- copied/updated: {copied}")
    print(f"- skipped: {skipped}")

    for r in results:
        if r.action == "skipped":
            print(f"SKIP {r.dst.relative_to(target)} ({r.note})")

    return 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in {"-h", "--help"}:
        print(
            "prodkit: Prod‑Kit overlay tooling\n\n"
            "Commands:\n"
            "  overlay    Apply/upgrade Prod‑Kit overlay files into a Spec‑Kit repo\n\n"
            "Run `prodkit <command> --help` for details.",
            file=sys.stdout,
        )
        return 0

    cmd, *rest = argv
    if cmd == "overlay":
        return cmd_overlay(rest)

    print(f"ERROR: unknown command: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
