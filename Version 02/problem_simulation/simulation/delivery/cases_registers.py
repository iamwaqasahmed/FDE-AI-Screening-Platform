"""Eval cases on the backlog, benefits, and accessibility."""

from __future__ import annotations

from simulation.delivery.cases_plan import D, ask
from simulation.delivery.letter_templates import FAILING

TEMPLATES = "handover/letters/templates"
STANDARD = "corpus/standards/standard-accessibility-letters-portal.md"


def cases(world: dict) -> list[dict]:
    gold, files = world["gold"], world["files"]
    backlog = gold["backlog"]
    tracker = files[f"{D}/tracker.csv"]
    first = backlog["duplicates"][0]
    benefits = gold["benefits"]
    failing = gold["accessibility"]["templates"][FAILING]
    sources = (f"{D}/tracker.csv",)
    return [
        ask("tracker-count", "How many tickets are in the tracker export, epics included?", {"count": backlog["tickets"]}, sources),
        ask("tracker-incident-links", "How many tickets link to the letter bureau duplicate-week incident INC-0233?",
            {"count": int(tracker["links"].astype(str).str.contains("INC-0233").sum())}, sources),
        ask("backlog-duplicate-count", "How many tickets duplicate an earlier ticket?", {"count": len(backlog["duplicates"])},
            sources, "analysis"),
        ask("backlog-duplicate-of", f"Which ticket does {first['ticket_id']} duplicate?", {"ticket_id": first["duplicate_of"]},
            sources, "multi_hop"),
        ask("backlog-missing-criteria", "How many stories have no acceptance criteria?", {"count": len(backlog["missing_criteria"])},
            sources),
        ask("backlog-blocked", "How many open tickets target a release date inside a change freeze?",
            {"count": len(backlog["blocked"])}, (*sources, f"{D}/freeze_calendar.csv"), "analysis"),
        ask("backlog-blocked-letters", "How many open tickets are blocked by the letter bureau freeze?",
            {"count": sum(row["freeze"] == "FRZ-0302" for row in backlog["blocked"])}, (*sources, f"{D}/freeze_calendar.csv"),
            "multi_hop"),
        ask("backlog-pilot-inflation", "How many open pilot story points are duplicates counted twice?",
            {"points": backlog["open_pilot_points_with_duplicates"] - backlog["open_pilot_points"]}, sources, "analysis"),
        ask("benefits-double-count", "Which two benefits count the same saving?", {"benefit_ids": benefits["pair"]},
            (f"{D}/benefits_register.csv",), "multi_hop", roles=("pm", "consultant")),
        ask("benefits-overlap", "How much a year is counted twice in the benefits register?", {"gbp": benefits["overlap_gbp"]},
            (f"{D}/benefits_register.csv",), "multi_hop", roles=("pm", "consultant")),
        ask("benefits-corrected", "What is the cashable benefit total once the double count is removed?",
            {"gbp": benefits["corrected_cashable_gbp"]}, (f"{D}/benefits_register.csv",), "analysis", roles=("pm", "consultant")),
        ask("accessibility-failing", "Which letter template fails the accessibility standard?",
            {"template_id": gold["accessibility"]["failing"]}, (TEMPLATES, STANDARD), "multi_hop"),
        ask("accessibility-requirements", f"Which requirements does the {FAILING} template fail?", {"requirements": failing["fails"]},
            (f"{TEMPLATES}/{FAILING}.md", STANDARD), "analysis"),
        ask("accessibility-contrast", f"What is the text contrast ratio of the {FAILING} template?", {"ratio": failing["contrast"]},
            (f"{TEMPLATES}/{FAILING}.md",), "multi_hop", roles=("pm", "software")),
    ]
