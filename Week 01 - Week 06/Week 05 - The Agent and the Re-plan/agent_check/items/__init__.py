"""One row per findings item: who it belongs to, whether a rerun grades it, and the check."""

from __future__ import annotations

from agent_check.items import agent, business, drop, governance, plan

DE, DS, ML, SW, AR, PM, CO = (
    ("data_engineering",), ("data_science",), ("ml",), ("software",), ("architect",), ("pm",), ("consultant",),
)


def _row(item_id, check, roles, mode):
    return {"id": item_id, "check": check, "roles": roles, "mode": mode}


ITEMS = [
    _row("drop_scope", drop.drop_scope, PM + CO, "read"),
    _row("outputs_changed", drop.outputs_changed, PM + CO, "read"),
    _row("second_site", governance.second_site, AR + CO, "computed"),
    _row("procurement_route", plan.procurement_route, PM + AR, "read"),
    _row("backlog_triage", business.backlog_triage, DE + PM, "computed"),
    _row("pace", plan.pace, DS + ML, "computed"),
    _row("critical_path", plan.critical_path, PM + CO, "read"),
    _row("roadmap_items", plan.roadmap_items, PM + AR, "read"),
    _row("gate_two", business.gate_two, CO + PM, "computed"),
    _row("risk_updates", business.risk_updates, PM + CO, "read"),
    _row("press_rules", governance.press_rules, CO + PM, "read"),
    _row("agent_tier", governance.agent_tier, AR + ML, "read"),
    _row("veto_sources", governance.veto_sources, AR + SW, "read"),
    _row("service_account", agent.service_account, SW + AR, "read"),
    _row("model_routing", agent.model_routing, ML + AR, "read"),
    _row("audit_and_logs", agent.audit_and_logs, DE + SW, "read"),
    _row("sweep_summary", agent.sweep_summary, SW + DE + DS, "computed"),
    _row("veto_evidence", agent.veto_evidence, ML + DS, "read"),
]
