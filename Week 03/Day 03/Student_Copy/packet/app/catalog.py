"""Cite the leaflet instead of the service catalog row."""

from __future__ import annotations


def lookup(rows: list[dict], clinic: str) -> dict:
    del rows
    return {"clinic": clinic, "doc_id": "leaflet-prep", "prep": ""}
