"""Pass rates by outcome, role, surface, and budget tier."""

from __future__ import annotations

from collections import defaultdict


def summarise(cases: list[dict], results: list[dict]) -> dict:
    by_id = {result["case_id"]: result for result in results}
    buckets: dict[str, dict[str, list[bool]]] = defaultdict(lambda: defaultdict(list))
    for case in cases:
        passed = bool(by_id.get(case["case_id"], {}).get("passed"))
        buckets["overall"]["all"].append(passed)
        buckets["outcome"][case["tags"]["outcome"]].append(passed)
        buckets["tier"][case["budget"]["tier"]].append(passed)
        for role in case["tags"]["roles"]:
            buckets["role"][role].append(passed)
        for surface in case["tags"]["surfaces"]:
            buckets["surface"][surface].append(passed)
    return {
        axis: {key: {"cases": len(values), "pass_rate": round(sum(values) / len(values), 3)} for key, values in sorted(groups.items())}
        for axis, groups in buckets.items()
    }
