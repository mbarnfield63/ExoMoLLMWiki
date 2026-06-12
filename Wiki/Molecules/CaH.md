---
tags:
  - "molecule"
formula: "CaH"
atoms:
  - "Ca"
  - "H"
parent_molecule: ""
exomol_id: ""
aliases: []
isotopologues:
  - "40Ca-1H"
line_list: "XAB"
marvel_data:
  is_marvelized: true
  latest_source_year: 2022
  energy_levels: 1260
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

# CaH

Calcium monohydride (CaH) is an important astrophysical molecule used to classify late-type M-dwarf and brown dwarf stars and to probe stellar magnetic fields. It was first detected in sunspots over a century ago and has since been observed in cool giant stars, active G-K-M dwarfs, and is expected in metal-rich exoplanetary atmospheres. The current primary ExoMol line list is the **XAB** list from [22OwDoMc](../Papers/22OwDoMc.md). Source: [22OwDoMc](../../Raw/Sources/22OwDoMc.json).

## Recommended Datasets

| Molecule entry | Dataset | Isotopologues | T max | Elec. states | N lines | MARVEL | Reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CaH | XAB | 1 (40Ca-1H) | 5000 K | X²Σ⁺, A²Π, B²Σ⁺ | 293,151 | Yes (1,260 levels) | [22OwDoMc](../Papers/22OwDoMc.md) |

## Named Isotopologues

| Isotopologue | Line list | MARVEL | ExoMolHR | Evidence |
| --- | --- | --- | --- | --- |
| [40Ca-1H](40Ca-1H.md) | XAB | Yes | Yes | XAB line list from [22OwDoMc](../Papers/22OwDoMc.md); also listed in ExoMolHR. |

## Notes

CaH spectra are particularly useful for probing stellar magnetic fields via Zeeman spectroscopy; the XAB line list provides Landé g-factors for all energy levels. The A–X and B–X rovibronic bands (visible/near-UV) dominate the spectrum and are used for M-dwarf spectral classification above ~3000 K. Source: [22OwDoMc](../../Raw/Sources/22OwDoMc.json).
