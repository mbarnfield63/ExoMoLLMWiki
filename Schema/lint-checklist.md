# Lint Checklist

Use this checklist before committing generated wiki content.

- Each compiled note has YAML frontmatter.
- Each compiled note uses one allowed compiled tag: `molecule`, `method`, `person`, `application`, or `log`.
- `sources` is a list of repository-relative paths.
- `source_count` exactly equals the number of entries in `sources`.
- Each source path points to a file under `Raw/Sources/`.
- Body text includes markdown links back to raw source files for scientific claims.
- Raw source files are not edited with summaries or generated interpretation.
- No missing numerical values are invented.
- `Wiki/catalog.jsonl`, `Wiki/index.md`, and subfolder indexes are rebuilt after content changes.
- `Schema/source-manifest.jsonl` reflects current raw source coverage.
