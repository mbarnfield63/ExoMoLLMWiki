#!/usr/bin/env python3
"""Fetch Elsevier article XML by DOI into Raw/Sources."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from config import ELSEVIER
from models import PaperMetadata


ROOT = Path(__file__).resolve().parents[1]
RAW_SOURCES = ROOT / "Raw" / "Sources"


def normalize_doi(value: str) -> str:
    value = value.strip()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value, flags=re.IGNORECASE)
    value = re.sub(r"^doi:\s*", "", value, flags=re.IGNORECASE)
    return value.strip()


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def element_text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return " ".join(part.strip() for part in element.itertext() if part.strip())


def first_text(root: ET.Element, names: set[str]) -> str:
    for element in root.iter():
        if local_name(element.tag) in names:
            text = element_text(element)
            if text:
                return text
    return ""


def creator_names(root: ET.Element) -> list[str]:
    creators: list[str] = []

    for element in root.iter():
        if local_name(element.tag) == "creator":
            text = element_text(element)
            if text and text not in creators:
                creators.append(text)

    if creators:
        return creators

    for element in root.iter():
        if local_name(element.tag) in {"contrib", "author"}:
            surname = first_text(element, {"surname"})
            given = first_text(element, {"given-names", "givenname", "firstname"})
            if surname:
                name = f"{surname}, {given}".strip().strip(",")
            else:
                name = first_text(element, {"string-name", "name"})
            if name and name not in creators:
                creators.append(name)

    return creators


def surname_from_name(name: str) -> str:
    name = name.strip()
    if "," in name:
        return name.split(",", 1)[0].strip()
    parts = name.split()
    return parts[-1] if parts else ""


def two_letter_code(name: str) -> str:
    letters = re.sub(r"[^A-Za-z]", "", surname_from_name(name)).lower()
    code = (letters + "xx")[:2]
    return code[0].upper() + code[1]


def publication_year(root: ET.Element) -> str:
    cover_date = first_text(root, {"coverdate", "cover-date"})
    match = re.search(r"\b(19|20)\d{2}\b", cover_date)
    if match:
        return match.group(0)

    year = first_text(root, {"year"})
    match = re.search(r"\b(19|20)\d{2}\b", year)
    if match:
        return match.group(0)

    raise ValueError("Could not determine publication year from XML")


def filename_from_xml(xml_text: str) -> str:
    root = ET.fromstring(xml_text)
    year = publication_year(root)[-2:]
    authors = creator_names(root)[:3]
    while len(authors) < 3:
        authors.append("")
    code = "".join(two_letter_code(author) for author in authors)
    return f"{year}{code}.xml"


_PARA_TAGS = frozenset({"para", "simple-para", "p", "note-para", "section-title"})

_SKIP_TAGS = frozenset({
    "bibliography", "bibliography-sec", "references", "reference",
    "bib-reference", "refkeys", "figure", "table", "footnote",
})


def _collect_paragraphs(
    element: ET.Element,
    parts: list[str],
) -> None:
    tag = local_name(element.tag)
    if tag in _SKIP_TAGS:
        return
    if tag in _PARA_TAGS:
        text = element_text(element)
        if text and len(text) > 20:
            parts.append(text)
        return  # element_text already flattens children; don't recurse
    for child in element:
        _collect_paragraphs(child, parts)


def extract_abstract(root: ET.Element) -> str:
    for element in root.iter():
        if local_name(element.tag) in {"abstract", "ce:abstract"}:
            return element_text(element)
    return ""


def extract_journal(root: ET.Element) -> str:
    return first_text(root, {"sourcetitle", "srctitle", "publicationname", "publication-name", "jtitle", "journal-title"})


def extract_body_text(root: ET.Element) -> str:
    """Return clean prose from the article body with XML structure stripped."""
    body: ET.Element | None = None
    for element in root.iter():
        if local_name(element.tag) in {"body", "article-body", "sections"}:
            body = element
            break
    target = body if body is not None else root
    parts: list[str] = []
    _collect_paragraphs(target, parts)
    return "\n\n".join(parts)


def build_metadata(root: ET.Element, *, doi: str, bibcode: str) -> PaperMetadata:
    year_str = publication_year(root)
    return PaperMetadata(
        bibcode=bibcode,
        title=first_text(root, {"title", "ce:title", "dctitle"}),
        authors=creator_names(root),
        year=int(year_str),
        doi=doi,
        journal=extract_journal(root),
        abstract=extract_abstract(root),
        body_text=extract_body_text(root),
    )


def fetch_jqsrt_paper(doi: str) -> Path:
    doi = normalize_doi(doi)
    url = f"https://api.elsevier.com/content/article/doi/{doi}"
    request = urllib.request.Request(
        url,
        headers={
            "X-ELS-APIKey": ELSEVIER,
            "Accept": "text/xml",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            status = response.status
            content = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Elsevier API returned HTTP {exc.code}\n{body}") from exc

    if status != 200:
        raise RuntimeError(f"Elsevier API returned HTTP {status}")

    filename = filename_from_xml(content)
    RAW_SOURCES.mkdir(parents=True, exist_ok=True)
    output_path = RAW_SOURCES / filename
    output_path.write_text(content, encoding="utf-8", newline="\n")

    root = ET.fromstring(content)
    metadata = build_metadata(root, doi=doi, bibcode=output_path.stem)
    sidecar = output_path.with_suffix(".json")
    sidecar.write_text(metadata.model_dump_json(indent=2), encoding="utf-8", newline="\n")

    return output_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fetch Elsevier paper XML by DOI")
    parser.add_argument("doi", help="DOI or DOI URL")
    args = parser.parse_args(argv)

    try:
        output_path = fetch_jqsrt_paper(args.doi)
    except Exception as exc:
        print(f"Failed to fetch paper: {exc}", file=sys.stderr)
        return 1

    print(f"Saved XML to {output_path.relative_to(ROOT).as_posix()}")
    sidecar = output_path.with_suffix(".json")
    print(f"Saved sidecar to {sidecar.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
