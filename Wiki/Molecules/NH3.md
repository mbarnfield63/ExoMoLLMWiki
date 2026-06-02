---
tags:
  - "molecule"
formula: "NH3"
atoms:
  - "N"
  - "H"
parent_molecule: ""
exomol_id: ""
aliases:
  - "ammonia"
isotopologues:
  - "14N-1H3"
  - "15N-1H3"
line_list: ""
marvel_data:
  is_marvelized: null
  latest_source_year: null
  energy_levels: null
associated_methods:
  - "ExoMol Database"
  - "MARVELization"
  - "ExoMolHR"
applications:
  - "Exoplanet Atmospheres"
  - "Plasma Modelling"
status: "seed"
created: "2026-05-29"
updated: "2026-05-29"
sources:
  - "Raw/Sources/24TeYuZh.json"
source_count: 1
---

# NH3

This formula-level MOC records molecule-level line-list coverage mentioned in the 2024 ExoMol release and keeps named isotopologues in separate files. Source: [24TeYuZh](../../Raw/Sources/24TeYuZh.json).

## Recommended Datasets

| Molecule entry | Dataset | Isotopologues counted | T max | N elec | N lines | MARVEL | Reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NH3 | CoYuTe | 1 | 1500 | 1 | 16,941,637,250 | yes | [349] Source: [Raw/Sources/24TeYuZh.json](Raw/Sources/24TeYuZh.json) Table 1 |
| 15NH3 | CoYuTe-15 | 1 | 1000 | 1 | 929,795,249 |  | [371] Source: [Raw/Sources/24TeYuZh.json](Raw/Sources/24TeYuZh.json) Table 1 |

## Named Isotopologues

| Isotopologue | Line list | MARVEL | ExoMolHR | Evidence |
| --- | --- | --- | --- | --- |
| [14N-1H3](14N-1H3.md) | CoYuTe |  | yes | Listed explicitly in the ExoMolHR contents table. |
| [15N-1H3](15N-1H3.md) | CoYuTe-15 |  |  | Listed in Table 1 as the 15NH3 CoYuTe-15 line list. |
