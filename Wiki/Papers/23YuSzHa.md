---
tags:
  - "paper"
bibcode: "23YuSzHa"
title: "ExoMol line lists — LIV: Empirical line lists for AlH and AlD and experimental emission spectroscopy of AlD"
authors:
  - "S. N. Yurchenko"
  - "W. Szajna"
  - "R. Hakalla"
  - "M. Semenov"
  - "A. Sokolov"
  - "J. Tennyson"
  - "R. R. Gamache"
  - "Y. Pavlenko"
  - "M. R. Schmidt"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2023
doi: ""
summary: "ExoMol LIV: Improved AloHa line lists for 27AlH, 27AlD, and 26AlH, replacing the earlier WYLLoT line lists. New FT-VIS emission spectroscopy of ten AlD A¹Π–X¹Σ⁺ bands at University of Rzeszów. MARVEL analysis yields 346 empirical energy levels for AlH and 423 for AlD. Spectroscopic model (Duo) uses diabatic treatment of the predissociative B¹Σ⁺ state; predissociative lifetimes included in the ExoMol States file for the first time. Temperature-dependent photo-absorption cross sections (100–5000 K) and collisional broadening parameters (H₂, He, N₂, AlH) via MCRB also provided."
mentioned_methods:
  - "Duo"
  - "MARVELization"
  - "ExoCross"
  - "ExoMol Database"
mentioned_molecules:
  - "AlH"
  - "27Al-1H"
  - "27Al-2H"
  - "26Al-1H"
mentioned_people:
  - "S_N_Yurchenko"
  - "W_Szajna"
  - "R_Hakalla"
  - "M_Semenov"
  - "A_Sokolov"
  - "J_Tennyson"
  - "R_R_Gamache"
  - "Y_Pavlenko"
  - "M_R_Schmidt"
status: "complete"
created: "2026-06-05"
updated: "2026-06-05"
sources:
  - "Raw/Sources/23YuSzHa.json"
source_count: 1
---

# 23YuSzHa — ExoMol LIV: AlH / AlD AloHa line lists

Source: [23YuSzHa](../../Raw/Sources/23YuSzHa.json)

## Summary

Reports the **AloHa** line lists for [27Al-1H](../Molecules/27Al-1H.md), [27Al-2H](../Molecules/27Al-2H.md), and [26Al-1H](../Molecules/26Al-1H.md) — the 54th paper in the ExoMol line list series (LIV). Published in *Monthly Notices of the Royal Astronomical Society* (2023). Replaces the earlier WYLLoT (AlHambra) line lists from Yurchenko et al. (2018).

New FT-VIS emission spectra of ten AlD A¹Π–X¹Σ⁺ bands were recorded with a Fourier transform spectrometer (Bruker IFS-125HR) at the University of Rzeszów, including the (2-1) and (2-2) bands reported for the first time. These data are combined with all available experimental data on AlH and AlD through the MARVEL algorithm to derive comprehensive empirical rovibronic energy sets covering the X¹Σ⁺ and A¹Π states.

The spectroscopic model was refined using the Duo variational code with a diabatic treatment of the predissociative B¹Σ⁺ state. AlD was processed first (14 free parameters, rms 0.06 cm⁻¹ over 423 MARVEL energies), then AlH (8 free parameters, rms 0.08 cm⁻¹ over 346 MARVEL energies). Predissociative lifetimes are included in the ExoMol States file for the first time. The new line lists reproduce the heavily predissociated lines in the Proxima Centauri spectrum that WYLLoT could not describe.

## Line List Summary

| Isotopologue | ExoMol ID | Line list | Wavenumber range | T_max | MARVEL | Reference |
|---|---|---|---|---|---|---|
| ²⁷AlH | [27Al-1H](../Molecules/27Al-1H.md) | AloHa | 0–30,000 cm⁻¹ | 5000 K | Yes (346 levels) | [23YuSzHa](../Papers/23YuSzHa.md) |
| ²⁷AlD | [27Al-2H](../Molecules/27Al-2H.md) | AloHa | 0–30,000 cm⁻¹ | 5000 K | Yes (423 levels) | [23YuSzHa](../Papers/23YuSzHa.md) |
| ²⁶AlH | [26Al-1H](../Molecules/26Al-1H.md) | AloHa | 0–30,000 cm⁻¹ | 5000 K | No | [23YuSzHa](../Papers/23YuSzHa.md) |

## Key Methods

- **Duo**: variational diatomic nuclear-motion code; Sinc DVR on 1601-point grid (0.5–13.5 Å); diabatic representation of B¹Σ⁺ predissociative state coupled to a dummy repulsive state via EMO-type coupling function
- **MARVEL**: combined all available AlH and AlD experimental transition frequencies (16 sources for AlH, 10 sources for AlD) into consistent empirical energy level sets
- **MCRB**: semi-classical approach for collisional line-broadening coefficients (H₂, He, N₂, AlH broadening); included in ExoMol database via diet format with new !m0! type for P/R-branch dependence
- **ExoCross / pyExoCross**: spectrum simulation including predissociative line broadening via state lifetimes

## Astrophysical Context

AlH has been observed in the Mira variable o Ceti, in the photosphere of χ Cygni, and in the spectrum of Proxima Cen (M6 V). The WYLLoT line list failed to describe the predissociative broadening of high-J A¹Π–X¹Σ⁺ lines in Proxima Cen, which motivated this work. The new AloHa line list also supplies temperature-dependent photo-absorption cross sections (100–5000 K) for the continuum contribution from bound-to-free transitions. The minor isotopologue ²⁶Al is radioactive (t½ ≈ 710 000 yr) and has been detected in the Milky Way.

## People

- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md) (primary)
- [Wojciech Szajna](../People/W_Szajna.md)
- [Rafał Hakalla](../People/R_Hakalla.md)
- [Mikhail Semenov](../People/M_Semenov.md)
- [Andrei Sokolov](../People/A_Sokolov.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
- [Robert R. Gamache](../People/R_R_Gamache.md)
- [Yakiv Pavlenko](../People/Y_Pavlenko.md)
- [Mirek R. Schmidt](../People/M_R_Schmidt.md)
