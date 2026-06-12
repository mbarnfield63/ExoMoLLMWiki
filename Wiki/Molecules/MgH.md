---
tags:
  - "molecule"
formula: "MgH"
atoms:
  - "Mg"
  - "H"
parent_molecule: ""
exomol_id: ""
aliases: []
isotopologues:
  - "24Mg-1H"
  - "25Mg-1H"
  - "26Mg-1H"
line_list: "XAB"
marvel_data:
  is_marvelized: true
  latest_source_year: 2022
  energy_levels: 1856
associated_methods:
  - "ExoMol Database"
  - "MARVELization"
  - "ExoMolHR"
  - "Duo"
applications:
  - "Exoplanet Atmospheres"
  - "Cool Stars"
status: "active"
created: "2026-05-29"
updated: "2026-06-12"
sources:
  - "Raw/Sources/24TeYuZh.json"
  - "Raw/Sources/22OwDoMc.json"
source_count: 2
---

# MgH

Magnesium monohydride (MgH) is an important astrophysical molecule observed in sunspots, M-dwarf and brown dwarf atmospheres, and cool giant stars. Its A–X band is widely used to determine magnesium isotope ratios in metal-poor stars, and it is a potential thermal inversion agent in hot Jupiter atmospheres. Three stable isotopologues are covered by the ExoMol XAB line list from [22OwDoMc](../Papers/22OwDoMc.md). Source: [22OwDoMc](../../Raw/Sources/22OwDoMc.json).

## Recommended Datasets

| Molecule entry | Dataset | Isotopologues | T max | Elec. states | N lines (main) | MARVEL | Reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MgH | XAB | 3 (24/25/26Mg-1H) | 5000 K | X²Σ⁺, A²Π, B²Σ⁺ | 88,575 (²⁴MgH) | Yes | [22OwDoMc](../Papers/22OwDoMc.md) |

## Named Isotopologues

| Isotopologue | Line list | MARVEL | ExoMolHR | Evidence |
| --- | --- | --- | --- | --- |
| [24Mg-1H](24Mg-1H.md) | XAB | Yes (1,856 levels) | Yes | XAB line list from [22OwDoMc](../Papers/22OwDoMc.md); also listed in ExoMolHR. |
| [25Mg-1H](25Mg-1H.md) | XAB | Yes (729 levels) | Yes | XAB line list from [22OwDoMc](../Papers/22OwDoMc.md); also listed in ExoMolHR. |
| [26Mg-1H](26Mg-1H.md) | XAB | Yes (729 levels) | Yes | XAB line list from [22OwDoMc](../Papers/22OwDoMc.md); also listed in ExoMolHR. |

## Notes

The A–X band of MgH is particularly important for establishing magnesium isotope ratios in metal-poor stars. Quasibound levels above the dissociation threshold but below the centrifugal barrier maximum are included in the XAB line list, influencing spectra at higher temperatures. Landé g-factors are provided for stellar magnetic-field diagnostics. Source: [22OwDoMc](../../Raw/Sources/22OwDoMc.json).
