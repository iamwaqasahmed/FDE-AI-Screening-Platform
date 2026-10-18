"""Combine item, cluster, probe, contract, and note results. Print failures without a gold value."""

from __future__ import annotations

from enterprise_check.contracts import passed as contracts_passed
from enterprise_check.items import ITEMS
from simulation.eval.enterprise.bars import ITEM_BAR, ROLE_BAR

ITEM_PASS = ITEM_BAR
ROLE_PASS = ROLE_BAR


def evaluate(gold, findings, cluster_row, probe_row, contract_rows, model_row, note_row, *, rerun: bool) -> dict:
    report = {
        "results": [_result(item, findings.get(item["id"]), gold) for item in ITEMS],
        "clusters": cluster_row,
        "probes": probe_row,
        "contracts": contract_rows,
        "model": model_row,
        "note": note_row,
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
    lines.append(_metric("clusters", report["clusters"]))
    lines.append(_metric("pathway", report["probes"]))
    if not rerun and report["contracts"] is not None:
        good = sum(row["ok"] for row in report["contracts"].values())
        lines.append(f"contracts {good}/{len(report['contracts'])}")
    if not rerun and report["model"] is not None:
        lines.append(f"model coverage {report['model']['coverage']:.2f}")
    if not rerun and report["note"] is not None:
        lines.append(f"note coverage {report['note']['coverage']:.2f}")
    failed = [row["id"] for row in results if not row["passed"]]
    if failed:
        lines.append("failed: " + ", ".join(failed))
    slices = [name for name, ok in report["clusters"].get("slices", {}).items() if not ok]
    if slices:
        lines.append("slices failed: " + ", ".join(slices))
    lines.append("Enterprise check passed." if _ok(report, rerun) else "Enterprise check failed.")
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


def _metric(name: str, row: dict) -> str:
    if "f05" in row:
        return f"{name} P {row['precision']:.2f} R {row['recall']:.2f} F0.5 {row['f05']:.2f}"
    return f"{name} coverage {row.get('coverage', 0):.2f}"


def _ok(report: dict, rerun: bool) -> bool:
    results = [row for row in report["results"] if row["mode"] == "computed" or not rerun]
    if not results or sum(row["passed"] for row in results) / len(results) < ITEM_PASS:
        return False
    for row in report["roles"].values():
        if rerun and row["computed"] == 0:
            continue
        rate = (row["computed_passed"] / row["computed"]) if rerun else (row["passed"] / row["total"])
        if rate < ROLE_PASS:
            return False
    if not report["clusters"].get("ok"):
        return False
    if not report["probes"].get("ok"):
        return False
    if rerun:
        return True
    if report["contracts"] is not None and not contracts_passed(report["contracts"]):
        return False
    if report["model"] is not None and not report["model"].get("ok"):
        return False
    if report["note"] is not None and not report["note"].get("ok"):
        return False
    return True
