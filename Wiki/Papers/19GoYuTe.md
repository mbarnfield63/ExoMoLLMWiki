---
tags:
  - "paper"
bibcode: "19GoYuTe"
title: "ExoMol molecular line lists XXXVI: A²Σ⁺–X²Π and X²Π–X²Π transitions of SH"
authors:
  - "Maire N. Gorman"
  - "Sergei N. Yurchenko"
  - "Jonathan Tennyson"
year: 2019
journal: "Monthly Notices of the Royal Astronomical Society"
doi: ""
exomol_series: "XXXVI"
line_list_name: "GYT"
mentioned_methods:
  - "Duo"
  - "ExoCross and PyExoCross"
  - "ExoMol Database"
mentioned_molecules:
  - "SH"
  - "32S-1H"
  - "33S-1H"
  - "34S-1H"
  - "36S-1H"
  - "32S-2H"
mentioned_people:
  - "M_N_Gorman"
  - "S_N_Yurchenko"
  - "J_Tennyson"
summary: "ExoMol XXXVI: GYT rovibronic line list for SH (mercapto radical), covering A²Σ⁺–X²Π and X²Π–X²Π transitions. Main isotopologue 32SH: 7,686 rovibronic states, 572,145 transitions, 0–39,000 cm⁻¹ (λ > 0.256 μm), T≤5000 K. Ab initio MRCI/aug-cc-pV5Z-DK PECs/SOCs/EAMCs empirically refined with Duo; RMS 0.06 cm⁻¹ (X²Π), 0.3 cm⁻¹ (A²Σ⁺–X²Π). Minor isotopologue line lists also generated for 33SH, 34SH, 36SH (mass substitution) and 32SD (separate BOB-corrected model). Supersedes SNaSH (X²Π only). Motivated by SH UV opacity in WASP-121b transmission spectrum."
sources:
  - "Raw/Sources/19GoYuTe.json"
source_count: 1
created: "2026-06-26"
updated: "2026-06-26"
---

# 19GoYuTe — ExoMol XXXVI: GYT line list for SH

ExoMol XXXVI: GYT rovibronic line list for the mercapto radical SH ([32S-1H](../Molecules/32S-1H.md)), covering A²Σ⁺–X²Π and X²Π–X²Π transitions. Published by [M_N_Gorman](../People/M_N_Gorman.md), [S_N_Yurchenko](../People/S_N_Yurchenko.md), and [J_Tennyson](../People/J_Tennyson.md) (2019, MNRAS).

## Line List: GYT

- **Molecule:** 32SH ([32S-1H](../Molecules/32S-1H.md))
- **States:** 7,686 rovibronic states
- **Transitions:** 572,145
- **Wavenumber range:** 0–39,000 cm⁻¹ (λ > 0.256 μm; extends into UV)
- **Temperature validity:** ~5,000 K
- **Electronic states:** X²Π, A²Σ⁺ (+ repulsive ²Σ⁻ coupling state)
- **MARVEL:** not MARVELized
- **Supersedes:** SNaSH line list (Yurchenko et al. 2018, MNRAS 478, 270)

Minor isotopologue line lists also produced: [33S-1H](../Molecules/33S-1H.md) (³³SH), [34S-1H](../Molecules/34S-1H.md) (³⁴SH), [36S-1H](../Molecules/36S-1H.md) (³⁶SH) — same PECs/SOCs/EAMCs as ³²SH with mass substitution; [32S-2H](../Molecules/32S-2H.md) (³²SD) — separately refined BOB correction model, RMS 0.4 cm⁻¹.

## Method

Duo code with empirical refinement. Ab initio PECs/SOCs/EAMCs at MRCI/aug-cc-pV5Z-DK level (MOLPRO), active space (8,4,4,1) with (3,1,1,0) closed orbitals, 417-point grid 0.7–19.2 Å. PECs represented by Extended Morse Oscillator (EMO) function. Vibrational basis: 120 sinc-DVR functions (40 per state, 501 points 0.85–5.00 Å). Final model: 3 PECs (X²Π, A²Σ⁺, ²Σ⁻), 3 SOCs, 2 EAMCs, 2 BOBCs, 2 SRCs, 2 DMCs/TDMCs. RMS fit: 0.06 cm⁻¹ (X²Π), 0.3 cm⁻¹ (A²Σ⁺–X²Π).

## Key Physical Data

- **Dissociation energy (X²Π):** D₀ = 3.791 eV (NIST recommended)
- **A²Σ⁺ v=0 lifetime:** 449 ns (computational, predissociation excluded)
- **A²Σ⁺ v=1 lifetime:** 513 ns (computational)
- **Vibrationally averaged TDM (A²Σ⁺–X²Π):** 0.340 D

## Motivation

Prompted by the tentative identification of SH UV features in the transmission spectrum of ultra-hot Jupiter WASP-121b (Evans et al. 2018, AJ 156, 283; T_eq ≈ 2500 K), and SH's astrophysical relevance in AGB stars, Mira variables, the solar atmosphere, the ISM, and comets.

## Source

Source: [19GoYuTe](../../Raw/Sources/19GoYuTe.json)
