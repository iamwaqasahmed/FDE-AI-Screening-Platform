"""Render one document to its original format. Markdown stays the searchable export."""

from __future__ import annotations

import hashlib
import io

import pandas as pd

from simulation.prose.formats.docx import render_docx
from simulation.prose.formats.pdf import render_pdf

FORMATS = ("pdf", "docx", "xlsx", "scan")
EXTENSIONS = {"pdf": ".pdf", "docx": ".docx", "xlsx": ".xlsx", "scan": ".scan.pdf"}


def paragraphs_of(body: str) -> list[str]:
    return [block.strip().replace("\n", " ") for block in body.split("\n\n") if block.strip()]


def ocr_noise(text: str, key: str) -> str:
    """Deterministic scan damage: confusable letters, a dropped space now and then, a smudged digit."""
    swaps = {"l": "1", "O": "0", "rn": "m", "e": "c", "S": "5"}
    seed = int.from_bytes(hashlib.sha256(key.encode()).digest()[:4], "big")
    out = []
    for index, word in enumerate(text.split(" ")):
        roll = (seed + index * 2654435761) % 97
        if roll < 6:
            for old, new in swaps.items():
                if old in word:
                    word = word.replace(old, new, 1)
                    break
        if roll == 7:
            word = word + "\u00b7"
        out.append(word)
    return " ".join(out)


def render(kind: str, doc_id: str, title: str, body: str, table: list[list[str]] | None = None) -> bytes:
    paragraphs = paragraphs_of(body)
    if kind == "pdf":
        return render_pdf(title, paragraphs, table)
    if kind == "docx":
        return render_docx(title, paragraphs, table)
    if kind == "scan":
        noisy = [ocr_noise(paragraph, f"{doc_id}:{index}") for index, paragraph in enumerate(paragraphs)]
        return render_pdf(ocr_noise(title, doc_id), noisy, table)
    if kind == "xlsx":
        return _xlsx(title, paragraphs, table)
    raise ValueError(f"Unknown format {kind}")


def _xlsx(title: str, paragraphs: list[str], table: list[list[str]] | None) -> bytes:
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        pd.DataFrame({"text": [title, *paragraphs]}).to_excel(writer, sheet_name="document", index=False)
        if table:
            pd.DataFrame(table[1:], columns=table[0]).to_excel(writer, sheet_name="table", index=False)
        writer.book.properties.created = pd.Timestamp("2026-01-01").to_pydatetime()
        writer.book.properties.modified = pd.Timestamp("2026-01-01").to_pydatetime()
    return buffer.getvalue()


def pick_format(doc_id: str, weights: tuple[float, ...] = (0.45, 0.30, 0.10, 0.15)) -> str:
    roll = int.from_bytes(hashlib.sha256(doc_id.encode()).digest()[:4], "big") / 2**32
    total = 0.0
    for kind, weight in zip(FORMATS, weights):
        total += weight
        if roll < total:
            return kind
    return FORMATS[-1]
