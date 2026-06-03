---
tags:
  - "paper"
bibcode: "24YuBoBr"
title: "ExoMol line lists -- LX. Molecular line list for the ammonia isotopologue 15NH3"
authors:
  - "Sergei N. Yurchenko"
  - "Charles A. Bowesman"
  - "Ryan P. Brady"
  - "Elizabeth R. Guest"
  - "Kyriaki Kefala"
  - "Georgi B. Mitev"
  - "Alec Owens"
  - "Armando N. Perri"
  - "Marco Pezzella"
  - "Oleksiy Smola"
  - "Andrei Sokolov"
  - "Jingxin Zhang"
  - "Jonathan Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2024
summary: "Presents CoYuTe-15, the ExoMol line list for 15NH3. Computed with TROVE using the same empirical PES and ab initio DMS as the parent 14NH3 CoYuTe list. MARVELised with 2,777 empirical energy levels derived from 21,095 transitions across 37 experimental sources (1947-2020), covering 40 vibrational bands up to 6,818 cm-1. Isotopologue extrapolation (IE) adds 326 pseudo-MARVEL levels. Line list covers 0-10,000 cm-1, T <= 1000 K; 929,795,249 transitions between 12,699,617 states. H2 and He broadening parameters (m0 and m1 diets) provided."
mentioned_methods:
  - "TROVE"
  - "MARVELization"
  - "ExoMol Database"
  - "HITRAN"
  - "Partition Functions"
mentioned_molecules:
  - "NH3"
  - "15N-1H3"
  - "14N-1H3"
mentioned_people:
  - "S_N_Yurchenko"
  - "C_A_Bowesman"
  - "R_P_Brady"
  - "E_R_Guest"
  - "K_Kefala"
  - "G_B_Mitev"
  - "A_Owens"
  - "A_N_Perri"
  - "M_Pezzella"
  - "O_Smola"
  - "A_Solokov"
  - "J_Zhang"
  - "J_Tennyson"
status: "complete"
created: "2026-06-03"
updated: "2026-06-03"
sources:
  - "Raw/Sources/24YuBoBr.json"
source_count: 1
---

# 24YuBoBr — ExoMol line lists LX: ¹⁵NH₃ CoYuTe-15

Source: [24YuBoBr](../../Raw/Sources/24YuBoBr.json)

## Summary

Presents **CoYuTe-15**, the ExoMol ro-vibrational line list for ¹⁵NH₃ (ExoMol series number LX, the 60th paper). Computed using the variational program TROVE with the same spectroscopic model — empirical PES fitted to ¹⁴NH₃ experimental data and an ab initio DMS — used for the CoYuTe ¹⁴NH₃ line list; only atomic masses are changed to ¹⁵N and ¹H. MARVELised with 2,777 empirical energy levels and supplemented by isotopologue extrapolation (IE) from ¹⁴NH₃. H₂ and He collisional line-broadening parameters are provided in m0 and m1 diet formats.

## Line List: CoYuTe-15

| Property | Value |
|---|---|
| States | 12,699,617 |
| Transitions | 929,795,249 |
| ν range (cm⁻¹) | 0–10,000 |
| T max (K) | 1000 |
| MARVEL | yes |

## MARVELisation

| Property | Value |
|---|---|
| MARVEL energy levels | 2,777 |
| MARVEL transitions | 21,095 |
| Experimental sources | 37 |
| ν range covered (cm⁻¹) | 0–6,818 |
| Vibrational bands | 40 |

Of the 2,777 MARVEL energies, 2,754 (residuals < 1 cm⁻¹) replace theoretical values in the line list. An isotopologue extrapolation (IE) procedure transfers obs–calc residuals from the ¹⁴NH₃ MARVEL set onto ¹⁵NH₃ states for the ground state, ν₂, and its overtones (326 IE levels). A further 14 effective-Hamiltonian (EH) term values are also included. In total, 53,856 MARVELised transitions are provided in HITRAN format.

## Key Methods

- **TROVE**: variational nuclear motion; same PES/DMS model as CoYuTe (¹⁴NH₃); masses switched to ¹⁵N/¹H
- **MARVEL**: 37 experimental sources from 1947–2020 systematised via MARVEL4 Online
- **Isotopologue extrapolation (IE)**: obs–calc residuals from ¹⁴NH₃ MARVEL transferred to ¹⁵NH₃ for ground state, ν₂, 2ν₂
- **Line broadening**: H₂ m0 and m1 diets; He m0 and m1 diets; based on HITRAN ¹⁴NH₃ broadening data

## People

- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md) (primary)
- [Charles A. Bowesman](../People/C_A_Bowesman.md)
- [Ryan P. Brady](../People/R_P_Brady.md)
- [Elizabeth R. Guest](../People/E_R_Guest.md)
- [Kyriaki Kefala](../People/K_Kefala.md)
- [Georgi B. Mitev](../People/G_B_Mitev.md)
- [Alec Owens](../People/A_Owens.md)
- [Armando N. Perri](../People/A_N_Perri.md)
- [Marco Pezzella](../People/M_Pezzella.md)
- [Oleksiy Smola](../People/O_Smola.md)
- [Andrei Solokov](../People/A_Solokov.md)
- [Jingxin Zhang](../People/J_Zhang.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
