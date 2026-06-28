---
tags:
  - "paper"
bibcode: "25ZhHiTe_ExoMolHR"
title: "ExoMolHR: A Relational Database of Empirical High-Resolution Molecular Spectra"
authors:
  - "Jingxin Zhang"
  - "Christian Hill"
  - "Jonathan Tennyson"
  - "Sergei N. Yurchenko"
journal: "The Astrophysical Journal"
year: 2025
summary: "Presents ExoMolHR, a relational database providing empirical high-resolution molecular spectral lines extracted from ExoMol using MARVEL-validated low-uncertainty energy levels, covering 33 molecules and 58 isotopologues."
mentioned_methods:
  - "ExoMolHR"
  - "MARVELization"
  - "ExoMol Database"
  - "PyExoCross"
mentioned_molecules: []
mentioned_people:
  - "J_Zhang"
  - "C_Hill"
  - "J_Tennyson"
  - "S_N_Yurchenko"
status: "seed"
created: "2026-06-28"
updated: "2026-06-28"
sources:
  - "Raw/Sources/25ZhHiTe_ExoMolHR.json"
source_count: 1
---

# ExoMolHR: A Relational Database of Empirical High-Resolution Molecular Spectra

[25ZhHiTe_ExoMolHR](../../Raw/Sources/25ZhHiTe_ExoMolHR.json)

Zhang et al. (2025) present [ExoMolHR](../Methods/ExoMolHR.md), an empirical high-resolution molecular spectrum calculator built on the ExoMol database. ExoMolHR extracts lines whose transition wavenumbers are determined to a resolving power R ≥ 10⁶ (uncertainty ≤ 0.01 cm⁻¹ on both upper and lower energy levels) from ExoMol datasets that carry explicit uncertainties — which are largely those improved via the [MARVEL](../Methods/MARVELization.md) procedure. The database provides 24,307,135 lines for 58 isotopologues from 33 molecules, accessible at www.exomol.com/exomolhr/ as a web interface or API download. Output is a CSV file containing wavenumber, uncertainty, Einstein A, intensity at user-specified temperature, lower-state energy, degeneracies, J values, and quantum numbers. The paper compares ExoMolHR coverage to HITRAN for 15 shared molecules, showing ExoMolHR to be more complete, especially at low wavenumber. Cross sections from the CSV can be computed using PyExoCross.

Source: [25ZhHiTe_ExoMolHR](../../Raw/Sources/25ZhHiTe_ExoMolHR.json)

## Related Methods

- [ExoMolHR](../Methods/ExoMolHR.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [MARVELization](../Methods/MARVELization.md)
