#!/usr/bin/env python3
"""Deterministic maintenance tooling for the ExoMol LLM Wiki."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_SOURCES = ROOT / "Raw" / "Sources"
WIKI = ROOT / "Wiki"
SCHEMA = ROOT / "Schema"
CATALOG = WIKI / "catalog.jsonl"
SOURCE_MANIFEST = SCHEMA / "source-manifest.jsonl"
ALLOWED_TAGS = {"molecule", "method", "paper", "person", "application", "log"}
WIKI_DIRS = {
    "Molecules": "molecule",
    "Methods": "method",
    "Papers": "paper",
    "People": "person",
    "Applications": "application",
    "Logs": "log",
}
WIKI_OVERVIEW_FILES = {
    "Molecules": "Molecules_Overview.md",
    "Methods": "Methods_Overview.md",
    "Papers": "Papers_Overview.md",
    "People": "People_Overview.md",
    "Applications": "Applications_Overview.md",
    "Logs": "Logs_Overview.md",
}
INDEX_BASENAMES = {"index.md"}.union(WIKI_OVERVIEW_FILES.values())


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def today() -> str:
    return dt.date.today().isoformat()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def parse_scalar(value: str):
    value = value.strip()
    if value == "":
        return ""
    if value.lower() in {"null", "~"}:
        return None
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        try:
            return json.loads(value.replace("'", '"'))
        except json.JSONDecodeError:
            return [
                item.strip().strip('"')
                for item in value[1:-1].split(",")
                if item.strip()
            ]
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = read_text(path)
    if not text.startswith("---"):
        return {}, text
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text

    data: dict[str, object] = {}
    current_key: str | None = None
    for raw in lines[1:end]:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and current_key and isinstance(
            data.get(current_key), list
        ):
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(parse_scalar(stripped[2:]))
            continue
        if line.startswith("  ") and current_key == "marvel_data" and ":" in stripped:
            if not isinstance(data.get(current_key), dict):
                data[current_key] = {}
            key, value = stripped.split(":", 1)
            cast = data[current_key]
            if isinstance(cast, dict):
                cast[key.strip()] = parse_scalar(value.split(" #", 1)[0].strip())
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.split(" #", 1)[0].strip()
            current_key = key
            if value == "":
                data[key] = {} if key == "marvel_data" else []
            else:
                data[key] = parse_scalar(value)
    body = "\n".join(lines[end + 1 :])
    return data, body


def xml_text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return " ".join(part.strip() for part in element.itertext() if part.strip())


def xml_local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def find_xml_text(root: ET.Element, names: tuple[str, ...]) -> str:
    wanted = {name.lower() for name in names}
    for element in root.iter():
        tag = xml_local_name(element.tag)
        if tag in wanted:
            text = xml_text(element)
            if text:
                return text
    return ""


def parse_xml_metadata(path: Path) -> dict:
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError:
        return {"Title": title_from_path(path), "Processed": False, "tags": ["source"]}

    title = find_xml_text(root, ("title", "article-title", "doc-title"))
    doi = find_xml_text(root, ("doi", "article-id"))
    journal = find_xml_text(
        root,
        (
            "publicationname",
            "publication-name",
            "journal-title",
            "journal",
            "publication-title",
        ),
    )
    year_text = find_xml_text(root, ("coverdate", "cover-date", "year"))
    year_match = re.search(r"\b(19|20)\d{2}\b", year_text)
    year = int(year_match.group(0)) if year_match else ""
    authors = []
    for element in root.iter():
        tag = xml_local_name(element.tag)
        if tag == "creator":
            name = xml_text(element)
            if name and name not in authors:
                authors.append(name)
    if not authors:
        for element in root.iter():
            tag = xml_local_name(element.tag)
            if tag not in {"contrib", "author"}:
                continue
            name = find_xml_text(element, ("string-name", "name", "surname"))
            if name and name not in authors:
                authors.append(name)

    return {
        "Title": title or title_from_path(path),
        "Authors": authors,
        "DOI": doi,
        "Journal": journal,
        "Year": year,
        "ContentType": ["parsed-paper"],
        "Processed": False,
        "tags": ["source"],
    }


def source_metadata(path: Path) -> dict:
    if path.suffix.lower() == ".xml":
        return parse_xml_metadata(path)
    meta, _ = parse_frontmatter(path)
    return meta


def dump_frontmatter(data: dict, body: str) -> str:
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(
                    f'  - "{item}"' if isinstance(item, str) else f"  - {item}"
                )
        elif isinstance(value, dict):
            lines.append(f"{key}:")
            for nested_key, nested_value in value.items():
                if isinstance(nested_value, list):
                    lines.append(f"  {nested_key}:")
                    for item in nested_value:
                        lines.append(
                            f'    - "{item}"'
                            if isinstance(item, str)
                            else f"    - {item}"
                        )
                elif isinstance(nested_value, bool):
                    lines.append(
                        f"  {nested_key}: {'true' if nested_value else 'false'}"
                    )
                elif isinstance(nested_value, str):
                    if nested_value == "" or any(
                        ch in nested_value for ch in [":", "#", "[", "]", "{", "}"]
                    ):
                        lines.append(f'  {nested_key}: "{nested_value}"')
                    else:
                        lines.append(f"  {nested_key}: {nested_value}")
                else:
                    lines.append(f"  {nested_key}: {nested_value}")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif value is None:
            lines.append(f"{key}: null")
        elif isinstance(value, str):
            if value == "" or any(ch in value for ch in [":", "#", "[", "]", "{", "}"]):
                lines.append(f'{key}: "{value}"')
            else:
                lines.append(f"{key}: {value}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n\n" + body.lstrip("\n")


def iter_wiki_notes() -> list[Path]:
    notes: list[Path] = []
    for dirname in WIKI_DIRS:
        base = WIKI / dirname
        if base.exists():
            notes.extend(
                sorted(
                    p
                    for p in base.rglob("*.md")
                    if p.is_file() and p.name not in INDEX_BASENAMES
                )
            )
    log_md = WIKI / "log.md"
    if log_md.exists():
        notes.append(log_md)
    return sorted(set(notes))


def iter_sources() -> list[Path]:
    if not RAW_SOURCES.exists():
        return []
    return sorted(
        p for p in RAW_SOURCES.rglob("*") if p.is_file() and p.suffix.lower() == ".xml"
    )


def title_from_path(path: Path) -> str:
    return path.stem.replace("_", " ")


def note_title(path: Path, meta: dict) -> str:
    return str(meta.get("title") or meta.get("Title") or title_from_path(path))


def note_tag(path: Path, meta: dict) -> str:
    tags = meta.get("tags")
    if isinstance(tags, list) and tags:
        return str(tags[0])
    for dirname, tag in WIKI_DIRS.items():
        try:
            path.relative_to(WIKI / dirname)
            return tag
        except ValueError:
            continue
    return ""


def build_catalog_entries() -> list[dict]:
    entries = []
    for path in iter_wiki_notes():
        meta, _ = parse_frontmatter(path)
        tag = note_tag(path, meta)
        if tag == "log":
            continue
        entry = {
            "path": rel(path),
            "title": note_title(path, meta),
            "tag": tag,
            "sources": (
                meta.get("sources", []) if isinstance(meta.get("sources"), list) else []
            ),
            "updated": str(meta.get("updated") or meta.get("created") or today()),
        }
        for key in (
            "formula",
            "bibcode",
            "exomol_id",
            "parent_molecule",
            "atoms",
            "aliases",
            "line_list",
            "summary",
            "authors",
            "mentioned_methods",
            "mentioned_molecules",
            "mentioned_people",
            "isotopologues",
            "marvel_data",
            "developer_group",
            "software_type",
            "institution",
            "orcid",
            "primary_papers",
            "secondary_papers",
            "field",
        ):
            if key in meta and meta[key] not in ("", []):
                entry[key] = meta[key]
        entries.append(entry)
    return sorted(entries, key=lambda item: item["path"])


def write_jsonl(path: Path, rows: list[dict]) -> None:
    write_text(path, "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows))


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in read_text(path).splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def command_doctor(_args: argparse.Namespace) -> int:
    required = [
        RAW_SOURCES,
        ROOT / "Raw" / "Files",
        WIKI,
        SCHEMA,
        ROOT / "_templates",
        ROOT / ".agents" / "skills",
        ROOT / "scripts",
    ]
    missing = [rel(path) for path in required if not path.exists()]
    print(f"Python: {sys.version.split()[0]}")
    print(f"Root: {ROOT}")
    print(f"Catalog: {'present' if CATALOG.exists() else 'missing'}")
    print(f"Source manifest: {'present' if SOURCE_MANIFEST.exists() else 'missing'}")
    print(f"Wiki notes: {len(iter_wiki_notes())}")
    print(f"Raw sources: {len(iter_sources())}")
    if missing:
        print("Missing required paths:")
        for path in missing:
            print(f"  - {path}")
        return 1
    return 0


def command_build(_args: argparse.Namespace) -> int:
    entries = build_catalog_entries()
    write_jsonl(CATALOG, entries)

    grouped: dict[str, list[dict]] = {}
    for entry in entries:
        grouped.setdefault(entry["tag"], []).append(entry)

    index_lines = ["# ExoMol LLM Wiki Index", ""]
    index_lines.append("## Category Overviews")
    for dirname in WIKI_DIRS:
        overview = WIKI_OVERVIEW_FILES[dirname]
        index_lines.append(
            f"- [{dirname} Overview]({(Path(dirname) / overview).as_posix()})"
        )
    index_lines.append("")
    write_text(WIKI / "index.md", "\n".join(index_lines).rstrip() + "\n")

    for dirname, tag in WIKI_DIRS.items():
        base = WIKI / dirname
        if not base.exists():
            continue
        overview_name = WIKI_OVERVIEW_FILES[dirname]
        lines = [f"# {dirname} Overview", ""]
        if tag == "molecule":
            formula_pages = [
                entry
                for entry in grouped.get(tag, [])
                if not entry.get("exomol_id")
            ]
            isotopologue_pages = [
                entry
                for entry in grouped.get(tag, [])
                if entry.get("exomol_id")
            ]
            lines.append("## Formula MOCs")
            if formula_pages:
                for entry in formula_pages:
                    lines.append(f"- [{entry['title']}]({Path(entry['path']).name})")
            else:
                lines.append("- No entries yet.")
            lines.append("")
            lines.append("## Isotopologue Notes")
            if isotopologue_pages:
                for entry in isotopologue_pages:
                    parent = entry.get("parent_molecule") or "unassigned"
                    lines.append(
                        f"- [{entry['title']}]({Path(entry['path']).name})"
                        f" - parent: {parent}"
                    )
            else:
                lines.append("- No entries yet.")
        else:
            for entry in grouped.get(tag, []):
                path = Path(entry["path"])
                lines.append(f"- [{entry['title']}]({path.name})")
            if len(lines) == 2:
                lines.append("- No entries yet.")
        write_text(base / overview_name, "\n".join(lines).rstrip() + "\n")

    print(f"Built catalog with {len(entries)} entries.")
    return 0


def command_lint(_args: argparse.Namespace) -> int:
    errors: list[str] = []
    for path in iter_wiki_notes():
        meta, _ = parse_frontmatter(path)
        path_rel = rel(path)
        if not meta:
            errors.append(f"{path_rel}: missing frontmatter")
            continue
        tag = note_tag(path, meta)
        if tag not in ALLOWED_TAGS:
            errors.append(f"{path_rel}: invalid or missing compiled tag '{tag}'")
        if tag == "molecule":
            marvel = meta.get("marvel_data")
            if not isinstance(marvel, dict):
                errors.append(f"{path_rel}: missing or invalid marvel_data dictionary")
            else:
                for key in ("is_marvelized", "latest_source_year", "energy_levels"):
                    if key not in marvel:
                        errors.append(f"{path_rel}: marvel_data missing key '{key}'")
        if tag == "paper":
            if not str(meta.get("bibcode") or "").strip():
                errors.append(f"{path_rel}: missing bibcode")
            if not str(meta.get("title") or "").strip():
                errors.append(f"{path_rel}: missing title")
            if not str(meta.get("summary") or "").strip():
                errors.append(f"{path_rel}: missing summary")
        if tag != "log":
            sources = meta.get("sources")
            source_count = meta.get("source_count")
            if not isinstance(sources, list):
                errors.append(f"{path_rel}: sources must be a list")
                sources = []
            if source_count != len(sources):
                errors.append(
                    f"{path_rel}: source_count {source_count!r} does not match {len(sources)} sources"
                )
            for source in sources:
                source_path = ROOT / str(source)
                try:
                    source_path.resolve().relative_to(RAW_SOURCES.resolve())
                except ValueError:
                    errors.append(f"{path_rel}: source outside Raw/Sources: {source}")
                if not source_path.exists():
                    errors.append(f"{path_rel}: missing source {source}")
    if errors:
        print("Lint failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Lint passed.")
    return 0


def source_coverage_from_wiki() -> dict[str, list[str]]:
    coverage: dict[str, list[str]] = {}
    for path in iter_wiki_notes():
        meta, _ = parse_frontmatter(path)
        sources = meta.get("sources", [])
        if not isinstance(sources, list):
            continue
        for source in sources:
            coverage.setdefault(str(source), []).append(rel(path))
    return {key: sorted(set(value)) for key, value in coverage.items()}


def source_manifest_rows(args: argparse.Namespace) -> list[dict]:
    existing = {row.get("path"): row for row in read_jsonl(SOURCE_MANIFEST)}
    coverage = source_coverage_from_wiki()
    rows = []
    for path in iter_sources():
        meta = source_metadata(path)
        source_rel = rel(path)
        old = existing.get(source_rel, {})
        covered_by = coverage.get(source_rel, old.get("covered_by", []))
        processed = bool(meta.get("Processed", old.get("processed", False)))
        if args.update and args.accept_covered and covered_by:
            processed = True
        rows.append(
            {
                "path": source_rel,
                "title": str(meta.get("Title") or title_from_path(path)),
                "processed": processed,
                "covered_by": covered_by,
                "updated": today(),
            }
        )
    return sorted(rows, key=lambda row: row["path"])


def command_source_scan(args: argparse.Namespace) -> int:
    rows = source_manifest_rows(args)
    write_jsonl(SOURCE_MANIFEST, rows)
    print(f"Wrote source manifest with {len(rows)} sources.")
    return 0


def command_source_lint(_args: argparse.Namespace) -> int:
    rows = read_jsonl(SOURCE_MANIFEST)
    errors = []
    for row in rows:
        if row.get("processed") and not row.get("covered_by"):
            errors.append(
                f"{row.get('path')}: processed without downstream Wiki coverage"
            )
    if errors:
        print("Source lint failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Source lint passed.")
    return 0


def command_source_delta(_args: argparse.Namespace) -> int:
    known = {row.get("path") for row in read_jsonl(SOURCE_MANIFEST)}
    new_sources = [rel(path) for path in iter_sources() if rel(path) not in known]
    if new_sources:
        print("New raw sources:")
        for source in new_sources:
            print(f"  - {source}")
    else:
        print("No new raw sources.")
    return 0


def command_source_coverage(_args: argparse.Namespace) -> int:
    rows = read_jsonl(SOURCE_MANIFEST)
    total = len(rows)
    processed = sum(1 for row in rows if row.get("processed"))
    covered = sum(1 for row in rows if row.get("covered_by"))
    print(f"Sources: {total}")
    print(f"Processed: {processed}")
    print(f"Covered: {covered}")
    print(f"Uncovered: {total - covered}")
    return 0


def command_search_catalog(args: argparse.Namespace) -> int:
    if not CATALOG.exists():
        print("Catalog missing. Run build first.")
        return 1
    pattern = re.compile(args.query, re.IGNORECASE)
    matches = []
    for row in read_jsonl(CATALOG):
        haystack = json.dumps(row, sort_keys=True)
        if pattern.search(haystack):
            matches.append(row)
    for row in matches:
        print(json.dumps(row, sort_keys=True))
    print(f"{len(matches)} match(es).")
    return 0


def command_log(args: argparse.Namespace) -> int:
    path = WIKI / "log.md"
    existing = read_text(path) if path.exists() else ""
    if not existing.startswith("---"):
        existing = (
            f'---\ntags:\n  - log\ncreated: {today()}\ntype: "ingest"\n---\n\n# Wiki Log\n\n'
            + existing.lstrip()
        )
    entry = f"## {today()} - {args.title}\n\n{args.details}\n\n"
    write_text(path, existing.rstrip() + "\n\n" + entry)
    print(f"Appended log entry to {rel(path)}.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("doctor").set_defaults(func=command_doctor)
    sub.add_parser("build").set_defaults(func=command_build)
    sub.add_parser("lint").set_defaults(func=command_lint)

    source_scan = sub.add_parser("source-scan")
    source_scan.add_argument("--update", action="store_true")
    source_scan.add_argument("--accept-covered", action="store_true")
    source_scan.set_defaults(func=command_source_scan)

    sub.add_parser("source-lint").set_defaults(func=command_source_lint)
    sub.add_parser("source-delta").set_defaults(func=command_source_delta)
    sub.add_parser("source-coverage").set_defaults(func=command_source_coverage)

    search = sub.add_parser("search-catalog")
    search.add_argument("--query", required=True)
    search.set_defaults(func=command_search_catalog)

    log = sub.add_parser("log")
    log.add_argument("--title", required=True)
    log.add_argument("--details", required=True)
    log.set_defaults(func=command_log)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
