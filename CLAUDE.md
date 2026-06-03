# ExoMol LLM Wiki — Claude Operating Rules

## Project Purpose

This repository is a research-grade LLM Wiki for the ExoMol molecular spectroscopy database. It maintains a structured, source-traceable knowledge base by separating raw literature (`Raw/Sources/`) from compiled wiki notes (`Wiki/`). Every scientific claim must link back to a peer-reviewed source. No hallucination of cross-sections, partition functions, transitions, or citations is permitted.

## Key Files

| File / Dir | Purpose |
|---|---|
| `instructions.md` | Full project setup guide and build order |
| `AGENTS.md` | Strict behavioral rules for LLM agents operating on this vault |
| `Schema/frontmatter-schema.md` | YAML metadata templates for all 7 note types |
| `Schema/naming-conventions.md` | Predictable filename standards |
| `Schema/workflow-examples.md` | Ingest, query, and maintenance workflow patterns |
| `Schema/lint-checklist.md` | Pre-commit validation checklist |
| `_templates/` | Markdown blueprints for each note type |
| `scripts/wiki_tool.py` | Deterministic maintenance CLI (stdlib only) |
| `scripts/xml_elsevier.py` | Fetch Elsevier paper XML by DOI; writes `.json` sidecar to `Raw/Sources/` |
| `scripts/tex_arxiv.py` | Parse arXiv LaTeX submission dir into `Raw/Sources/<bibcode>.json` sidecar |
| `scripts/models.py` | Shared `PaperMetadata` Pydantic model used by both ingestion scripts |
| `Wiki/catalog.jsonl` | Master catalog — read before ingesting to prevent duplicates |
| `Raw/Sources/` | Pre-extracted paper sidecars (`.json`) and raw XML — read-only input for ingest |
| `Raw/Files/` | arXiv LaTeX submission directories (`<bibcode>_<molecule>/`) — gitignored |

## Operating Rules

### 1. Initialize
When the user says **"get up to speed"**, immediately read the Obsidian state file at:
`C:/Obsidian/Claude_State/ExoMol Wiki.md`, `AGENTS.md` and most recent commit to reconstruct full context.

### 2. Log & Save
When reaching a milestone or when the user says **"save state"**, overwrite the Obsidian state file (`C:/Obsidian/Claude_state/Quantum Number Prediction.md`) with a clean update (see Rule 3 format) and append a summary of work done to the log file (`C:/Obsidian/Logs/ExoMol Wiki Log.md`). Never change any other files within `C:/Obsidian/`.

### 3. Obsidian State File Format
When writing to `C:/Obsidian/Claude_State/ExoMol Wiki.md`, always overwrite with:

```
# ExoMol Wiki — Claude State

**Last Modified:** YYYY-MM-DD HH:MM

**Current Status:**
2–3 sentences on exactly where the code/wiki stands.

**Recent Wins:**
- What was just fixed or completed.

**Next Steps / Blockers:**
- Exactly what needs to be tackled next session.
```

### 4. /init Behavior
When asked to run `/init`, read in order:
1. The Obsidian state file (for recent context)
2. `instructions.md` (setup guide)
3. `AGENTS.md` (agent rules)
4. `Schema/frontmatter-schema.md` and `Schema/naming-conventions.md`

### 5. Agent Rules (from AGENTS.md)
- `Raw/Sources/` is read-only input — no summaries written there.
- Every `Wiki/` note must have strict markdown tracking links back to `Raw/Sources/`.
- Read `Wiki/catalog.jsonl` before parsing any paper to prevent duplicates.
- No hallucination of cross-sections, partition functions, transitions, or citations.
- **Prefer the `.json` sidecar over raw XML during ingest** — `Raw/Sources/<bibcode>.json` contains pre-extracted title, authors, abstract, and clean body prose (~45× fewer tokens than the raw XML). Only read the raw XML if the sidecar is absent or a specific value is missing.
- **No autonomous git commits** — stage changes with `git add`, then wait for human approval before committing.
- After any wiki changes, run: `python scripts/wiki_tool.py build`, then `lint`, then `source-scan --update --accept-covered`, then `source-lint`.

## Architecture Summary

```
Raw/
  Sources/       ← Pre-extracted .json sidecars + raw XML (read-only ingest input)
  Files/         ← arXiv LaTeX submission dirs, e.g. 26YuBaBo_CO2/ (gitignored)
Wiki/
  Molecules/     ← 91+ isotopologue pages (e.g. 1H2-16O.md)
  Methods/       ← ~30 computational tools and databases
  Papers/        ← Paper reference notes (bibcode filenames, e.g. 24TeYuZh.md)
  People/        ← Researcher notes
  Applications/  ← 15 use-case pages
  Logs/          ← Ingestion/maintenance event log
  catalog.jsonl  ← Master catalog of all wiki notes
  index.md       ← Top-level link index
Schema/          ← Frontmatter schemas, naming conventions, workflows
_templates/      ← Markdown blueprints for each note type
scripts/         ← Ingestion + maintenance tooling (xml_elsevier, tex_arxiv, wiki_tool)
.agents/skills/  ← LLM prompting payloads (ingest, query, lint, maintain)
```

## Note Naming Conventions

| Type | Pattern | Example |
|---|---|---|
| Molecule MOC | Formula | `H2O.md` |
| Isotopologue | exomol_id | `1H2-16O.md` |
| Method | PascalCase | `DVR3D.md` |
| Paper | bibcode | `24TeYuZh.md` |
| Person | Initials_Surname | `J_Tennyson.md` |
| Application | Title_Case_Underscores | `Exoplanet_Atmospheres.md` |
