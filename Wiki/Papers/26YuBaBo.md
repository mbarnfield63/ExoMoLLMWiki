---
tags:
  - "paper"
bibcode: "26YuBaBo"
title: "ExoMol line lists -- LXIII: ExoMol line lists for 12 isotopologues of CO2"
authors:
  - "Sergei N. Yurchenko"
  - "Marco G. Barnfield"
  - "Charles A. Bowesman"
  - "Ryan P. Brady"
  - "Elizabeth R. Guest"
  - "Kyriaki Kefala"
  - "Qing-He Ni"
  - "Armando N. Perri"
  - "Oleksiy A. Smola"
  - "Andrei Sokolov"
  - "Chenyi Tao"
  - "Jonathan Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2026
summary: "Presents the 'Dozen' rovibrational line lists for 12 CO2 isotopologues computed with TROVE using the Ames-2 PES and Ames-2021-40K DMS, refined via empirical band-centre corrections and MARVELization from HITRAN/CDSD, with ML-based AFGL/Herzberg quantum number assignment, partition functions to 5000 K, and ExoMolOP opacities for ARCiS, TauREx, NEMESIS, and petitRADTRANS."
mentioned_methods:
  - "TROVE"
  - "MARVELization"
  - "ExoMolOP"
  - "ExoCross and PyExoCross"
  - "HITRAN"
  - "HITEMP"
  - "Partition Functions"
  - "Collisional Line Broadening"
  - "ExoMol Data Format"
  - "ARCiS"
  - "TauREx"
  - "NEMESIS"
  - "petitRADTRANS"
mentioned_molecules:
  - "CO2"
  - "12C-16O2"
  - "13C-16O2"
  - "12C-17O2"
  - "13C-17O2"
  - "12C-18O2"
  - "13C-18O2"
  - "16O-12C-17O"
  - "16O-12C-18O"
  - "16O-13C-17O"
  - "16O-13C-18O"
  - "17O-12C-18O"
  - "17O-13C-18O"
mentioned_people:
  - "Sergei N. Yurchenko"
  - "Marco G. Barnfield"
  - "Charles A. Bowesman"
  - "Ryan P. Brady"
  - "Elizabeth R. Guest"
  - "Kyriaki Kefala"
  - "Qing-He Ni"
  - "Armando N. Perri"
  - "Oleksiy A. Smola"
  - "Andrei Sokolov"
  - "Chenyi Tao"
  - "Jonathan Tennyson"
mentioned_applications:
  - "Exoplanet Atmospheres"
  - "Solar System Atmospheres"
  - "Terrestrial Applications"
  - "Opacity Modelling"
  - "Radiative Transfer"
status: "seed"
created: "2026-06-02"
updated: "2026-06-02"
sources:
  - "Raw/Sources/26YuBaBo.json"
source_count: 1
---

# ExoMol line lists -- LXIII: ExoMol line lists for 12 isotopologues of CO2

## Summary

This paper presents the "Dozen" line lists — a comprehensive set of rovibrational line lists for 12 isotopologues of CO2 (626, 636, 727, 737, 828, 838, 627, 628, 637, 638, 728, 738). Line lists were computed variationally using [[TROVE]] with the Ames-2 empirical PES and Ames-2021-40K ab initio DMS, covering 0–20 000 cm⁻¹. Calculated energies are refined by empirical band-centre corrections and MARVELization from MARVEL, HITRAN, and CDSD-2024-PI. A PyTorch multi-head neural network assigns AFGL and Herzberg quantum numbers to states not covered by MARVEL. Partition functions are computed on a 1 K grid to 5000 K. Opacities for four retrieval codes (ARCiS, TauREx, NEMESIS, petitRADTRANS) are generated via ExoMolOP. Source: [26YuBaBo](../../Raw/Sources/26YuBaBo.json).

## Bibliographic Details

- Journal: Monthly Notices of the Royal Astronomical Society
- Year: 2026
- DOI: (not available in sidecar)

## Key Results

- Line list name: **Dozen**
- 12 isotopologues covered: 12C-16O2, 13C-16O2, 12C-17O2, 13C-17O2, 12C-18O2, 13C-18O2, 16O-12C-17O, 16O-12C-18O, 16O-13C-17O, 16O-13C-18O, 17O-12C-18O, 17O-13C-18O
- Spectral range: 0–20 000 cm⁻¹
- Temperature range: up to 3000 K (main isotopologue); ~2000 K (minor isotopologues)
- PES: Ames-2 (Huang et al.)
- DMS: Ames-2021-40K (Huang et al.)
- Empirical energy sources: MARVEL analyses, HITRAN2020, CDSD-2024-PI
- AFGL/Herzberg quantum number assignment via ML (PyTorch multi-head network, MC Dropout uncertainty)
- Supersedes UCL-4000 for the main isotopologue 12C-16O2

## Mentioned Methods

- [TROVE](../Methods/TROVE.md)
- [MARVELization](../Methods/MARVELization.md)
- [ExoMolOP](../Methods/ExoMolOP.md)
- [ExoCross and PyExoCross](../Methods/ExoCross.md)
- [HITRAN](../Methods/HITRAN.md)
- [HITEMP](../Methods/HITEMP.md)
- [Partition Functions](../Methods/Partition_Functions.md)
- [Collisional Line Broadening](../Methods/Collisional_Line_Broadening.md)
- [ExoMol Data Format](../Methods/ExoMol_Data_Format.md)
- [ARCiS](../Methods/ARCiS.md)
- [TauREx](../Methods/TauREx.md)
- [NEMESIS](../Methods/NEMESIS.md)
- [petitRADTRANS](../Methods/petitRADTRANS.md)

## Mentioned Applications

- [Exoplanet Atmospheres](../Applications/Exoplanet_Atmospheres.md)
- [Solar System Atmospheres](../Applications/Solar_System_Atmospheres.md)
- [Terrestrial Applications](../Applications/Terrestrial_Applications.md)
- [Opacity Modelling](../Applications/Opacity_Modelling.md)
- [Radiative Transfer](../Applications/Radiative_Transfer.md)

## Mentioned Molecules

### Formula MOCs

- [CO2](../Molecules/CO2.md)

### Named Isotopologues

- [12C-16O2](../Molecules/12C-16O2.md)
- [13C-16O2](../Molecules/13C-16O2.md)
- [12C-17O2](../Molecules/12C-17O2.md)
- [13C-17O2](../Molecules/13C-17O2.md)
- [12C-18O2](../Molecules/12C-18O2.md)
- [13C-18O2](../Molecules/13C-18O2.md)
- [16O-12C-17O](../Molecules/16O-12C-17O.md)
- [16O-12C-18O](../Molecules/16O-12C-18O.md)
- [16O-13C-17O](../Molecules/16O-13C-17O.md)
- [16O-13C-18O](../Molecules/16O-13C-18O.md)
- [17O-12C-18O](../Molecules/17O-12C-18O.md)
- [17O-13C-18O](../Molecules/17O-13C-18O.md)

## Mentioned People

- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Marco G. Barnfield](../People/M_G_Barnfield.md)
- [Charles A. Bowesman](../People/C_A_Bowesman.md)
- [Ryan P. Brady](../People/R_P_Brady.md)
- [Elizabeth R. Guest](../People/E_R_Guest.md)
- [Kyriaki Kefala](../People/K_Kefala.md)
- [Qing-He Ni](../People/Q_H_Ni.md)
- [Armando N. Perri](../People/A_N_Perri.md)
- [Oleksiy A. Smola](../People/O_Smola.md)
- [Andrei Sokolov](../People/A_Sokolov.md)
- [Chenyi Tao](../People/C_Tao.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
