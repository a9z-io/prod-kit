# /prodkit.create diagram

## User Input

```text
$ARGUMENTS
```

If `$ARGUMENTS` is empty, ask the user to provide either:
- a path to an existing architecture/dataflow artifact file, or
- inline architecture/dataflow content to convert.

## Goal

Generate a Mermaid diagram artifact from architecture or dataflow source content and store the output in the same directory as the source artifact file.

## Supported Inputs

- Output files from `/prodkit.architecture`
- Output files from `/prodkit.dataflow` (canonical name)
- Inline content that clearly describes components/services and relationships

## Naming Note

- Canonical companion command name: `/prodkit.dataflow`
- Deprecated terminology: `/prodkit.dataflowdiagram` (migration alias only)

## Output Rules

1. Default output format: Markdown file containing a Mermaid fenced block.
2. Default output location: same directory as the source artifact.
3. Default output filename pattern:
   - `architecture-diagram.mmd.md` for architecture sources
   - `dataflow-diagram.mmd.md` for dataflow sources
4. If target filename already exists, do not overwrite silently; use deterministic suffixing:
   - `*-1.mmd.md`, `*-2.mmd.md`, etc.
5. Return the final output path on success.

## Mermaid Minimum Validity

A successful output MUST include:
- at least one node
- at least one edge between nodes
- syntactically valid Mermaid diagram block

## Error Handling

Return clear, actionable failures for:
- missing input
- unreadable source file
- empty or malformed source content
- ambiguous relationships that cannot be converted confidently
- unsupported source artifact type
- write-permission failure in target directory

On failure, do not report creation success and do not claim an output file was generated.

## Suggested Generation Flow

1. Identify source type (`architecture` or `dataflow`) and load content.
2. Extract entities/components/services and relationships.
3. Choose Mermaid diagram style (`flowchart TD` by default).
4. Generate Mermaid nodes and edges.
5. Validate minimum validity requirements.
6. Resolve output path in source directory with non-overwrite suffixing.
7. Write artifact and report absolute/relative output path.

## Usage Examples

- ` /prodkit.create diagram .specify/memory/architecture.md`
- ` /prodkit.create diagram .specify/memory/architecture/dataflow-order-processing.md`
- ` /prodkit.create diagram --from .specify/memory/architecture.md --name system-context`

## Post-Write Validation

After execution, confirm:
1. Output file exists in the same directory as the source artifact.
2. Mermaid block is present and valid.
3. At least one node and one edge are present.
4. Existing files were not silently overwritten.
