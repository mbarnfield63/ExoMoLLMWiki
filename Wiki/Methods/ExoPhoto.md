---
tags:
  - "method"
title: "ExoPhoto"
developer_group: "ExoMol"
software_type: "Photodissociation cross-section database"
status: "seed"
created: "2026-06-28"
updated: "2026-06-28"
sources:
  - "Raw/Sources/25NiHiYu_ExoPhoto.json"
source_count: 1
---

# ExoPhoto

ExoPhoto (www.exomol.com/exophoto/) is an extension of the ExoMol database providing temperature-dependent photodissociation cross sections in ExoMol format. It currently covers 20 molecules (AlH, HCl, HF, MgH, OH, NaO, MgO, O₂, AlCl, AlF, CS, HeH⁺, CO, CO₂, H₂O, SO₂, C₂H₂, C₂H₄, H₂CO, NH₃) from five source databases: ExoMol (theoretical, using Duo), PhoMol (theoretical, explicit continuum states), UGAMOP (theoretical), DTU (experimental far-UV), and EXACT (experimental). Cross sections are stored in `.photo` files (one per temperature per molecule) following the ExoMol file naming and JSON organisational conventions. For selected species (CS, MgH) partial cross sections by outgoing electronic channel and branching ratios are also given. The `.pdef.json` definition file describes isotopologue metadata, wavelength/temperature coverage, and version information. Predissociation is currently only included in ExoMol-sourced datasets. Source: [25NiHiYu_ExoPhoto](../../Raw/Sources/25NiHiYu_ExoPhoto.json).

## Related Methods

- [ExoMol Database](ExoMol_Database.md)
- [Photodissociation Cross Sections](Photodissociation_Cross_Sections.md)
- [Duo](Duo.md)

## Papers

- [25NiHiYu_ExoPhoto](../Papers/25NiHiYu_ExoPhoto.md)
