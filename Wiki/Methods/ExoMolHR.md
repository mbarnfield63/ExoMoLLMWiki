---
tags:
  - "method"
title: "ExoMolHR"
developer_group: "ExoMol"
software_type: "High-resolution empirical spectral database"
status: "seed"
created: "2026-05-29"
updated: "2026-06-28"
sources:
  - "Raw/Sources/24TeYuZh.json"
  - "Raw/Sources/25ZhHiTe_ExoMolHR.json"
source_count: 2
---

# ExoMolHR

ExoMolHR (www.exomol.com/exomolhr/) is an empirical high-resolution molecular spectral database built from ExoMol line lists. It extracts transitions whose wavenumbers are known to resolving power R ≥ 10⁶ (energy-level uncertainty ≤ 0.01 cm⁻¹ on both upper and lower states), relying largely on MARVEL-validated empirical energy levels. The database currently provides 24,307,135 lines for 58 isotopologues from 33 molecules. Output is a CSV file with wavenumber, uncertainty, Einstein A, intensity at user-specified temperature, lower-state energy, degeneracies, J values, and quantum numbers. A web interface and API are available for interactive selection by wavenumber range, temperature, and intensity threshold. Cross sections from ExoMolHR CSV files can be computed using PyExoCross. Sources: [24TeYuZh](../../Raw/Sources/24TeYuZh.json), [25ZhHiTe_ExoMolHR](../../Raw/Sources/25ZhHiTe_ExoMolHR.json).

## Related Methods

- [ExoMol Database](ExoMol_Database.md)
- [MARVELization](MARVELization.md)

## Papers

- [25ZhHiTe_ExoMolHR](../Papers/25ZhHiTe_ExoMolHR.md)
