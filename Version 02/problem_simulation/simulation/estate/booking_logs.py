"""Booking API application log around the debug-logging release. Inside the incident window, names and phones leak."""

from __future__ import annotations

from datetime import timedelta

import numpy as np
import pandas as pd

from simulation.corpus.add import pii_spans
from simulation.estate.common import base_people, id_map
from simulation.world.timeline import TIMELINE

INCIDENT = next(item for item in TIMELINE if item.ref == "INC-0270")
LOG_PATH = "handover/booking/api.log"
MARGIN_DAYS = 7


def build_booking_logs(world: dict, history: pd.DataFrame, rng: np.random.Generator) -> None:
    start = (INCIDENT.start - timedelta(days=MARGIN_DAYS)).isoformat()
    end = (INCIDENT.end + timedelta(days=MARGIN_DAYS)).isoformat()
    changes = history[(history["updated_at"] >= start) & (history["updated_at"] < end)].sort_values(["updated_at", "appointment_id"])
    people = base_people(world).set_index("person_uid")
    phones = id_map(world["identifiers"], "phone", ("assigned", "household"))
    lines, spans, offset = [], [], 0
    for row in changes.itertuples(index=False):
        ms = int(rng.integers(12, 400))
        line = f"{row.updated_at}:{int(rng.integers(0, 60)):02d}Z INFO PUT /appointments/{row.appointment_id} 200 status={row.status} {ms}ms"
        lines.append(line)
        offset += len(line) + 1
        if INCIDENT.start.isoformat() <= row.updated_at[:10] <= INCIDENT.end.isoformat():
            person = people.loc[row.person_uid]
            values = {"name": f"{person['forename']} {person['surname']}", "phone": str(phones.get(row.person_uid, ""))}
            debug = f"{row.updated_at}:00Z DEBUG payload booking={row.booking_id} name={values['name']} phone={values['phone']}"
            spans.extend({"file": LOG_PATH, **span, "start": span["start"] + offset, "end": span["end"] + offset}
                         for span in pii_spans(debug, values))
            lines.append(debug)
            offset += len(debug) + 1
    world["files"][LOG_PATH] = "\n".join(lines) + "\n"
    world["gold"].setdefault("pii_logs", []).extend(spans)
