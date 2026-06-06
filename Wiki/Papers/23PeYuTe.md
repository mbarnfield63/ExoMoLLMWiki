---
tags:
  - "paper"
bibcode: "23PeYuTe"
title: "ExoMol line lists — LII: Line Lists for the Methylidyne Cation (CH+)"
authors:
  - "O. Pearce"
  - "S. N. Yurchenko"
  - "J. Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2023
doi: ""
summary: "ExoMol LII: PYT rovibronic line lists for 12C-1H+ and 13C-1H+ covering the X¹Σ⁺ and A¹Π states up to 5000 K. MARVEL applied to 12CH+ using 767 collected line positions from laboratory and astronomical sources; empirical energy levels replace LEVEL-16 calculated values where available. 12C-1H+: 1505 states, 34,194 transitions, 0–33,010 cm⁻¹, J_max=68. 13C-1H+: 1519 states, 42,387 transitions, J_max=69. λ-doubling in the A¹Π state treated empirically via expectation-value scaling of correction factors."
mentioned_methods:
  - "LEVEL"
  - "MARVELization"
  - "ExoCross"
  - "ExoMol Database"
mentioned_molecules:
  - "CH+"
  - "12C-1H+"
  - "13C-1H+"
mentioned_people:
  - "O_Pearce"
  - "S_N_Yurchenko"
  - "J_Tennyson"
status: "complete"
created: "2026-06-06"
updated: "2026-06-06"
sources:
  - "Raw/Sources/23PeYuTe.json"
source_count: 1
---

# 23PeYuTe — ExoMol LII: CH+ PYT line lists

Source: [23PeYuTe](../../Raw/Sources/23PeYuTe.json)

## Summary

Reports the **PYT** rovibronic line lists for [12C-1H+](../Molecules/12C-1H+.md) and [13C-1H+](../Molecules/13C-1H+.md) — the 52nd paper in the ExoMol line list series (LII). Published in *Monthly Notices of the Royal Astronomical Society* (2023).

Nuclear-motion calculations are performed with LEVEL-16 using empirical potential energy curves (PECs) from Cho & Le Roy for the X¹Σ⁺ and A¹Π states, and ab initio dipole and transition dipole moment curves. λ-doubling in the A¹Π state is not handled natively by LEVEL; an empirical correction scheme is implemented by computing the expectation value of the λ-doubling operator for each vibrational level and scaling by ratios derived from MARVEL observations, with extrapolation to higher levels. For 12CH+, MARVEL is applied to 767 collected line positions from laboratory and astronomical sources, and empirical energy levels replace LEVEL-16 calculated values in the States file where available (labelled 'Ma' vs 'Ca'). Insufficient data precluded a MARVEL study for 13CH+.

## Line List Summary

| Isotopologue | ExoMol ID | Line list | States | Transitions | J_max | Wavenumber range | MARVEL | Reference |
|---|---|---|---|---|---|---|---|---|
| ¹²CH⁺ | [12C-1H+](../Molecules/12C-1H+.md) | PYT | 1,505 | 34,194 | 68 | 0–33,010 cm⁻¹ | Yes | [23PeYuTe](../Papers/23PeYuTe.md) |
| ¹³CH⁺ | [13C-1H+](../Molecules/13C-1H+.md) | PYT | 1,519 | 42,387 | 69 | — | No | [23PeYuTe](../Papers/23PeYuTe.md) |

## Key Methods

- **LEVEL-16**: nuclear-motion code solving the radial Schrödinger equation; used to compute rovibronic energy levels and Einstein coefficients within the X¹Σ⁺ and A¹Π potentials; input PECs from Cho & Le Roy (empirical direct-potential-fit). Source code modified to resolve parameter ordering errors and to read DM/TDM curves and compute Einstein A coefficients.
- **MARVEL**: 767 ¹²CH⁺ transitions collected from laboratory and astronomical sources (including 97CeLiGoCo and 21NeGoChFa as astronomical observations); uncertainties for older sources increased for self-consistency; 2 lines excluded. MARVEL energy levels used to replace calculated values in the States file.
- **λ-doubling correction**: empirical expectation-value scheme applied per vibrational level of A¹Π; correction factors scaled by ratios from MARVEL observations, with exponential extrapolation to higher vibrational levels.
- **ExoCross**: used to calculate partition functions (0–10,000 K in 1 K steps) and simulate absorption/emission spectra.

## Astrophysical Context

CH⁺ was among the first molecules — and the first molecular ion — detected in interstellar space. It is ubiquitous in diffuse clouds, protostellar disks, star-forming regions, and extragalactic sources. Strong A¹Π–X¹Σ⁺ emission is observed in the Red Rectangle nebula (HD 44179). CH⁺ acts as an intermediary in interstellar hydrocarbon formation, contributing to the build-up of C₂, CN, CO, and CH. Its observed abundance historically exceeded chemical-network predictions by orders of magnitude, motivating sustained investigation into its formation and destruction pathways.

## People

- [Oliver Pearce](../People/O_Pearce.md) (primary)
- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
