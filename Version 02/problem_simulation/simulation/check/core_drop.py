"""The written handover: owners, registry files, stale register, no images, no truth ids."""

from __future__ import annotations

import re

import pandas as pd

from simulation.paths import CORPUS, HANDOVER
from simulation.policy.parse import parse_header
from simulation.systems.catalog import STALE_REGISTER
from simulation.world.clock import STALE_FEED

UID = re.compile(r"\bP\d{7}\b")
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".dcm", ".tif", ".tiff"}
TEXT_SUFFIXES = {".csv", ".md", ".txt", ".sql", ".json", ".jsonl", ".pipe", ".log"}


def check(world: dict, errors: list[str]) -> None:
    owners = pd.read_csv(HANDOVER / "owners.csv", dtype=str).fillna("")
    owner = owners.loc[owners["role"] == "clinical_safety_owner", "name"]
    if owner.empty or owner.iloc[0] != "":
        errors.append("clinical_safety_owner is not blank.")
    current = pd.read_csv(HANDOVER / "registry" / "current.csv", dtype=str).fillna("")
    if current.loc[current["REGISTRY_NO"] != "", "REGISTRY_NO"].duplicated().any():
        errors.append("Current registry numbers are not unique.")
    stale = pd.read_csv(HANDOVER / "registry" / "month" / f"{STALE_FEED:%Y-%m}.csv", dtype=str).fillna("")
    if not stale.loc[stale["REGISTRY_NO"] != "", "REGISTRY_NO"].duplicated().any():
        errors.append(f"{STALE_FEED:%B %Y} feed does not repeat a reissued number.")
    register = pd.read_csv(CORPUS / "register.csv", dtype=str).fillna("")
    for document_id in STALE_REGISTER:
        status = register.loc[register["document_id"] == document_id, "status"]
        text = world["rendered"][document_id]
        if status.empty or status.iloc[0] != "draft" or parse_header(text).get("status") == "draft":
            errors.append(f"Register status for {document_id} is not the stale draft.")
    _scan(errors)


def _scan(errors: list[str]) -> None:
    for path in HANDOVER.rglob("*"):
        if path.suffix.lower() in IMAGE_SUFFIXES:
            errors.append(f"Image bytes were written: {path.name}")
            return
        if path.suffix.lower() in TEXT_SUFFIXES and path.stat().st_size < 400_000_000:
            text = path.read_text(encoding="utf-8", errors="ignore")
            if "person_uid" in text or UID.search(text):
                errors.append(f"A person id leaked into {path.relative_to(HANDOVER)}")
                return
    book = pd.read_excel(HANDOVER / "grader" / "workbook.xlsx", dtype=str)
    if "person_uid" in book.columns or UID.search("\n".join(book.fillna("").astype(str).values.ravel()[:5000])):
        errors.append("Workbook contains a person id.")
