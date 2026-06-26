---
tags:
  - "molecule"
formula: "SH"
atoms:
  - "S"
  - "H"
parent_molecule: ""
exomol_id: ""
aliases: []
isotopologues:
  - "32S-1H"
  - "33S-1H"
  - "34S-1H"
  - "36S-1H"
  - "32S-2H"
line_list: "GYT"
marvel_data:
  is_marvelized: false
  latest_source_year: null
  energy_levels: null
associated_methods:
  - "Duo"
  - "ExoMol Database"
applications:
  - "Exoplanet Atmospheres"
  - "Cool Star Atmospheres"
  - "Astrochemistry"
status: "complete"
created: "2026-05-29"
updated: "2026-06-26"
sources:
  - "Raw/Sources/24TeYuZh.json"
  - "Raw/Sources/19GoYuTe.json"
source_count: 2
---

# SH

Parent molecule MOC for the mercapto radical SH. GYT line list published in [19GoYuTe](../Papers/19GoYuTe.md). Five isotopologue files cover ³²SH, ³³SH, ³⁴SH, ³⁶SH, and ³²SD. Source: [24TeYuZh](../../Raw/Sources/24TeYuZh.json).

## Recommended Datasets

| Molecule entry | Dataset | Isotopologues | T max (K) | N lines | MARVEL | Reference |
| --- | --- | --- | --- | --- | --- | --- |
| SH | GYT | 5 (³²SH, ³³SH, ³⁴SH, ³⁶SH, ³²SD) | 5000 | 572,145 (³²SH) | No | [19GoYuTe](../Papers/19GoYuTe.md) |

## Named Isotopologues

| Isotopologue | Line list | Status | Notes |
| --- | --- | --- | --- |
| [32S-1H](32S-1H.md) | GYT | complete | Main isotopologue; 7,686 states, 572,145 transitions |
| [33S-1H](33S-1H.md) | GYT | seed | Mass substitution from ³²SH model |
| [34S-1H](34S-1H.md) | GYT | seed | Mass substitution from ³²SH model |
| [36S-1H](36S-1H.md) | GYT | seed | Mass substitution from ³²SH model |
| [32S-2H](32S-2H.md) | GYT | seed | Separately refined BOB-corrected model |

Source: [19GoYuTe](../../Raw/Sources/19GoYuTe.json)
