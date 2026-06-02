# Naming Conventions

Use predictable filenames so catalog search and local agents can avoid duplicate notes.

## Molecules

Use compact molecular formula filenames for chemical-formula MOC pages, and `exomol_id` filenames for isotopologue pages:

```text
Wiki/Molecules/H2O.md
Wiki/Molecules/1H2-16O.md
Wiki/Molecules/CO2.md
Wiki/Molecules/12C-16O2.md
```

Lower-level category overviews should be named explicitly:

```text
Wiki/Molecules/Molecules_Overview.md
Wiki/Methods/Methods_Overview.md
Wiki/People/People_Overview.md
Wiki/Applications/Applications_Overview.md
```

## Methods

Use the established method, software, or workflow name:

```text
Wiki/Methods/DVR3D.md
Wiki/Methods/Duo.md
Wiki/Methods/MARVEL.md
Wiki/Methods/ExoMol_Database.md
```

## Papers

Use the bibcode for paper notes:

```text
Wiki/Papers/24TeYuZh.md
Wiki/Papers/18ChJoYu.md
```

## People

Use initial and surname with underscores:

```text
Wiki/People/J_Tennyson.md
Wiki/People/S_N_Yurchenko.md
```

## Applications

Use title case concepts with underscores:

```text
Wiki/Applications/Exoplanet_Atmospheres.md
Wiki/Applications/Cool_Stars.md
```

## Raw Sources

Use stable citation-like slugs. The `.json` sidecar is the canonical source file for linking — it contains pre-extracted title, authors, abstract, and body prose. Raw XML files may also be present but are not used as link targets.

```text
Raw/Sources/24TeYuZh.json
Raw/Sources/11YuXxXx.json
```
