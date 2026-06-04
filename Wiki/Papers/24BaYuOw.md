---
tags:
  - "paper"
bibcode: "24BaYuOw"
title: "ExoMol line lists — LXV. Mid-Infrared rovibronic spectroscopy of isotopologues of NiH"
authors:
  - "K. Batrakov"
  - "S. N. Yurchenko"
  - "A. Owens"
  - "J. Tennyson"
  - "A. Mitrushchenkov"
  - "A. J. Ross"
  - "P. Crozet"
  - "A. Pashov"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2024
doi: ""
summary: "ExoMol LXV: BYOT line lists for four isotopologues of nickel monohydride (58NiH, 60NiH, 62NiH, 58NiD) covering 0–10,000 cm⁻¹, transitions within and between the three lowest-lying electronic states X²Δ, ²Π, and ²Σ⁺. Applicable up to 5000 K (recommended up to 3000 K). Spectroscopic model adapted from Havalyova et al. (2021) for the Duo variational code; ab initio MCSCF/aug-cc-pVTZ-DK dipole moment curves scaled to match the experimental ground-state dipole moment."
mentioned_methods:
  - "Duo"
  - "ExoCross"
  - "ExoMol Database"
mentioned_molecules:
  - "NiH"
  - "58Ni-1H"
  - "60Ni-1H"
  - "62Ni-1H"
  - "58Ni-2H"
mentioned_people:
  - "K_Batrakov"
  - "S_N_Yurchenko"
  - "A_Owens"
  - "J_Tennyson"
  - "A_Mitrushchenkov"
  - "A_J_Ross"
  - "P_Crozet"
  - "A_Pashov"
status: "complete"
created: "2026-06-04"
updated: "2026-06-04"
sources:
  - "Raw/Sources/24BaYuOw.json"
source_count: 1
---

# 24BaYuOw — ExoMol LXV: NiH BYOT line lists

Source: [24BaYuOw](../../Raw/Sources/24BaYuOw.json)

## Summary

Reports the **BYOT** line lists for four isotopologues of nickel monohydride — [58Ni-1H](../Molecules/58Ni-1H.md), [60Ni-1H](../Molecules/60Ni-1H.md), [62Ni-1H](../Molecules/62Ni-1H.md), and [58Ni-2H](../Molecules/58Ni-2H.md) — the 65th paper in the ExoMol line list series (LXV). Published in *Monthly Notices of the Royal Astronomical Society* (2024).

Line lists cover 0–10,000 cm⁻¹ with transitions within and between the three lowest-lying electronic states X²Δ, ²Π, and ²Σ⁺. Applicable for temperatures up to 5000 K; authors recommend use up to 3000 K. Calculated energies for 58NiH, 60NiH, and 62NiH are replaced with empirical values from Havalyova et al. (2021); 58NiD empirical energies from a separate source. Energy uncertainties are computed as a function of vibrational and rotational quantum numbers.

## Line List Summary

| Isotopologue | ExoMol ID | Line list | Wavenumber range | T_max | Empirical energies |
|---|---|---|---|---|---|
| ⁵⁸NiH | [58Ni-1H](../Molecules/58Ni-1H.md) | BYOT | 0–10,000 cm⁻¹ | 5000 K | Yes (Havalyova 2021) |
| ⁶⁰NiH | [60Ni-1H](../Molecules/60Ni-1H.md) | BYOT | 0–10,000 cm⁻¹ | 5000 K | Yes (Havalyova 2021) |
| ⁶²NiH | [62Ni-1H](../Molecules/62Ni-1H.md) | BYOT | 0–10,000 cm⁻¹ | 5000 K | Yes (Havalyova 2021) |
| ⁵⁸NiD | [58Ni-2H](../Molecules/58Ni-2H.md) | BYOT | 0–10,000 cm⁻¹ | 5000 K | Yes (separate source) |

## Key Methods

- **Duo**: variational nuclear-motion code solving coupled Schrödinger equations on a 301-point grid (Sinc DVR); spectroscopic model with PECs, SOCs, EAMCs, SRCs, BOB curves adapted from Havalyova et al. (2021) via EMO re-parameterisation
- **Ab initio DMCs**: MCSCF/aug-cc-pVTZ-DK dipole moment curves for X²Δ, ²Π, ²Σ⁺ states, scaled by factor 0.77 (ratio of experimental to theoretical ground-state dipole moment, 2.44 D observed vs. 3.13 D computed) 
- **ExoCross**: partition functions computed by summing over energy levels up to J_max; compared to NIST/Barklem & Collet estimates; ExoMol BYOT line lists available at www.exomol.com

## Astrophysical Context

NiH has cosmic abundance comparable to chromium or calcium. Its visible spectrum is masked by TiO bands in stellar atmospheres, but strong rotation-vibration and ro-vibronic systems are expected in the mid-infrared. These line lists are intended to aid detection of NiH in cool stellar atmospheres and other astrophysical environments. The partition function of NiH from prior literature (based only on the ground X²Δ state) is shown to be severely incomplete even at moderate temperatures.

## People

- [Kirill Batrakov](../People/K_Batrakov.md) (primary)
- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Alec Owens](../People/A_Owens.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
- [Alexander Mitrushchenkov](../People/A_Mitrushchenkov.md)
- [Amanda J. Ross](../People/A_J_Ross.md)
- [Patrick Crozet](../People/P_Crozet.md)
- [Asen Pashov](../People/A_Pashov.md)
