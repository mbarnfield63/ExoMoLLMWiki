---
tags:
  - "paper"
bibcode: "22OwDoMc"
title: "ExoMol line lists -- XLV. Rovibronic molecular line lists of calcium monohydride (CaH) and magnesium monohydride (MgH)"
authors:
  - "A. Owens"
  - "S. Dooley"
  - "L. McLaughlin"
  - "B. Tan"
  - "G. Zhang"
  - "S. N. Yurchenko"
  - "J. Tennyson"
primary_authors:
  - "A. Owens"
secondary_authors:
  - "S. Dooley"
  - "L. McLaughlin"
  - "B. Tan"
  - "G. Zhang"
  - "S. N. Yurchenko"
  - "J. Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2022
doi: ""
summary: "ExoMol XLV: XAB rovibronic line lists for 40Ca-1H and three MgH isotopologues (24Mg-1H, 25Mg-1H, 26Mg-1H) covering 0–30,000 cm⁻¹, applicable up to 5000 K. Electronic states X²Σ⁺, A²Π, B²Σ⁺. CaH: 293,151 transitions, 6,825 states; MARVEL: 1,260 empirical energy levels from 3,663 input transitions. 24MgH: 88,575 transitions, 3,148 states; MARVEL: 1,856 levels from 8,520 transitions. 25MgH: 88,776 transitions, 3,156 states; MARVEL: 729 levels. 26MgH: 88,891 transitions, 3,160 states; MARVEL: 729 levels. Landé g-factors provided for stellar magnetic-field probing."
mentioned_methods:
  - "ExoMol Database"
  - "MARVEL"
  - "MARVELization"
  - "Duo"
  - "ExoCross"
  - "ExoMolHR"
mentioned_molecules:
  - "CaH"
  - "MgH"
  - "40Ca-1H"
  - "24Mg-1H"
  - "25Mg-1H"
  - "26Mg-1H"
mentioned_people:
  - "A_Owens"
  - "S_Dooley"
  - "L_McLaughlin"
  - "B_Tan"
  - "G_Zhang"
  - "S_N_Yurchenko"
  - "J_Tennyson"
status: "complete"
created: "2026-06-12"
updated: "2026-06-12"
sources:
  - "Raw/Sources/22OwDoMc.json"
source_count: 1
---

# 22OwDoMc — ExoMol XLV: CaH and MgH XAB line lists

Source: [22OwDoMc](../../Raw/Sources/22OwDoMc.json)

## Summary

Reports the **XAB** rovibronic line lists for [40Ca-1H](../Molecules/40Ca-1H.md) and the three stable MgH isotopologues — [24Mg-1H](../Molecules/24Mg-1H.md), [25Mg-1H](../Molecules/25Mg-1H.md), and [26Mg-1H](../Molecules/26Mg-1H.md) — the 45th paper in the ExoMol line list series (XLV). Published in *Monthly Notices of the Royal Astronomical Society* (2022).

The line lists cover the X²Σ⁺ (ground), A²Π, and B²Σ⁺ electronic states in the 0–30,000 cm⁻¹ region and are suitable for temperatures up to 5000 K. CaH and [MgH](../Molecules/MgH.md) are important probes of brown dwarf, late-type stellar, and planetary atmospheres; their spectra are used to classify M-dwarf stars and probe stellar magnetic fields. Landé g-factors are provided for all energy levels to support Zeeman spectroscopy applications.

MARVEL analyses were performed for all four isotopologues using extensive published spectroscopic datasets. For CaH, 3,663 experimental wavenumbers yielded 1,260 empirical energy levels; for 24MgH, 8,520 transitions yielded 1,856 empirical energy levels. These MARVEL values were used to refine the spectroscopic models (PECs and couplings computed with **Duo**) and to replace calculated energy levels in the post-processed line lists, making them suitable for high-resolution applications. Spectroscopic models treat spin-orbit, electronic angular momentum, Born-Oppenheimer breakdown, spin-rotation, and Λ-doubling couplings. Ab initio couplings computed at MCSCF/cc-pCVQZ level were morphed to experiment.

## Line List Summary

| Isotopologue | ExoMol ID | Line list | States | Transitions | Wavenumber range | T_max | MARVEL levels | Reference |
|---|---|---|---|---|---|---|---|---|
| CaH | [40Ca-1H](../Molecules/40Ca-1H.md) | XAB | 6,825 | 293,151 | 0–30,000 cm⁻¹ | 5000 K | 1,260 | [22OwDoMc](../Papers/22OwDoMc.md) |
| ²⁴MgH | [24Mg-1H](../Molecules/24Mg-1H.md) | XAB | 3,148 | 88,575 | 0–30,000 cm⁻¹ | 5000 K | 1,856 | [22OwDoMc](../Papers/22OwDoMc.md) |
| ²⁵MgH | [25Mg-1H](../Molecules/25Mg-1H.md) | XAB | 3,156 | 88,776 | 0–30,000 cm⁻¹ | 5000 K | 729 | [22OwDoMc](../Papers/22OwDoMc.md) |
| ²⁶MgH | [26Mg-1H](../Molecules/26Mg-1H.md) | XAB | 3,160 | 88,891 | 0–30,000 cm⁻¹ | 5000 K | 729 | [22OwDoMc](../Papers/22OwDoMc.md) |

## Key Methods

- **MARVEL**: Measured Active Rotational-Vibrational Energy Levels procedure applied independently to CaH and all three MgH isotopologues. CaH: 3,663 input transitions → 1,260 empirical energy levels ≤ 25,323 cm⁻¹. 24MgH: 8,520 transitions → 1,856 levels ≤ 29,748 cm⁻¹. 25MgH: 1,357 transitions → 729 levels. 26MgH: 1,237 transitions → 729 levels.
- **Duo**: Variational diatomic nuclear motion code used for rovibronic line list calculations. CaH: 501-point sinc-DVR grid; MgH: 401-point grid. Extensive state couplings treated explicitly (spin-orbit, electronic angular momentum, Born-Oppenheimer breakdown, spin-rotation, Λ-doubling).
- **Ab initio**: MCSCF/cc-pCVQZ (Ca or Mg) + cc-pVQZ (H) calculations via MOLPRO2015 for spin-orbit and electronic angular momentum coupling curves, subsequently morphed to experimental data.
- **ExoCross**: Partition functions computed on 1 K grid from 1–5000 K; absorption cross-sections simulated at 1 cm⁻¹ resolution.
- **Landé g-factors**: Computed for all energy levels via Duo; listed in the .states file for stellar magnetic-field diagnostics.

## Astrophysical Context

CaH and MgH are detected in sunspots, M-dwarf, brown dwarf, and cool giant stellar atmospheres. The A–X and B–X bands (visible/near-UV) are used for spectral classification of late-type dwarfs (> ~3000 K) and to probe stellar magnetic fields on active G-K-M stars. The A–X band of MgH is central to measuring magnesium isotope ratios in metal-poor stars. Both molecules are expected in exoplanetary atmospheres of metal-rich gas giants and are considered likely missing opacities in brown dwarf photosphere models. The Zeeman-sensitive Landé g-factors make these line lists directly applicable to stellar magnetic-field measurements.

## People

- [Alec Owens](../People/A_Owens.md) (primary)
- [Sophie Dooley](../People/S_Dooley.md)
- [Luke McLaughlin](../People/L_McLaughlin.md)
- [Brandon Tan](../People/B_Tan.md)
- [Guanming Zhang](../People/G_Zhang.md)
- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
