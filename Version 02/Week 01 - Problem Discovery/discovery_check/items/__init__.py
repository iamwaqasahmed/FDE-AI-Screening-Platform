"""One row per findings item: who it belongs to, whether a rerun grades it, and the check."""

from __future__ import annotations

from discovery_check.items import landscape, profiling, ranking, sizing

DE = ("data_engineering",)
DS = ("data_science",)
ML = ("ml",)
SW = ("software",)
AR = ("architect",)
PM = ("pm",)
CO = ("consultant",)


def _row(item_id, check, roles, mode):
    return {"id": item_id, "check": check, "roles": roles, "mode": mode}


ITEMS = [
    _row("systems", landscape.systems, AR, "read"),
    _row("safety_owner", landscape.safety_owner, PM + CO, "read"),
    _row("record_owners", landscape.record_owners, AR, "read"),
    _row("vendor_hosting", landscape.vendor_hosting, AR, "read"),
    _row("freezes", landscape.freezes, AR + PM, "read"),
    _row("no_master_key", landscape.no_master_key, SW, "read"),
    _row("timeline_refs", landscape.timeline_refs, PM, "computed"),
    _row("registry_months", profiling.registry_months, DE, "computed"),
    _row("dob_formats", profiling.dob_formats, DE, "computed"),
    _row("district_spellings", profiling.district_spellings, DE, "computed"),
    _row("lab_units", profiling.lab_units, DE, "computed"),
    _row("call_schema", profiling.call_schema, DE, "computed"),
    _row("firmware_lag", profiling.firmware_lag, SW + ML + AR, "computed"),
    _row("pii_log", profiling.pii_log, SW, "computed"),
    _row("finance_recode", profiling.finance_recode, DE + PM, "computed"),
    _row("eligible_people", sizing.eligible_people, DE, "computed"),
    _row("warehouse_defect", sizing.warehouse_defect, DE + AR, "computed"),
    _row("reminder", sizing.reminder, DS, "computed"),
    _row("agency_spend", sizing.agency_spend, PM, "computed"),
    _row("board_fee", sizing.board_fee, SW + CO, "computed"),
    _row("backlog", sizing.backlog, DS + CO, "computed"),
    _row("urgent_notes", sizing.urgent_notes, ML, "computed"),
    _row("vendor_claims", sizing.vendor_claims, ML + AR, "computed"),
    _row("letter_peak", sizing.letter_peak, DS, "computed"),
    _row("hospital_calls", sizing.hospital_calls, DS, "computed"),
    _row("letter_cause", sizing.letter_cause, DS + CO, "computed"),
    _row("rota", sizing.rota, ML + DS, "computed"),
    _row("ranking", ranking.ranking, CO + PM + DS, "computed"),
    _row("workshop", ranking.workshop, CO, "computed"),
    _row("voiced_vs_costly", ranking.voiced_vs_costly, CO, "computed"),
]
