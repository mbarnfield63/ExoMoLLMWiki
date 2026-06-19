---
tags:
  - "paper"
bibcode: "22MiTaTe"
title: "ExoMol molecular line lists -- XLIII: Rovibronic transitions corresponding to the close-lying X²Π and A²Σ⁺ states of NaO"
authors:
  - "G. B. Mitev"
  - "S. Taylor"
  - "Jonathan Tennyson"
  - "S. N. Yurchenko"
  - "A. A. Buchachenko"
  - "A. V. Stolyarov"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2022
doi: "10.1093/mnras/stab3357"
summary: "ExoMol XLIII: Rovibronic NaOUCMe line list for the X²Π and A²Σ⁺ states of NaO. Variational coupled-channel calculation using Duo with MRCI/aug-cc-pVQZ ab initio PECs (MOLPRO), permanent and transition dipole moments, and non-adiabatic spin-orbit and Λ-uncoupling matrix elements, empirically refined against available rotational (X state) and A–X rovibronic data. A state excitation energy ~1982 cm⁻¹. Line list: 36,120 rovibronic levels, 4,726,137 transitions, 0–10,000 cm⁻¹, T_max = 2500 K. Vibrationally averaged permanent dipole moment (X state) 8.44 D. Relevant to Chapman mesospheric airglow mechanism and s-block metal monoxide astrophysics."
mentioned_methods:
  - "Duo"
  - "ExoCross"
  - "ExoMol Database"
  - "ExoMol Data Format"
  - "Partition Functions"
mentioned_molecules:
  - "NaO"
  - "23Na-16O"
mentioned_people:
  - "G_B_Mitev"
  - "S_Taylor"
  - "J_Tennyson"
  - "S_N_Yurchenko"
  - "A_A_Buchachenko"
  - "A_V_Stolyarov"
status: "active"
created: "2026-06-19"
updated: "2026-06-19"
sources:
  - "Raw/Sources/22MiTaTe.json"
source_count: 1
---

# 22MiTaTe

[22MiTaTe](../Papers/22MiTaTe.md) — Mitev, Taylor, Tennyson, Yurchenko, Buchachenko & Stolyarov (2022), *MNRAS* 511, 2349–2355.

## Summary

ExoMol XLIII presents **NaOUCMe**, a rovibronic line list for the sodium monoxide radical [23Na-16O](../Molecules/23Na-16O.md) covering the close-lying ground X²Π and first excited A²Σ⁺ electronic states. The A state lies only ~1982 cm⁻¹ above X, placing the A–X electronic transition in the mid-infrared (3–5 µm). NaO is observed in terrestrial mesospheric airglow (~90 km altitude) via the Chapman mechanism, and is an analogue of CaO relevant to bolide chemistry.

Ab initio PECs for both states were computed at the MRCI level using aug-cc-pVQZ all-electron basis sets with the MOLPRO suite, using SA-CASSCF reference orbitals and the Davidson correction. Permanent and transition dipole moments, spin-orbit coupling (SOC), and Λ-uncoupling matrix elements were computed from the same MR-CISD wave functions. Point-wise PECs were fitted to Extended Morse Oscillator (EMO) analytical forms, then empirically refined using Duo by least-squares fitting to: (i) pure rotational transitions in X²Π (v=0–5); (ii) rovibronic A²Σ⁺–X²Π transitions from Joo et al. (J_max ~22) and a vibrational spacing constraint (A state, v₀=498.9 cm⁻¹). RMS residuals: ~0.006 cm⁻¹ (X rotational), ~0.2 cm⁻¹ (A–X rovibronic). Partition functions were computed by direct state summation and benchmarked against JPL values (good agreement to 300 K, poorer at low T for the external reference).

The NaOUCMe line list contains 36,120 rovibronic levels and 4,726,137 dipole-allowed transitions (ΔΩ=0, ±1; Δε=±1) over 0–10,000 cm⁻¹, applicable up to T_max = 2500 K. The vibrationally averaged X state permanent dipole moment is 8.44 D; JPL predictions based on 8.71 D are therefore ~6% too strong. State uncertainties following the ExoMol standard are provided. Source: [22MiTaTe](../../Raw/Sources/22MiTaTe.json).

## Mentioned Methods

- [Duo](../Methods/Duo.md)
- [ExoCross](../Methods/ExoCross.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [ExoMol Data Format](../Methods/ExoMol_Data_Format.md)
- [Partition Functions](../Methods/Partition_Functions.md)

## Mentioned Molecules

- [NaO](../Molecules/NaO.md)
- [23Na-16O](../Molecules/23Na-16O.md)

## Mentioned People

- [G_B_Mitev](../People/G_B_Mitev.md)
- [S_Taylor](../People/S_Taylor.md)
- [J_Tennyson](../People/J_Tennyson.md)
- [S_N_Yurchenko](../People/S_N_Yurchenko.md)
- [A_A_Buchachenko](../People/A_A_Buchachenko.md)
- [A_V_Stolyarov](../People/A_V_Stolyarov.md)
