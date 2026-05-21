# LLM Wiki Lint

Use this skill when validating generated wiki content.

## Checks

Run:

```bash
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-scan --update --accept-covered
python scripts/wiki_tool.py source-lint
```

Confirm that `source_count` equals the number of sources in each compiled note and that processed raw sources have downstream wiki coverage.
