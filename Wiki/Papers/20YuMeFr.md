---
tags:
  - "paper"
bibcode: "20YuMeFr"
title: "ExoMol line lists -- XXXIX. Ro-vibrational molecular line list for CO2"
authors:
  - "S. N. Yurchenko"
  - "Thomas M. Mellor"
  - "Richard S. Freedman"
  - "J. Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2020
doi: ""
summary: "ExoMol XXXIX: UCL-4000 ro-vibrational line list for 12C-16O2 (main isotopologue only). 3,480,477 states and 2,557,551,923 transitions, 0–20,000 cm⁻¹, T_max ~2500 K. TROVE with new exact kinetic energy (EKE) operator, Ames-2 PES, UCL ab initio DMS. HITRAN energies substituted for 337 vibrational bands (rms 0.016 cm⁻¹ after correction). Superseded by Dozen (26YuBaBo, 2026)."
mentioned_methods:
  - "TROVE"
  - "ExoMol Database"
  - "ExoMol Data Format"
  - "Partition Functions"
  - "HITRAN"
  - "HITEMP"
  - "DVR3D"
mentioned_molecules:
  - "CO2"
  - "12C-16O2"
mentioned_people:
  - "S_N_Yurchenko"
  - "T_M_Mellor"
  - "R_S_Freedman"
  - "J_Tennyson"
status: "active"
created: "2026-06-26"
updated: "2026-06-26"
sources:
  - "Raw/Sources/20YuMeFr.json"
source_count: 1
---

# 20YuMeFr

[20YuMeFr](../Papers/20YuMeFr.md) — Yurchenko, Mellor, Freedman & Tennyson (2020), *Monthly Notices of the Royal Astronomical Society*.

## Summary

ExoMol XXXIX presents **UCL-4000**, a hot ro-vibrational line list for the main isotopologue of CO2, [12C-16O2](../Molecules/12C-16O2.md). CO2 is a dominant opacity source in Venus (95%), hot Jupiter exoplanets, and a key C/O ratio indicator in directly imaged planets. The line list is designed for high-temperature atmospheric retrievals where HITRAN (room-temperature) and HITEMP (effective Hamiltonian) are insufficient.

Calculations used TROVE with a new exact kinetic energy (EKE) operator for triatomics in bisector embedding — a generalization enabling exact treatment of the nuclear-motion Hamiltonian. The Ames-2 empirical PES (Huang et al.) was used for ro-vibrational energies, and UCL's ab initio DMS for dipole transition moments. A multi-step contraction scheme controlled by polyad number P ≤ 62 produced a vibrational basis of convergence-tested completeness.

To maximize accuracy of line positions, TROVE ro-vibrational energies were replaced by HITRAN values where available: 18,392 empirical energies from 337 vibrational bands (J ≤ 129) were substituted via empirical basis set correction (EBSC), giving a residual rms of 0.016 cm⁻¹. UCL-4000 contains **3,480,477 states** and **2,557,551,923 transitions** covering 0–20,000 cm⁻¹ (lower state energy ≤ 16,000 cm⁻¹, upper threshold 36,000 cm⁻¹). Valid to ~2500 K for the full range; ~4000 K for 10,000–20,000 cm⁻¹. UCL-4000 outperforms CDSD-4000 and 2010 HITEMP in completeness at high temperatures due to inclusion of more hot bands. Source: [20YuMeFr](../../Raw/Sources/20YuMeFr.json).

## Key Results

- Line list name: **UCL-4000**
- Isotopologue: 12C-16O2 (main isotopologue, HITRAN 626) only
- N states: 3,480,477
- N transitions: 2,557,551,923
- Wavenumber range: 0–20,000 cm⁻¹ (split into 20 transition files of 1000 cm⁻¹)
- Lower energy threshold: 16,000 cm⁻¹
- Upper energy threshold: 36,000 cm⁻¹
- T_max: ~2500 K (full range); ~4000 K (10,000–20,000 cm⁻¹)
- PES: Ames-2 (Huang et al.)
- DMS: UCL ab initio DMS
- TROVE with new EKE operator (bisector embedding)
- HITRAN energies substituted for 337 vibrational bands (18,392 empirical values, J ≤ 129); rms 0.016 cm⁻¹
- Mean intensity ratio to HITRAN: 1.0029 (std error 0.00029) over 171,143 lines

## Mentioned Methods

- [TROVE](../Methods/TROVE.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [ExoMol Data Format](../Methods/ExoMol_Data_Format.md)
- [Partition Functions](../Methods/Partition_Functions.md)
- [HITRAN](../Methods/HITRAN.md)
- [HITEMP](../Methods/HITEMP.md)
- [DVR3D](../Methods/DVR3D.md)

## Mentioned Molecules

- [CO2](../Molecules/CO2.md)
- [12C-16O2](../Molecules/12C-16O2.md)

## Mentioned People

- [S. N. Yurchenko](../People/S_N_Yurchenko.md)
- [Thomas M. Mellor](../People/T_M_Mellor.md)
- [Richard S. Freedman](../People/R_S_Freedman.md)
- [J. Tennyson](../People/J_Tennyson.md)

## Superseded By

- [26YuBaBo](../Papers/26YuBaBo.md) — Dozen (2026): 12 CO2 isotopologues; supersedes UCL-4000 for 12C-16O2 with extended coverage and MARVELization.
