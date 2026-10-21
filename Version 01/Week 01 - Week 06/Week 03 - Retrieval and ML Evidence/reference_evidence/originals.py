"""Read the PDF, DOCX, and XLSX originals. The Markdown export is not the only copy."""

from __future__ import annotations

import zipfile
from pathlib import Path
from xml.etree import ElementTree

import pandas as pd

from simulation.eval.evidence.pdftext import pdf_text


def pdf(path: Path) -> str:
    return pdf_text(path.read_bytes())


def docx(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        root = ElementTree.fromstring(archive.read("word/document.xml"))
    return "\n".join(node.text or "" for node in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"))


def xlsx_table(path: Path) -> pd.DataFrame:
    frame = pd.read_excel(path, sheet_name="table")
    frame.columns = [str(column).strip() for column in frame.columns]
    return frame
