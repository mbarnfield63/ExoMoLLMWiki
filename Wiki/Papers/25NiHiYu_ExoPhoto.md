---
tags:
  - "paper"
bibcode: "25NiHiYu_ExoPhoto"
title: "ExoPhoto: A Database of Temperature-Dependent Photodissociation Cross Sections"
authors:
  - "Qing-He Ni"
  - "Christian Hill"
  - "Sergei N. Yurchenko"
  - "Marco Pezzella"
  - "Alexander Fateev"
  - "Zhi Qin"
  - "Olivia Venot"
  - "Jonathan Tennyson"
journal: "RAS Techniques and Instruments"
year: 2025
summary: "Presents ExoPhoto, an ExoMol database extension providing temperature-dependent photodissociation cross sections for 20 molecules sourced from ExoMol, PhoMol, UGAMOP, DTU, and EXACT."
mentioned_methods:
  - "ExoPhoto"
  - "ExoMol Database"
  - "Photodissociation Cross Sections"
  - "Duo"
mentioned_molecules: []
mentioned_people:
  - "Q_H_Ni"
  - "C_Hill"
  - "S_N_Yurchenko"
  - "M_Pezzella"
  - "A_Fateev"
  - "Z_Qin"
  - "O_Venot"
  - "J_Tennyson"
status: "seed"
created: "2026-06-28"
updated: "2026-06-28"
sources:
  - "Raw/Sources/25NiHiYu_ExoPhoto.json"
source_count: 1
---

# ExoPhoto: A Database of Temperature-Dependent Photodissociation Cross Sections

[25NiHiYu_ExoPhoto](../../Raw/Sources/25NiHiYu_ExoPhoto.json)

Ni et al. (2025) present [ExoPhoto](../Methods/ExoPhoto.md), an extension of the ExoMol database providing temperature-dependent photodissociation cross sections at www.exomol.com/exophoto/. The database currently covers 20 molecules: AlH, HCl, HF, MgH, OH, NaO, MgO, O₂, AlCl, AlF, CS, HeH⁺, CO, CO₂, H₂O, SO₂, C₂H₂, C₂H₄, H₂CO, and NH₃. Data are sourced from three computational groups (ExoMol, PhoMol, UGAMOP) and two experimental sources (DTU and the EXACT database). Cross sections are stored in `.photo` files, one per temperature per molecule, following the ExoMol framework with a hierarchical JSON-based organization and standardised naming convention encoding isotopologue slug, dataset, wavelength range, temperature, pressure, and wavelength grid. For selected molecules (CS, MgH) partial cross sections by dissociation channel and branching ratios are also provided. The paper notes that ExoMol's methodology treats photodissociation via a time-independent bound-state approach using Duo, while PhoMol and UGAMOP use explicit continuum-state methods; predissociation is currently only included in ExoMol calculations.

Source: [25NiHiYu_ExoPhoto](../../Raw/Sources/25NiHiYu_ExoPhoto.json)

## Related Methods

- [ExoPhoto](../Methods/ExoPhoto.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [Photodissociation Cross Sections](../Methods/Photodissociation_Cross_Sections.md)
- [Duo](../Methods/Duo.md)
