---
tags:
  - "paper"
bibcode: "21QuYuTe"
title: "ExoMol molecular line lists -- XLII: Rovibronic molecular line list for the low-lying states of NO"
authors:
  - "Qianwei Qu"
  - "Sergei N. Yurchenko"
  - "Jonathan Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2021
doi: ""
summary: "ExoMol XLII: XABC rovibronic line list for 14N-16O covering the four lowest doublet electronic states (X²Π, A²Σ⁺, B²Π, C²Π) and their γ (A–X), β (B–X), and δ (C–X) band systems plus ground-state rotational/vibrational transitions. Diabatic model resolves the B/C avoided crossing. TDMCs: empirical polynomial (Luque & Crosley) for X–X; CASSCF+MRCI/cc-pVQZ ab initio, empirically scaled, for A–X and B–X. SPFIT/SPCAT effective-Hamiltonian energies replace calculated values for lower X²Π levels; MARVEL energies used where available (labeled Ma). 30,811 rovibronic states, 4,596,666 transitions, 0–63,000 cm⁻¹, T_max ~3500 K. Updates and supersedes the ExoMol NOname line list."
mentioned_methods:
  - "Duo"
  - "MARVELization"
  - "ExoMol Database"
  - "ExoMol Data Format"
  - "Partition Functions"
  - "ExoCross"
  - "HITRAN"
mentioned_molecules:
  - "NO"
  - "14N-16O"
mentioned_people:
  - "Q_Qu"
  - "S_N_Yurchenko"
  - "J_Tennyson"
status: "active"
created: "2026-06-24"
updated: "2026-06-24"
sources:
  - "Raw/Sources/21QuYuTe.json"
source_count: 1
---

# 21QuYuTe

[21QuYuTe](../Papers/21QuYuTe.md) — Qu, Yurchenko & Tennyson (2021), *Monthly Notices of the Royal Astronomical Society*.

## Summary

ExoMol XLII presents **XABC**, a rovibronic line list for nitric oxide [14N-16O](../Molecules/14N-16O.md) covering the four lowest doublet electronic states: X²Π, A²Σ⁺, B²Π, and C²Π. The line list provides comprehensive spectral coverage of NO's three main electronic band systems — γ (A²Σ⁺–X²Π), β (B²Π–X²Π), and δ (C²Π–X²Π) — as well as pure rotational and vibrational transitions within the ground state. XABC updates and supersedes the earlier ExoMol NOname line list.

The central challenge is the avoided crossing between the adiabatic B²Π and C²Π potential energy curves near 1.18 Å, which produces erratic behaviour in transition dipole moment curves (TDMCs) if handled adiabatically. A diabatic model is adopted using a bell-shaped coupling curve, producing smooth PECs and TDMCs and allowing high-accuracy state mixing to be captured through the fitted rovibronic wavefunctions. PECs, spin-orbit couplings, and TDMCs for the A, B, C states were computed at the CASSCF+MRCI level using MOLPRO with a cc-pVQZ basis. The X–X TDMC uses the empirical Luque & Crosley polynomial. The A–X and B–X TDMCs are scaled empirically against measured radiative lifetimes and absorption cross-sections to balance all available intensity data. Rovibronic energies and wavefunctions were calculated using Duo. Lower X²Π levels are replaced with SPFIT/SPCAT effective-Hamiltonian energies (labeled EH), and MARVEL empirical energies are used for all four states where available (labeled Ma). Energy uncertainties following ExoMol conventions are provided for every state.

The XABC line list contains 30,811 rovibronic states (21,668 X²Π; 1,209 A²Σ⁺; 6,873 B²Π; 1,041 C²Π) and 4,596,666 transitions covering 0–63,000 cm⁻¹ (rovibronic cutoffs: 53,000 cm⁻¹ for the A state, 63,000 cm⁻¹ for all others), applicable up to ~3500 K. NO is observed in the Earth, Venus, and Mars atmospheres, in ISM dark clouds (L134N, TMC1), and in the extragalactic source NGC 253. Source: [21QuYuTe](../../Raw/Sources/21QuYuTe.json).

## Mentioned Methods

- [Duo](../Methods/Duo.md)
- [MARVELization](../Methods/MARVELization.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [ExoMol Data Format](../Methods/ExoMol_Data_Format.md)
- [Partition Functions](../Methods/Partition_Functions.md)
- [ExoCross](../Methods/ExoCross.md)
- [HITRAN](../Methods/HITRAN.md)

## Mentioned Molecules

- [NO](../Molecules/NO.md)
- [14N-16O](../Molecules/14N-16O.md)

## Mentioned People

- [Q_Qu](../People/Q_Qu.md)
- [S_N_Yurchenko](../People/S_N_Yurchenko.md)
- [J_Tennyson](../People/J_Tennyson.md)
