---
tags:
  - "paper"
bibcode: "24YuMeTe"
title: "ExoMol line lists -- LIX. High-temperature line list for N2O"
authors:
  - "Sergei N. Yurchenko"
  - "Thomas M. Mellor"
  - "Jonathan Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2024
summary: "Presents the TYM rovibrational line lists for five isotopologues of N2O (14N2-16O, 14N2-17O, 14N2-18O, 14N-15N-16O, 15N-14N-16O) computed with TROVE using a new empirical PES refined against 17532 MARVEL energy levels and the ab initio Ames-1 DMS, valid to 2000 K and 20000 cm-1 with J up to 160. The parent 14N2-16O states file is MARVELised, yielding 365041 lines with experimentally accurate positions. Introduces an artificial symmetry group Cns(n) for efficient ro-vibrational basis set construction for linear non-symmetric XYZ molecules. ExoMolOP opacities provided for ARCiS, TauREx, NEMESIS, and petitRADTRANS."
mentioned_methods:
  - "TROVE"
  - "MARVELization"
  - "ExoMolOP"
  - "HITRAN"
  - "HITEMP"
  - "Partition Functions"
mentioned_molecules:
  - "N2O"
  - "14N2-16O"
  - "14N2-17O"
  - "14N2-18O"
  - "14N-15N-16O"
  - "15N-14N-16O"
mentioned_people:
  - "S_N_Yurchenko"
  - "T_M_Mellor"
  - "J_Tennyson"
status: "complete"
created: "2026-06-03"
updated: "2026-06-03"
sources:
  - "Raw/Sources/24YuMeTe.json"
source_count: 1
---

# 24YuMeTe — ExoMol line lists LIX: N2O TYM

Source: [24YuMeTe](../../Raw/Sources/24YuMeTe.json)

## Summary

Presents the **TYM** ro-vibrational line lists for five isotopologues of N₂O computed with the variational program TROVE. The empirical PES was refined by fitting to 17,532 MARVEL energy levels of ¹⁴N₂¹⁶O derived by Tennyson et al. (2024, JQSRT 316, 108902). The ab initio Ames-1 DMS from Huang et al. (2023) was used for intensities.

## Line List: TYM

| Isotopologue | States | Transitions | T max (K) | ν max (cm⁻¹) | J max | MARVEL |
|---|---|---|---|---|---|---|
| 14N2-16O | 2,078,676 | 1,532,806,222 | 2000 | 20000 | 160 | yes |
| 14N2-17O | — | ~1.3–1.7 billion | 2000 | 20000 | 160 | no |
| 14N2-18O | — | ~1.3–1.7 billion | 2000 | 20000 | 160 | no |
| 14N-15N-16O | — | ~1.3–1.7 billion | 2000 | 20000 | 160 | no |
| 15N-14N-16O | — | ~1.3–1.7 billion | 2000 | 20000 | 160 | no |

The TYM line lists and ExoMolOP opacities are available from [ExoMol](https://exomol.com/data/molecules/N2O/14N2-16O/TYM).

## MARVELisation

The ¹⁴N₂¹⁶O states file is MARVELised: 17,532 empirical MARVEL energies (J = 0–80) replace calculated TROVE values where available, producing 365,041 lines with experimentally accurate positions. Source: jt908 (Tennyson et al. 2024).

## Key Methods

- **TROVE**: variational nuclear motion, exact KEO, bisector frame, associated Laguerre polynomials
- **Artificial symmetry group Cns(n)**: new construction for linear non-symmetric XYZ molecules
- **Ames-1 DMS**: CCSD(T)/aug-cc-pV(T,Q,5)Z level, Huang et al. (2023)
- **MARVEL PES refinement**: PES fitted to 6563 energies (J = 0, 1, 2, 3, 4, 5, 8, 10, …, 80), RMS 0.02 cm⁻¹

## People

- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md) (primary)
- [Thomas M. Mellor](../People/T_M_Mellor.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
