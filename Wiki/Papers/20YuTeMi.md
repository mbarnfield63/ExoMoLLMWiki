---
tags:
  - "paper"
bibcode: "20YuTeMi"
title: "ExoMol line lists -- XL. Ro-vibrational molecular line list for the hydronium ion (H3O+)"
authors:
  - "S. N. Yurchenko"
  - "Jonathan Tennyson"
  - "Steve Miller"
  - "V. V. Melnikov"
  - "J. O'Donoghue"
  - "L. Moore"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2020
doi: ""
summary: "ExoMol XL: eXeL ro-vibrational line list for 1H3-16O+ (hydronium ion). New ab initio DMS (CCSD(T)/aug-cc-pVQZ, MOLPRO) and new empirical PES obtained by refining an ab initio surface against available SPFIT/SPCAT empirical energies for the ground and ν2, ν3, ν4, 2ν2 vibrational states. Variational calculations with TROVE; Einstein A coefficients via GPU code GAIN-MPI. Empirical SPFIT/SPCAT energies substituted for TROVE values where available. Line list: 1,173,114 states, 2,089,331,073 transitions, 0–10,000 cm⁻¹, J_max=40, T_max~1500 K. Applications: Saturn ionosphere, giant planets, exoplanets, brown dwarfs, ISM."
mentioned_methods:
  - "TROVE"
  - "ExoMol Database"
  - "ExoMol Data Format"
  - "Partition Functions"
  - "HITRAN"
mentioned_molecules:
  - "H3O+"
  - "1H3-16O+"
mentioned_people:
  - "S_N_Yurchenko"
  - "J_Tennyson"
  - "S_Miller"
  - "V_V_Melnikov"
  - "J_ODonoghue"
  - "L_Moore"
status: "active"
created: "2026-06-24"
updated: "2026-06-24"
sources:
  - "Raw/Sources/20YuTeMi.json"
source_count: 1
---

# 20YuTeMi

[20YuTeMi](../Papers/20YuTeMi.md) — Yurchenko, Tennyson, Miller, Melnikov, O'Donoghue & Moore (2020), *Monthly Notices of the Royal Astronomical Society*.

## Summary

ExoMol XL presents **eXeL**, the first comprehensive hot ro-vibrational line list for the hydronium ion [1H3-16O+](../Molecules/1H3-16O+.md). Hydronium is a pyramidal C₃ᵥ molecule with a very low inversion barrier (~650.9 cm⁻¹) and a tunnelling splitting in the ground state of 55.35 cm⁻¹. It is relevant to Saturn's ionosphere, giant planet atmospheres, ISM molecular clouds, cometary comae, and potentially sub-Neptune exoplanets.

A new ab initio DMS was computed at CCSD(T)/aug-cc-pVQZ level using MOLPRO. A new empirical PES was obtained by fitting a high-level ab initio starting surface to the SPFIT/SPCAT empirical energies of Müller et al. (covering the ground, ν₂, ν₃, ν₄, and 2ν₂ vibrational states, J ≤ ~40). Variational ro-vibrational calculations used TROVE with a contracted basis set comprising 9,134 functions (J = 0–40). Einstein A coefficients were generated with the GPU code GAIN-MPI. TROVE theoretical energies were replaced by the SPFIT/SPCAT empirical values where available; state uncertainties are provided for every level.

The eXeL line list contains 1,173,114 ro-vibrational states and 2,089,331,073 transitions, covering 0–10,000 cm⁻¹ with lower state energy up to 10,000 cm⁻¹. The partition function is ~98% complete at 1500 K; T_max is taken as ~1500 K. The line list is split into 100 transition files of 100 cm⁻¹ each. Applications demonstrated include simulated H₃O⁺ emission spectra for Saturn's equatorial ionosphere (T~370 K), identifying a window at 10.40–10.50 µm accessible to ground-based mid-IR spectrometers such as TEXES. Source: [20YuTeMi](../../Raw/Sources/20YuTeMi.json).

## Mentioned Methods

- [TROVE](../Methods/TROVE.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [ExoMol Data Format](../Methods/ExoMol_Data_Format.md)
- [Partition Functions](../Methods/Partition_Functions.md)
- [HITRAN](../Methods/HITRAN.md)

## Mentioned Molecules

- [H3O+](../Molecules/H3O+.md)
- [1H3-16O+](../Molecules/1H3-16O+.md)

## Mentioned People

- [S_N_Yurchenko](../People/S_N_Yurchenko.md)
- [J_Tennyson](../People/J_Tennyson.md)
- [S_Miller](../People/S_Miller.md)
- [V_V_Melnikov](../People/V_V_Melnikov.md)
- [J_ODonoghue](../People/J_ODonoghue.md)
- [L_Moore](../People/L_Moore.md)
