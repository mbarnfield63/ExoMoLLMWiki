# Frontmatter Schema

All compiled wiki notes use YAML frontmatter. Required fields vary by category, but every compiled note must include `tags`, `status`, `created`, `updated`, `sources`, and `source_count`.

## Source Notes

```yaml
Title: ""
Authors: []
DOI: ""
Journal: ""
Year: YYYY
ContentType:
  - "parsed-paper"
Created: YYYY-MM-DD
Processed: false
tags:
  - "source"
```

## Molecule Formula / MOC Notes

```yaml
tags:
  - "molecule"
formula: ""
atoms: []
parent_molecule: ""
exomol_id: ""
aliases: []
isotopologues: []
line_list: ""
marvel_data:
  is_marvelized: null
  latest_source_year: null
  energy_levels: null
associated_methods: []
applications: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
```

## Molecule Isotopologue Notes

```yaml
tags:
  - "molecule"
formula: ""
atoms: []
parent_molecule: ""
exomol_id: ""
aliases: []
line_list: ""
marvel_data:
  is_marvelized: false
  latest_source_year: null
  energy_levels: null
associated_methods: []
applications: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
```

## Method Notes

```yaml
tags:
  - "method"
developer_group: ""
software_type: ""
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
```

## Paper Notes

```yaml
tags:
  - "paper"
bibcode: ""
title: ""
authors: []
journal: ""
year: null
summary: ""
mentioned_methods: []
mentioned_molecules: []
mentioned_people: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
```

## Person Notes

```yaml
tags:
  - "person"
institution: ""
orcid: ""
primary_papers: []
secondary_papers: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
```

## Application Notes

```yaml
tags:
  - "application"
field: ""
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
```

## Log Notes

```yaml
tags:
  - "log"
created: YYYY-MM-DD
type: "ingest"
```

Allowed compiled tags are `molecule`, `method`, `paper`, `person`, `application`, and `log`.
