---
tags:
  - "paper"
bibcode: "19LiTeYu"
title: "ExoMol line lists XXXII: The rovibronic spectrum of MgO"
authors:
  - "Heng Ying Li"
  - "Jonathan Tennyson"
  - "Sergei N. Yurchenko"
year: 2019
journal: "Monthly Notices of the Royal Astronomical Society"
doi: ""
exomol_series: "XXXII"
summary: "ExoMol XXXII: LiTY rovibronic line lists for five MgO isotopologues (24Mg-16O, 25Mg-16O, 26Mg-16O, 24Mg-17O, 24Mg-18O) covering the five lowest electronic states. 24Mg-16O: 186,842 states, 72,833,173 transitions, J_max=300, ≤33,000 cm⁻¹, T≤5000 K. MARVEL analysis of 24Mg-16O yields 757 empirical energy levels from 2457 transitions. Duo nuclear-motion calculations with MRCI/aug-cc-pwCVQZ ab initio SOCs/EAMCs and literature DMCs. Partition function agrees with JPL at 300 K. Line lists suitable for exoplanet atmospheres, cool stars, and brown dwarfs."
mentioned_molecules:
  - "MgO"
  - "24Mg-16O"
  - "24Mg-17O"
  - "24Mg-18O"
  - "25Mg-16O"
  - "26Mg-16O"
mentioned_methods:
  - "Duo"
  - "MARVELization"
  - "ExoMol Database"
  - "ExoCross and PyExoCross"
mentioned_people:
  - "H_Y_Li"
  - "J_Tennyson"
  - "S_N_Yurchenko"
sources:
  - "Raw/Sources/19LiTeYu.json"
source_count: 1
created: "2026-06-26"
updated: "2026-06-26"
---

# 19LiTeYu

ExoMol XXXII: [19LiTeYu](../../Raw/Sources/19LiTeYu.json). Rovibronic LiTY line lists for five isotopologues of magnesium oxide (MgO), covering the five lowest electronic states. Duo nuclear-motion calculations with potential energy, spin-orbit (SOC), and electronic angular momentum (EAMC) curves empirically refined to MARVEL energy levels. Ab initio dipole moment curves (DMCs) from Bauschlicher (MRCI/aug-cc-pV5Z). MARVEL study of 24Mg-16O validated 757 empirical energy levels from 2457 collected transitions across nine electronic states. Line lists available at CDS and ExoMol.

Source: [19LiTeYu](../../Raw/Sources/19LiTeYu.json)

## Line List Summary

| Isotopologue | Line list | N states | N transitions | J_max | Coverage | T max |
| --- | --- | --- | --- | --- | --- | --- |
| [24Mg-16O](../Molecules/24Mg-16O.md) | LiTY | 186,842 | 72,833,173 | 300 | ≤33,000 cm⁻¹ (≥ 0.3 μm) | 5000 K |
| [25Mg-16O](../Molecules/25Mg-16O.md) | LiTY | comparable | — | — | ≤33,000 cm⁻¹ | 5000 K |
| [26Mg-16O](../Molecules/26Mg-16O.md) | LiTY | comparable | — | — | ≤33,000 cm⁻¹ | 5000 K |
| [24Mg-17O](../Molecules/24Mg-17O.md) | LiTY | comparable | — | — | ≤33,000 cm⁻¹ | 5000 K |
| [24Mg-18O](../Molecules/24Mg-18O.md) | LiTY | comparable | — | — | ≤33,000 cm⁻¹ | 5000 K |

## Electronic States Covered

Five lowest electronic states of MgO. Red band system (A–X singlet) and green band system (B–A singlet) are the strongest bands, with significant overlap at visible wavelengths (15,000–20,000 cm⁻¹, 0.5–0.66 μm). Upper states to 37,500 cm⁻¹; lower states to 24,000 cm⁻¹.

## Methods

- **Nuclear motion:** Duo; fully coupled Schrödinger equation; sinc DVR grid (501 points, 0.02–8 Å).
- **PECs:** Initial ab initio PECs from Bauschlicher; four lowest states represented as EMO (extended Morse oscillator) and refined to experiment. Fifth state PEC interpolated on grid via cubic splines.
- **SOCs and EAMCs:** MRCI/aug-cc-pwCVQZ (MOLPRO); all-electron correlated, Douglas-Kroll relativistic correction; active space (8,4,4,0); morphed to experiment.
- **DMCs:** Diagonal and transition DMCs from Bauschlicher (aug-cc-pV5Z); remaining TDMCs computed ab initio; represented analytically via damped expansion.
- **Fit:** PECs, SOCs, EAMCs refined to 2457 experimental transitions + 756 MARVEL term values; RMS 0.029 cm⁻¹ overall (0.009, 0.002, 0.016, 0.04 cm⁻¹ per state).
- **Spectral simulations:** ExoCross.

## MARVEL

24Mg-16O MARVEL study: 2457 transitions collected across nine electronic states → 757 validated empirical energy levels. MARVEL energies used to refine the spectroscopic model. Minor isotopologues (25Mg-16O, 26Mg-16O, 24Mg-17O, 24Mg-18O) generated from the same Born-Oppenheimer curves without additional MARVEL refinement.

## Evidence

Paper explicitly reports LiTY line lists for 24Mg-16O (186,842 states; 72,833,173 transitions; J_max=300; wavenumbers to 33,000 cm⁻¹; T≤5000 K). Minor isotopologues have comparable sizes. Partition function at 300 K ≈ 374, matching JPL value of 374.621. A¹Π state lifetimes at (J=0, J=70): 21.8 ns and 21.7 ns, consistent with fluorescence decay measurements. Source: [19LiTeYu](../../Raw/Sources/19LiTeYu.json)
