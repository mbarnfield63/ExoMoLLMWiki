---
tags:
  - "paper"
bibcode: "22OwMiYu"
title: "ExoMol line lists -- XLVII. Rovibronic molecular line list of the calcium monohydroxide radical (CaOH)"
authors:
  - "A. Owens"
  - "A. Mitrushchenkov"
  - "S. N. Yurchenko"
  - "J. Tennyson"
primary_authors:
  - "A. Owens"
secondary_authors:
  - "A. Mitrushchenkov"
  - "S. N. Yurchenko"
  - "J. Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2022
doi: ""
summary: "ExoMol XLVII: OYT6 rovibronic line list for 40Ca-16O-1H covering 0–35,000 cm⁻¹, applicable up to ~3000 K (soft limit). First comprehensive line list covering the X̃²Σ⁺ rovibrational and Ã²Π–X̃²Σ⁺ rovibronic bands. 24,215,753,701 transitions between 3,187,522 states, J_max=175.5. EVEREST code used for rovibronic calculations with refined Ã state PES. MARVELized: 1614 energy levels replaced with empirical MARVEL values."
mentioned_methods:
  - "ExoMol Database"
  - "EVEREST"
  - "MARVEL"
  - "MARVELization"
  - "ExoCross"
  - "ExoMolHR"
mentioned_molecules:
  - "CaOH"
  - "40Ca-16O-1H"
mentioned_people:
  - "A_Owens"
  - "A_Mitrushchenkov"
  - "S_N_Yurchenko"
  - "J_Tennyson"
status: "complete"
created: "2026-06-09"
updated: "2026-06-09"
sources:
  - "Raw/Sources/22OwMiYu.json"
source_count: 1
---

# 22OwMiYu — ExoMol XLVII: CaOH OYT6 line list

Source: [22OwMiYu](../../Raw/Sources/22OwMiYu.json)

## Summary

Reports the **OYT6** rovibronic line list for [40Ca-16O-1H](../Molecules/40Ca-16O-1H.md) — the 47th paper in the ExoMol line list series (XLVII). Published in *Monthly Notices of the Royal Astronomical Society* (2022).

This is the first comprehensive molecular line list of [CaOH](../Molecules/CaOH.md) covering both the X̃²Σ⁺ rotation-vibration and the Ã²Π–X̃²Σ⁺ rotation-vibration-electronic (rovibronic) bands. The strong Ã–X̃ band around 16,000 cm⁻¹ (~625 nm) is highlighted as the most astrophysically important spectral feature, likely observable in hot rocky super-Earth exoplanets. CaOH had previously been identified as a missing opacity source in M-dwarf photospheric models (BT-Settl), alongside AlH and NaH.

The rovibronic calculations employ the EVEREST nuclear motion code. A key contribution is the extension of EVEREST to support potential energy surface (PES) refinement, enabling the Ã²Π state PES to be rigorously refined to experimental MARVEL data for the first time. This refinement improved Ã-state energy level accuracy by several orders of magnitude relative to ab initio values. The ground X̃²Σ⁺ PES was previously refined in an earlier study by the same group.

Post-processing for high-resolution applications: 1,614 computed energy levels (X̃ and Ã states, up to J=175.5) were replaced with empirically-derived MARVEL values where available. All computed energy levels carry a conservative estimated uncertainty of 10 cm⁻¹; MARVELized levels carry their individual MARVEL uncertainties.

## Line List Summary

| Isotopologue | ExoMol ID | Line list | States | Transitions | J_max | Wavenumber range | T_max | MARVEL | Reference |
|---|---|---|---|---|---|---|---|---|---|
| CaOH | [40Ca-16O-1H](../Molecules/40Ca-16O-1H.md) | OYT6 | 3,187,522 | 24,215,753,701 | 175.5 | 0–35,000 cm⁻¹ | ~3000 K | Yes (1614 levels) | [22OwMiYu](../Papers/22OwMiYu.md) |

## Key Methods

- **EVEREST** (extended): rovibronic nuclear motion code for triatomic molecules; treats Renner-Teller and spin-orbit coupling effects exactly. Extended in this work to perform PES refinement via the Hellmann-Feynman theorem and Newton's steepest descent least-squares fitting.
- **Ã state PES refinement**: 10 potential parameters of the two Renner-Taylor component surfaces refined simultaneously along with the spin-orbit coupling zeroth-order parameter. 308 term values up to J=28.5 used; RMS residual 0.318 cm⁻¹ against MARVEL energies.
- **Basis**: 100 Sinc-DVR functions each for the Ca-O (2.6–7.0 a₀) and O-H (1.1–6.0 a₀) stretches; 120 Legendre polynomials for the bond angle. Vibrational eigenfunctions computed up to 10,000 cm⁻¹ above the lowest vibronic state for |K|=0,1,2,3. Hamiltonian dimension 10,000; Renner-Teller coupled problem solved for |K|>0.
- **MARVEL**: 1,614 computed rovibronic energy levels replaced with empirical MARVEL values from the prior CaOH MARVEL analysis by the same group. Covers X̃ and Ã state levels up to J=175.5.
- **ExoCross**: partition function computed on a K grid from 1–4000 K; absolute absorption cross-sections simulated at 1 cm⁻¹ resolution (Gaussian HWHM = 1 cm⁻¹).
- **CDMS validation**: OYT6 pure-rotational stick spectrum compared to CDMS data; ground X̃ dipole moment 0.94 D (RCCSD(T)/aug-pwCVQZ-PP) vs CDMS value of 1.465 D — discrepancy discussed; OYT6 intensities consistent with other ab initio values (~0.98 D, semiempirical ~1.2 D).

## Astrophysical Context

CaOH had been flagged as a missing opacity source in M-dwarf BT-Settl photosphere models (alongside AlH and NaH). The OYT6 list completes that trio. The strong Ã²Π–X̃²Σ⁺ band at ~16,000 cm⁻¹ (~625 nm) dominates the CaOH spectrum even at T = 3000 K, making it the key detection target in hot rocky super-Earth exoplanet atmospheres (T up to ~4000 K). The list also supports laser cooling schemes for ultracold CaOH molecules (direct laser cooling to ~1 mK already achieved); Einstein coefficients from OYT6 enable branching ratio calculations.

The partition function is compared to JANAF values; OYT6 is more accurate as it sums over all rotation-vibration levels in both lowest electronic states. The Ã-state contribution to the partition function is near-negligible (<0.08% at 3000 K).

## People

- [Alec Owens](../People/A_Owens.md) (primary)
- [Alexander Mitrushchenkov](../People/A_Mitrushchenkov.md)
- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
