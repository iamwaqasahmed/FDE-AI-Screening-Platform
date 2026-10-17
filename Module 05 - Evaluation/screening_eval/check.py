"""Score the practice set. Optionally report the instructor set."""

from __future__ import annotations

import argparse

from screening_eval.model import RoutingModel
from screening_eval.runner import INSTRUCTOR_SET, PRACTICE_SET, load_cases, practice_passed, run_set


def main() -> None:
    parser = argparse.ArgumentParser(description="Score the Hartland agent on labeled cases.")
    parser.add_argument("--instructor", action="store_true", help="Also report data/eval/cases.jsonl.")
    args = parser.parse_args()
    practice = load_cases(PRACTICE_SET)
    if not practice:
        raise SystemExit(f"Practice set is missing: {PRACTICE_SET}")
    practice_rows = run_set(practice, RoutingModel())
    _print_report("practice", practice_rows)
    if not practice_passed(practice_rows):
        raise SystemExit("Practice evaluation failed.")
    if args.instructor:
        instructor = load_cases(INSTRUCTOR_SET)
        if not instructor:
            print("Instructor set is not present. Practice set passed.")
        else:
            _print_report("instructor", run_set(instructor, RoutingModel()))
    print("Practice evaluation passed.")


def _print_report(title: str, rows: list[dict]) -> None:
    passed = sum(1 for row in rows if row["passed"])
    unsupported = sum(1 for row in rows if row["error_type"] == "unsupported")
    failed = len(rows) - passed - unsupported
    print(f"{title}: {passed} passed, {failed} failed, {unsupported} unsupported, {len(rows)} total")
    for row in rows:
        if row["passed"]:
            continue
        print(
            f"  {row['case_id']}: {row['error_type']} "
            f"tool_ok={row['tool_ok']} document_ok={row['document_ok']} "
            f"result_ok={row['result_ok']} refusal_ok={row['refusal_ok']} "
            f"latency_ms={row['latency_ms']} model_calls={row['model_calls']}"
        )


if __name__ == "__main__":
    main()
