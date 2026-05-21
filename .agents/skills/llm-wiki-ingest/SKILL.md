# LLM Wiki Ingest

Use this skill when converting parsed ExoMol literature from `Raw/Sources/` into structured notes under `Wiki/`.

## Steps

1. Search `Wiki/catalog.jsonl` for entities from the source before creating files.
2. Read only the relevant raw source files.
3. Create or update notes in `Wiki/Molecules/`, `Wiki/Methods/`, `Wiki/People/`, and `Wiki/Applications/`.
4. Add source paths to frontmatter `sources` and update `source_count`.
5. Include markdown source links in the note body for scientific claims.
6. Omit values not present in the raw text.
7. Run build and lint commands after editing.

Never write summaries into `Raw/Sources/`.
