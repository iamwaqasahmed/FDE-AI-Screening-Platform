"""Combine item, answer, redaction, extract, contract, and note results."""

from __future__ import annotations

from evidence_check.items import ITEMS
from simulation.eval.evidence.bars import ITEM_BAR, ROLE_BAR


def evaluate(gold, findings, answers, redaction, extract, contract, card, note, *, rerun: bool) -> dict:
    report = {
        "results": [_result(item, findings.get(item["id"]), gold) for item in ITEMS],
        "answers": answers,
        "redaction": redaction,
        "extract": extract,
        "contract": contract,
        "card": card,
        "note": note,
    }
    report["roles"] = _roles(report["results"])
    report["ok"] = _ok(report, rerun)
    return report


def render(report: dict, *, rerun: bool) -> str:
    results = [row for row in report["results"] if row["mode"] == "computed" or not rerun]
    lines = [f"items {sum(row['passed'] for row in results)}/{len(results)}"]
    for role, row in sorted(report["roles"].items()):
        if rerun and row["computed"] == 0:
            continue
        counted = row["computed"] if rerun else row["total"]
        passed = row["computed_passed"] if rerun else row["passed"]
        lines.append(f"  {role} {passed}/{counted}")
    lines.append(f"answers {report['answers'].get('overall', 0):.2f}")
    for name, rate in sorted(report["answers"].get("slices", {}).items()):
        lines.append(f"  {name} {rate:.2f}")
    lines.append(f"redaction recall {report['redaction'].get('recall', 0):.2f} precision {report['redaction'].get('precision', 0):.2f}")
    lines.append("extract ok" if report["extract"].get("ok") else "extract failed")
    if not rerun and report["contract"] is not None:
        lines.append(f"contract coverage {report['contract'].get('coverage', 0):.2f}")
    if not rerun and report["card"] is not None:
        lines.append(f"card coverage {report['card'].get('coverage', 0):.2f}")
    if not rerun and report["note"] is not None:
        lines.append(f"note coverage {report['note'].get('coverage', 0):.2f}")
    failed = [row["id"] for row in results if not row["passed"]]
    if failed:
        lines.append("failed: " + ", ".join(failed))
    missed = report["answers"].get("failed", [])
    if missed:
        lines.append("answers failed: " + ", ".join(missed[:12]) + (" ..." if len(missed) > 12 else ""))
    lines.append("Evidence check passed." if report["ok"] else "Evidence check failed.")
    return "\n".join(lines)


def _result(item: dict, answer, gold: dict) -> dict:
    try:
        ok = isinstance(answer, dict) and bool(item["check"](answer, gold))
    except (TypeError, ValueError, KeyError):
        ok = False
    return {"id": item["id"], "roles": item["roles"], "mode": item["mode"], "passed": ok}


def _roles(results: list[dict]) -> dict:
    found: dict[str, dict] = {}
    for row in results:
        for role in row["roles"]:
            slot = found.setdefault(role, {"total": 0, "passed": 0, "computed": 0, "computed_passed": 0})
            slot["total"] += 1
            slot["passed"] += int(row["passed"])
            if row["mode"] == "computed":
                slot["computed"] += 1
                slot["computed_passed"] += int(row["passed"])
    return found


def _ok(report: dict, rerun: bool) -> bool:
    results = [row for row in report["results"] if row["mode"] == "computed" or not rerun]
    if not results or sum(row["passed"] for row in results) / len(results) < ITEM_BAR:
        return False
    for row in report["roles"].values():
        if rerun and row["computed"] == 0:
            continue
        rate = (row["computed_passed"] / row["computed"]) if rerun else (row["passed"] / row["total"])
        if rate < ROLE_BAR:
            return False
    if not report["answers"].get("ok") or not report["redaction"].get("ok") or not report["extract"].get("ok"):
        return False
    if rerun:
        return True
    return all(report[name] is None or report[name].get("ok") for name in ("contract", "card", "note"))
