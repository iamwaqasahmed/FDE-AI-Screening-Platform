"""One way for any stage to add a corpus document: Markdown text, register row, optional original file, gold spans."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

from simulation.policy.render import render_document
from simulation.policy.types import Document
from simulation.prose.formats.render import EXTENSIONS, render


@dataclass
class Extra:
    """Optional parts of a document beyond its Markdown body."""

    original: str = ""
    table: list[list[str]] | None = None
    pii: list[dict] = field(default_factory=list)
    injection: str = ""
    cites: tuple[str, ...] = ()
    supersedes: tuple[str, ...] = ()
    status: str = "in_force"
    sunset: date | None = None
    meta: dict = field(default_factory=dict)


def add_document(world: dict, doc_id: str, family: str, title: str, body: str, effective: date,
                 site: str = "", extra: Extra | None = None) -> str:
    """Register a document and return its corpus-relative Markdown path."""
    extra = extra or Extra()
    if doc_id in world.setdefault("catalog", {}):
        raise ValueError(f"Duplicate corpus document {doc_id}")
    document = Document(
        document_id=doc_id, title=title, status=extra.status, effective=effective, sunset=extra.sunset,
        site=site, programme="diabetic-eye", version=doc_id, supersedes=extra.supersedes, cites=extra.cites,
        applies_to=(), constrains=(), clause_ids=(),
    )
    relative = f"{family}/{doc_id}.md"
    world["catalog"][doc_id] = document
    text = render_document(document, body)
    world.setdefault("rendered", {})[doc_id] = text
    world.setdefault("paths", {})[doc_id] = relative
    meta = {"doc_id": doc_id, "family": family, "path": relative, "original": "", **extra.meta}
    if extra.original:
        original = f"{family}/originals/{doc_id}{EXTENSIONS[extra.original]}"
        world["files"][f"corpus/{original}"] = render(extra.original, doc_id, title, body, extra.table)
        meta["original"] = original
    world.setdefault("corpus_meta", {})[doc_id] = meta
    gold = world.setdefault("gold", {})
    values = sorted({(span["kind"], span["value"]) for span in extra.pii})
    for kind, value in values:
        for span in pii_spans(text, {kind: value}):
            gold.setdefault("pii", []).append({"doc_id": doc_id, "path": relative, **span})
    if extra.injection:
        gold.setdefault("injection", []).append({"doc_id": doc_id, "text": extra.injection})
    return relative


def add_composed(world: dict, spec, draft, effective: date, site: str = "", extra: Extra | None = None) -> str:
    """Compose a fact-checked body for the spec, then register it. The spec family is the corpus folder."""
    from simulation.prose import compose

    return add_document(world, spec.doc_id, spec.family, spec.title, compose(spec, draft), effective, site, extra)


def pii_spans(body: str, values: dict[str, str]) -> list[dict]:
    """Character spans of each personal value in the body. Keys are the PII kind.

    add_document re-anchors these spans on the final Markdown file, header included.
    """
    spans = []
    for kind, value in values.items():
        start = body.find(value)
        while value and start >= 0:
            spans.append({"kind": kind, "value": value, "start": start, "end": start + len(value)})
            start = body.find(value, start + 1)
    return spans
