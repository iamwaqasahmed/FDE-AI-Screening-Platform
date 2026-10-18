"""Write the Week 5 folder the checker scores."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from agent_check.gold import load
from reference_agent import backlog as backlog_mod
from reference_agent import business, cohort, governance, replan
from reference_agent.answers import solve
from reference_agent.load import read_csv
from reference_agent.texts import card, contract, press_text, reply
from simulation.eval.agent.bars import BACKLOG_COLUMNS, SWEEP_COLUMNS
from simulation.eval.agent.truth import wilson
from simulation.eval.evidence.text import _percent


def build(data: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    triage, done, backlog = backlog_mod.facts(data)
    planned = replan.facts(data, done)
    items = {**planned, "backlog_triage": triage, "pace": backlog_mod.pace(read_csv(data, "handover/delivery/velocity.csv"), done, planned["critical_path"], triage)}
    items.update(business.facts(data))
    items.update(governance.facts(data))
    chase, resend, scope = cohort.load(data)
    sweep = cohort.sweep(data, chase)
    items["sweep_summary"] = cohort.summary(sweep)
    items["veto_evidence"] = {"stop_tasks": 11, "families": 8, "wilson_lower": wilson(11, 11)}
    gold = load(data)
    questions = gold["questions"]
    _write_json(out / "findings.json", {"items": items})
    _write_jsonl(out / "answers.jsonl", solve(data, questions, items, chase, scope, resend, sweep))
    backlog[list(BACKLOG_COLUMNS)].to_csv(out / "backlog.csv", index=False)
    sweep[list(SWEEP_COLUMNS)].to_csv(out / "sweep.csv", index=False)
    (out / "contracts").mkdir(exist_ok=True)
    (out / "contracts/agent_trajectory.yaml").write_text(contract(items["service_account"]["client"]), encoding="utf-8")
    rates = gold["baselines"]
    (out / "agent-card.md").write_text(card(_percent(rates["single_loop"]["overall"]), _percent(rates["keyword_veto"]["overall"])), encoding="utf-8")
    (out / "cdo-reply.md").write_text(reply(items), encoding="utf-8")
    (out / "press-line.md").write_text(press_text(data), encoding="utf-8")


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
