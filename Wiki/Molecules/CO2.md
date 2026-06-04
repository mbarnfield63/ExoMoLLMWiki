---
tags:
  - "molecule"
formula: "CO2"
atoms:
  - "C"
  - "O"
parent_molecule: ""
exomol_id: ""
aliases: []
isotopologues:
  - "12C-16O2"
  - "13C-16O2"
  - "12C-17O2"
  - "13C-17O2"
  - "12C-18O2"
  - "13C-18O2"
  - "16O-12C-17O"
  - "16O-12C-18O"
  - "16O-13C-17O"
  - "16O-13C-18O"
  - "17O-12C-18O"
  - "17O-13C-18O"
line_list: "Dozen"
marvel_data:
  is_marvelized: null
  latest_source_year: null
  energy_levels: null
associated_methods:
  - "ExoMol Database"
  - "MARVELization"
  - "ExoMolHR"
  - "TROVE"
  - "ExoMolOP"
applications:
  - "Exoplanet Atmospheres"
  - "Solar System Atmospheres"
  - "Terrestrial Applications"
  - "Opacity Modelling"
status: "seed"
created: "2026-05-29"
updated: "2026-06-02"
sources:
  - "Raw/Sources/24TeYuZh.json"
  - "Raw/Sources/26YuBaBo.json"
source_count: 2
---

# CO2

Carbon dioxide (CO2) is a key atmospheric constituent with extensive line list coverage in ExoMol. Sources: [24TeYuZh](../../Raw/Sources/24TeYuZh.json), [26YuBaBo](../../Raw/Sources/26YuBaBo.json).

## Recommended Datasets

| Molecule entry | Dataset | Isotopologues covered | T max | Reference |
| --- | --- | --- | --- | --- |
| CO2 | UCL-4000 | 1 (12C-16O2) | 3000 K | [24TeYuZh](../../Raw/Sources/24TeYuZh.json) Table 1 |
| CO2 | Dozen | 12 isotopologues | 3000 K (main), ~2000 K (minor) | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |

## Named Isotopologues

| Isotopologue | HITRAN | Line list | MARVEL | Evidence |
| --- | --- | --- | --- | --- |
| [12C-16O2](12C-16O2.md) | 626 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json); supersedes UCL-4000 |
| [13C-16O2](13C-16O2.md) | 636 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |
| [12C-17O2](12C-17O2.md) | 727 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |
| [13C-17O2](13C-17O2.md) | 737 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |
| [12C-18O2](12C-18O2.md) | 828 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |
| [13C-18O2](13C-18O2.md) | 838 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |
| [16O-12C-17O](16O-12C-17O.md) | 627 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |
| [16O-12C-18O](16O-12C-18O.md) | 628 | Dozen | no | [26YuBaBo](../../Raw/Sources/26YuBaBo.json); EBCC not applied |
| [16O-13C-17O](16O-13C-17O.md) | 637 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |
| [16O-13C-18O](16O-13C-18O.md) | 638 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |
| [17O-12C-18O](17O-12C-18O.md) | 728 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |
| [17O-13C-18O](17O-13C-18O.md) | 738 | Dozen | yes | [26YuBaBo](../../Raw/Sources/26YuBaBo.json) |
