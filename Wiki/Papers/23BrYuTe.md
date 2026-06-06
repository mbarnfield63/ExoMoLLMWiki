---
tags:
  - "paper"
bibcode: "23BrYuTe"
title: "ExoMol line lists — LVI: The SO line list, MARVEL analysis of experimental transition data and refinement of the spectroscopic model"
authors:
  - "R. P. Brady"
  - "S. N. Yurchenko"
  - "J. Tennyson"
  - "G.-S. Kim"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2023
doi: ""
summary: "ExoMol LVI: SOLIS semi-empirical rovibronic line list for 32S-16O covering X³Σ⁻, a¹Δ, b¹Σ⁺, A³Π electronic states up to 43303.5 cm⁻¹ (222.22 nm), J_max=250. MARVEL analysis of 50,106 experimental transitions from 29 sources yields 8,558 self-consistent rovibronic energy levels. 7,008,190 Einstein A coefficients between 84,114 bound rovibronic states. Spectroscopic model refined via Duo from ic-MRCI/aug-cc-pV5Z ab initio; ground-state dipole scaled to 1.535 D. ExoMolOP opacities for ARCiS, TauREx, NEMESIS, petitRADTRANS."
mentioned_methods:
  - "ExoMol Database"
  - "MARVELization"
  - "Duo"
  - "ExoMolOP"
  - "ExoCross"
  - "TauREx"
  - "NEMESIS"
  - "ARCiS"
  - "petitRADTRANS"
  - "HITRAN"
mentioned_molecules:
  - "SO"
  - "32S-16O"
mentioned_people:
  - "R_P_Brady"
  - "S_N_Yurchenko"
  - "J_Tennyson"
  - "G_S_Kim"
status: "complete"
created: "2026-06-06"
updated: "2026-06-06"
sources:
  - "Raw/Sources/23BrYuTe.json"
source_count: 1
---

# 23BrYuTe — ExoMol LVI: SO SOLIS line list

Source: [23BrYuTe](../../Raw/Sources/23BrYuTe.json)

## Summary

Reports the **SOLIS** semi-empirical rovibronic line list for [32S-16O](../Molecules/32S-16O.md) — the 56th paper in the ExoMol line list series (LVI). Published in *Monthly Notices of the Royal Astronomical Society* (2023).

The paper combines a MARVEL analysis of 50,106 experimental transitions (49,613 non-redundant) from 29 experimental sources — yielding 8,558 self-consistent rovibronic energy levels for the X³Σ⁻, a¹Δ, b¹Σ⁺, A³Π, B³Π, and C³Π electronic states with J ≤ 69, v ≤ 30 — with a refined ic-MRCI spectroscopic model to produce the SOLIS line list. The spectroscopic model was originally computed at ic-MRCI/aug-cc-pV5Z with 12 active electrons covering 13 electronic states; for the IR/Vis line list, curves for 8 states (X, a, b, A, B, C, c, d) are used. Refinement to the MARVEL energies is performed using the variational diatomic code [Duo](../Methods/Duo.md). The ground-state permanent dipole is scaled to 1.535 D (average of two Stark measurements). The A³Π → X³Σ⁻ transition dipole is scaled from the experimental lifetime of the A state. Forbidden band intensities arise through the intensity-stealing mechanism via spin-orbit and electronic angular momentum couplings, not magnetic dipole transitions.

SOLIS covers 7,008,190 Einstein A coefficients between 84,114 bound rovibronic states up to J = 250, with wavenumbers up to 43,303.5 cm⁻¹ (222.22 nm). MARVELised energies replace computed energies where available; the predicted-shift method fills gaps and extrapolates to higher J. The UV region (B and C states) is left for future work due to insufficient experimental constraints. ExoMolOP opacities are generated for ARCiS, TauREx, NEMESIS, and petitRADTRANS.

## Line List Summary

| Isotopologue | ExoMol ID | Line list | States | Transitions | J_max | Wavenumber range | MARVEL | Reference |
|---|---|---|---|---|---|---|---|---|
| ³²SO | [32S-16O](../Molecules/32S-16O.md) | SOLIS | 84,114 | 7,008,190 | 250 | 0–43,303.5 cm⁻¹ | Yes (8,558 levels) | [23BrYuTe](../Papers/23BrYuTe.md) |

## MARVEL Analysis

| Property | Value |
|---|---|
| Experimental sources | 29 |
| Total transitions compiled | 50,106 |
| Non-redundant transitions | 49,613 |
| Validated transitions | 48,972 |
| Invalidated transitions | 546 |
| Rovibronic energy levels | 8,558 |
| Electronic states covered | X³Σ⁻, a¹Δ, b¹Σ⁺, A³Π, B³Π, C³Π |
| Rotational coverage | J ≤ 69 |
| Vibrational coverage | v ≤ 30 |

## Key Methods

- **MARVEL**: critical evaluation of 29 experimental transition sources; MARVEL 4 with bootstrap (100 iterations) for energy level uncertainties.
- **Ab initio model**: ic-MRCI/aug-cc-pV5Z, 12 active electrons, occupied (8,3,3,0)/closed (4,1,1,0) under C2v symmetry; 13 electronic states; diabatic representation for avoided crossings.
- **Duo**: variational rovibronic calculation; 301-point sinc-DVR grid (0.6–6.0 Å); 58 vibrational wavefunctions per state; EMO potential energy curves; spin-orbit, electronic angular momentum, dipole moment, and empirical Born-Oppenheimer breakdown curves included.
- **Ground-state DMS**: fitted to "irregular DMC" analytical form (13 Chebyshev parameters); scaled to experimental dipole 1.535 D.
- **Predicted-shift method**: used to MARVELise energy levels not directly covered by the MARVEL network.
- **ExoMolOP**: opacity k-tables for ARCiS, TauREx, NEMESIS, petitRADTRANS on extended T/P grid.
- **ExoCross**: partition function and cross-section simulations (Gaussian 0.6 cm⁻¹ HWHM profile).

## Astrophysical Context

SO is important across a wide range of environments: it was the first ground-state molecule detected in the ISM by radio astronomy, and the first molecule observed in excited electronic states by microwave spectroscopy. It has been observed in molecular clouds, planetary and lunar atmospheres (Venus, Io), and protoplanetary disks. The detection of SO₂ in the atmosphere of WASP-39b implicates SO in photochemical production pathways. SOLIS supplements the existing ExoMol line lists for SO₂ and SO₃, completing coverage of the sulphur oxide family. The UV model (B and C band contributions) remains a target for future work.

## People

- [Ryan P. Brady](../People/R_P_Brady.md) (primary)
- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
- [Gap-Sue Kim](../People/G_S_Kim.md)
