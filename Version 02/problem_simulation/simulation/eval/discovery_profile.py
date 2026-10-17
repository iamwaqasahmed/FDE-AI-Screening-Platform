"""Profiling facts for the Week 1 gold: schema changes, units, firmware lag, the log window, the recode."""

from __future__ import annotations

from simulation.devices.inventory import inventory_frame
from simulation.estate.call_centre import EXPORT_V2
from simulation.estate.finance import RECODE
from simulation.world import clock as c
from simulation.world.sites import DISTRICT_VARIANTS
from simulation.world.timeline import TIMELINE


def profiling() -> dict:
    new_code, old_codes = next(iter(_merged_codes().items()))
    incident = next(item for item in TIMELINE if item.ref == "INC-0270")
    return {
        "old_month": f"{c.OLD_SNAPSHOT:%Y-%m}",
        "old_columns": ["DOB", "REG_NO", "STATUS", "SURNAME"],
        "mixed_month": f"{c.MIXED_SNAPSHOT:%Y-%m}",
        "duplicate_month": f"{c.STALE_FEED:%Y-%m}",
        "dob_formats": ["dmy", "excel_serial", "iso"],
        "district_extras": sorted(name for names in DISTRICT_VARIANTS.values() for name in names),
        "lab_unit_change": c.iso(c.LAB_UNIT_CHANGE),
        "lab_unit_before": "%",
        "lab_unit_after": "mmol/mol",
        "call_schema_from": EXPORT_V2.isoformat()[:7],
        "call_columns_after": ["agent_notes", "disposition_code", "queue"],
        "firmware": _firmware_lag(),
        "pii": {"ref": incident.ref, "start": c.iso(incident.start), "end": c.iso(incident.end) if incident.end else ""},
        "finance": {"recoded_on": c.iso(c.FINANCE_RECODE), "old_codes": old_codes, "new_code": new_code},
    }


def _firmware_lag() -> list[dict]:
    lagged, truth = inventory_frame(True), inventory_frame(False)
    paired = lagged.merge(truth, on=["device_id", "site"], suffixes=("_shown", "_true"))
    changed = paired[paired["firmware_shown"] != paired["firmware_true"]]
    rows = []
    for site, group in changed.groupby("site"):
        row = group.iloc[0]
        rows.append({"site": site, "shown_version": row.firmware_shown, "true_version": row.firmware_true, "ref": "CHG-0240"})
    return rows


def _merged_codes() -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for old, new in RECODE.items():
        grouped.setdefault(new, []).append(old)
    return {new: sorted(olds) for new, olds in grouped.items() if len(olds) > 1}
