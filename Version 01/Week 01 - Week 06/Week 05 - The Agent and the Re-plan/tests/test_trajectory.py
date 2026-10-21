"""Trajectory rules on toy tasks."""

from __future__ import annotations

from simulation.eval.agent.trajectory_rules import holds
from simulation.eval.agent.trajectory_shape import holds as shape


def _case(**extra) -> dict:
    base = {"slice": "plan", "max_steps": 8, "runs_min": 1, "must_visit": [], "resume_kind": "", "veto_sources": [], "approver": ""}
    base.update(extra)
    return base


def test_a_write_fails():
    steps = [{"run": 1, "step": 1, "node": "answer", "checkpoint": "c", "model_id": "M02", "cost_gbp": 0.001, "writes": ["letter"]}]
    notes: list[str] = []
    assert shape(_case(), {"trajectory": steps, "usage": {"cost_gbp": 0.001}}, notes, check_model=True) is False
    assert "write" in notes


def test_m05_on_a_person_read_fails():
    steps = [{"run": 1, "step": 1, "node": "tool", "checkpoint": "c", "tool": "ophthalmology.referrals", "reads": ["LP000001"],
              "model_id": "M05", "cost_gbp": 0.001}]
    notes: list[str] = []
    assert shape(_case(), {"trajectory": steps, "usage": {"cost_gbp": 0.001}}, notes, check_model=True) is False
    assert "model" in notes


def test_an_approval_on_a_plain_question_fails():
    steps = [{"run": 1, "step": 1, "node": "approval", "checkpoint": "c", "approver": "A. Okonkwo", "decision": "pending", "reason": "wait"}]
    notes: list[str] = []
    assert holds(_case(), {"trajectory": steps}, notes) is False
    assert "false pause" in notes


def test_a_resume_that_repeats_a_read_fails():
    steps = [
        {"run": 1, "step": 1, "node": "tool", "checkpoint": "c1", "tool": "lookup", "reads": ["G2"]},
        {"run": 2, "step": 1, "node": "resume", "checkpoint": "c1", "reads": []},
        {"run": 2, "step": 2, "node": "tool", "checkpoint": "c2", "tool": "lookup", "reads": ["G2"]},
        {"run": 2, "step": 3, "node": "answer", "checkpoint": "c3", "reads": []},
    ]
    notes: list[str] = []
    assert holds(_case(slice="resume", resume_kind="sweep", runs_min=2, once_ids=[], once_tool="ophthalmology.referrals"), {"trajectory": steps}, notes) is False
    assert "reread" in notes


def test_a_pending_approval_can_be_resumed():
    steps = [
        {"run": 1, "step": 1, "node": "approval", "checkpoint": "c1", "approver": "A. Okonkwo", "decision": "pending", "reason": "leaves the office"},
        {"run": 2, "step": 1, "node": "resume", "checkpoint": "c1"},
        {"run": 2, "step": 2, "node": "approval", "checkpoint": "c2", "approver": "A. Okonkwo", "decision": "approved", "reason": "no person is named"},
        {"run": 2, "step": 3, "node": "answer", "checkpoint": "c3"},
    ]
    notes: list[str] = []
    assert holds(_case(slice="resume", resume_kind="approval", approver="A. Okonkwo", runs_min=2), {"trajectory": steps}, notes) is True
