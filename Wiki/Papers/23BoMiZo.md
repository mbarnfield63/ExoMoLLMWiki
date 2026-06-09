---
tags:
  - "paper"
bibcode: "23BoMiZo"
title: "ExoMol line lists -- L: High-resolution line lists of H3+, H2D+, D2H+ and D3+"
authors:
  - "Charles A. Bowesman"
  - "Irina I. Mizus"
  - "Nikolay F. Zobov"
  - "Oleg L. Polyansky"
  - "János Sarka"
  - "Bill Poirier"
  - "Marco Pezzella"
  - "Sergei N. Yurchenko"
  - "Jonathan Tennyson"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2023
doi: ""
summary: "ExoMol L: Updated MiZATeP (H3+) and Sochi/ST (H2D+) line lists plus new MiZo line lists for D2H+ and D3+. MARVEL networks updated for H3+ (703 empirical levels, 1,656 validated transitions), H2D+ (109 levels, 208 transitions), and D2H+ (115 levels, 210 transitions). D3+ uses effective Hamiltonian energies (J=0–15, T_max=800 K). DVR3D used for variational nuclear motion calculations; line list stats: H3+ 127,542,657 transitions (J_max=37, 5000 K); H2D+ 22,164,810 (J_max=20, 1750 K); D2H+ 2,290,235,000 (J_max=25, 2000 K); D3+ 36,078,183 (J_max=15, 800 K)."
mentioned_methods:
  - "DVR3D"
  - "MARVELization"
  - "ExoMol Database"
  - "ExoCross"
mentioned_molecules:
  - "H3+"
  - "1H3+"
  - "1H2-2H+"
  - "2H2-1H+"
  - "2H3+"
mentioned_people:
  - "C_A_Bowesman"
  - "I_I_Mizus"
  - "N_F_Zobov"
  - "O_L_Polyansky"
  - "J_Sarka"
  - "B_Poirier"
  - "M_Pezzella"
  - "S_N_Yurchenko"
  - "J_Tennyson"
status: "complete"
created: "2026-06-09"
updated: "2026-06-09"
sources:
  - "Raw/Sources/23BoMiZo.json"
source_count: 1
---

# 23BoMiZo — ExoMol L: H3+, H2D+, D2H+, D3+ line lists

Source: [23BoMiZo](../../Raw/Sources/23BoMiZo.json)

## Summary

Reports updated and new high-resolution line lists for all four isotopologues of H₃⁺ — the 50th paper in the ExoMol line list series (L). Published in *Monthly Notices of the Royal Astronomical Society* (2023).

The paper presents new **MiZo** line lists for [2H2-1H+](../Molecules/2H2-1H+.md) (D₂H⁺) and [2H3+](../Molecules/2H3+.md) (D₃⁺), and updates the existing [1H3+](../Molecules/1H3+.md) **MiZATeP** and [1H2-2H+](../Molecules/1H2-2H+.md) **ST** (Sochi) line lists using empirical energy levels from updated MARVEL spectroscopic networks. For D₃⁺, where insufficient laboratory data preclude MARVEL, effective Hamiltonian (EH) energies from molecular constants are used instead. The new line lists enable accurate far-infrared frequency predictions for all four species.

MARVEL networks are updated for H₃⁺, H₂D⁺, and D₂H⁺ incorporating all published spectroscopic transition data available at time of writing. Variational nuclear motion calculations use [DVR3D](../Methods/DVR3D.md). The D₃⁺ quantum number assignments are extended using a combination of the ScalIT/GENIUSH codes and manual assignment, providing full (ν₁, ν₂, L₂, J, G, U, K, Γ) labelling for 1,327 states.

## Line List Summary

| Isotopologue | ExoMol ID | Line list | States | Transitions | J_max | T_max (K) | MARVEL levels | Reference |
|---|---|---|---|---|---|---|---|---|
| H₃⁺ | [1H3+](../Molecules/1H3+.md) | MiZATeP (updated) | 158,721 | 127,542,657 | 37 | 5000 | 703 | [23BoMiZo](../Papers/23BoMiZo.md) |
| H₂D⁺ | [1H2-2H+](../Molecules/1H2-2H+.md) | ST/Sochi (updated) | 33,330 | 22,164,810 | 20 | 1750 | 109 | [23BoMiZo](../Papers/23BoMiZo.md) |
| D₂H⁺ | [2H2-1H+](../Molecules/2H2-1H+.md) | MiZo (new) | 369,500 | 2,290,235,000 | 25 | 2000 | 115 | [23BoMiZo](../Papers/23BoMiZo.md) |
| D₃⁺ | [2H3+](../Molecules/2H3+.md) | MiZo (new) | 37,410 | 36,078,183 | 15 | 800 | 0 (EH) | [23BoMiZo](../Papers/23BoMiZo.md) |

## MARVEL Analysis

| Species | Sources used | Transitions compiled | Validated | Empirical energy levels |
|---|---|---|---|---|
| H₃⁺ | 32 (original) + 6 new | 1,719 total | 1,656 | 703 (primary component) |
| H₂D⁺ | 13 (original) + 2 new | 210 total | 208 | 109 (primary component) |
| D₂H⁺ | 9 (original) + 4 new | 210 total | 210 | 115 (primary component) |
| D₃⁺ | — | — | — | 0 (EH used instead) |

New H₃⁺ MARVEL sources: 12BeWoPe, 13HoPeJeSi, 15PeHoMaKo, 16JuKoScAs, 18GuChLiPe, 19MaMc (102 new transitions + 7 previously missed). New H₂D⁺ sources: 16JuKoScAs, 17JuToMuGh. New D₂H⁺ sources: 16JuKoScAs, 17JuToMuGh, 17YuPeAmMa, 19MaKoMc (55 new transitions).

## Key Methods

- **DVR3D**: variational nuclear motion code for energy levels and Einstein A-coefficients; new LINELIST module added to convert output to ExoMol format.
- **MARVEL**: updated spectroscopic networks for H₃⁺, H₂D⁺, D₂H⁺; empirical energies replace calculated values where available.
- **Effective Hamiltonian (PGOPHER)**: used for D₃⁺ energies in place of MARVEL (insufficient lab data).
- **GENIUSH/ScalIT**: rigid rotor decomposition for extended quantum number assignment of H₃⁺ (1,525 additional states labelled) and D₃⁺ (1,045 states assigned manually).
- **ExoCross**: spectra simulations for comparison.

## Astrophysical Context

H₃⁺ is the dominant molecular ion in H₂ gas environments, forming rapidly via ionisation cascades. It acts as a coolant in giant planet ionospheres (Jupiter, Saturn, Uranus) and is a tracer of cosmic ray ionisation rates in the ISM. Deuterated isotopologues (H₂D⁺, D₂H⁺, D₃⁺) form preferentially at low temperatures due to fractionation and have been detected in the ISM via far-infrared/THz pure-rotation transitions. The updated line lists enable high-resolution studies with JWST (NIRCam long-wavelength channel) and are suited for far-infrared ISM searches.

## People

- [Charles A. Bowesman](../People/C_A_Bowesman.md) (primary)
- [Irina I. Mizus](../People/I_I_Mizus.md)
- [Nikolay F. Zobov](../People/N_F_Zobov.md)
- [Oleg L. Polyansky](../People/O_L_Polyansky.md)
- [János Sarka](../People/J_Sarka.md)
- [Bill Poirier](../People/B_Poirier.md)
- [Marco Pezzella](../People/M_Pezzella.md)
- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
