"""Workshop dot votes and sticky clusters. The idea with the most dots has one of the lowest net values."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.stakeholders.queries import summary_for
from simulation.world.staff import BY_KEY, PERSONAS

PUBLIC = "engagement/workshop"
DOTS = 5
IDEAS = (
    ("I01", "AI grades every photograph at every site", "vendor_model_expansion", 0.30),
    ("I02", "Patient chatbot for appointment questions", "", 0.13),
    ("I03", "Predict who will not attend", "dna_prediction", 0.12),
    ("I04", "Board dashboard of live waiting times", "", 0.10),
    ("I05", "Vendor score orders the primary-care queue", "grader_triage_ai", 0.10),
    ("I06", "Self-service answers for callers", "call_deflection", 0.07),
    ("I07", "Smarter fast-track slot booking", "fast_track_scheduling", 0.06),
    ("I08", "Target reminders where they work", "reminder_targeting", 0.04),
    ("I09", "Reconcile bureau dispatches and reissue lost letters", "letter_bureau_fix", 0.04),
    ("I10", "One record per person across systems", "identity_resolution", 0.04),
)
VOTERS = tuple(person.key for person in PERSONAS) + ("analyst", "bi_developer", "product_owner", "delivery_manager",
                                                       "booking_admin", "call_centre_lead")
STICKIES = {
    "Letters and post": ("Letters arrive after the appointment", "Cannot see if the bureau sent it", "Calls chasing letters"),
    "Grading queue": ("Queue never shrinks", "Long sessions are tiring", "Urgent notes get missed"),
    "Hospital waits": ("No fast-track slots", "Consultant post empty", "Seen dates missing"),
    "Attendance": ("Empty afternoon slots", "Bus times in the river districts", "Texts help some people"),
    "Data quality": ("Same person, three records", "Photos with no patient", "Warehouse counts look wrong"),
    "AI and vendor": ("Let AI grade everything", "Vendor numbers look great", "Who signs the result?"),
}


def dot_votes(rng: np.random.Generator) -> pd.DataFrame:
    weights = np.array([idea[3] for idea in IDEAS])
    rows = []
    for voter in VOTERS:
        picks = rng.choice(len(IDEAS), size=DOTS, replace=True, p=weights / weights.sum())
        for index in sorted(set(picks.tolist())):
            rows.append({"voter_role": BY_KEY[voter].role, "idea_id": IDEAS[index][0], "idea": IDEAS[index][1],
                         "dots": int((picks == index).sum())})
    return _lead_strictly(_ensure_top(pd.DataFrame(rows)))


def _ensure_top(frame: pd.DataFrame) -> pd.DataFrame:
    """If seeded noise put another idea on top, swap the two ideas' dots so the planted favourite leads."""
    totals = frame.groupby("idea_id")["dots"].sum()
    top = max(sorted(totals.index), key=lambda idea: totals[idea])
    if top == IDEAS[0][0]:
        return frame
    texts = {idea[0]: idea[1] for idea in IDEAS}
    swap = {top: IDEAS[0][0], IDEAS[0][0]: top}
    ids = frame["idea_id"].map(lambda value: swap.get(value, value))
    return frame.assign(idea_id=ids, idea=ids.map(texts))


def _lead_strictly(frame: pd.DataFrame) -> pd.DataFrame:
    """Move single dots from a tied rival to the favourite, voter by voter, until the favourite leads alone."""
    favourite = IDEAS[0][0]
    rows = frame.to_dict("records")
    while True:
        totals: dict[str, int] = {}
        for row in rows:
            totals[row["idea_id"]] = totals.get(row["idea_id"], 0) + row["dots"]
        rivals = sorted(idea for idea, count in totals.items() if idea != favourite and count >= totals.get(favourite, 0))
        if not rivals:
            return pd.DataFrame([row for row in rows if row["dots"] > 0])
        donor = next(row for row in rows if row["idea_id"] == rivals[0] and row["dots"] > 0)
        donor["dots"] -= 1
        target = next((row for row in rows if row["voter_role"] == donor["voter_role"] and row["idea_id"] == favourite), None)
        if target is None:
            target = {"voter_role": donor["voter_role"], "idea_id": favourite, "idea": IDEAS[0][1], "dots": 0}
            rows.append(target)
        target["dots"] += 1


def stickies(rng: np.random.Generator) -> pd.DataFrame:
    rows = []
    for cluster, texts in STICKIES.items():
        for text in texts:
            author = VOTERS[int(rng.integers(0, len(VOTERS)))]
            rows.append({"sticky_id": f"N{len(rows) + 1:03d}", "author_role": BY_KEY[author].role, "text": text,
                         "cluster": cluster})
    return pd.DataFrame(rows)


def workshop_gold(world: dict, votes: pd.DataFrame) -> dict:
    summary = summary_for(world)
    net = {row["key"]: row["net_annual_gbp"] for row in summary["opportunities"]}
    totals = votes.groupby("idea_id")["dots"].sum()
    top = max(sorted(totals.index), key=lambda idea: totals[idea])
    opportunity = next(idea[2] for idea in IDEAS if idea[0] == top)
    ordered = sorted(net.values())
    return {
        "top_voted_idea": top,
        "top_voted_opportunity": opportunity,
        "top_votes": int(totals[top]),
        "votes_by_idea": {idea: int(count) for idea, count in totals.items()},
        "idea_to_opportunity": {idea[0]: idea[2] for idea in IDEAS},
        "top_voted_net_gbp": net.get(opportunity, 0.0),
        "top_voted_net_rank": summary["net_rank"].index(opportunity) + 1 if opportunity in net else None,
        "median_net_gbp": (ordered[len(ordered) // 2 - 1] + ordered[len(ordered) // 2]) / 2,
        "highest_net_opportunity": summary["net_rank"][0],
    }


def build_workshop(world: dict, rng: np.random.Generator) -> dict:
    votes = dot_votes(rng)
    world["files"][f"{PUBLIC}/dot_votes.csv"] = votes
    world["files"][f"{PUBLIC}/stickies.csv"] = stickies(rng)
    gold = workshop_gold(world, votes)
    world.setdefault("gold", {})["workshop"] = gold
    return gold
