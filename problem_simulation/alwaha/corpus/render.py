"""One original rendering beside the markdown: PDF, DOCX, XLSX, or a one-pixel PNG."""

from __future__ import annotations

import struct
import zipfile
import zlib
from pathlib import Path

KINDS = ("pdf", "docx", "xlsx", "png")


def kind_for(index: int) -> str:
    return KINDS[index % len(KINDS)]


def write_original(path: Path, kind: str, text: str) -> None:
    if kind == "pdf":
        path.write_bytes(_pdf(text))
    elif kind == "docx":
        _office(path, "word/document.xml", _docx_xml(text), "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml")
    elif kind == "xlsx":
        _xlsx(path, text)
    else:
        path.write_bytes(_png())


def _pdf(text: str) -> bytes:
    safe = "".join(char if 32 <= ord(char) < 127 else " " for char in text)[:60]
    stream = f"BT /F1 12 Tf 36 100 Td ({safe}) Tj ET".encode("ascii")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Count 1 /Kids [3 0 R] >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 144] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
        b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    chunks = [b"%PDF-1.4\n"]
    offsets = [0]
    for number, body in enumerate(objects, start=1):
        offsets.append(sum(len(chunk) for chunk in chunks))
        chunks.append(f"{number} 0 obj\n".encode("ascii") + body + b"\nendobj\n")
    xref_at = sum(len(chunk) for chunk in chunks)
    xref = [f"xref\n0 {len(objects) + 1}\n", "0000000000 65535 f \n"]
    xref.extend(f"{offset:010d} 00000 n \n" for offset in offsets[1:])
    trailer = f"trailer << /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_at}\n%%EOF\n"
    return b"".join(chunks) + "".join(xref).encode("ascii") + trailer.encode("ascii")


def _docx_xml(text: str) -> str:
    safe = _xml(text)[:200]
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body><w:p><w:r><w:t>{safe}</w:t></w:r></w:p></w:body></w:document>"
    )


def _office(path: Path, part: str, xml: str, content_type: str) -> None:
    types = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        f'<Override PartName="/{part}" ContentType="{content_type}"/>'
        "</Types>"
    )
    with zipfile.ZipFile(path, "w") as archive:
        _store(archive, "[Content_Types].xml", types)
        _store(archive, part, xml)


def _store(archive: zipfile.ZipFile, name: str, text: str) -> None:
    info = zipfile.ZipInfo(filename=name, date_time=(2027, 1, 10, 0, 0, 0))
    archive.writestr(info, text)


def _xlsx(path: Path, text: str) -> None:
    sheet = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        f"<sheetData><row><c t=\"inlineStr\"><is><t>{_xml(text)[:80]}</t></is></c></row></sheetData>"
        "</worksheet>"
    )
    _office(
        path,
        "xl/worksheets/sheet1.xml",
        sheet,
        "application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml",
    )


def _png() -> bytes:
    def chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    raw = b"\x00\xff\xff\xff"
    header = struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b"")


def _xml(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
