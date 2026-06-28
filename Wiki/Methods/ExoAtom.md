---
tags:
  - "method"
title: "ExoAtom"
developer_group: "ExoMol"
software_type: "Atomic spectroscopy database"
status: "seed"
created: "2026-06-28"
updated: "2026-06-28"
sources:
  - "Raw/Sources/25NiWaXi_ExoAtom.json"
source_count: 1
---

# ExoAtom

ExoAtom (www.exomol.com/exoatom) is an extension of the ExoMol database providing atomic line lists in ExoMol format. It currently covers 80 neutral atoms and 74 singly charged ions, with data extracted from the NIST Atomic Spectra Database (79 neutral, 71 ion species; high-accuracy experimental) and the Kurucz Atomic Line Lists (38 neutral, 37 ion; theoretically complete). For each species, ExoAtom provides `.states`, `.trans`, and `.pf` files following ExoMol conventions. No recommended dataset is designated — NIST favours accuracy, Kurucz favours completeness — and the user selects based on their application. Post-processing (spectra, cross-sections, lifetimes) is handled by PyExoCross. Future development will add higher ionization stages and line-broadening parameters. Source: [25NiWaXi_ExoAtom](../../Raw/Sources/25NiWaXi_ExoAtom.json).

## Related Methods

- [ExoMol Database](ExoMol_Database.md)
- [ExoMol Data Format](ExoMol_Data_Format.md)

## Papers

- [25NiWaXi_ExoAtom](../Papers/25NiWaXi_ExoAtom.md)
