"""Text checks for the estate: PII spans match the text exactly, the seen date is in each letter, no person ids leak."""

from __future__ import annotations

import re

import pandas as pd

from simulation.estate.booking_logs import INCIDENT as LOG_INCIDENT, LOG_PATH
from simulation.estate.epr_letters import seen_texts

UID = re.compile(r"\bP\d{7}\b")
ESTATE_FOLDERS = ("handover/booking/", "handover/sms/", "handover/call_centre/", "handover/lab/", "handover/service_desk/",
                  "handover/identity/", "handover/audit/", "handover/finance/", "handover/complaints/", "handover/epr_letters/",
                  "handover/architecture/")


def check_pii_calls(world: dict, errors: list[str]) -> None:
    notes = {}
    for path, frame in world["files"].items():
        if path.startswith("handover/call_centre/export/"):
            column = "note" if "note" in frame.columns else "agent_notes"
            notes.update(zip(frame["call_id"], frame[column]))
    spans = world["gold"].get("pii_calls", [])
    if not any(span["kind"] == "national_id" for span in spans):
        errors.append("No national id in the call notes gold.")
    if any(notes.get(span["call_id"], "")[span["start"]:span["end"]] != span["value"] for span in spans):
        errors.append("A call-note PII span does not match the note text.")


def check_epr(world: dict, errors: list[str]) -> None:
    files = world["files"]
    letters = files["truth/estate/epr_letters.parquet"]
    if letters.empty or not letters["message_blank"].any():
        errors.append("No EPR letter covers a blank referral message.")
        return
    for row in letters.itertuples(index=False):
        if not any(text in files[row.file] for text in seen_texts(row.seen_at)):
            errors.append(f"{row.letter_id} does not state the seen date.")
            return
    if any(files[span["file"]][span["start"]:span["end"]] != span["value"] for span in world["gold"].get("pii_epr", [])):
        errors.append("An EPR PII span does not match the letter text.")
    if not {"name", "dob", "mrn"} <= {span["kind"] for span in world["gold"].get("pii_epr", [])}:
        errors.append("EPR PII gold lacks a name, date of birth, or MRN.")


def check_logs(world: dict, errors: list[str]) -> None:
    text = world["files"].get(LOG_PATH, "")
    spans = world["gold"].get("pii_logs", [])
    if not spans or any(text[span["start"]:span["end"]] != span["value"] for span in spans):
        errors.append("Booking log PII spans are missing or do not match.")
    window = (LOG_INCIDENT.start.isoformat(), LOG_INCIDENT.end.isoformat() + "T23:59")
    debug = [line[:16] for line in text.splitlines() if " DEBUG " in line]
    if not debug or not all(window[0] <= stamp <= window[1] for stamp in debug):
        errors.append("Debug PII lines fall outside the INC-0270 window.")


def check_person_ids(world: dict, errors: list[str]) -> None:
    for path, content in world["files"].items():
        if not path.startswith(ESTATE_FOLDERS) or "/stream/" in path:
            continue
        if _leaks(content):
            errors.append(f"A person id leaked into {path}")
            return


def _leaks(content) -> bool:
    if isinstance(content, pd.DataFrame):
        text = content.select_dtypes(exclude=["number", "bool", "datetime"])
        return "person_uid" in content.columns or any(text[column].astype(str).str.contains(UID).any() for column in text.columns)
    return isinstance(content, str) and ("person_uid" in content or bool(UID.search(content)))
