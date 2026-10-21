"""Eval cases on the weekly drops and on the integrated answers that need several workstreams combined."""

from __future__ import annotations

from simulation.delivery.cases_plan import ask

FDE = ("data_engineering", "software", "pm")


def _drop(case_id: str, question: str, expected: dict, week: int, budget: str = "multi_hop", roles=FDE) -> dict:
    return ask(case_id, question, expected, (f"drops/week-{week}",), budget, outcome="fde", roles=roles)


def cases(world: dict) -> list[dict]:
    drops = world["gold"]["drops"]
    two, three, four, five, six = (drops[f"week-{week}"] for week in range(2, 7))
    return [
        _drop("drop2-renamed", "Which registry field was renamed in schema v3, and to what?", {"renamed": two["renamed"]}, 2, "lookup"),
        _drop("drop2-new-fields", "Which columns does registry schema v3 add?", {"fields": two["new_fields"]}, 2, "lookup"),
        _drop("drop2-reissued", "How many registry numbers were reissued in the week 2 batch?", {"count": two["reissued"]}, 2, "lookup"),
        _drop("drop3-banned", "Which field did the DPO ban from extracts leaving the authority, and what replaces it?",
              {"banned": three["banned_field"], "replacement": three["replacement_field"]}, 3, "lookup", ("ml", "architect")),
        _drop("drop3-removed-sites", "Which capture sites in the vendor cohort are no longer allowed after the DPO restriction?",
              {"sites": three["removed_sites"]}, 3, "multi_hop", ("ml", "data_science")),
        _drop("drop3-cohort", "How many vendor-scored encounters remain in scope after the DPO restriction?",
              {"count": three["vendor_cohort_after"]}, 3, "analysis", ("ml", "data_science")),
        _drop("drop4-lost", "How many letter requests in the bureau incident window were never dispatched?",
              {"count": four["lost_count"]}, 4, "analysis", ("software", "data_engineering")),
        _drop("drop4-duplicates", "How many dispatch rows are duplicates of a request already dispatched?",
              {"count": four["duplicate_rows"]}, 4, "multi_hop", ("software", "data_engineering")),
        _drop("drop4-loop-days", "On which days did the bureau retry loop run?", {"days": four["retry_loop_days"]}, 4, "analysis",
              ("software",)),
        _drop("drop5-second-site", "May the second site the CDO asked for join the pilot?",
              {"allowed": five["second_site_allowed"], "site": five["second_site"]}, 5, "multi_hop", ("pm", "consultant")),
        _drop("drop5-feasible", "Is the CDO's new pilot date achievable?", {"feasible": five["requested_feasible"]}, 5, "analysis",
              ("pm", "consultant")),
        _drop("drop6-owner", "Who is the clinical safety owner, and may the pilot start?",
              {"owner": six["owner"], "pilot_may_start": six["pilot_may_start"]}, 6, "multi_hop", ("pm", "consultant")),
        _drop("drop6-register", "What does the handover owners register show for the clinical safety owner after week 6?",
              {"clinical_safety_owner": six["handover_owner_register"]}, 6, "lookup", ("pm",)),
        _drop("drop6-unmet", "Which of the clinical safety owner's conditions are met at the week 6 drop?",
              {"met": [item["id"] for item in six["conditions"] if item["met"]]}, 6, "analysis", ("pm", "consultant")),
        *_integration(world),
        *_written(world),
    ]


def _integration(world: dict) -> list[dict]:
    value = world["gold"]["integration"]
    sources = ("handover/registry", "handover/ophthalmology", "handover/epr_letters", "drops/week-3", "engagement/workstreams")
    roles = ("data_engineering", "data_science", "ml")
    return [
        ask("integration-overdue-rows", "How many referral rows have no seen date, before any identity resolution?",
            {"count": value["overdue_rows_naive"]}, sources[:2], "multi_hop", "fde", roles),
        ask("integration-overdue-people", "How many people alive and resident at the snapshot have an overdue referable referral?",
            {"count": value["overdue_people"]}, sources, "analysis", "fde", roles),
        ask("integration-overdue-primary-care", "How many of those people are in the pilot scope after the DPO restriction?",
            {"count": value["overdue_people_primary_care"]}, sources, "analysis", "fde", roles),
        ask("integration-lost-chase", "How many people with an overdue referral never received their week 4 chase letter?",
            {"count": value["overdue_chase_letters_lost"]}, (*sources, "drops/week-4"), "analysis", "fde", roles),
    ]


def _written(world: dict) -> list[dict]:
    five, six = world["gold"]["drops"]["week-5"], world["gold"]["drops"]["week-6"]
    pilot = world["gold"].get("pilot_date", {})
    press = five["press"]
    reply_mention = [f"The earliest feasible go-live is {pilot.get('earliest_pilot', five['earliest_pilot_lower_bound'])}.",
                     f"The contract needs a {pilot.get('required_route', 'framework_call_off').replace('_', ' ')}, not a direct award.",
                     "FRZ-0301 blocks registry interface changes until the end of January.",
                     f"{five['second_site']} is a hospital site and the DPO restriction excludes it."]
    reply_not = [f"that {five['requested_pilot']} is achievable", f"that {five['second_site']} can join the pilot",
                 "that the pilot can start before the clinical safety owner's conditions are met"]
    decision_mention = [f"{six['owner']} is named as clinical safety owner in the week 6 drop.",
                        *[f"{item['id']} is not yet met: {item['evidence']}" for item in six["conditions"] if not item["met"]]]
    return [
        ask("press-answer", "Draft the two-paragraph public answer to the media and ministerial query.",
            {"must_mention": press["must_mention"], "must_not_claim": press["must_not_claim"],
             "forbidden_terms": press["forbidden_terms"]}, ("drops/week-5", "drops/week-4"), "written", "consulting",
            ("consultant", "pm"), "written"),
        ask("cdo-reply", "Reply to the CDO's scope change with a plan and the evidence for it.",
            {"must_mention": reply_mention, "must_not_claim": reply_not}, ("drops/week-5", "handover/delivery"), "written",
            "consulting", ("consultant", "pm"), "written"),
        ask("owner-decision", "Write the go or no-go note for the pilot after the week 6 drop.",
            {"must_mention": decision_mention, "must_not_claim": ["that the pilot may start", "that the owners register names the owner"]},
            ("drops/week-6", "handover/owners.csv"), "written", "consulting", ("consultant", "pm"), "written"),
    ]
