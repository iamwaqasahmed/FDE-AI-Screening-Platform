"""One row per findings item: who it belongs to, whether a rerun grades it, and the check."""

from __future__ import annotations

from evidence_check.items import cohorts, corpus, drop, evidence, governance, vendor

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
    _row("drop_restriction", drop.drop_restriction, PM + AR, "computed"),
    _row("outputs_changed", drop.outputs_changed, PM + CO, "read"),
    _row("policy_graph", corpus.policy_graph, DE + AR, "computed"),
    _row("originals", corpus.originals, DE, "computed"),
    _row("table_only", corpus.table_only, DE + SW, "computed"),
    _row("scan_damage", corpus.scan_damage, DE + SW, "read"),
    _row("near_duplicates", corpus.near_duplicates, DE, "computed"),
    _row("injections", governance.injections, SW + ML, "computed"),
    _row("models", governance.models, AR + SW, "read"),
    _row("vendor_region", governance.vendor_region, AR + CO, "read"),
    _row("vendor_scope", vendor.vendor_scope, ML + DS, "computed"),
    _row("label_noise", vendor.label_noise, DS + ML, "computed"),
    _row("reference_gap", vendor.reference_gap, ML + DS, "computed"),
    _row("operating_points", evidence.operating_points, ML, "computed"),
    _row("firmware_drift", evidence.firmware_drift, ML + DE, "computed"),
    _row("claims", evidence.claims, ML + CO, "computed"),
    _row("proposal_terms", cohorts.proposal_terms, PM + CO, "read"),
    _row("dna_leak", cohorts.dna_leak, DS, "computed"),
    _row("overdue_pilot_scope", cohorts.overdue_pilot_scope, DS + CO, "computed"),
]
