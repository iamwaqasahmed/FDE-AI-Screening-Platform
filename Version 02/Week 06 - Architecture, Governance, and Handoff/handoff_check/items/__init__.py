"""One row per findings item: who it belongs to, whether a rerun grades it, and the check."""

from __future__ import annotations

from handoff_check.items import conditions, drop, estate, governance, security

DE, DS, ML, SW, AR, PM, CO = (
    ("data_engineering",), ("data_science",), ("ml",), ("software",), ("architect",), ("pm",), ("consultant",),
)


def _row(item_id, check, roles, mode):
    return {"id": item_id, "check": check, "roles": roles, "mode": mode}


ITEMS = [
    _row("drop_owner", drop.drop_owner, PM + CO, "read"),
    _row("outputs_changed", drop.outputs_changed, PM + CO, "read"),
    _row("conditions", conditions.conditions, PM + CO + DS, "computed"),
    _row("register_state", conditions.register_state, PM + CO, "read"),
    _row("current_state", estate.current_state, AR + DE, "read"),
    _row("flow_rules", estate.flow_rules, AR + DE, "computed"),
    _row("threat_summary", security.threat_summary, AR + SW, "computed"),
    _row("service_levels", estate.service_levels, SW + AR, "read"),
    _row("prototype_gaps", security.prototype_gaps, SW + ML, "read"),
    _row("production_account", security.production_account, SW + DE, "read"),
    _row("tier_three", governance.tier_three, AR + CO + ML + DS, "read"),
    _row("model_evidence", governance.model_evidence, ML + DS, "computed"),
    _row("adr_index", security.adr_index, AR, "read"),
]
