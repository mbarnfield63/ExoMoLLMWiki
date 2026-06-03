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
updated: "2026-06-03"
sources:
  - "Raw/Sources/24TeYuZh.json"
  - "Raw/Sources/24YuBoBr.json"
source_count: 2
---

# NH3

This formula-level MOC records molecule-level line-list coverage for NH₃ and keeps named isotopologues in separate files. Sources: [24TeYuZh](../../Raw/Sources/24TeYuZh.json), [24YuBoBr](../../Raw/Sources/24YuBoBr.json).

## Recommended Datasets

| Molecule entry | Dataset | Isotopologues counted | T max | N elec | N lines | MARVEL | Reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NH3 | CoYuTe | 1 | 1500 | 1 | 16,941,637,250 | yes | [349] Source: [Raw/Sources/24TeYuZh.json](Raw/Sources/24TeYuZh.json) Table 1 |
| 15NH3 | CoYuTe-15 | 1 | 1000 | 1 | 929,795,249 | yes | [24YuBoBr](../Papers/24YuBoBr.md) |

## Named Isotopologues

| Isotopologue | Line list | MARVEL | ExoMolHR | Evidence |
| --- | --- | --- | --- | --- |
| [14N-1H3](14N-1H3.md) | CoYuTe |  | yes | Listed explicitly in the ExoMolHR contents table. |
| [15N-1H3](15N-1H3.md) | CoYuTe-15 | yes |  | Dedicated line list paper [24YuBoBr](../Papers/24YuBoBr.md) (ExoMol LX). |
