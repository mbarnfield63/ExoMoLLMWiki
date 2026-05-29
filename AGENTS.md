# ExoMol LLM Wiki Agent Guide

This repository is a structured knowledge base for the ExoMol project. Agents must keep raw source literature separate from compiled wiki knowledge and preserve traceability for every scientific claim.

## Operating Rules

1. Treat `Raw/Sources/` purely as raw source literature. Do not write summaries, annotations, or compiled interpretation directly inside raw source files.
2. Every note generated inside `Wiki/` must include strict markdown tracking links back to one or more files in `Raw/Sources/`.
3. Read `Wiki/catalog.jsonl` before parsing new papers to locate existing molecules, methods, people, or applications and prevent duplicate files.
4. Do not hallucinate cross-sections, partition functions, transition frequencies, author citations, molecules, methods, or identifiers. If a value is missing from the raw text, omit it or mark the field empty.

## Workflow

Search the catalog first, then open only the raw source files required for the task. Compile concise structured notes into the relevant `Wiki/` category and link each claim to source markdown paths.

After generating or updating wiki notes, run the deterministic tooling:

```bash
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-scan --update --accept-covered
python scripts/wiki_tool.py source-lint
```

## Source Tracking

Use repository-relative links for source references, for example:

```markdown
- Source: [Tennyson 2012 sample](../../Raw/Sources/tennyson2012-sample.md)
```

Each wiki note frontmatter must keep `sources` and `source_count` synchronized. The `source_count` value must exactly equal the number of entries in `sources`.

## Category Boundaries

- `Wiki/Molecules/`: molecules, isotopologues, line lists, states, transitions, and molecular metadata.
- `Wiki/Methods/`: software, algorithms, ab initio methods, variational calculations, MARVEL, R-matrix, and related workflows.
- `Wiki/People/`: researchers, authors, collaborators, institutions, and identifiers.
- `Wiki/Applications/`: use cases such as exoplanet atmospheres, cool stars, astrochemistry, and diagnostics.
- `Wiki/Logs/`: automated run summaries and ingestion records.

Raw PDF files or heavy data products belong under ignored local storage, not in committed wiki notes.

## Molecule & Isotopologue Rules
- **Atomic Files:** Every unique isotopologue MUST get its own separate markdown file in `Wiki/Molecules/` named after its `exomol_id` (e.g., `1H2-16O.md`). Do NOT combine multiple isotopologues into one file.
- **Parent Hierarchy:** Use the `parent_molecule` field to group isotopologues. For example, `1H2-16O` and `1H-2H-16O` (HDO) both have the parent_molecule `"H2O"`.
- **Aliases:** If an isotopologue has common structural names (like `D2O` or `Heavy Water`), put them in the `aliases` array. 
- **MARVELization:** If a paper explicitly states a molecule has been evaluated using the MARVEL algorithm, set `is_marvelized: true`. Extract the number of validated `energy_levels` and the `latest_source_year` included in that specific MARVEL study. If this data is missing, leave them as `null`. Do not guess.

## Git & Commit Protocol
- **NO AUTONOMOUS COMMITS:** You are strictly forbidden from running `git commit` or `git push` autonomously.
- **Human Approval Required:** After you have created/updated files, run the linting scripts, and successfully staged the files using `git add`, you MUST stop and ask the human user for permission to commit. 
- **Present the Summary:** When asking for permission, present a short, bulleted summary of exactly which files were changed and what data was extracted.