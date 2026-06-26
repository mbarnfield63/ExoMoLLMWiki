---
tags:
  - "paper"
bibcode: "19CoYuTe"
title: "ExoMol molecular line lists XXXV: a rotation-vibration line list for hot ammonia"
authors:
  - "Phillip A. Coles"
  - "Sergei N. Yurchenko"
  - "Jonathan Tennyson"
year: 2019
journal: "Monthly Notices of the Royal Astronomical Society"
doi: ""
exomol_series: "XXXV"
summary: "ExoMol XXXV: CoYuTe rotation-vibration line list for 14NH3 covering 0–20,000 cm⁻¹ (≥0.5 µm) at T≤1500 K. Computed with TROVE using the empirically refined C2018 PES and the CCSD(T)/aug-cc-pVQZ DMS from BYTe. 4,493 of 5,095,730 energy levels replaced with MARVEL empirical values. 16.9 billion transitions — an order of magnitude more than the predecessor BYTe (1.1 billion). Line strengths computed with the GPU-accelerated GAIN-MPI program on the Wilkes2 cluster. Successor to BYTe; validated against hot FTIR and emission spectra up to 1300–1473 K, and room-temperature spectra to visible wavelengths."
mentioned_molecules:
  - "NH3"
  - "14N-1H3"
mentioned_methods:
  - "TROVE"
  - "MARVELization"
  - "ExoMol Database"
  - "ExoMol Data Format"
  - "Partition Functions"
  - "ExoCross"
mentioned_people:
  - "P_A_Coles"
  - "S_N_Yurchenko"
  - "J_Tennyson"
sources:
  - "Raw/Sources/19CoYuTe.json"
source_count: 1
created: "2026-06-26"
updated: "2026-06-26"
---

# 19CoYuTe

ExoMol XXXV: [19CoYuTe](../../Raw/Sources/19CoYuTe.json). Rotation-vibration CoYuTe line list for ¹⁴NH₃ ([14N-1H3](../Molecules/14N-1H3.md)). Computed with TROVE using the C2018 empirically refined PES and the CCSD(T)/aug-cc-pVQZ DMS previously constructed for BYTe (Yurchenko et al. 2011). Line strengths and Einstein-A coefficients evaluated with the GPU-accelerated GAIN-MPI program on the Wilkes2 cluster (~22,000 transitions/second on 10 parallel GPU nodes). Hamiltonian construction on COSMOS HPC (725 real-time hours, up to 223 GB RAM); diagonalisation on Darwin HPC (272 real-time hours; largest matrix 246,311 rows). Succeeds and supersedes BYTe. Available from ExoMol and the CDS database.

Source: [19CoYuTe](../../Raw/Sources/19CoYuTe.json)

## Line List Summary

| Isotopologue | Line list | N states | N transitions | Coverage | T max |
| --- | --- | --- | --- | --- | --- |
| [14N-1H3](../Molecules/14N-1H3.md) | CoYuTe | 5,095,730 | 16,941,637,250 | 0–20,000 cm⁻¹ | 1500 K |

## Electronic States Covered

Ground electronic state rotation-vibration only (no rovibronic transitions). Upper state energy threshold 23,000 cm⁻¹; complete representation of hot spectrum below 12,000 cm⁻¹. Line list complete at 1500 K (partition function ratio ~0.99). Intensity threshold 10⁻⁴⁰ cm/molecule at 1500 K.

## Methods

- **Nuclear motion:** TROVE (variational nuclear motion code); symmetry-adapted basis set for NH₃ (D₃h/C₃v symmetry blocks A₁, A₂, E); basis truncated at 32,000 cm⁻¹.
- **PES:** C2018 empirically refined PES; constrained to experimental energy levels up to 7,254 cm⁻¹ above ground state.
- **DMS:** CCSD(T)/aug-cc-pVQZ (same DMS as BYTe); preferred over new MRCI/aug-cc-pwCVQZ DMS due to larger grid coverage of the former.
- **MARVEL:** 4,493 computed energy levels replaced with empirical values from two MARVEL studies of ¹⁴NH₃.
- **Line strengths:** GAIN-MPI (GPU-accelerated parallel program); ~100× speedup over traditional CPU approach.
- **Quantum labels:** Normal-mode vibrational labels (ν₁–ν₄, l₃, l₄) assigned via vibrational angular momentum operator eigenfunctions; local-mode labels (TROVE native) also retained.
- **Validation:** Compared against FTIR absorbance spectra at 500–5,500 cm⁻¹ up to 1,300 K; high-resolution FTIR emission at 740–5,500 cm⁻¹ up to 1,473 K; room-temperature spectra at 7,400–10,400 cm⁻¹ and visible (15,500 and 18,000 cm⁻¹); brown dwarf T-dwarf spectrum of UGPS 0722.

## Evidence

Paper reports CoYuTe line list for ¹⁴NH₃: 5,095,730 states, 16.9 billion transitions (16,941,637,250), 0–20,000 cm⁻¹, T≤1500 K. 4,493 MARVEL empirical energy levels incorporated. Intensity threshold 10⁻⁴⁰ cm/molecule at 1500 K. Partition function ratio 0.99 at 1500 K. Replaces BYTe (1.1 billion transitions). Source: [19CoYuTe](../../Raw/Sources/19CoYuTe.json)
