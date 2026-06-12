---
tags:
  - paper
bibcode: 24McBoKe
title: "A hybrid approach to generating diatomic line lists for high resolution studies of exoplanets and other hot astronomical objects: Updates to ExoMol MgO, TiO and VO line lists"
authors:
  - Laura K. McKemmish
  - Charles A. Bowesman
  - Kyriaki Kefala
  - Armando N. Perri
  - Anna-Maree Syme
  - Sergei N. Yurchenko
  - Jonathan Tennyson
journal: RAS Techniques and Instruments
year: 2024
summary: "Introduces the hybrid approach to diatomic line list construction, consolidating methodology for combining MARVEL, predicted-shift, isotopologue-extrapolation, and variational energy levels into a single uncertainty-ranked framework. MgO (LiTY): new MARVEL study yields 820 empirical energy levels from 1181 transitions across 9 sources; IE applied to four minor isotopologues (7017 levels each). TiO (Toto 2024): expanded MARVEL dataset with 12,164 energy levels from 61,509 validated transitions (latest source year 2021); PS + IE for all 5 isotopologues. VO (HyVO): hyperfine-resolved line list with 3,410,598 energy levels (28,760 MARVEL, 105,566 PS, 3,276,272 variational) and 58,904,173,243 transitions."
mentioned_methods:
  - MARVELization
  - Duo
  - ExoMol Database
  - Isotopologue Extrapolation
  - Predicted Shift Method
  - ExoMolHR
mentioned_molecules:
  - MgO
  - 24Mg-16O
  - 24Mg-17O
  - 24Mg-18O
  - 25Mg-16O
  - 26Mg-16O
  - TiO
  - 46Ti-16O
  - 47Ti-16O
  - 48Ti-16O
  - 49Ti-16O
  - 50Ti-16O
  - VO
  - 51V-16O
mentioned_people:
  - L_K_McKemmish
  - C_A_Bowesman
  - K_Kefala
  - A_N_Perri
  - A_M_Syme
  - S_N_Yurchenko
  - J_Tennyson
status: complete
created: 2026-06-03
updated: 2026-06-03
sources:
  - Raw/Sources/24McBoKe.json
source_count: 1
---

# 24McBoKe — Hybrid diatomic line lists: MgO, TiO, VO updates

Source: [24McBoKe](../../Raw/Sources/24McBoKe.json)

## Summary

Introduces the **hybrid approach** to diatomic ExoMol line list construction: a unified framework that assigns each quantum state the highest-quality energy level available — ranked MARVEL (Ma) > predicted-shift (PS) > isotopologue-extrapolation (IE) > variational (Ca) — with explicit uncertainty estimates at every step. Applied to update three astrophysically important molecules: MgO, TiO, and VO.

## MgO: Updated LiTY Line List

| Property | Value |
|---|---|
| Line list | LiTY (hybrid update) |
| Main isotopologue | 24Mg-16O |
| MARVEL energy levels | 820 |
| MARVEL transitions | 1,181 validated / 1,169 used (9 sources) |
| Electronic states covered | 4 lowest (X, A, B, +1) |
| IE isotopologues | 25Mg-16O, 26Mg-16O, 24Mg-17O, 24Mg-18O |
| IE levels per minor isotopologue | 7,017 |
| Negative transitions removed | 92–139 per isotopologue |

## TiO: 2024 Toto Update

| Property | Value |
|---|---|
| Line list | Toto (2024 update; supersedes 2021) |
| Main isotopologue | 48Ti-16O |
| MARVEL energy levels (2024) | 12,164 |
| MARVEL transitions validated | 61,509 (of 62,935 total) |
| Previous MARVEL (2019) | 10,761 energy levels / 51,547 transitions |
| Latest MARVEL source year | 2021 (21WiBrDo) |
| IE isotopologues | 46Ti-16O, 47Ti-16O, 49Ti-16O, 50Ti-16O |
| Negative transitions removed | 1,147–1,902 per isotopologue |

## VO: HyVO Hyperfine-Resolved Line List

| Property | Value |
|---|---|
| Line list | HyVO |
| Main isotopologue | 51V-16O |
| Total energy levels | 3,410,598 |
| MARVEL (Ma) levels | 28,760 |
| Predicted-shift (PS) levels | 105,566 |
| Variational (Ca) levels | 3,276,272 |
| Transitions | 58,904,173,243 |
| Hyperfine-unresolved MARVEL levels | 4,813 |
| Electronic states | 15 |

## Key Methods

- **Hybrid approach**: energy-hybridised line list built by applying the highest-quality energy source for each quantum state; uncertainty estimates rank Ma > PS > IE > Ca
- **Predicted Shift (PS)**: extrapolates obs.–calc. residuals across rotational series to unobserved levels; reduces discontinuity at MARVEL/variational boundary
- **Isotopologue Extrapolation (IE)**: transfers hybrid corrections from the main to minor isotopologues via mass-scaling of energy residuals
- **MARVELization**: collects all published experimental transition frequencies into a self-consistent spectroscopic network via weighted least-squares inversion
- **Duo**: variational diatomic nuclear-motion code used for all spectroscopic models

## People

- [Laura K. McKemmish](../People/L_K_McKemmish.md) (primary)
- [Charles A. Bowesman](../People/C_A_Bowesman.md)
- [Kyriaki Kefala](../People/K_Kefala.md)
- [Armando N. Perri](../People/A_N_Perri.md)
- [Anna-Maree Syme](../People/A_M_Syme.md)
- [Sergei N. Yurchenko](../People/S_N_Yurchenko.md)
- [Jonathan Tennyson](../People/J_Tennyson.md)
