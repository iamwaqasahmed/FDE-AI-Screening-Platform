"""One row per findings item: who it belongs to, whether a rerun grades it, and the check."""

from __future__ import annotations

from graph_check.items import calls, cohort, cost, drop, governance

DE, DS, ML, SW, AR, PM, CO = (
    ("data_engineering",),
    ("data_science",),
    ("ml",),
    ("software",),
    ("architect",),
    ("pm",),
    ("consultant",),
)


def _row(item_id, check, roles, mode):
    return {"id": item_id, "check": check, "roles": roles, "mode": mode}


ITEMS = [
    _row("drop_incident", drop.drop_incident, PM + SW, "computed"),
    _row("outputs_changed", drop.outputs_changed, PM + CO, "read"),
    _row("dedupe_keys", drop.dedupe_keys, SW + DE, "computed"),
    _row("precedent", governance.precedent, PM + CO, "read"),
    _row("catalogue_lineage", governance.catalogue_lineage, DE + AR, "read"),
    _row("contact_status", cohort.contact_status, DS + DE, "computed"),
    _row("chase_lost_people", cohort.chase_lost_people, DS + CO, "computed"),
    _row("pilot_scope_lost", cohort.pilot_scope_lost, DS + ML, "computed"),
    _row("clock_breaches", cohort.clock_breaches, ML + DS, "computed"),
    _row("bureau_agreement", governance.bureau_agreement, AR + CO, "read"),
    _row("resend_summary", cohort.resend_summary, SW + AR, "computed"),
    _row("resend_window", governance.resend_window, PM + AR, "read"),
    _row("header_edges", governance.header_edges, DE + AR, "computed"),
    _row("referral_sites", governance.referral_sites, DE + SW, "computed"),
    _row("call_signal", calls.call_signal, ML + DS, "computed"),
    _row("incident_cost", cost.incident_cost, CO + PM, "computed"),
]
