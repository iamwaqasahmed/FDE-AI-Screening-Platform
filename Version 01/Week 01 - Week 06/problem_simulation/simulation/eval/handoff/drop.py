"""The week 6 drop: a conditional owner, and which contracts this week touches."""

from __future__ import annotations

from datetime import timedelta

from simulation.world.engagement import OWNER_NAMED


def facts(world: dict) -> dict:
    six = world["gold"]["drops"]["week-6"]
    return {
        "drop_owner": {
            "owner": six["owner"],
            "owner_role": six["owner_role"],
            "named_on": six["named_on"],
            "conditions": [item["id"] for item in six["conditions"]],
            "register_owner": six["handover_owner_register"],
            "pilot_may_start": bool(six["pilot_may_start"]),
            "friday": (OWNER_NAMED + timedelta(days=4)).isoformat(),
        },
        "outputs_changed": {
            "delivered": ["C-05"],
            "consumed": ["C-06", "C-07", "C-08"],
            "unchanged": ["C-01", "C-02", "C-03", "C-04"],
            "changed": [],
        },
    }
