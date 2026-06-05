---
tags:
  - "paper"
bibcode: "23YuBrTe"
title: "ExoMol line lists — LIII: Empirical Rovibronic spectra of Yttrium Oxide (YO)"
authors:
  - "S. N. Yurchenko"
  - "R. P. Brady"
  - "J. Tennyson"
  - "A. N. Smirnov"
  - "O. A. Vasilyev"
  - "V. G. Solomonik"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2023
doi: ""
summary: "ExoMol LIII: BRYTS empirical rovibronic line lists for 89Y16O, 89Y17O, and 89Y18O covering the 6 lowest doublet electronic states up to 60,000 cm⁻¹ (≤ 166.67 nm). A pseudo-MARVEL procedure yields 5,089 empirically derived energy levels for 89Y16O used in spectroscopic model refinement via Duo. The model uses a diabatic representation to handle avoided crossings between two state pairs. The 89Y16O BRYTS line list contains 173,621 bound rovibronic states and 60,678,140 Einstein coefficients up to J = 400.5; rms fitting residual 0.29 cm⁻¹."
mentioned_methods:
  - "Duo"
  - "MARVELization"
  - "ExoCross"
  - "ExoMolOP"
  - "ExoMol Database"
mentioned_molecules:
  - "YO"
  - "89Y-16O"
  - "89Y-17O"
  - "89Y-18O"
mentioned_people:
  - "S_N_Yurchenko"
  - "R_P_Brady"
  - "J_Tennyson"
  - "A_N_Smirnov"
  - "O_A_Vasilyev"
  - "V_G_Solomonik"
status: "complete"
created: "2026-06-05"
updated: "2026-06-05"
sources:
  - "Raw/Sources/23YuBrTe.json"
source_count: 1
---

# 23YuBrTe — ExoMol LIII: YO BRYTS line lists

Source: [23YuBrTe](../../Raw/Sources/23YuBrTe.json)

## Summary

Reports the **BRYTS** empirical rovibronic line lists for [89Y-16O](../Molecules/89Y-16O.md), [89Y-17O](../Molecules/89Y-17O.md), and [89Y-18O](../Molecules/89Y-18O.md) — the 53rd paper in the ExoMol line list series (LIII). Published in *Monthly Notices of the Royal Astronomical Society* (2023).

A pseudo-MARVEL procedure assembles 5,089 experimentally derived rovibronic energy levels for ⁸⁹Y¹⁶O from published laboratory data (line positions and spectroscopic constants from 11 sources spanning 1961–2023), including a new high-resolution study of excited states by Murtz & Narayanan (2023). A diabatic spectroscopic model is constructed and refined via the Duo variational diatomic code, covering the 6 lowest doublet electronic states with non-adiabatic coupling curves for two pairs of avoided-crossing states computed at the CASSCF level using MOLPRO. Dipole moment curves are represented analytically using the "irregular DMC" form to ensure a physical Normal Intensity Distribution Law for overtone transitions. The final rms residual is 0.29 cm⁻¹ over 5,906 empirical energies.

## Line List Summary

| Isotopologue | ExoMol ID | Line list | Wavenumber range | J_max | MARVEL | Reference |
|---|---|---|---|---|---|---|
| ⁸⁹Y¹⁶O | [89Y-16O](../Molecules/89Y-16O.md) | BRYTS | 0–60,000 cm⁻¹ | 400.5 | Yes (5,089 levels) | [23YuBrTe](../Papers/23YuBrTe.md) |
| ⁸⁹Y¹⁷O | [89Y-17O](../Molecules/89Y-17O.md) | BRYTS | 0–60,000 cm⁻¹ | 400.5 | No | [23YuBrTe](../Papers/23YuBrTe.md) |
| ⁸⁹Y¹⁸O | [89Y-18O](../Molecules/89Y-18O.md) | BRYTS | 0–60,000 cm⁻¹ | 400.5 | No | [23YuBrTe](../Papers/23YuBrTe.md) |

## Key Methods

- **Duo**: variational diatomic nuclear-motion code; sinc-DVR grid of 151 points (1.4–3.5 Å); diabatic representation handling avoided crossings of Σ/Σ and Π/Π state pairs; 30–35 contracted vibronic basis functions per state
- **Pseudo-MARVEL**: spectroscopic-network approach adapted for YO where many sources provide only spectroscopic constants rather than raw line positions; effective Hamiltonian used to reconstruct term values from constants; 5,089 empirical levels derived
- **MOLPRO**: DDR procedure with state-averaged CASSCF (6 doublet states, 7e/13 orbitals, aug-cc-pwCVTZ/aug-cc-pwCVTZ-PP basis) for non-adiabatic coupling curves between Σ/Σ and Π/Π state pairs
- **Irregular DMC**: analytical dipole moment curve form with Chebyshev polynomial expansion enforcing a physically correct Normal Intensity Distribution Law for vibrational overtones
- **ExoMolOP**: temperature- and pressure-dependent opacities generated for ARCiS, TauREx, NEMESIS, and petitRADTRANS

## Astrophysical Context

YO has been observed in the spectra of cool stars including R-Cygni, Pi-Gruis, V838 Mon, and V4332 Sgr. It has also been used in molecular laser cooling experiments and as a probe for high-temperature materials. The BRYTS line list targets stellar atmosphere modelling and retrieval codes; opacities are provided for four retrieval frameworks via the ExoMolOP pipeline.

## People

- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md) (primary)
- [Ryan P. Brady](../People/R_P_Brady.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
- [Alexander N. Smirnov](../People/A_N_Smirnov.md)
- [Oleg A. Vasilyev](../People/O_A_Vasilyev.md)
- [Victor G. Solomonik](../People/V_G_Solomonik.md)
