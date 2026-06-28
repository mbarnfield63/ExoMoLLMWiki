---
tags:
  - "paper"
bibcode: "25NiWaXi_ExoAtom"
title: "ExoAtom: A Database of Atomic Spectra in ExoMol Format"
authors:
  - "Qing-He Ni"
  - "Rujia Wang"
  - "Tianyang Xie"
  - "Jingxin Zhang"
  - "Christian Hill"
  - "Sergei N. Yurchenko"
  - "Jonathan Tennyson"
journal: "RAS Techniques and Instruments"
year: 2025
summary: "Introduces ExoAtom, an extension of the ExoMol database providing atomic line lists in ExoMol format for 80 neutral atoms and 74 singly charged ions, sourced from NIST and Kurucz databases."
mentioned_methods:
  - "ExoAtom"
  - "ExoMol Data Format"
  - "PyExoCross"
mentioned_molecules: []
mentioned_people:
  - "Q_H_Ni"
  - "R_Wang"
  - "T_Xie"
  - "J_Zhang"
  - "C_Hill"
  - "S_N_Yurchenko"
  - "J_Tennyson"
status: "seed"
created: "2026-06-28"
updated: "2026-06-28"
sources:
  - "Raw/Sources/25NiWaXi_ExoAtom.json"
source_count: 1
---

# ExoAtom: A Database of Atomic Spectra in ExoMol Format

[25NiWaXi_ExoAtom](../../Raw/Sources/25NiWaXi_ExoAtom.json)

Ni et al. (2025) present [ExoAtom](../Methods/ExoAtom.md), an extension of the ExoMol database that provides atomic line lists in ExoMol format at www.exomol.com/exoatom. The database covers 80 neutral atoms and 74 singly charged ions. Data are sourced from two complementary databases: NIST (79/71 neutral/ion species, high-accuracy experimental measurements) and Kurucz (38/37 neutral/ion species, theoretically complete). ExoAtom uses the ExoMol file types `.all`, `.def`, `.states`, `.trans`, and `.pf` for atomic data. The `.states` file contains energy levels with quantum numbers, uncertainties, lifetimes, and optionally Landé g-factors; the `.trans` file provides Einstein A coefficients and wavenumbers; the `.pf` file provides partition functions up to 6000 K (NIST) or using Kurucz-supplied values. Post-processing is provided by [PyExoCross](../Methods/ExoCross.md). The paper notes that ExoAtom does not recommend one dataset over the other — NIST favours accuracy while Kurucz favours completeness — so users choose based on their requirements.

Source: [25NiWaXi_ExoAtom](../../Raw/Sources/25NiWaXi_ExoAtom.json)

## Related Methods

- [ExoAtom](../Methods/ExoAtom.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [ExoMol Data Format](../Methods/ExoMol_Data_Format.md)
