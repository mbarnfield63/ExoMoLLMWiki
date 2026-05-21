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

## Molecule Notes

```yaml
tags:
  - "molecule"
formula: ""
exomol_id: ""
associated_methods: []
applications: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
aliases: []
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

## Person Notes

```yaml
tags:
  - "person"
institution: ""
orcid: ""
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

Allowed compiled tags are `molecule`, `method`, `person`, `application`, and `log`.
