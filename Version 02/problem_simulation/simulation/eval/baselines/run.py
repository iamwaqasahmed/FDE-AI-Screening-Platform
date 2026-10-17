"""Run every baseline over the gold cases and write scores to eval/baselines/. They are meant to lose."""

from __future__ import annotations

import json
from pathlib import Path

from simulation.eval.baselines.answerer import answer as text_answer
from simulation.eval.baselines.corpus_index import CorpusIndex
from simulation.eval.baselines.retrieval import keyword, tfidf
from simulation.eval.baselines.single_loop import SingleLoopAgent
from simulation.eval.baselines.sql_single_hop import SqlBaseline
from simulation.eval.score import score_case, summarise


def baselines(data: Path) -> dict:
    index = CorpusIndex.load(data / "corpus")
    return {
        "keyword": lambda case: text_answer(case, keyword(index, case["question"])),
        "tfidf": lambda case: text_answer(case, tfidf(index, case["question"])),
        "sql_single_hop": SqlBaseline(data / "handover", index),
        "single_loop_agent": SingleLoopAgent(index),
    }


def run_all(data: Path) -> dict:
    cases = [json.loads(line) for line in (data / "eval" / "cases.jsonl").read_text(encoding="utf-8").splitlines() if line]
    out = data / "eval" / "baselines"
    out.mkdir(parents=True, exist_ok=True)
    summary = {}
    for name, baseline in baselines(data).items():
        results = [score_case(case, baseline(case)) for case in cases]
        summary[name] = summarise(cases, results)
        (out / f"{name}.json").write_text(json.dumps({"summary": summary[name], "results": results}, indent=1), encoding="utf-8")
    (out / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary
