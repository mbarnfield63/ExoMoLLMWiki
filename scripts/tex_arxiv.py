#!/usr/bin/env python3
"""Parse an arXiv LaTeX submission directory into a Raw/Sources sidecar JSON.

Usage:
    python tex_arxiv.py Raw/Files/26YuBaBo_CO2 --bibcode 26YuBaBo [--doi 10.xxx/xxx] [--year 2026]

The script reads the toplevel .tex file (from 00README.json if present), extracts
metadata and clean body prose, and writes Raw/Sources/<bibcode>.json.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from models import PaperMetadata

ROOT = Path(__file__).resolve().parents[1]
RAW_SOURCES = ROOT / "Raw" / "Sources"

# Journals identifiable from the documentclass name
_JOURNAL_MAP: dict[str, str] = {
    "mnras": "Monthly Notices of the Royal Astronomical Society",
    "aa": "Astronomy & Astrophysics",
    "aastex": "The Astrophysical Journal",
    "jcp": "The Journal of Chemical Physics",
    "jqsrt": "Journal of Quantitative Spectroscopy and Radiative Transfer",
    "revtex": "Physical Review",
}

# Environments whose full content is discarded
_SKIP_ENVS: list[str] = [
    "abstract",
    "figure", "figure*",
    "table", "table*", "tabular", "tabular*", "longtable",
    "thebibliography",
    "equation", "equation*",
    "align", "align*",
    "eqnarray", "eqnarray*",
    "multline", "multline*",
    "gather", "gather*",
    "split",
    "comment", "verbatim",
    "appendix",
    "keywords",
]

# Text-formatting commands whose braced argument is kept verbatim
_KEEP_ARG_CMDS: tuple[str, ...] = (
    "textit", "textbf", "textsc", "textrm", "textsf", "texttt",
    "emph", "underline", "mbox",
)


# ── Comment stripping ─────────────────────────────────────────────────────────

def _strip_comments(tex: str) -> str:
    """Remove LaTeX % comments (but not \\%)."""
    return re.sub(r"(?<!\\)%[^\n]*", "", tex)


def _normalize_chem_math(text: str) -> str:
    """Convert simple inline-math subscripts/superscripts to plain text.

    CO$_2$ → CO2,  $^{12}$C → 12C,  H$_2$O → H2O
    """
    # $_{N}$ or $_N$ subscript (digits or single letter)
    text = re.sub(r"\$_\{?([A-Za-z0-9+\-]+)\}?\$", r"\1", text)
    # $^{N}$ or $^N$ superscript
    text = re.sub(r"\$\^\{?([A-Za-z0-9+\-]+)\}?\$", r"\1", text)
    return text


# ── Balanced-brace extraction ──────────────────────────────────────────────────

def _extract_braced(text: str, pos: int) -> tuple[str, int]:
    """Return (content, end_pos) of the balanced-brace group starting at pos."""
    if pos >= len(text) or text[pos] != "{":
        return "", pos
    depth = 0
    i = pos
    while i < len(text):
        c = text[i]
        if c == "\\" and i + 1 < len(text):
            i += 2  # skip escaped character
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[pos + 1 : i], i + 1
        i += 1
    return text[pos + 1 :], len(text)


# ── Newcommand parser ──────────────────────────────────────────────────────────

def _parse_newcommands(tex: str) -> dict[str, tuple[int, str]]:
    """Return {name: (nargs, body)} for \\newcommand definitions in the preamble."""
    commands: dict[str, tuple[int, str]] = {}
    pattern = re.compile(r"\\(?:newcommand|renewcommand|providecommand)\s*\{\\([A-Za-z]+)\}")
    for m in pattern.finditer(tex):
        name = m.group(1)
        pos = m.end()
        # Optional [nargs]
        nargs = 0
        opt = re.match(r"\s*\[(\d)\]", tex[pos:])
        if opt:
            nargs = int(opt.group(1))
            pos += opt.end()
        # Optional default value [default] — skip it
        opt2 = re.match(r"\s*\[[^\]]*\]", tex[pos:])
        if opt2:
            pos += opt2.end()
        # Body in braces
        body, _ = _extract_braced(tex, pos + (len(tex[pos:]) - len(tex[pos:].lstrip())))
        commands[name] = (nargs, body)
    return commands


def _expand_zero_arg(text: str, commands: dict[str, tuple[int, str]]) -> str:
    """Expand zero-argument \\newcommands that produce plain text (no math)."""
    for name, (nargs, body) in sorted(commands.items(), key=lambda x: -len(x[0])):
        if nargs != 0:
            continue
        # Only expand if the body is plain text (no math, no backslashes)
        if "$" in body or "\\" in body:
            continue
        text = re.sub(rf"\\{re.escape(name)}(?![A-Za-z])", body, text)
    return text


# ── Environment stripper ───────────────────────────────────────────────────────

def _strip_environments(tex: str) -> str:
    for env in _SKIP_ENVS:
        tex = re.sub(
            rf"\\begin\{{{re.escape(env)}\*?}}.*?\\end\{{{re.escape(env)}\*?}}",
            " ",
            tex,
            flags=re.DOTALL,
        )
    return tex


# ── Body text cleaner ──────────────────────────────────────────────────────────

def _clean_body(tex: str, commands: dict[str, tuple[int, str]]) -> str:
    """Return clean prose body extracted from compiled LaTeX source."""
    tex = _strip_comments(tex)
    # Expand zero-arg plain-text macros (e.g. \TROVE → TROVE, \name → Dozen)
    tex = _expand_zero_arg(tex, commands)

    # Trim to document body
    start = tex.find(r"\begin{document}")
    if start != -1:
        tex = tex[start + len(r"\begin{document}") :]
    end = tex.find(r"\end{document}")
    if end != -1:
        tex = tex[:end]

    # Drop skipped environments (figures, tables, equations, bibliography)
    tex = _strip_environments(tex)

    # Convert simple chemistry inline-math before stripping: CO$_2$ → CO2
    tex = _normalize_chem_math(tex)

    # Drop display math \[...\]
    tex = re.sub(r"\\\[.*?\\\]", " ", tex, flags=re.DOTALL)

    # Drop inline math $...$ — use non-greedy, capped at 300 chars to avoid runaway
    tex = re.sub(r"\$\$.*?\$\$", " ", tex, flags=re.DOTALL)
    tex = re.sub(r"\$[^$\n]{0,300}?\$", " ", tex)

    # Keep argument of text-formatting commands
    for cmd in _KEEP_ARG_CMDS:
        tex = re.sub(rf"\\{cmd}\{{([^}}{{]*)\}}", r"\1", tex)

    # Drop \thanks, \footnote, \label, \ref, \eqref, \pageref (and their args)
    for cmd in ("thanks", "footnote", "label", "ref", "eqref", "pageref",
                "vspace", "hspace", "includegraphics", "caption"):
        tex = re.sub(rf"\\{cmd}\*?\{{[^}}]*\}}", "", tex)

    # Drop citations entirely
    tex = re.sub(r"\\cite[a-z]*\*?\{[^}]*\}", "", tex)

    # Keep URL content
    tex = re.sub(r"\\url\{([^}]*)\}", r"\1", tex)

    # Keep section titles as plain text headings
    tex = re.sub(r"\\(?:sub)*section\*?\{([^}]*)\}", r"\n\n\1\n", tex)

    # Keep argument of remaining single-arg commands, drop the command name
    tex = re.sub(r"\\[A-Za-z]+\*?\{([^}{]*)\}", r"\1", tex)

    # Drop bare commands (no argument)
    tex = re.sub(r"\\[A-Za-z]+\*?", " ", tex)

    # Clean up LaTeX punctuation
    tex = re.sub(r"[{}]", " ", tex)
    tex = re.sub(r"~", " ", tex)
    tex = re.sub(r"\\\\", "\n", tex)
    tex = re.sub(r"--+", "-", tex)
    tex = re.sub(r"``|''", '"', tex)

    # Collapse whitespace
    tex = re.sub(r"[ \t]+", " ", tex)
    tex = re.sub(r"\n{3,}", "\n\n", tex)

    return tex.strip()


# ── Metadata extractors ────────────────────────────────────────────────────────

def _extract_title(tex: str, commands: dict[str, tuple[int, str]]) -> str:
    # \title[short title]{full title}
    m = re.search(r"\\title\s*(?:\[[^\]]*\])?\s*\{", tex)
    if not m:
        return ""
    title, _ = _extract_braced(tex, m.end() - 1)
    title = _strip_comments(title)
    title = _expand_zero_arg(title, commands)
    title = _normalize_chem_math(title)
    title = re.sub(r"\$[^$]*\$", "", title)
    for cmd in _KEEP_ARG_CMDS:
        title = re.sub(rf"\\{cmd}\{{([^}}]*)\}}", r"\1", title)
    title = re.sub(r"\\[A-Za-z]+\*?\{([^}]*)\}", r"\1", title)
    title = re.sub(r"\\[A-Za-z]+\*?", "", title)
    title = re.sub(r"[{}]", "", title)
    return re.sub(r"\s+", " ", title).strip()


def _extract_authors(tex: str) -> list[str]:
    # \author[...]{...}  — ends before \date or \begin{document}
    m = re.search(r"\\author\s*(?:\[[^\]]*\])?\s*\{", tex)
    if not m:
        return []
    raw, _ = _extract_braced(tex, m.end() - 1)
    raw = _strip_comments(raw)
    raw = re.sub(r"\\thanks\{[^}]*\}", "", raw)       # strip \thanks{...}
    raw = re.sub(r"\\\\.*", "", raw, flags=re.DOTALL)  # strip affiliation after \\
    raw = re.sub(r"\\(?:newauthor|and|noindent)\b", ",", raw)
    raw = re.sub(r"\\[A-Za-z]+\*?", "", raw)
    raw = re.sub(r"[{}]", "", raw)
    parts = [p.strip().strip(",").strip() for p in re.split(r",|\n", raw)]
    return [p for p in parts if len(p) > 2 and re.search(r"[A-Za-z]", p)]


def _extract_year(tex: str) -> int:
    for pat in (r"\\pubyear\{(\d{4})\}", r"\\year\{(\d{4})\}"):
        m = re.search(pat, tex)
        if m:
            return int(m.group(1))
    # Fallback: \date{Accepted...; original form XXXX} — skip, unreliable
    return 0


def _extract_journal(tex: str) -> str:
    m = re.search(r"\\documentclass\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}", tex)
    if m:
        cls = m.group(1).strip().lower()
        for key, name in _JOURNAL_MAP.items():
            if key in cls:
                return name
    return ""


def _extract_abstract(tex: str, commands: dict[str, tuple[int, str]]) -> str:
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.DOTALL)
    if not m:
        return ""
    text = m.group(1)
    text = _strip_comments(text)
    text = _expand_zero_arg(text, commands)
    text = _normalize_chem_math(text)
    text = re.sub(r"\$[^$]*\$", "", text)
    text = re.sub(r"\\cite[a-z]*\*?\{[^}]*\}", "", text)
    text = re.sub(r"\\url\{([^}]*)\}", r"\1", text)
    for cmd in _KEEP_ARG_CMDS:
        text = re.sub(rf"\\{cmd}\{{([^}}]*)\}}", r"\1", text)
    text = re.sub(r"\\[A-Za-z]+\*?\{([^}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z]+\*?", " ", text)
    text = re.sub(r"[{}~]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


# ── Public API ─────────────────────────────────────────────────────────────────

def build_metadata(
    tex: str,
    *,
    bibcode: str,
    doi: str = "",
    year_override: int = 0,
) -> PaperMetadata:
    commands = _parse_newcommands(tex)
    return PaperMetadata(
        bibcode=bibcode,
        title=_extract_title(tex, commands),
        authors=_extract_authors(tex),
        year=year_override or _extract_year(tex),
        doi=doi,
        journal=_extract_journal(tex),
        abstract=_extract_abstract(tex, commands),
        body_text=_clean_body(tex, commands),
    )


def process_directory(
    directory: Path,
    *,
    bibcode: str,
    doi: str = "",
    year_override: int = 0,
) -> Path:
    readme = directory / "00README.json"
    if readme.exists():
        info = json.loads(readme.read_text(encoding="utf-8"))
        tex_name = next(
            (s["filename"] for s in info.get("sources", []) if s.get("usage") == "toplevel"),
            None,
        )
    else:
        tex_name = None

    if tex_name:
        tex_path = directory / tex_name
    else:
        candidates = list(directory.glob("*.tex"))
        if not candidates:
            raise FileNotFoundError(f"No .tex file found in {directory}")
        tex_path = candidates[0]

    tex = tex_path.read_text(encoding="utf-8")
    metadata = build_metadata(tex, bibcode=bibcode, doi=doi, year_override=year_override)

    RAW_SOURCES.mkdir(parents=True, exist_ok=True)
    sidecar = RAW_SOURCES / f"{bibcode}.json"
    sidecar.write_text(metadata.model_dump_json(indent=2), encoding="utf-8", newline="\n")
    return sidecar


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Parse LaTeX arXiv submission into Raw/Sources sidecar JSON"
    )
    parser.add_argument("directory", help="Path to Raw/Files/<bibcode>_<molecule> directory")
    parser.add_argument("--bibcode", required=True, help="Wiki bibcode (e.g. 26YuBaBo)")
    parser.add_argument("--doi", default="", help="DOI of the published paper")
    parser.add_argument("--year", type=int, default=0, help="Override publication year")
    args = parser.parse_args(argv)

    directory = Path(args.directory)
    if not directory.is_dir():
        print(f"Error: {directory} is not a directory", file=sys.stderr)
        return 1

    try:
        sidecar = process_directory(
            directory,
            bibcode=args.bibcode,
            doi=args.doi,
            year_override=args.year,
        )
    except Exception as exc:
        print(f"Failed: {exc}", file=sys.stderr)
        return 1

    print(f"Saved sidecar to {sidecar.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
