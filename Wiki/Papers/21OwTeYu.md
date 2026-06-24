---
tags:
  - "paper"
bibcode: "21OwTeYu"
title: "ExoMol line lists -- XLI. High-temperature molecular line lists for the alkali metal hydroxides KOH and NaOH"
authors:
  - "A. Owens"
  - "J. Tennyson"
  - "S. N. Yurchenko"
journal: "Monthly Notices of the Royal Astronomical Society"
year: 2021
doi: ""
summary: "ExoMol XLI: OYT4 (KOH) and OYT5 (NaOH) purely ab initio rovibrational line lists for the alkali metal hydroxides, targeting hot rocky super-Earth exoplanet atmospheres. Both computed with TROVE using new high-level ab initio PES and DMS; no empirical refinement. KOH OYT4: 38,362,078,911 transitions between 7,307,923 levels, 0–6,000 cm⁻¹, J_max=255, T_max=3500 K. NaOH OYT5: 49,663,923,092 transitions between 7,927,877 levels, 0–9,000 cm⁻¹, J_max=206, T_max=3500 K. Neither line list is MARVELised. Pure rotational bands compared with CDMS data; good agreement. Low-resolution line lists only (resolving power ~1000)."
mentioned_methods:
  - "TROVE"
  - "ExoCross"
  - "ExoMol Database"
  - "ExoMol Data Format"
  - "Partition Functions"
mentioned_molecules:
  - "KOH"
  - "NaOH"
  - "39K-16O-1H"
  - "23Na-16O-1H"
mentioned_people:
  - "A_Owens"
  - "J_Tennyson"
  - "S_N_Yurchenko"
status: "active"
created: "2026-06-24"
updated: "2026-06-24"
sources:
  - "Raw/Sources/21OwTeYu.json"
source_count: 1
---

# 21OwTeYu

[21OwTeYu](../Papers/21OwTeYu.md) — Owens, Tennyson & Yurchenko (2021), *Monthly Notices of the Royal Astronomical Society*.

## Summary

ExoMol XLI presents **OYT4** and **OYT5**, comprehensive purely ab initio rovibrational line lists for potassium hydroxide [39K-16O-1H](../Molecules/39K-16O-1H.md) and sodium hydroxide [23Na-16O-1H](../Molecules/23Na-16O-1H.md), targeting the atmospheres of hot rocky super-Earth exoplanets (up to ~4000 K dayside). Both molecules are linear triatomics in the gas phase. A lack of reliable rotation-vibration data means no empirical refinement of the spectroscopic model was possible; the line lists are therefore purely ab initio and recommended only for low-resolution studies (resolving power ~1000).

High-level ab initio PES and DMS were computed on extensive nuclear geometry grids and fitted with 3D analytic representations. Rovibrational calculations used TROVE, exploiting a new linear triatomic implementation developed for SiO₂ and CO₂. No MARVEL analysis was performed. Line positions for the fundamental bands are expected to be accurate to within 3–5 cm⁻¹ for KOH and 1–3 cm⁻¹ for NaOH; intensities within 5–10% of experiment. Both line lists reproduce CDMS pure rotational data well, with residuals increasing by only ~0.001 cm⁻¹ per J step.

**OYT4 (KOH):** 38,362,078,911 transitions between 7,307,923 rovibrational energy levels, covering 0–6,000 cm⁻¹, J_max = 255, T_max = 3500 K (soft limit). **OYT5 (NaOH):** 49,663,923,092 transitions between 7,927,877 energy levels, covering 0–9,000 cm⁻¹, J_max = 206, T_max = 3500 K (soft limit). Partition functions computed on a 1 K grid from 1–4000 K. ExoCross used for spectral simulations. Source: [21OwTeYu](../../Raw/Sources/21OwTeYu.json).

## Mentioned Methods

- [TROVE](../Methods/TROVE.md)
- [ExoCross](../Methods/ExoCross.md)
- [ExoMol Database](../Methods/ExoMol_Database.md)
- [ExoMol Data Format](../Methods/ExoMol_Data_Format.md)
- [Partition Functions](../Methods/Partition_Functions.md)

## Mentioned Molecules

- [KOH](../Molecules/KOH.md)
- [NaOH](../Molecules/NaOH.md)
- [39K-16O-1H](../Molecules/39K-16O-1H.md)
- [23Na-16O-1H](../Molecules/23Na-16O-1H.md)

## Mentioned People

- [A_Owens](../People/A_Owens.md)
- [J_Tennyson](../People/J_Tennyson.md)
- [S_N_Yurchenko](../People/S_N_Yurchenko.md)
