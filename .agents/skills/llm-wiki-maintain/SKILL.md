# LLM Wiki Maintain

Use this skill during maintenance or literature ingestion rounds.

## Steps

1. Run `python scripts/wiki_tool.py source-delta`.
2. Inspect uncataloged or uncovered raw sources.
3. Search `Wiki/catalog.jsonl` before opening broad raw context.
4. Ingest new claims into structured notes with source links.
5. Rebuild indexes and source manifests.
6. Run lint and source-lint.
7. Summarize literature additions in a log note.

Keep raw literature untouched except for source metadata fields that deterministic tooling explicitly updates.
