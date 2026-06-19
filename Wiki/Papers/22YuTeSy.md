---
tags:
  - "paper"
bibcode: "22YuTeSy"
title: "ExoMol line lists -- XLIV. IR and UV line list for silicon monoxide (28Si16O)"
authors:
  - "Sergei N. Yurchenko"
  - "Jonathan Tennyson"
  - "Anna-Maree Syme"
  - "Ahmad Y. Adam"
  - "Victoria H. J. Clark"
  - "Bridgette Cooper"
  - "C. Pria Dobney"
  - "Shaun T. E. Donnelly"
  - "Maire N. Gorman"
  - "Anthony E. Lynas-Gray"
  - "Thomas Meltzer"
  - "Alec Owens"
  - "Qianwei Qu"
  - "Mikhail Semenov"
  - "Wilfrid Somogyi"
  - "Apoorva Upadhyay"
  - "Samuel Wright"
  - "Juan C. Zapata Trujillo"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2022
summary: "ExoMol XLIV: SiOUVenIR IR and UV rovibronic line list for 28Si16O covering nine electronic states (X1Sigma+, A1Pi, E1Sigma+, C1Sigma-, D1Delta, a3Sigma+, b3Pi, e3Sigma-, d3Delta) up to 72,000 cm-1 (lambda > 140 nm). Contains 91,395,763 transitions and 174,250 states, valid up to 10,000 K with J up to 250. MARVEL analysis yields 2617 empirical energy levels from 6051 experimental transitions (latest source 13MuSpBi, 2013) across 97 vibronic bands. Ab initio PECs/SOCs/EAMCs computed at IC-MRCI-F12c/QZ-F12 level with MOLPRO2015, empirically refined with Duo against MARVEL energies. Supersedes the EBJT rotation-vibration line list (13BaYuTe). MARVELised energies, state uncertainties, Lande g-factors, and lifetimes provided."
mentioned_methods:
  - "Duo"
  - "MARVELization"
  - "ExoMol Database"
  - "ExoMol Data Format"
  - "Partition Functions"
  - "ExoCross and PyExoCross"
mentioned_molecules:
  - "SiO"
  - "28Si-16O"
mentioned_people:
  - "S_N_Yurchenko"
  - "J_Tennyson"
  - "A_M_Syme"
  - "A_Y_Adam"
  - "V_H_J_Clark"
  - "B_Cooper"
  - "C_P_Dobney"
  - "S_T_E_Donnelly"
  - "M_N_Gorman"
  - "A_E_Lynas-Gray"
  - "T_Meltzer"
  - "A_Owens"
  - "Q_Qu"
  - "M_Semenov"
  - "W_Somogyi"
  - "A_Upadhyay"
  - "S_O_M_Wright"
  - "J_C_Zapata_Trujillo"
status: "active"
created: "2026-06-12"
updated: "2026-06-12"
sources:
  - "Raw/Sources/22YuTeSy.json"
source_count: 1
---

# 22YuTeSy

[22YuTeSy](../Papers/22YuTeSy.md) — Yurchenko, Tennyson, Syme et al. (2022), *MNRAS*.

## Summary

ExoMol XLIV presents **SiOUVenIR**, an IR and UV rovibronic line list for [28Si-16O](../Molecules/28Si-16O.md). The line list supersedes the previous ExoMol EBJT rotation-vibration line list (13BaYuTe) by including vibronic transitions to the A¹Π and E¹Σ⁺ excited electronic states and explicitly modelling perturbations from six dark states (C¹Σ⁻, D¹Δ, a³Σ⁺, b³Π, e³Σ⁻, d³Δ). Together with the X¹Σ⁺ ground state, nine electronic states are included.

The SiOUVenIR line list contains **91,395,763 transitions** and **174,250 states** covering wavenumbers up to 72,000 cm⁻¹ (λ > 140 nm) for J = 0–250, suitable for temperatures up to 10,000 K. Ab initio PECs, SOCs, and EAMCs were computed at the IC-MRCI-F12c/QZ-F12 level using MOLPRO2015, then empirically refined with Duo against MARVEL energy levels. Published ab initio TDMCs from Bauschlicher (2016) were used for the E–X and A–X bands. MARVELised energies replace calculated Duo values where available.

A MARVEL analysis of ²⁸Si¹⁶O processed 6051 experimental and 3426 pseudo-experimental transitions from literature sources covering the X–X, A–X, and E–X systems (plus 112 forbidden transitions assigned to dark bands), yielding **2617 empirical energy levels** with J ≤ 103 for states below 61,881 cm⁻¹. The latest experimental source used is 13MuSpBi (2013). Partition functions (to 10,000 K), Landé g-factors, state uncertainties, and radiative lifetimes are provided. Source: [22YuTeSy](../../Raw/Sources/22YuTeSy.json).

## Mentioned Methods

- [Duo](../Methods/Duo.md)
- [MARVELization](../Methods/MARVELization.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [ExoMol Data Format](../Methods/ExoMol_Data_Format.md)
- [Partition Functions](../Methods/Partition_Functions.md)
- [ExoCross and PyExoCross](../Methods/ExoCross.md)

## Mentioned Molecules

- [SiO](../Molecules/SiO.md)
- [28Si-16O](../Molecules/28Si-16O.md)

## Mentioned People

- [S_N_Yurchenko](../People/S_N_Yurchenko.md)
- [J_Tennyson](../People/J_Tennyson.md)
- [A_M_Syme](../People/A_M_Syme.md)
- [A_Y_Adam](../People/A_Y_Adam.md)
- [V_H_J_Clark](../People/V_H_J_Clark.md)
- [B_Cooper](../People/B_Cooper.md)
- [C_P_Dobney](../People/C_P_Dobney.md)
- [S_T_E_Donnelly](../People/S_T_E_Donnelly.md)
- [M_N_Gorman](../People/M_N_Gorman.md)
- [A_E_Lynas-Gray](../People/A_E_Lynas-Gray.md)
- [T_Meltzer](../People/T_Meltzer.md)
- [A_Owens](../People/A_Owens.md)
- [Q_Qu](../People/Q_Qu.md)
- [M_Semenov](../People/M_Semenov.md)
- [W_Somogyi](../People/W_Somogyi.md)
- [A_Upadhyay](../People/A_Upadhyay.md)
- [S_O_M_Wright](../People/S_O_M_Wright.md)
- [J_C_Zapata_Trujillo](../People/J_C_Zapata_Trujillo.md)
