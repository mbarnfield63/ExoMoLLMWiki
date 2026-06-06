---
tags:
  - "paper"
bibcode: "23OwWrPa"
title: "ExoMol line lists — LI: Molecular line list for lithium hydroxide (LiOH)"
authors:
  - "A. Owens"
  - "S. O. M. Wright"
  - "Y. Pavlenko"
  - "A. Mitrushchenkov"
  - "J. Koput"
  - "S. N. Yurchenko"
  - "J. Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2023
doi: ""
summary: "ExoMol LI: OYT7 rovibrational line list for 7Li-16O-1H covering 0–10,000 cm⁻¹, applicable up to ~4000 K (soft limit). Ab initio PES (CCSD(T)/aug-cc-pCV6Z, previously published) and new DMS (CCSD(T)/aug-cc-pCVQZ/aug-cc-pVQZ). Variational nuclear motion with Sinc-DVR + Legendre basis, J_max=95. 331,274,717 transitions between 203,762 states. Not MARVELized — no gas-phase rovibrational data for LiOH. ExoMolOP opacities generated for ARCiS, TauREx, NEMESIS, petitRADTRANS. TauREx-III simulated spectra for 55 Cancri e."
mentioned_methods:
  - "ExoMol Database"
  - "ExoMolOP"
  - "ExoCross"
  - "TauREx"
  - "NEMESIS"
  - "ARCiS"
  - "petitRADTRANS"
  - "MARVEL"
mentioned_molecules:
  - "LiOH"
  - "7Li-16O-1H"
mentioned_people:
  - "A_Owens"
  - "S_O_M_Wright"
  - "Y_Pavlenko"
  - "A_Mitrushchenkov"
  - "J_Koput"
  - "S_N_Yurchenko"
  - "J_Tennyson"
status: "complete"
created: "2026-06-06"
updated: "2026-06-06"
sources:
  - "Raw/Sources/23OwWrPa.json"
source_count: 1
---

# 23OwWrPa — ExoMol LI: LiOH OYT7 line list

Source: [23OwWrPa](../../Raw/Sources/23OwWrPa.json)

## Summary

Reports the **OYT7** rovibrational line list for [7Li-16O-1H](../Molecules/7Li-16O-1H.md) — the 51st paper in the ExoMol line list series (LI). Published in *Monthly Notices of the Royal Astronomical Society* (2023).

Line list calculations use a high-level ab initio PES (CCSD(T)/aug-cc-pCV6Z, previously published) and a newly computed DMS (CCSD(T)/aug-cc-pCVQZ for Li and O; aug-cc-pVQZ for H; using MOLPRO2015). A variational nuclear motion code is employed with a discrete variable representation (DVR) basis: 100 Sinc-DVR functions each for the Li-O (2.0–7.0 bohr) and O-H (1.1–6.0 bohr) stretches, and 120 Legendre polynomials for the bending angle. Vibrational eigenfunctions up to 10,000 cm⁻¹ are computed for K=0,1 with a Hamiltonian of dimension 10,000; the full rovibrational Hamiltonian is then diagonalised up to J=95. Zero-point energy: 2780.676 cm⁻¹. Predicted fundamentals: ~640 cm⁻¹ (Li-O stretch), ~317 cm⁻¹ (Li-O-H bend), ~3740 cm⁻¹ (O-H stretch), expected accurate to within ~1 cm⁻¹ on average.

No gas-phase rovibrational spectroscopic data exist for LiOH, so MARVELization is not possible. The line list is validated against CDMS pure-rotational data (ground vibrational state), showing good band shape agreement. A partition function comparison with CDMS reveals that CDMS accounts only for the ground vibrational state — low-lying bending states contribute substantially at astrophysically relevant temperatures.

ExoMolOP opacities are generated for four retrieval codes (ARCiS, TauREx, NEMESIS, petitRADTRANS) on a 27-point temperature grid (100–3400 K). TauREx-III forward modelling produces transit and emission spectra for 55 Cancri e in H₂O/CO₂-dominated and mineral-vapour-dominated scenarios. The strongest LiOH bands (O-H stretch at 2.6 µm; NIR at 1.35 µm) overlap with H₂O features; the bending mode at 6.7 µm is within a spectral window but may be too weak to detect.

## Line List Summary

| Isotopologue | ExoMol ID | Line list | States | Transitions | J_max | Wavenumber range | T_max | MARVEL | Reference |
|---|---|---|---|---|---|---|---|---|---|
| ⁷LiOH | [7Li-16O-1H](../Molecules/7Li-16O-1H.md) | OYT7 | 203,762 | 331,274,717 | 95 | 0–10,000 cm⁻¹ | ~4000 K | No | [23OwWrPa](../Papers/23OwWrPa.md) |

## Key Methods

- **Ab initio PES**: CCSD(T)/aug-cc-pCV6Z composite approach including core-valence correlation, higher-order CC terms beyond perturbative triples, scalar relativistic effects, and diagonal Born-Oppenheimer correction. Tenth-order polynomial expansion in valence coordinates (44 parameters).
- **New DMS**: CCSD(T)/aug-cc-pCVQZ (Li, O) + aug-cc-pVQZ (H), 274 grid points. Fitted to sixth-order expansions: Aₓ component (72 parameters), Aᵧ component (64 parameters). Dipole moment at equilibrium ~4.755 D (consistent with CDMS value).
- **Variational nuclear motion**: Sinc-DVR basis + Legendre polynomials; vibrational step with Hamiltonian dimension 10,000; full rovibrational diagonalisation up to J=95.
- **ExoCross**: partition function on 1–4000 K grid and cross-section simulations (1 cm⁻¹ Gaussian profile).
- **ExoMolOP**: k-table opacities on 27 temperatures (100–3400 K) × 22 pressures for ARCiS, TauREx, NEMESIS, petitRADTRANS.
- **TauREx-III**: forward modelling of transit and emission spectra for 55 Cancri e.
- **CDMS**: validation of pure-rotational intensities and partition function.

## Astrophysical Context

LiOH is one of the most abundant Li-bearing molecules in late L- and T-dwarf atmospheres (alongside LiF and LiCl), where temperatures are too low for atomic Li to dominate. The lithium test — detecting Li lines in ultracool dwarf spectra to confirm substellar nature — requires accurate LiOH opacity data. The OYT7 line list is the first comprehensive line list for LiOH and enables future molecular detection in exoplanet and brown dwarf atmospheres. The paper notes that the OYT7 LiOH line list joins ExoMol line lists for NaOH and KOH, and that the CaOH ExoMol line list was produced using the same variational nuclear motion code.

## People

- [Alec Owens](../People/A_Owens.md) (primary)
- [Samuel O.M. Wright](../People/S_O_M_Wright.md)
- [Yakiv Pavlenko](../People/Y_Pavlenko.md)
- [Alexander Mitrushchenkov](../People/A_Mitrushchenkov.md)
- [Jacek Koput](../People/J_Koput.md)
- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
