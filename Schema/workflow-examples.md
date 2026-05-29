# Workflow Examples

## Ingest A Parsed Paper

1. Search `Wiki/catalog.jsonl` for existing entities mentioned in the paper.
2. Read the target file in `Raw/Sources/`.
3. Create or update category notes under `Wiki/`.
4. Add source links in frontmatter and body text for each compiled claim.
5. Rebuild the catalog and run lint checks.

## Query Existing Knowledge

1. Search `Wiki/catalog.jsonl` for the molecule, method, person, or application.
2. Open the matching wiki notes.
3. Follow source links back to `Raw/Sources/` only when exact provenance is needed.
4. Report only claims that can be traced to source links.

## Maintenance Round

1. Run source-delta to identify new raw sources.
2. Run source-coverage to inspect literature coverage.
3. Ingest only unprocessed or uncovered sources.
4. Rebuild indexes and manifests.
5. Verify the category overview pages and molecule MOCs still link correctly.
6. Record a concise log entry in `Wiki/Logs/` or `Wiki/log.md`.
