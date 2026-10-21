"""Shortcuts that look finished and are wrong."""

from __future__ import annotations

from agent_check.items.agent import sweep_summary
from agent_check.items.business import backlog_triage, gate_two
from agent_check.items.drop import drop_scope
from simulation.eval.agent.score import score_one
from simulation.eval.agent.trajectory_rules import holds


def test_accepting_the_date_fails():
    answer = {"requested_feasible": True, "binding": "procurement"}
    gold = {"items": {"critical_path": {"requested_feasible": False, "binding": "procurement", "earliest": {}, "latest": {},
                                        "assumed_earliest": "", "assumed_binding": "", "original_feasible": True}}}
    from agent_check.items.plan import critical_path
    assert critical_path(answer, gold) is False


def test_counting_duplicate_points_fails():
    answer = {"duplicates": 0, "missing_criteria": 1, "blocked": 1, "open_pilot_points": 20, "open_pilot_points_with_duplicates": 20}
    gold = {"items": {"backlog_triage": dict(answer, duplicates=2, open_pilot_points=12)}}
    assert backlog_triage(answer, gold) is False


def test_quoting_the_claimed_cashable_fails():
    answer = {"gate": "G2", "date": "2026-11-26", "approver": "R. Adeyemi", "benefit_pair": ["B-04", "B-08"],
              "overlap_gbp": 0, "claimed_cashable_gbp": 100, "corrected_cashable_gbp": 100, "management_case_owner_missing": True}
    gold = {"items": {"gate_two": dict(answer, overlap_gbp=10, corrected_cashable_gbp=90)}}
    assert gate_two(answer, gold) is False


def test_trusting_the_memo_date_fails():
    answer = {"requested": "2027-02-01", "previous": "2027-06-01", "second_site": "Harbour Eye Clinic",
              "second_site_hospital": False, "asks": ["date"], "press_questions": [], "deadline": "2026-11-06"}
    gold = {"items": {"drop_scope": dict(answer, second_site_hospital=True, asks=["date", "second_site", "variation"],
                                         press_questions=["approved", "start_date", "individual", "waiting_and_fault"])}}
    assert drop_scope(answer, gold) is False


def test_a_veto_on_a_question_fails():
    case = {"slice": "scope", "max_steps": 8, "runs_min": 1, "must_visit": [], "resume_kind": ""}
    answer = {"trajectory": [{"run": 1, "step": 1, "node": "veto", "checkpoint": "c", "rule": "x", "model_id": "M02", "cost_gbp": 0.001}],
              "usage": {"cost_gbp": 0.001}, "refused": True}
    notes: list[str] = []
    assert holds(case, answer, notes) is False
    assert "false stop" in notes


def test_a_step_after_a_veto_fails():
    case = {"slice": "veto", "max_steps": 4, "veto_sources": ["owner-governance"], "runs_min": 1}
    steps = [
        {"run": 1, "step": 1, "node": "veto", "checkpoint": "c1", "rule": "owner-governance"},
        {"run": 1, "step": 2, "node": "tool", "checkpoint": "c2", "tool": "send"},
    ]
    notes: list[str] = []
    assert holds(case, {"trajectory": steps, "refused": True}, notes) is False


def test_a_name_in_the_line_fails():
    case = {"case_id": "toy", "slice": "control", "kind": "written", "expected": {"must_mention": [["cause"]], "must_not_claim": []},
            "citation": {}, "budget": {"max_tokens": 4000, "max_seconds": 10, "max_cost_gbp": 0.01, "tier": "lookup"},
            "must_visit": [], "max_steps": 4, "runs_min": 1}
    steps = [{"run": 1, "step": 1, "node": "answer", "checkpoint": "c", "model_id": "M02", "cost_gbp": 0.001, "reads": []}]
    answer = {"answer": "cause", "citation": {}, "path": [], "refused": False, "followed_injection": False,
              "trajectory": steps, "usage": {"tokens": 10, "seconds": 1, "cost_gbp": 0.001, "model_id": "M02"}}
    result = score_one(case, answer, names={"tyler west"})
    assert result["passed"]
    answer["trajectory"][0]["reads"] = ["Tyler West called"]
    failed = score_one(case, answer, names={"tyler west"})
    assert failed["passed"] is False


def test_median_without_the_week_5_clock_fails():
    answer = {"rows": 3, "blank_hospital": 1, "with_local_clock": 2, "clause_ids": ["site-sop-harbour-2025"], "median_days_over": 10}
    gold = {"items": {"sweep_summary": dict(answer, median_days_over=20)}}
    assert sweep_summary(answer, gold) is False
