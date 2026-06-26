---
tags:
  - "paper"
bibcode: "19McMaJe"
title: "ExoMol Molecular linelists -- XXXIII. The spectrum of Titanium Oxide"
authors:
  - "Laura K. McKemmish"
  - "Thomas Masseron"
  - "H. Jens Hoeijmakers"
  - "Víctor Pérez-Mesa"
  - "Simon L. Grimm"
  - "Sergei N. Yurchenko"
  - "Jonathan Tennyson"
year: 2019
journal: "Monthly Notices of the Royal Astronomical Society"
doi: ""
exomol_series: "XXXIII"
summary: "ExoMol XXXIII: Toto line lists for five TiO isotopologues (46Ti-16O, 47Ti-16O, 48Ti-16O, 49Ti-16O, 50Ti-16O) covering 13 coupled low-lying electronic states. 48Ti-16O: 301,245 energy levels (17,802 empirically refined), 58,983,952 transitions, J_max=200, ≤30,000 cm⁻¹, T≤5000 K. Ab initio PECs/SOCs/couplings at icMRCI level, refined empirically using Duo. Minor isotopologues generated via isotopologue extrapolation. Line lists validated against M-dwarf spectra (GJ876, GL581, Wolf 359) and laboratory Kitt Peak emission spectra."
mentioned_molecules:
  - "TiO"
  - "46Ti-16O"
  - "47Ti-16O"
  - "48Ti-16O"
  - "49Ti-16O"
  - "50Ti-16O"
mentioned_methods:
  - "Duo"
  - "MARVELization"
  - "ExoMol Database"
  - "ExoCross and PyExoCross"
  - "Isotopologue Extrapolation"
mentioned_people:
  - "L_K_McKemmish"
  - "T_Masseron"
  - "H_J_Hoeijmakers"
  - "V_Perez-Mesa"
  - "S_L_Grimm"
  - "S_N_Yurchenko"
  - "J_Tennyson"
sources:
  - "Raw/Sources/19McMaJe.json"
source_count: 1
created: "2026-06-26"
updated: "2026-06-26"
---

# 19McMaJe

ExoMol XXXIII: [19McMaJe](../../Raw/Sources/19McMaJe.json). Toto line lists for five isotopologues of titanium oxide (TiO), covering 13 low-lying coupled electronic states. Variational nuclear-motion calculations using Duo with ab initio PECs and coupling curves at icMRCI level, iteratively refined to MARVEL empirical energy levels. Ab initio diagonal and off-diagonal dipole moment curves computed at MRCI/aug-cc-pVQZ (SS/MS CASSCF). Line lists validated against M-dwarf optical spectra (GJ876, GL581 via HARPS; Wolf 359 via UVES) and laboratory Kitt Peak emission spectra. Line lists available at CDS and ExoMol.

Source: [19McMaJe](../../Raw/Sources/19McMaJe.json)

## Line List Summary

| Isotopologue | Line list | N states | N transitions | J_max | Coverage | T max |
| --- | --- | --- | --- | --- | --- | --- |
| [48Ti-16O](../Molecules/48Ti-16O.md) | Toto | 301,245 | 58,983,952 | 200 | ≤30,000 cm⁻¹ (≥ 0.33 μm) | 5000 K |
| [46Ti-16O](../Molecules/46Ti-16O.md) | Toto | — | — | — | ≤30,000 cm⁻¹ | 5000 K |
| [47Ti-16O](../Molecules/47Ti-16O.md) | Toto | — | — | — | ≤30,000 cm⁻¹ | 5000 K |
| [49Ti-16O](../Molecules/49Ti-16O.md) | Toto | — | — | — | ≤30,000 cm⁻¹ | 5000 K |
| [50Ti-16O](../Molecules/50Ti-16O.md) | Toto | — | — | — | ≤30,000 cm⁻¹ | 5000 K |

## Electronic States Covered

13 low-lying electronic states of TiO included in the spectroscopic model. Strongest observable bands: A–X (α-band, triplet), B–X (β-band, triplet), C–X (γ-band, triplet), E–X. Singlet states contribute <7% of population at 3000 K. States without reliable experimental observations (five higher states) included via ab initio energies only; their dipole transitions are excluded from the model as results are qualitative.

## Methods

- **Nuclear motion:** Duo; variational solution of fully coupled rovibronic Schrödinger equation; sinc DVR grid (301 points, 1.2–4.0 Å); vibrational basis contracted to 30 per state; J_max = 200.
- **PECs:** Extended Morse oscillator (EMO) functional form; parameters iteratively refined against MARVEL empirical energy levels, one electronic state at a time.
- **SOCs and couplings:** Constant diagonal spin-orbit parameters refined against experiment; off-diagonal SOC and L-coupling terms from icMRCI/aug-cc-pVDZ (SS/MS CASSCF, biorth keyword in Molpro 2015); explicit λ-doubling terms used for E–X coupling.
- **Diagonal DMCs:** icMRCI/aug-cc-pVQZ (SS/MS CASSCF); ionic-neutral diabatic functional form fitted to ab initio grid points.
- **Off-diagonal DMCs (triplet):** New icMRCI/aug-cc-pVQZ calculations; fitted to arctan functional form. Singlet off-diagonal DMCs adopted from Langhoff (1991).
- **Empirical refinement:** MARVEL-derived energy levels (collated by Balf et al.); 17,802 of 301,245 energy levels in the 48Ti-16O states file replaced with empirical values.
- **Minor isotopologues:** Generated via isotopologue extrapolation (predicted isotopic energy differences from Duo added to 48Ti-16O MARVEL energies).
- **Spectral simulations and partition functions:** ExoCross; partition functions computed at 1 K intervals to 8000 K.

## MARVEL

MARVEL analysis of 48Ti-16O collated all available experimentally assigned ro-vibrational and ro-electronic data; 17,802 of the 301,245 energy levels in the original Toto states file were replaced with empirically derived values. The 2024 Toto update ([24McBoKe](../Papers/24McBoKe.md)) clarified the MARVEL-validated subset as 10,761 energy levels (original 2019) and expanded it to 12,164 by adding E–X, B–X, and X rovibrational datasets from 19BrWaTu and 21WiBrDo.

## Evidence

Paper explicitly reports Toto line list for 48Ti-16O: 301,245 energy levels, 58,983,952 transitions, J_max=200, coverage up to 30,000 cm⁻¹, T≤5000 K. Partition function computed following HITRAN convention with full nuclear spin degeneracy. Lifetimes computed via ExoCross; agreement with experimental A and B state lifetimes is close. Cross-correlation validation against M-dwarf spectra shows improvement over Plez-2012 across 430–900 nm, with significant gains at 840–850 nm and 450–470 nm. Source: [19McMaJe](../../Raw/Sources/19McMaJe.json)
