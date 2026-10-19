"""A minimal text PDF writer. Body lines in Helvetica, table rows in Courier, A4 pages."""

from __future__ import annotations

import textwrap

PAGE_W, PAGE_H = 595, 842
MARGIN = 56
LEADING = 13
LINES_PER_PAGE = (PAGE_H - 2 * MARGIN) // LEADING


def _escape(text: str) -> str:
    safe = text.encode("latin-1", "replace").decode("latin-1")
    return safe.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def layout(title: str, paragraphs: list[str], table: list[list[str]] | None = None) -> list[tuple[str, str]]:
    """Return (font, line) pairs. Font F1 is Helvetica, F2 Helvetica-Bold, F3 Courier."""
    lines: list[tuple[str, str]] = [("F2", title), ("F1", "")]
    for paragraph in paragraphs:
        if paragraph.startswith("## "):
            lines.extend([("F1", ""), ("F2", paragraph[3:])])
            continue
        for line in textwrap.wrap(paragraph, 92) or [""]:
            lines.append(("F1", line))
        lines.append(("F1", ""))
    if table:
        widths = [max(len(str(row[i])) for row in table) + 2 for i in range(len(table[0]))]
        for row in table:
            lines.append(("F3", "".join(str(cell).ljust(width) for cell, width in zip(row, widths))[:96]))
    return lines


def render_pdf(title: str, paragraphs: list[str], table: list[list[str]] | None = None) -> bytes:
    lines = layout(title, paragraphs, table)
    pages = [lines[i : i + LINES_PER_PAGE] for i in range(0, len(lines), LINES_PER_PAGE)] or [[("F1", "")]]
    objects: list[bytes] = []
    fonts = b"<< /F1 4 0 R /F2 5 0 R /F3 6 0 R >>"
    page_ids = [7 + 2 * index for index in range(len(pages))]
    objects.append(b"<< /Type /Catalog /Pages 2 0 R >>")
    kids = " ".join(f"{pid} 0 R" for pid in page_ids).encode()
    objects.append(b"<< /Type /Pages /Kids [" + kids + b"] /Count " + str(len(pages)).encode() + b" >>")
    objects.append(b"<< /Producer (Hartland simulation) >>")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>")
    for index, page in enumerate(pages):
        stream = _stream(page)
        content_id = page_ids[index] + 1
        objects.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] /Resources << /Font ".encode()
            + fonts
            + f" >> /Contents {content_id} 0 R >>".encode()
        )
        objects.append(b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream")
    return _assemble(objects)


def _stream(page: list[tuple[str, str]]) -> bytes:
    parts = ["BT", f"{MARGIN} {PAGE_H - MARGIN} Td", f"{LEADING} TL"]
    for font, line in page:
        size = 12 if font == "F2" else 9 if font == "F3" else 10
        parts.append(f"/{font} {size} Tf ({_escape(line)}) Tj T*")
    parts.append("ET")
    return "\n".join(parts).encode("latin-1", "replace")


def _assemble(objects: list[bytes]) -> bytes:
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for number, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{number} 0 obj\n".encode() + body + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode()
    for offset in offsets:
        out += f"{offset:010d} 00000 n \n".encode()
    out += f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R /Info 3 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    return bytes(out)
