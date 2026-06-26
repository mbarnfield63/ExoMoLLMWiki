---
tags:
  - "paper"
bibcode: "19YuSzPy"
title: "ExoMol line lists XXXI: Spectroscopy of lowest eight electronic states of C2"
authors:
  - "Sergei N. Yurchenko"
  - "István Szabó"
  - "Elizaveta Pyatenko"
  - "Jonathan Tennyson"
year: 2019
journal: "Monthly Notices of the Royal Astronomical Society"
doi: ""
exomol_series: "XXXI"
summary: "ExoMol XXXI: 8states rovibronic line lists for three isotopologues of C2 (12C2, 13C2, 12C13C), covering the eight lowest electronic states (singlet and triplet: X¹Σg⁺, a³Πu, b³Σg⁻, c³Σu⁺, A¹Πu, d³Πg, B'¹Σg⁺, e³Πg). 12C2: 44,189 states, 6,080,920 transitions; 13C2: 94,003 states, 13,361,992 transitions; 12C13C: 91,067 states, 12,743,954 transitions. Coverage 0–50,000 cm⁻¹ (≥ 0.25 μm). Duo nuclear motion code with MRCI/aug-cc-pwCVQZ-DK PECs/TDMs refined to 4900 MARVEL energies of 12C2. Partition functions to 10,000 K. MARVELized (12C2 .states file)."
mentioned_molecules:
  - "C2"
  - "12C2"
  - "13C2"
  - "12C-13C"
mentioned_methods:
  - "Duo"
  - "MOLPRO"
  - "MARVELization"
  - "ExoCross and PyExoCross"
  - "ExoMol Database"
  - "DVR"
mentioned_people:
  - "S_N_Yurchenko"
  - "I_Szabo"
  - "E_Pyatenko"
  - "J_Tennyson"
sources:
  - "Raw/Sources/19YuSzPy.json"
source_count: 1
created: "2026-06-26"
updated: "2026-06-26"
---

# 19YuSzPy

ExoMol XXXI: [19YuSzPy](../../Raw/Sources/19YuSzPy.json). Rovibronic 8states line lists for three isotopologues of the carbon dimer C2 (12C2, 13C2, 12C13C), covering the eight lowest electronic states (singlet and triplet). Duo nuclear motion calculations with MRCI/aug-cc-pwCVQZ-DK potential energy and transition dipole moment curves, empirically refined to 4900 MARVEL energies of 12C2. Line lists are MARVELized (MARVEL values substituted in 12C2 .states file). Partition functions to 10,000 K. Benchmarked against carbon star, comet, and high-temperature plasma spectra.

Source: [19YuSzPy](../../Raw/Sources/19YuSzPy.json)

## Line List Summary

| Isotopologue | Line list | N states | N transitions | Coverage |
| --- | --- | --- | --- | --- |
| [12C2](../Molecules/12C2.md) | 8states | 44,189 | 6,080,920 | 0–50,000 cm⁻¹ (≥ 0.25 μm) |
| [13C2](../Molecules/13C2.md) | 8states | 94,003 | 13,361,992 | 0–50,000 cm⁻¹ (≥ 0.25 μm) |
| [12C-13C](../Molecules/12C-13C.md) | 8states | 91,067 | 12,743,954 | 0–50,000 cm⁻¹ (≥ 0.25 μm) |

## Electronic States Covered

Eight lowest electronic states (singlet and triplet): X¹Σg⁺, a³Πu, b³Σg⁻, c³Σu⁺, A¹Πu, d³Πg, B'¹Σg⁺, e³Πg. Six electric-dipole-allowed band systems included: Phillips (A¹Πu–X¹Σg⁺), Swan (d³Πg–a³Πu), Ballik-Ramsay (b³Σg⁻–a³Πu), Duck (B'¹Σg⁺–A¹Πu), Bernath, and the singlet-triplet intercombination band.

## Methods

- **Nuclear motion:** Duo; fully coupled Schrödinger equation; sinc DVR vibrational basis, 401 grid points (0.85–4 Å).
- **Electronic structure:** MRCI/aug-cc-pwCVQZ-DK in MOLPRO; spin-orbit (SOC) and electronic angular momentum (EAMC) curves computed ab initio and morphed empirically.
- **PEC representation:** Extended Morse oscillator (EMO) functions; diabatic representation for states with avoided crossings (d, B', e).
- **Couplings:** Spin-spin, spin-rotation, and Λ-doubling (Π and Δ states); Born-Oppenheimer breakdown (BOB) for the X state; 89 parameters total.
- **Refinement:** Fitted to 4900 MARVEL energies of 12C2; robust weighting; MARVEL values replace theoretical energies in .states file where available (flagged `!m!`).
- **Spectral simulations:** ExoCross.

## MARVEL

MARVELized using 4900 experimentally-derived energy levels of 12C2 from a prior MARVEL study. MARVEL energies are substituted into the final 12C2 .states file. The 13C2 and 12C13C line lists use the same empirical model but do not have MARVEL substitution in their .states files.

## Evidence

Paper explicitly reports 8states line lists for 12C2 (44,189 states; 6,080,920 transitions), 13C2 (94,003 states; 13,361,992 transitions), and 12C13C (91,067 states; 12,743,954 transitions). Upper energy truncation at 50,000 cm⁻¹; lower state threshold at 30,000 cm⁻¹; wavelength coverage up to 0.25 μm. Partition functions to 10,000 K at 1 K intervals. Source: [19YuSzPy](../../Raw/Sources/19YuSzPy.json)
