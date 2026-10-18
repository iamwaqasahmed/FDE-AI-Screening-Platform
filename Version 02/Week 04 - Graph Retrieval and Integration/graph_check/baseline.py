"""Run a checked-in retriever and write its answers. The path is the document it cited.

    python -m graph_check.baseline --name keyword|tfidf --data <build> --out <file>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from graph_check.gold import load
from simulation.eval.baselines.answerer import answer as text_answer
from simulation.eval.baselines.corpus_index import CorpusIndex
from simulation.eval.baselines.retrieval import keyword, tfidf

RETRIEVERS = {"keyword": keyword, "tfidf": tfidf}


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Write keyword or TF-IDF answers for the Week 4 questions.")
    parser.add_argument("--name", required=True, choices=sorted(RETRIEVERS))
    parser.add_argument("--data", default="data")
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    data = Path(args.data)
    index = CorpusIndex.load(data / "corpus")
    retrieve = RETRIEVERS[args.name]
    rows = [_row(text_answer(case, retrieve(index, case["question"]))) for case in load(data)["questions"]]
    Path(args.out).write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")
    print(f"Wrote {len(rows)} {args.name} answers to {args.out}")


def _row(answer: dict) -> dict:
    usage = dict(answer.get("usage") or {})
    usage["cost_gbp"] = usage.get("cost_usd", 0)
    usage["model_id"] = "M02"
    cited = str((answer.get("citation") or {}).get("document_id", ""))
    return {
        "case_id": answer.get("case_id"),
        "answer": answer.get("answer"),
        "citation": answer.get("citation") or {},
        "refused": bool(answer.get("refused")),
        "followed_injection": bool(answer.get("followed_injection")),
        "path": [cited] if cited else [],
        "usage": usage,
    }


if __name__ == "__main__":
    main()
