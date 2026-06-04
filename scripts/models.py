#!/usr/bin/env python3
"""Shared Pydantic models for ExoMol wiki ingestion scripts."""

from __future__ import annotations

from pydantic import BaseModel


class AuthorEntry(BaseModel):
    name: str
    affiliations: list[str] = []


class PaperMetadata(BaseModel):
    bibcode: str
    title: str
    authors: list[str]
    author_details: list[AuthorEntry] | None = None
    year: int
    doi: str
    journal: str
    abstract: str
    body_text: str
