"""Catalogue, agreement, notices, header edges, calls, and cost. Read from the handover."""

from __future__ import annotations

import re
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from reference_graph import load
from reference_graph.calls import signal
from simulation.policy.parse import parse_header

NOTICE_DATES = re.compile(r"(\d{4}-\d{2}-\d{2})")


def governance(data: Path, today: date, end: date) -> dict:
    hospital, ambiguous = load.hospitals(data)
    messages = load.messages(data)
    return {
        "precedent": _precedent(data),
        "catalogue_lineage": _catalogue(data),
        "bureau_agreement": _agreement(data, end),
        "resend_window": _window(data, today),
        "header_edges": _edges(data),
        "referral_sites": {
            "hospitals": sorted(set(hospital.values())),
            "blank_mrn": int(messages["mrn"].eq("").sum()),
            "ambiguous": ambiguous,
        },
    }


def call_signal(data: Path) -> dict:
    migration = _notice_span(data, "notice-chg-0158")
    incident = _notice_span(data, "notice-inc-0233")
    return signal(load.calls(data), migration, incident)


def incident_cost(data: Path, reconciled: pd.DataFrame, resend: list[dict]) -> dict:
    costs = load.read_csv(data, "engagement/economics/unit_costs.csv").set_index("item")["unit_cost_gbp"].astype(float)
    duplicates = int(reconciled["copies"].sum() - (reconciled["copies"] > 0).sum())
    reprints = sum(row["action"] == "resend" for row in resend)
    duplicate_gbp = round(duplicates * float(costs["letter"]), 2)
    reprint_gbp = round(reprints * float(costs["letter_reprint"]), 2)
    return {"duplicates_gbp": duplicate_gbp, "resends_gbp": reprint_gbp, "total_gbp": round(duplicate_gbp + reprint_gbp, 2)}


def _precedent(data: Path) -> dict:
    notice = (data / "corpus/notices/notice-inc-0233.md").read_text(encoding="utf-8")
    opened, closed = _notice_span(data, "notice-inc-0233")
    incident = load.read_csv(data, "handover/letters/incident_2025-03.csv")
    record = (data / "corpus/policy/incident-letter-2025.md").read_text(encoding="utf-8")
    return {
        "ref": "INC-0233",
        "start": opened.isoformat(),
        "end": closed.isoformat(),
        "notice": "notice-inc-0233",
        "notice_says_lost": "lost" in notice.lower(),
        "record": "incident-letter-2025",
        "record_says_lost": "lost" in record.lower(),
        "has_request_id": "request_id" in incident.columns,
        "second_copies": int(incident.duplicated().sum()),
    }


def _catalogue(data: Path) -> dict:
    catalogue = load.read_csv(data, "handover/architecture/data_catalogue.csv")
    lineage = load.read_csv(data, "handover/architecture/lineage.csv")
    claim = catalogue.loc[catalogue["dataset"].eq("letters_dispatch"), "definition"].iloc[0]
    edge = lineage[lineage["target_dataset"].eq("letters_dispatch")].iloc[0]
    return {
        "dataset": "letters_dispatch",
        "grain_claim": "One row per letter." if "One row per letter." in claim else claim,
        "grain_holds": False,
        "upstream": edge["source_dataset"],
        "verified": str(edge["last_verified"])[:10],
        "requests_catalogued": bool(catalogue["dataset"].str.contains("request").any()),
    }


def _agreement(data: Path, end: date) -> dict:
    text = (data / "corpus/data-sharing/dsa-postright-2020.md").read_text(encoding="utf-8")
    components = load.read_csv(data, "handover/architecture/components.csv")
    zone = components.loc[components["component"].eq("letters"), "zone"].iloc[0]
    return {
        "document_id": "dsa-postright-2020",
        "cited": "dpo-rule-2018",
        "letters_covered": ["invitation", "result"],
        "covers_chase": "chase" in text.lower(),
        "retention_days": 90,
        "evidence_deadline": (end + timedelta(days=90)).isoformat(),
        "region": "UK",
        "zone": zone,
        "dob_crosses": False,
        "needs_dpo_decision": True,
    }


def _window(data: Path, today: date) -> dict:
    calendar = load.read_csv(data, "handover/delivery/freeze_calendar.csv")
    letters = calendar[calendar["system"].eq("letters")]
    freeze = letters[letters["ref"].eq("FRZ-0302")].iloc[0]
    windows = letters.loc[letters["kind"].eq("release_window"), "start"].sort_values()
    return {
        "freeze": "FRZ-0302",
        "start": str(freeze["start"])[:10],
        "end": str(freeze["end"])[:10],
        "next_window": str(windows[windows.ge(today.isoformat())].iloc[0])[:10],
        "last_before": str(windows[windows.lt(str(freeze["start"])[:10])].iloc[-1])[:10],
        "first_after": str(windows[windows.gt(str(freeze["end"])[:10])].iloc[0])[:10],
        "resend_needs_release": False,
    }


def _edges(data: Path) -> dict:
    counts = {name: 0 for name in ("supersedes", "cites", "applies_to", "constrains")}
    documents = 0
    for path in (data / "corpus").rglob("*.md"):
        header = parse_header(path.read_text(encoding="utf-8"))
        edges = {name: header.get(name) or () for name in counts}
        if any(edges.values()):
            documents += 1
        for name, values in edges.items():
            counts[name] += len(values)
    counts["documents"] = documents
    return counts


def _notice_span(data: Path, name: str) -> tuple[date, date]:
    dates = [date.fromisoformat(value) for value in NOTICE_DATES.findall((data / "corpus/notices" / f"{name}.md").read_text(encoding="utf-8"))]
    return min(dates), max(dates)
