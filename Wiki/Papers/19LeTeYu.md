---
tags:
  - "paper"
bibcode: "19LeTeYu"
title: "ExoMol line list XXXIV: A Rovibrational Line List for Phosphinidene (PH) in its X and A Electronic States"
authors:
  - "Jonathan Langleben"
  - "Jonathan Tennyson"
  - "Sergei N. Yurchenko"
  - "Peter Bernath"
year: 2019
journal: "Monthly Notices of the Royal Astronomical Society"
doi: ""
exomol_series: "XXXIV"
summary: "ExoMol XXXIV: LaTY rovibronic line list for 31PH (phosphinidene) covering the X³Σ⁻ ground state and A³Π first excited state. 2,528 rovibronic states and 65,055 transitions; energies up to 24,500 cm⁻¹; T≤4000 K. PECs fitted by EMO function to experimental transition frequencies (RMS 0.01 cm⁻¹); ab initio MRCI+Q DMCs; LEVEL variational calculations. Partition function at 300 K: 302.14. Line list suitable for exoplanetary and cool stellar atmospheres."
mentioned_molecules:
  - "PH"
  - "31P-1H"
mentioned_methods:
  - "ExoMol Database"
  - "LEVEL"
mentioned_people:
  - "J_Langleben"
  - "J_Tennyson"
  - "S_N_Yurchenko"
  - "P_Bernath"
sources:
  - "Raw/Sources/19LeTeYu.json"
source_count: 1
created: "2026-06-26"
updated: "2026-06-26"
---

# 19LeTeYu

ExoMol XXXIV: [19LeTeYu](../../Raw/Sources/19LeTeYu.json). Rovibronic LaTY line list for phosphinidene (31PH), covering the X³Σ⁻ ground state and A³Π first excited state. PECs represented by the Extended Morse Oscillator (EMO) function, empirically refined to laboratory transition frequencies (submillimeter-wave, IR vibration-rotation); RMS 0.01 cm⁻¹. Spin-spin and spin-rotation correction terms included for the X³Σ⁻ state. Ab initio MRCI+Q DMCs computed with MOLPRO. Nuclear-motion calculations performed with LEVEL (variational diatomic program). Partition function follows HITRAN convention (full nuclear spin degeneracy, g_ns=4). Line list available at CDS and ExoMol.

Source: [19LeTeYu](../../Raw/Sources/19LeTeYu.json)

## Line List Summary

| Isotopologue | Line list | N states | N transitions | Coverage | T max |
| --- | --- | --- | --- | --- | --- |
| [31P-1H](../Molecules/31P-1H.md) | LaTY | 2,528 | 65,055 | ≤24,500 cm⁻¹ | 4000 K |

## Electronic States Covered

Two lowest electronic states of PH: X³Σ⁻ (ground, triplet) and A³Π (first excited). States are fully uncoupled in this model; weak forbidden transitions between them are not included. The X³Σ⁻ state is Hund's case (b), so quantum numbers were converted from Hund's case (a) for the states file. Landé g-factors included for modelling behaviour in weak magnetic fields.

## Methods

- **Nuclear motion:** LEVEL (variational nuclear motion program for diatomics); sinc DVR.
- **PECs:** Extended Morse Oscillator (EMO); X state: 5th-order EMO refined to 381 experimental lines (six fine-structure branches, v=0–5); A state: 4th-order EMO refined using 64 IR (0–0 band) transitions with remaining parameters fixed to MRCI+Q values.
- **Corrections (X state):** Born-Oppenheimer breakdown (BOB), spin-spin (SS), spin-rotation (SR) curves, each represented by damped-coordinate polynomial expansions.
- **DMCs:** MRCI+Q/aug-cc-pV5Z (MOLPRO); X-state DMC equilibrium value 0.4771 D; vibrationally averaged dipole 0.4499 D. Represented via damped-Surkus expansion to reduce numerical noise in overtone intensities.
- **Experimental data:** Submillimeter-wave rotational spectra (Bürger et al., Müller et al.); IR vibration-rotation (Bernath et al., five bands v=0–5, J_max high); A–X 0–0 band IR transitions from lab spectra.
- **Spectral simulations:** Compared against CDMS microwave data and Bernath et al. IR emission spectra (non-LTE two-temperature model, T_rot≈900 K, T_vib=2300 K).

## Evidence

Paper explicitly reports LaTY line list for 31PH: 2,528 rovibronic states, 65,055 transitions, energies to 24,500 cm⁻¹, T≤4000 K. ZPE = 1170.47 cm⁻¹. Partition function at 300 K = 302.14, consistent with CDMS (302.12). Dipole moment equilibrium 0.4771 D; vibrationally averaged 0.4499 D (∼1.27× larger than CDMS value of 0.396 D). Agreement with observed IR emission spectra confirmed across entire spectral region. Source: [19LeTeYu](../../Raw/Sources/19LeTeYu.json)
