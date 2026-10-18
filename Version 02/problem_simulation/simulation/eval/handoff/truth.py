"""Values the debrief prints. They are not a findings item."""

from __future__ import annotations


def facts(world: dict, items: dict) -> dict:
    evidence = items["model_evidence"]
    hidden = world["gold"].get("integration", {}).get("overdue_chase_letters_lost")
    return {
        "owner": items["drop_owner"]["owner"],
        "named_on": items["drop_owner"]["named_on"],
        "friday": items["drop_owner"]["friday"],
        "people": items["conditions"]["CSO-4"]["people"],
        "hidden_lost": hidden,
        "earliest": items["conditions"]["CSO-5"]["not_before"],
        "requested": items["conditions"]["CSO-5"]["requested"],
        "design_rpm": items["service_levels"]["design_rpm"],
        "downtime_hours": items["service_levels"]["vendor_downtime_hours"],
        "event_lag_minutes": items["service_levels"]["event_lag_minutes"],
        "sensitivity": evidence["sensitivity"],
        "age_75_plus": evidence["age_75_plus"],
        "drift_site": evidence["drift_site"],
        "drift_before": evidence["drift_before"],
        "drift_after": evidence["drift_after"],
        "replace_with": items["prototype_gaps"]["replace_with"],
        "token_expires": items["production_account"]["expires"],
    }
