"""A sweep that is killed and resumed, and a public line that waits for a decision."""

from __future__ import annotations

from simulation.drops.press import press_gold
from simulation.eval.agent.question import cite, make
from simulation.world.staff import name


def cases(world: dict, sweep) -> list[dict]:
    return [_sweep(world, sweep), _line(world)]


def _sweep(world: dict, sweep) -> dict:
    summary = {"rows": int(len(sweep)), "with_local_clock": int(sweep["local_clock"].sum())}
    clauses = sorted(set(sweep.loc[sweep["local_clock"], "clause_id"]))
    steps = int(len(sweep)) + 6
    question = "How many lost chase referrals inside the upper bound were read, and how many of them have a local clock?"
    return make(
        "resume-sweep", question, summary, "value", "resume", ("rows", "with_local_clock"), None, "multi_hop",
        clauses or ["ophthalmology"], max_steps=steps, runs_min=2, once_ids=list(sweep["local_pid"]),
        once_tool="ophthalmology.referrals", resume_kind="sweep",
    )


def _line(world: dict) -> dict:
    press = press_gold()
    expected = {"must_mention": press["must_mention"], "must_not_claim": press["must_not_claim"]}
    question = "The public line was paused for the accountable person. Record their decision and finish the line."
    return make(
        "resume-line", question, expected, "written", "resume", (), cite(world["catalog"]["ai-risk-tier-policy"]),
        "written", ["ai-risk-tier-policy"], max_steps=8, approver=name("cdo"), runs_min=2, resume_kind="approval",
    )
