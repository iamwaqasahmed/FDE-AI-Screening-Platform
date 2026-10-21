"""A minimal DOCX writer: paragraphs, level-2 headings, and one optional table."""

from __future__ import annotations

import io
import zipfile
from xml.sax.saxutils import escape

CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" '
    'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    "</Types>"
)
RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
    'Target="word/document.xml"/></Relationships>'
)
NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def _run(text: str, bold: bool = False) -> str:
    props = "<w:rPr><w:b/></w:rPr>" if bold else ""
    return f'<w:r>{props}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def _paragraph(text: str, bold: bool = False) -> str:
    return f"<w:p>{_run(text, bold)}</w:p>"


def _table(rows: list[list[str]]) -> str:
    body = "".join(
        "<w:tr>" + "".join(f"<w:tc><w:p>{_run(str(cell), index == 0)}</w:p></w:tc>" for cell in row) + "</w:tr>"
        for index, row in enumerate(rows)
    )
    return f'<w:tbl><w:tblPr><w:tblBorders><w:insideH w:val="single"/></w:tblBorders></w:tblPr>{body}</w:tbl>'


def render_docx(title: str, paragraphs: list[str], table: list[list[str]] | None = None) -> bytes:
    parts = [_paragraph(title, bold=True)]
    for paragraph in paragraphs:
        if paragraph.startswith("## "):
            parts.append(_paragraph(paragraph[3:], bold=True))
        else:
            parts.append(_paragraph(paragraph))
    if table:
        parts.append(_table(table))
    document = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document {NS}><w:body>{"".join(parts)}</w:body></w:document>'
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, data in (("[Content_Types].xml", CONTENT_TYPES), ("_rels/.rels", RELS), ("word/document.xml", document)):
            info = zipfile.ZipInfo(name, date_time=FIXED_TIME)
            archive.writestr(info, data)
    return buffer.getvalue()
