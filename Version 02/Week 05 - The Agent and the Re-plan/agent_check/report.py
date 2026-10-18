"""Combine item, answer, file, contract, and prose results."""

from __future__ import annotations

from agent_check.items import ITEMS
from simulation.eval.agent.bars import ITEM_BAR, ROLE_BAR


def evaluate(gold, findings, answers, backlog, sweep, contract, card, reply, line, *, rerun: bool) -> dict:
    report = {
        "results": [_result(item, findings.get(item["id"]), gold) for item in ITEMS],
        "answers": answers,
        "backlog": backlog,
        "sweep": sweep,
        "contract": contract,
        "card": card,
        "reply": reply,
        "line": line,
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
        count = report["answers"].get("counts", {}).get(name, 0)
        lines.append(f"  {name} {rate:.2f} ({count})")
    lines.append("backlog ok" if report["backlog"].get("ok") else "backlog failed")
    lines.append("sweep ok" if report["sweep"].get("ok") else "sweep failed")
    if not rerun:
        for name in ("contract", "card", "reply", "line"):
            lines.append(f"{name} coverage {report[name].get('coverage', 0):.2f}")
        terms = (report["line"] or {}).get("terms") or []
        if terms:
            lines.append("line terms: " + ", ".join(terms))
    failed = [row["id"] for row in results if not row["passed"]]
    if failed:
        lines.append("failed: " + ", ".join(failed))
    missed = report["answers"].get("failed", [])
    if missed:
        lines.append("answers failed: " + ", ".join(missed[:12]) + (" ..." if len(missed) > 12 else ""))
    stops = report["answers"].get("missed_stops") or []
    if stops:
        lines.append("missed stops: " + ", ".join(stops[:8]))
    lines.append("Agent check passed." if report["ok"] else "Agent check failed.")
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
    if not report["answers"].get("ok") or not report["backlog"].get("ok") or not report["sweep"].get("ok"):
        return False
    if rerun:
        return True
    return all(report[name] is not None and report[name].get("ok") for name in ("contract", "card", "reply", "line"))
