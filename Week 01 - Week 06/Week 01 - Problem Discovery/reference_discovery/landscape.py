"""Systems, records, hosting, freezes, keys, and timeline refs, read from the notes and the tickets."""

from __future__ import annotations

from reference_discovery.io import Drop, field, notice

KEYS = {
    "registry_no": ("handover/registry/current.csv", "REGISTRY_NO"),
    "local_pid": ("handover/registry/current.csv", "LOCAL_PID"),
    "lab_pid": ("handover/lab/hba1c_results.csv", "lab_pid"),
    "booking_id": ("handover/booking/appointments.csv", "booking_id"),
}


def items(drop: Drop) -> dict:
    notes = _notes(drop)
    return {
        "systems": {"systems": [{"id": name, "zone": field(text, "Trust zone")} for name, text in notes]},
        "safety_owner": {"named": bool(_owner(drop))},
        "record_owners": _records(notes),
        "vendor_hosting": {"region": _region(notes)},
        "freezes": _freezes(drop),
        "no_master_key": {"master": False, "keys": _keys(drop)},
        "timeline_refs": {"refs": _refs(drop)},
    }


def _notes(drop: Drop) -> list[tuple[str, str]]:
    folder = drop.path("handover", "interfaces")
    return [(path.stem, path.read_text(encoding="utf-8")) for path in sorted(folder.glob("*.md"))]


def _owner(drop: Drop) -> str:
    frame = drop.frame("handover", "owners.csv")
    rows = frame[frame["role"] == "clinical_safety_owner"]["name"]
    return str(rows.iloc[0]).strip() if len(rows) else ""


def _records(notes: list[tuple[str, str]]) -> dict:
    record = {name: field(text, "System of record for").lower() for name, text in notes}
    defect = {name: field(text, "Known defect").lower() for name, text in notes}
    return {
        "grade": next(name for name, line in record.items() if "signed grade" in line and "model score" not in line),
        "dispatch": next(name for name, line in record.items() if "dispatched" in line),
        "score": next(name for name, line in record.items() if "model score" in line),
        "seen": sorted(name for name, line in defect.items() if "seen" in line),
    }


def _region(notes: list[tuple[str, str]]) -> str:
    hosting = field(dict(notes)["vendor"], "Hosting").lower()
    return "eu" if "eu" in hosting else "uk"


def _freezes(drop: Drop) -> dict:
    found = {}
    for name, ref in (("registry", "FRZ-0301"), ("bureau", "FRZ-0302")):
        found[name] = {"ref": ref, "start": field(notice(drop, ref), "effective")}
    return found


def _keys(drop: Drop) -> list[str]:
    found = [key for key, (relative, column) in KEYS.items() if _has_column(drop, relative, column)]
    pacs = next(drop.path("handover", "pacs").glob("*.csv"), None)
    if pacs is not None and "MRN" in drop.frame("handover", "pacs", pacs.name, nrows=0).columns:
        found.append("mrn")
    return sorted(found)


def _has_column(drop: Drop, relative: str, column: str) -> bool:
    frame = drop.frame(*relative.split("/"), nrows=0)
    return column in frame.columns


def _refs(drop: Drop) -> list[str]:
    tickets = drop.frame("handover", "service_desk", "tickets.csv", usecols=["ticket_ref"])
    refs = tickets["ticket_ref"]
    return sorted(ref for ref in refs if ref.startswith(("CHG-", "INC-", "FRZ-")))

