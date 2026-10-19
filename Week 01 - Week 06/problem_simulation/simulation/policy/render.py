"""Turn a document into text. The header is the signed record."""

from __future__ import annotations

import hashlib

from simulation.policy.apply import CLAUSES, DOCUMENTS
from simulation.policy.types import Document
from simulation.world.clock import SEED, iso


def render_document(document: Document, body: str | None = None) -> str:
    lines = _header(document)
    lines.append("")
    lines.append(f"# {document.title}")
    lines.append("")
    if body is None:
        for clause_id in document.clause_ids:
            clause = CLAUSES[clause_id]
            lines.append(clause.frames[_pick(clause_id, len(clause.frames))])
            lines.append("")
    else:
        lines.append(body.rstrip())
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_control() -> dict[str, str]:
    rendered = {document_id: render_document(document) for document_id, document in DOCUMENTS.items()}
    rendered["sop-national-v2-scan"] = render_document(
        DOCUMENTS["sop-national-v2-scan"],
        garble(_body(rendered["sop-national-v2"])),
    )
    return rendered


def garble(text: str) -> str:
    chars = []
    for index, char in enumerate(text):
        if char.isalpha() and index % 23 == 0:
            chars.append("0" if char in "oO" else "1" if char in "lI" else char)
        else:
            chars.append(char)
    return "".join(chars)


def _body(text: str) -> str:
    parts = text.split("\n\n", 1)
    return parts[1] if len(parts) > 1 else text


def _header(document: Document) -> list[str]:
    lines = [
        f"document_id: {document.document_id}",
        f"title: {document.title}",
        f"status: {document.status}",
        f"effective: {iso(document.effective)}",
        f"sunset: {iso(document.sunset) if document.sunset else ''}",
        f"site: {document.site}",
        f"programme: {document.programme}",
        f"version: {document.version}",
    ]
    lines.extend(_edges("supersedes", document.supersedes))
    lines.extend(_edges("cites", document.cites))
    lines.extend(_edges("applies_to", document.applies_to))
    lines.extend(_edges("constrains", document.constrains))
    return lines


def _edges(name: str, values: tuple[str, ...]) -> list[str]:
    if not values:
        return [f"{name}:"]
    return [f"{name}: {value}" for value in values]


def _pick(key: str, count: int) -> int:
    digest = hashlib.sha256(f"{SEED}:{key}".encode()).digest()
    return int.from_bytes(digest[:4], "big") % count
