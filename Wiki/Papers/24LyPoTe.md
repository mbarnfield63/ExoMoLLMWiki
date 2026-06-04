---
tags:
  - "paper"
bibcode: "24LyPoTe"
title: "ExoMol Line Lists — LXII: Ro-Vibrational Energy Levels and Line-Strengths for Propadienediylidene (C3) in its Ground Electronic State"
authors:
  - "A. E. Lynas-Gray"
  - "O. L. Polyansky"
  - "J. Tennyson"
  - "S. N. Yurchenko"
  - "N. F. Zobov"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2024
doi: ""
summary: "ExoMol LXII: variational AtLast line lists for tricarbon (12C3) and two 13C-substituted isotopologues using TROVE. 12C3 incorporates MARVEL corrections from 1887 empirical energy levels (Tennyson 2024, Mol. Phys.); maximum line-position errors 0.03 cm-1 below the conical-intersection threshold. Opacities deposited in ExoMol database."
mentioned_methods:
  - "TROVE"
  - "ExoCross"
  - "MARVELization"
  - "ExoMol Database"
  - "ExoMolHR"
mentioned_molecules:
  - "C3"
  - "12C3"
  - "12C-13C-12C"
  - "12C-12C-13C"
mentioned_people:
  - "A_E_Lynas-Gray"
  - "O_L_Polyansky"
  - "J_Tennyson"
  - "S_N_Yurchenko"
  - "N_F_Zobov"
status: "complete"
created: "2026-06-04"
updated: "2026-06-04"
sources:
  - "Raw/Sources/24LyPoTe.json"
source_count: 1
---

# 24LyPoTe — ExoMol LXII: C3 AtLast line lists

Source: [24LyPoTe](../../Raw/Sources/24LyPoTe.json)

## Summary

Reports the **AtLast** variational line lists for the tricarbon ([12C3](../Molecules/12C3.md)) molecule and two ¹³C-substituted isotopologues ([12C-13C-12C](../Molecules/12C-13C-12C.md) and [12C-12C-13C](../Molecules/12C-12C-13C.md)) in their ground electronic states — the 62nd paper in the ExoMol line list series (LXII).

For ¹²C₃, 1887 empirical energy levels from a MARVEL analysis (Tennyson 2024, *Mol. Phys.*, 122, e2276912) were used to refine the PES and replace calculated energies in the states file, yielding 16,178 MARVELised transitions at 296 K. Comparison with Martin-Drumel et al. (2023) FTIR absorption confirms band structure and intensities. The ¹³C-substituted line lists use the same PES without isotopologue-specific MARVEL correction and show systematic residuals in frequency comparisons.

## Line List Summary

| Isotopologue | ExoMol ID | States | Transitions | J_max | E_max (cm⁻¹) | MARVEL |
|---|---|---|---|---|---|---|
| ¹²C₃ | [12C3](../Molecules/12C3.md) | 2,166,503 | 5,481,690,507 | 155 | 20,000 | Yes (1887 levels) |
| ¹²C¹³C¹²C | [12C-13C-12C](../Molecules/12C-13C-12C.md) | 2,282,841 | 6,071,530,477 | 155 | 20,000 | No |
| ¹²C¹²C¹³C | [12C-12C-13C](../Molecules/12C-12C-13C.md) | 2,442,205 | 14,503,868,150 | 150 | 17,000 | No |

## Key Methods

- **TROVE**: variational nuclear-motion code with exact kinetic energy operator for quasi-linear molecules; bisector frame and valence coordinates; two-step contraction procedure for basis functions
- **PES refinement**: Schröder & Sebald (2016) PES refined against 276 MARVEL ro-vibrational term values (J ≤ 60); rms residual 0.026 cm⁻¹
- **MARVELization**: 1887 empirical energy levels from 21 publications (Tennyson 2024); replaces calculated energies in 12C3 states file
- **ExoCross**: cross-sections, partition functions (1–5000 K), and opacities for ARCiS, TauREx, NEMESIS, petitRADTRANS
- **ExoMolHR**: high-accuracy MARVELised transitions accessible online

## Astrophysical Context

C₃ (propadienediylidene / tricarbon) is detected in comets, carbon stars (including R CrB), the interstellar medium (Sgr B2(M)), and Titan's atmosphere. The 2000 cm⁻¹ asymmetric-stretch feature completely dominates C₃ infrared opacity from 300 K upward. AtLast supersedes the earlier line list of Jørgensen et al. and is suitable for high-dispersion transit spectroscopy at λ > 1 μm; conical intersections complicate accuracy at shorter wavelengths.

## People

- [A.E. Lynas-Gray](../People/A_E_Lynas-Gray.md) (primary)
- [Oleg L. Polyansky](../People/O_L_Polyansky.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Nikolai F. Zobov](../People/N_F_Zobov.md)
