---
tags:
  - "paper"
bibcode: "20ChTeYu"
title: "ExoMol molecular line lists - XXXVII: spectra of acetylene"
authors:
  - "Katy L. Chubb"
  - "Jonathan Tennyson"
  - "Sergei N. Yurchenko"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2020
doi: ""
summary: "ExoMol XXXVII: aCeTY ro-vibrational line list for the ground electronic state of the main isotopologue of acetylene (12C2H2, HCCH). 4,347,381,911 transitions between 5,160,803 energy levels, 0–10,000 cm⁻¹ (≥ 1 µm), complete to ~2200 K, J_max = 99, l_max = 16. TROVE variational calculations using a VQZ-F12/CCSD(T)-F12c PES (refined to MARVEL energies) and CCSD(T)/aug-cc-PVQZ DMS. Line list is MARVELised using empirical energies from a 2017 MARVEL analysis. Vibrational transition dipole moments scaled band-by-band to HITRAN-2016 intensities. Recommended for exoplanet and cool stellar atmosphere modelling."
mentioned_methods:
  - "TROVE"
  - "MARVELization"
  - "ExoMol Database"
  - "ExoMol Data Format"
  - "Partition Functions"
  - "ExoCross and PyExoCross"
  - "HITRAN"
mentioned_molecules:
  - "C2H2"
  - "12C2-1H2"
mentioned_people:
  - "K_L_Chubb"
  - "J_Tennyson"
  - "S_N_Yurchenko"
status: "active"
created: "2026-06-26"
updated: "2026-06-26"
sources:
  - "Raw/Sources/20ChTeYu.json"
source_count: 1
---

# 20ChTeYu

[20ChTeYu](../Papers/20ChTeYu.md) — Chubb, Tennyson & Yurchenko (2020), *Monthly Notices of the Royal Astronomical Society*.

## Summary

ExoMol XXXVII presents **aCeTY**, a ro-vibrational line list for the ground electronic state of the main isotopologue of acetylene, [12C2-1H2](../Molecules/12C2-1H2.md) (HCCH). Acetylene is an important opacity source in cool carbon stars, brown dwarf atmospheres, gas giants in our Solar System (Saturn, Uranus, Jupiter, Titan), and potentially super-Earth and hot-Jupiter exoplanet atmospheres. The aCeTY line list is the most complete and accurate line list for acetylene available at time of publication.

Variational calculations were performed with TROVE for the linear tetratomic geometry of HCCH, using a VQZ-F12/CCSD(T)-F12c PES (originally computed by a referenced group, refined here to MARVEL energies) and a CCSD(T)/aug-cc-PVQZ DMS. The potential energy surface was refined by fitting to MARVEL empirical energy levels from a 2017 MARVEL analysis of all published ¹²C₂H₂ spectral data. A band-centre replacement procedure then shifted 128 vibrational band centres to minimise residuals against MARVEL term values. Energy levels in the states file are MARVELised — replaced with MARVEL empirical values where available, with associated uncertainties. Vibrational transition dipole moments were scaled band-by-band against HITRAN-2016 room-temperature intensities across 216 bands to improve intensity accuracy.

**aCeTY:** 4,347,381,911 transitions between 5,160,803 ro-vibrational energy levels, covering 0–10,000 cm⁻¹ (≥ 1 µm), complete to ~2200 K, J_max = 99, l_max = 16. Source: [20ChTeYu](../../Raw/Sources/20ChTeYu.json).

## Key Results

- Line list name: **aCeTY**
- Isotopologue: ¹²C₂H₂ (main isotopologue, HCCH)
- N states: 5,160,803
- N transitions: 4,347,381,911
- Wavenumber range: 0–10,000 cm⁻¹ (≥ 1 µm)
- Lower energy cutoff: 12,000 cm⁻¹; upper energy cutoff: 22,000 cm⁻¹
- T_max completeness: ~2200 K
- J_max: 99; l_max (vibrational angular momentum): 16
- PES: VQZ-F12/CCSD(T)-F12c, refined to MARVEL energies
- DMS: CCSD(T)/aug-cc-PVQZ
- Nuclear motion: TROVE (linear tetratomic implementation)
- MARVELised: Yes (2017 MARVEL analysis of all published ¹²C₂H₂ data)
- DMS scaling: 216 bands scaled to HITRAN-2016 room-temperature intensities

## Mentioned Methods

- [TROVE](../Methods/TROVE.md)
- [MARVELization](../Methods/MARVELization.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [ExoMol Data Format](../Methods/ExoMol_Data_Format.md)
- [Partition Functions](../Methods/Partition_Functions.md)
- [ExoCross and PyExoCross](../Methods/ExoCross.md)
- [HITRAN](../Methods/HITRAN.md)

## Mentioned Molecules

- [C2H2](../Molecules/C2H2.md)
- [12C2-1H2](../Molecules/12C2-1H2.md)

## Mentioned People

- [K. L. Chubb](../People/K_L_Chubb.md)
- [J. Tennyson](../People/J_Tennyson.md)
- [S. N. Yurchenko](../People/S_N_Yurchenko.md)
