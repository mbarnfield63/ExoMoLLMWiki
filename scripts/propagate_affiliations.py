#!/usr/bin/env python3
"""Propagate author affiliations from paper sidecars into person notes.

Reads all Raw/Sources/*.json sidecars, collects author_details, and
updates Wiki/People/*.md notes with parsed affiliation data.

Usage:
    python propagate_affiliations.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_SOURCES = ROOT / "Raw" / "Sources"
PEOPLE = ROOT / "Wiki" / "People"

TODAY = date.today().isoformat()

# ── Affiliation string parsing ─────────────────────────────────────────────────

COUNTRIES = {
    "UK", "USA", "United Kingdom", "United States", "France", "Germany",
    "Australia", "Russia", "Italy", "Austria", "South Africa", "UAE",
    "United Arab Emirates", "China", "Japan", "Canada", "Netherlands",
    "Poland", "India", "Brazil", "Spain", "Sweden", "Switzerland",
    "Belgium", "Denmark", "Finland", "Norway", "Ireland", "Czech Republic",
    "Hungary", "Romania", "Portugal",
}
COUNTRY_NORMALIZE = {
    "United Kingdom": "UK",
    "United States": "USA",
    "United States of America": "USA",
}
INSTITUTION_KEYWORDS = (
    "university", "college", "academy", "agency",
    "universit",  # catches université, università, universität
)
DEPT_PREFIXES = (
    "department ", "school of ", "division ", "center ", "centre ",
    "section ", "dipartimento ", "nuclear data ", "space and planetary ",
    "institute of ", "institut ",  # French (Institut UTINAM)
)
_ADDRESS_RE = re.compile(
    r"(gower street|route de|via |private bag|tyndall|"
    r"keble road|ulyanov|pascoli|\bbs\d|\bbn\d|\bwc\d|\bse\d|\bec\d)",
    re.IGNORECASE,
)


def parse_affiliation(raw: str) -> dict:
    """Parse a raw affiliation string into a structured dict."""
    raw = raw.strip().rstrip(".,").strip()
    parts = [p.strip() for p in raw.split(",")]
    parts = [p for p in parts if p and len(p) > 1]

    if not parts:
        return _make_aff(raw, "", "")

    # Country: last part if it looks like a country name
    country = ""
    candidate = parts[-1]
    if candidate in COUNTRIES or (
        len(candidate) <= 25
        and re.match(r"^[A-Za-z ]+$", candidate)
        and not _ADDRESS_RE.search(candidate)
    ):
        country = COUNTRY_NORMALIZE.get(candidate, candidate)
        parts = parts[:-1]

    # Remove address-like parts (street numbers, postal codes, street names)
    clean = [
        p for p in parts
        if not _ADDRESS_RE.search(p)
        and not re.match(r"^[A-Z]{1,2}\d", p)  # postal codes like BS8, WC1E
        and not re.match(r"^\d", p)             # starts with digit
    ]

    institution = ""
    department = ""

    for p in clean:
        pl = p.lower()
        if not institution and any(k in pl for k in INSTITUTION_KEYWORDS):
            institution = p
        elif not department and any(pl.startswith(k) for k in DEPT_PREFIXES):
            department = p

    # Fallback: first non-dept clean item as institution
    if not institution:
        for p in clean:
            if p != department:
                institution = p
                break

    # If institution fragment starts with a conjunction (comma-split artifact),
    # trim to start from the actual institution name
    if institution and not any(institution.lower().startswith(k) for k in INSTITUTION_KEYWORDS):
        for marker in ("University of ", "University College ", "Royal ", "National ", "Institute "):
            idx = institution.find(marker)
            if idx > 0:
                institution = institution[idx:]
                break

    # Last fallback: use raw string
    if not institution and not department:
        institution = raw

    return _make_aff(institution, department, country)


def _make_aff(institution: str, department: str, country: str) -> dict:
    return {
        "institution": institution,
        "department": department,
        "country": country,
        "start_year": None,
        "end_year": None,
    }


# ── Name → surname matching ────────────────────────────────────────────────────

def surname_from_filename(name: str) -> str:
    """J_Tennyson.md → tennyson, A_E_Lynas-Gray.md → lynas-gray."""
    return Path(name).stem.split("_")[-1].lower()


def surname_from_author_name(name: str) -> str:
    """Jonathan Tennyson → tennyson, Tennyson → tennyson."""
    name = name.strip()
    if "," in name:
        return name.split(",")[0].strip().lower()
    parts = name.split()
    return (parts[-1] if parts else name).lower()


# ── Frontmatter YAML writer ────────────────────────────────────────────────────

def _affiliations_yaml_lines(aff_dicts: list[dict]) -> list[str]:
    lines = ["affiliations:"]
    for aff in aff_dicts:
        # Escape double quotes in values
        inst = aff["institution"].replace('"', "'")
        dept = aff["department"].replace('"', "'")
        cntry = aff["country"].replace('"', "'")
        lines.append(f'  - institution: "{inst}"')
        lines.append(f'    department: "{dept}"')
        lines.append(f'    country: "{cntry}"')
        lines.append(f"    start_year: null")
        lines.append(f"    end_year: null")
    return lines


def update_frontmatter(text: str, aff_dicts: list[dict]) -> str:
    """Replace institution/affiliations block and update 'updated' date."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return text

    fm_end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm_end = i
            break
    if fm_end is None:
        return text

    fm_lines = lines[1:fm_end]
    aff_block = _affiliations_yaml_lines(aff_dicts)
    new_fm: list[str] = []

    i = 0
    affiliations_inserted = False
    while i < len(fm_lines):
        line = fm_lines[i]
        stripped = line.strip()

        if stripped.startswith("institution:"):
            # Old schema: replace flat institution string with affiliations block
            new_fm.extend(aff_block)
            affiliations_inserted = True
            i += 1
        elif stripped.startswith("affiliations:"):
            # New schema: replace existing block (which may be multi-line)
            new_fm.extend(aff_block)
            affiliations_inserted = True
            i += 1
            # Skip indented sub-lines belonging to this key
            while i < len(fm_lines) and fm_lines[i].startswith("  "):
                i += 1
        elif stripped.startswith("updated:"):
            new_fm.append(f'updated: "{TODAY}"')
            i += 1
        else:
            new_fm.append(line)
            i += 1

    if not affiliations_inserted:
        # Insert before orcid or primary_papers
        for j, ln in enumerate(new_fm):
            if re.match(r"^(orcid|primary_papers):", ln.strip()):
                new_fm[j:j] = aff_block
                affiliations_inserted = True
                break
        if not affiliations_inserted:
            new_fm.extend(aff_block)

    result = ["---"] + new_fm + ["---"] + lines[fm_end + 1:]
    return "\n".join(result)


# ── Deduplication ─────────────────────────────────────────────────────────────

def dedup_affiliations(aff_dicts: list[dict]) -> list[dict]:
    """Deduplicate by institution name (case-insensitive)."""
    seen: set[str] = set()
    result = []
    for a in aff_dicts:
        key = a["institution"].lower()
        if key and key not in seen:
            seen.add(key)
            result.append(a)
    return result


# ── Main ───────────────────────────────────────────────────────────────────────

def load_surname_affiliations() -> dict[str, list[str]]:
    """Build {surname_lower: [raw_affiliation_strings]} from all sidecars."""
    mapping: dict[str, list[str]] = {}
    for path in sorted(RAW_SOURCES.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for entry in data.get("author_details") or []:
            name = entry.get("name", "")
            affiliations = entry.get("affiliations", [])
            if not affiliations:
                continue
            surname = surname_from_author_name(name)
            if surname not in mapping:
                mapping[surname] = []
            for aff in affiliations:
                if aff not in mapping[surname]:
                    mapping[surname].append(aff)
    return mapping


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Propagate affiliations to person notes")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing")
    args = parser.parse_args(argv)

    surname_affs = load_surname_affiliations()

    updated = 0
    unchanged = 0
    no_data = 0

    for path in sorted(PEOPLE.glob("*.md")):
        if path.name in ("People_Overview.md",):
            continue
        surname = surname_from_filename(path.name)
        raw_affs = surname_affs.get(surname, [])

        if not raw_affs:
            print(f"  no data : {path.name} (surname={surname!r})")
            no_data += 1
            continue

        aff_dicts = dedup_affiliations([parse_affiliation(r) for r in raw_affs])
        text = path.read_text(encoding="utf-8-sig")
        new_text = update_frontmatter(text, aff_dicts)

        if new_text == text:
            print(f"  same    : {path.name}")
            unchanged += 1
        elif args.dry_run:
            insts = ", ".join(a["institution"] for a in aff_dicts)
            print(f"  [DRY]   : {path.name} => {insts}")
            updated += 1
        else:
            path.write_text(new_text, encoding="utf-8", newline="\n")
            insts = ", ".join(a["institution"] for a in aff_dicts)
            print(f"  updated : {path.name} => {insts}")
            updated += 1

    print(f"\n{'Dry-run' if args.dry_run else 'Done'}: {updated} updated, {unchanged} unchanged, {no_data} no data.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
