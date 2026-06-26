---
tags:
  - "molecule"
formula: "MgO"
atoms:
  - "Mg"
  - "O"
parent_molecule: ""
exomol_id: ""
aliases: []
isotopologues:
  - "24Mg-16O"
  - "24Mg-17O"
  - "24Mg-18O"
  - "25Mg-16O"
  - "26Mg-16O"
line_list: ""
marvel_data:
  is_marvelized: true
  latest_source_year: null
  energy_levels: 820
associated_methods:
  - "ExoMol Database"
  - "MARVELization"
  - "Predicted Shift Method"
  - "Isotopologue Extrapolation"
applications:
  - "Exoplanet Atmospheres"
  - "Lava Planets"
status: "complete"
created: "2026-05-29"
updated: "2026-06-03"
sources:
  - "Raw/Sources/19LiTeYu.json"
  - "Raw/Sources/24TeYuZh.json"
  - "Raw/Sources/24McBoKe.json"
source_count: 3
---

# MgO

Formula-level MOC for magnesium oxide. Five isotopologues covered by the LiTY line list, originally published in [19LiTeYu](../Papers/19LiTeYu.md). Sources: [19LiTeYu](../../Raw/Sources/19LiTeYu.json), [24TeYuZh](../../Raw/Sources/24TeYuZh.json), [24McBoKe](../Papers/24McBoKe.md).

## Recommended Datasets

| Molecule entry | Dataset | Isotopologues counted | T max | N elec | N lines | MARVEL | Reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MgO | LiTY | 5 | 5000 | 5 | 72,833,173 |  | [19LiTeYu](../Papers/19LiTeYu.md); hybrid update [24McBoKe](../Papers/24McBoKe.md); 2024 release [24TeYuZh](../Papers/24TeYuZh.md) |

## Named Isotopologues

| Isotopologue | Line list | MARVEL | Evidence |
| --- | --- | --- | --- |
| [24Mg-16O](24Mg-16O.md) | LiTY | 820 energy levels | Original LiTY in [19LiTeYu](../Papers/19LiTeYu.md) (757 MARVEL levels); hybrid MARVEL + PS update in [24McBoKe](../Papers/24McBoKe.md) (820 levels). |
| [24Mg-17O](24Mg-17O.md) | LiTY | IE | Original LiTY in [19LiTeYu](../Papers/19LiTeYu.md); IE update in [24McBoKe](../Papers/24McBoKe.md). |
| [24Mg-18O](24Mg-18O.md) | LiTY | IE | Original LiTY in [19LiTeYu](../Papers/19LiTeYu.md); IE update in [24McBoKe](../Papers/24McBoKe.md). |
| [25Mg-16O](25Mg-16O.md) | LiTY | IE | Original LiTY in [19LiTeYu](../Papers/19LiTeYu.md); IE update in [24McBoKe](../Papers/24McBoKe.md). |
| [26Mg-16O](26Mg-16O.md) | LiTY | IE | Original LiTY in [19LiTeYu](../Papers/19LiTeYu.md); IE update in [24McBoKe](../Papers/24McBoKe.md). |
