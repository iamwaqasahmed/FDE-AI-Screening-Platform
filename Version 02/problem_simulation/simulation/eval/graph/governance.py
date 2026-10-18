"""The precedent, the catalogue, the bureau agreement, and the edges in the headers."""

from __future__ import annotations

from datetime import timedelta

import pandas as pd

from simulation.architecture.catalogue import ENTRIES
from simulation.architecture.lineage import EDGES
from simulation.delivery.freezes import freeze_calendar
from simulation.eval.graph.bars import RETENTION_DAYS
from simulation.policy.parse import parse_header
from simulation.systems.catalog import SYSTEMS
from simulation.systems.resolve import ids_on
from simulation.world.clock import INCIDENT_END, INCIDENT_START, SNAPSHOT, iso
from simulation.world.engagement import BUREAU_INCIDENT, WEEKS

LETTERS = next(system for system in SYSTEMS if system["system_id"] == "letters")


def facts(world: dict, linked: dict) -> dict:
    return {
        "precedent": _precedent(world),
        "catalogue_lineage": _catalogue(),
        "bureau_agreement": _agreement(),
        "resend_window": _window(),
        "header_edges": _edges(world),
        "referral_sites": {
            "hospitals": list(linked["hospitals"]),
            "blank_mrn": linked["blank_mrn"],
            "ambiguous": linked["ambiguous"],
        },
    }


def _precedent(world: dict) -> dict:
    return {
        "ref": "INC-0233",
        "start": iso(INCIDENT_START),
        "end": iso(INCIDENT_END),
        "notice": "notice-inc-0233",
        "notice_says_lost": True,
        "record": "incident-letter-2025",
        "record_says_lost": False,
        "has_request_id": False,
        "second_copies": _second_copies(world),
    }


def _second_copies(world: dict) -> int:
    events = world["events"]
    incident = events[events["letter_duplicate"]].copy()
    local = ids_on(world["identifiers"], "local_pid", iso(SNAPSHOT))
    incident["local_pid"] = incident["person_uid"].map(local).fillna("")
    rows = incident[["local_pid", "letter_at", "site"]].copy()
    rows["template"] = "result"
    doubled = pd.concat([rows, rows.copy()], ignore_index=True)
    return int(doubled.duplicated().sum())


def _catalogue() -> dict:
    edge = next(row for row in EDGES if row[1] == "letters_dispatch")
    names = {row[0] for row in ENTRIES}
    return {
        "dataset": "letters_dispatch",
        "grain_claim": "One row per letter.",
        "grain_holds": False,
        "upstream": edge[0],
        "verified": edge[4],
        "requests_catalogued": any("request" in name for name in names),
    }


def _agreement() -> dict:
    deadline = BUREAU_INCIDENT[1] + timedelta(days=RETENTION_DAYS)
    return {
        "document_id": "dsa-postright-2020",
        "cited": "dpo-rule-2018",
        "letters_covered": ["invitation", "result"],
        "covers_chase": False,
        "retention_days": RETENTION_DAYS,
        "evidence_deadline": iso(deadline),
        "region": "UK",
        "zone": LETTERS["trust_zone"],
        "dob_crosses": False,
        "needs_dpo_decision": True,
    }


def _window() -> dict:
    calendar = freeze_calendar()
    letters = calendar[calendar["system"].eq("letters")]
    freeze = letters[letters["ref"].eq("FRZ-0302")].iloc[0]
    windows = letters.loc[letters["kind"].eq("release_window"), "start"].sort_values()
    today = iso(WEEKS[4])
    return {
        "freeze": "FRZ-0302",
        "start": freeze["start"],
        "end": freeze["end"],
        "next_window": windows[windows.ge(today)].iloc[0],
        "last_before": windows[windows.lt(freeze["start"])].iloc[-1],
        "first_after": windows[windows.gt(freeze["end"])].iloc[0],
        "resend_needs_release": False,
    }


def _edges(world: dict) -> dict:
    counts = {name: 0 for name in ("supersedes", "cites", "applies_to", "constrains")}
    documents = 0
    for text in world["rendered"].values():
        header = parse_header(text)
        edges = {name: header.get(name) or () for name in counts}
        if any(edges.values()):
            documents += 1
        for name, values in edges.items():
            counts[name] += len(values)
    counts["documents"] = documents
    return counts
