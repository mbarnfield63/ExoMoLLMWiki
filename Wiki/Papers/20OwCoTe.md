---
tags:
  - "paper"
bibcode: "20OwCoTe"
title: "ExoMol line lists -- XXXVIII. High-temperature molecular line list of silicon dioxide (SiO2)"
authors:
  - "A. Owens"
  - "E.K. Conway"
  - "J. Tennyson"
  - "S. N. Yurchenko"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2020
doi: "10.1093/mnras/staa1287"
summary: "ExoMol XXXVIII: OYT3 purely ab initio rovibrational line list for 28Si-16O2. First comprehensive line list for SiO2. 32,951,275,437 transitions between 5,688,942 energy levels, 0–6000 cm⁻¹, T_max 3000 K (soft limit). TROVE (extended for linear triatomics) with CCSD(T)-F12b/CBS PES and DMS; no empirical refinement. No MARVEL. Recommended for low-resolution studies (resolving power ~1000) targeting hot rocky super-Earth exoplanet atmospheres."
mentioned_methods:
  - "TROVE"
  - "DVR3D"
  - "ExoCross"
  - "ExoMol Database"
  - "ExoMol Data Format"
  - "Partition Functions"
mentioned_molecules:
  - "SiO2"
  - "28Si-16O2"
mentioned_people:
  - "A_Owens"
  - "E_K_Conway"
  - "J_Tennyson"
  - "S_N_Yurchenko"
status: "active"
created: "2026-06-26"
updated: "2026-06-26"
sources:
  - "Raw/Sources/20OwCoTe.json"
source_count: 1
---

# 20OwCoTe

[20OwCoTe](../Papers/20OwCoTe.md) — Owens, Conway, Tennyson & Yurchenko (2020), *Monthly Notices of the Royal Astronomical Society*.

## Summary

ExoMol XXXVIII presents **OYT3**, the first comprehensive rovibrational line list for silicon dioxide [28Si-16O2](../Molecules/28Si-16O2.md). SiO2 is a linear triatomic in the gas phase, analogous to CO2, and is expected in the atmospheres of hot rocky super-Earth exoplanets (dayside temperatures up to ~4000 K). A lack of high-resolution experimental data meant the OYT3 line list is purely ab initio with no empirical refinement; it is recommended for low-resolution studies (resolving power ~1000).

High-level CCSD(T)-F12b/CBS PES and DMS were computed on a grid of 15,365 nuclear geometries and fitted analytically. TROVE was extended to treat linear triatomic molecules for this work and benchmarked against DVR3D. Partition functions were computed on a 1 K grid from 1–3000 K. ExoCross was used for spectral simulations. OYT3 exhibits a prominent spectral feature at 4.5 μm that overlaps with the CO2 photometric band used by the Spitzer IRAC instrument, relevant to phase-curve studies of super-Earths such as 55 Cancri e and Corot-7b.

**OYT3:** 32,951,275,437 transitions between 5,688,942 rovibrational energy levels, covering 0–6,000 cm⁻¹, T_max 3000 K (soft limit; partition function completeness ~99.998% at 3000 K). Source: [20OwCoTe](../../Raw/Sources/20OwCoTe.json).

## Key Results

- Line list name: **OYT3**
- Isotopologue: 28Si-16O2 (main isotopologue)
- N states: 5,688,942
- N transitions: 32,951,275,437
- Wavenumber range: 0–6,000 cm⁻¹
- T_max: 3000 K (soft limit)
- PES: ab initio CCSD(T)-F12b/CBS with scalar relativistic corrections
- DMS: ab initio CCSD(T)-F12b with large augmented correlation-consistent basis set
- Nuclear motion: TROVE (new linear triatomic extension) + DVR3D (benchmarking)
- Symmetry group: C₂ᵥ(M)
- Fundamental accuracy: ~1–3 cm⁻¹ (conservative); intensities within 5–10% of experiment
- MARVEL: No
- Recommended resolution: ~1000 (low-resolution only)

## Mentioned Methods

- [TROVE](../Methods/TROVE.md)
- [DVR3D](../Methods/DVR3D.md)
- [ExoCross](../Methods/ExoCross.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [ExoMol Data Format](../Methods/ExoMol_Data_Format.md)
- [Partition Functions](../Methods/Partition_Functions.md)

## Mentioned Molecules

- [SiO2](../Molecules/SiO2.md)
- [28Si-16O2](../Molecules/28Si-16O2.md)

## Mentioned People

- [A. Owens](../People/A_Owens.md)
- [E.K. Conway](../People/E_K_Conway.md)
- [J. Tennyson](../People/J_Tennyson.md)
- [S. N. Yurchenko](../People/S_N_Yurchenko.md)
