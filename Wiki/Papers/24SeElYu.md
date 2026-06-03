---
tags:
  - "paper"
bibcode: "24SeElYu"
title: "ExoMol line lists -- LXIV: Empirical rovibronic spectra of phosphorous mononitride (PN) covering the IR and UV regions"
authors:
  - "Mikhail Semenov"
  - "Nayla El-Kork"
  - "Sergei N. Yurchenko"
  - "Jonathan Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2024
summary: "Presents PaiN, the ExoMol line list for 31P-14N (ExoMol series LXIV). Replaces the YYLT line list by extending coverage to the A1Pi-X1Sigma+ vibronic system (IR and UV). MARVELised with 1224 empirical energy levels from 6005 transitions across 8 active experimental sources (1933-2006). Model computed with Duo; 30327 states and 1333445 transitions for 31P-14N, valid up to 5000 K and wavenumbers 0-82500 cm-1 (>121 nm). A1Pi state modelled with PGOPHER EH to fill MARVEL gaps around vibronic perturbations from dark states."
mentioned_methods:
  - "Duo"
  - "MARVELization"
  - "ExoCross"
  - "ExoMolOP"
  - "ExoMol Database"
  - "Partition Functions"
mentioned_molecules:
  - "PN"
  - "31P-14N"
mentioned_people:
  - "M_Semenov"
  - "N_El-Kork"
  - "S_N_Yurchenko"
  - "J_Tennyson"
status: "complete"
created: "2026-06-03"
updated: "2026-06-03"
sources:
  - "Raw/Sources/24SeElYu.json"
source_count: 1
---

# 24SeElYu — ExoMol line lists LXIV: PN PaiN

Source: [24SeElYu](../../Raw/Sources/24SeElYu.json)

## Summary

Presents **PaiN**, the ExoMol rovibronic line list for ³¹P¹⁴N (ExoMol series LXIV, the 64th paper). Replaces the earlier YYLT line list by extending coverage from the X¹Σ⁺ ground state to include the A¹Π excited state, covering the IR through UV. The spectroscopic model is built with Duo, refining ab initio PECs and coupling curves from [Semenov et al. 2021] to 1224 MARVEL empirical energy levels. The A¹Π state is heavily perturbed by multiple dark states (e³Σ⁻, b³Π, d³Δ, D¹Δ, C¹Σ⁻) at vibronic crossings in v=0,1,2,3,7; PGOPHER effective Hamiltonian values are used to fill MARVEL gaps in the A state coverage.

## Line List: PaiN

| Property | Value |
|---|---|
| States (³¹P¹⁴N) | 30,327 |
| Transitions (³¹P¹⁴N) | 1,333,445 |
| States (³¹P¹⁵N) | 31,563 |
| Transitions (³¹P¹⁵N) | 1,438,181 |
| ν range (cm⁻¹) | 0–82,500 |
| Wavelength cutoff | >121 nm |
| T max (K) | 5,000 |
| Electronic states | X¹Σ⁺, A¹Π |
| MARVEL | yes |
| Replaces | YYLT |

## MARVELisation

| Property | Value |
|---|---|
| MARVEL energy levels | 1,224 |
| MARVEL transitions used | 6,005 |
| Active experimental sources | 8 |
| Excluded from MARVEL | 2 (81CoPr E–X band; 87VeGhIq unassigned) |
| Latest source year | 2006 (06CaClPu) |

### Experimental Sources

| Key | Year | System | Available/Validated |
|---|---|---|---|
| 33CuHeHe | 1933 | A–X | 570 / 199 |
| 72HoTiTo | 1972 | X–X | 2 / 2 |
| 72WyGoMa | 1972 | X–X | 19 / 19 |
| 81GhVeVa | 1981 | A–X | 2188 / 1586 |
| 81MaLo | 1981 | X–X | 22 / 22 |
| 95AhHa | 1995 | X–X | 62 / 61 |
| 96LeMeDu | 1996 | A–X | 1680 / 959 |
| 06CaClPu | 2006 | X–X | 16 / 16 |

## Key Methods

- **Duo**: variational diatomic nuclear motion code; sinc DVR on 701-point grid 1.0–5.0 Å; coupled X¹Σ⁺ and A¹Π states only; 12 parameters fitted
- **MARVEL**: MARVEL4 algorithm; 1224 energy levels from X and A states; J=0–61
- **PGOPHER**: effective Hamiltonian fills A state gaps in v=2,3,4,5,6,7,9 for J=0–30
- **ExoCross**: radiative lifetimes calculated; A v=0 lifetime 222.9 ns (experimental: 227 ± 70 ns)
- **ExoMolOP**: opacities for ARCiS, TauREx, NEMESIS, petitRADTRANS (86% H₂ + 14% He Voigt profile)

## People

- [Mikhail Semenov](../People/M_Semenov.md) (primary)
- [Nayla El-Kork](../People/N_El-Kork.md)
- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
