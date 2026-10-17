"""Score agent replies against a labeled case."""

from __future__ import annotations

TOOL_MAP = {
    "coverage_query": "coverage",
    "blank_results": "unfinished_photos",
    "queue": "grader_queue",
    "urgent_wait": "urgent_wait",
    "draft_letter": "letter_fields",
    "vendor_scores": "vendor_pilot",
    "coverage": "coverage",
    "unfinished_photos": "unfinished_photos",
    "grader_queue": "grader_queue",
    "letter_fields": "letter_fields",
    "vendor_pilot": "vendor_pilot",
    "retrieve": "retrieve",
    "letter_timing": "letter_timing",
}

COUNT_ALIASES = {
    "blank": "unfinished",
    "ungradable": "unreadable",
    "urgent": "sight_threatening",
}


def unsupported_reason(case: dict) -> str | None:
    tool = case.get("tool")
    expected = _expected(case)
    if tool == "session_list":
        return "a clinic due-count or capture count is not a catalog tool"
    if "wait_days" in expected:
        return "one person's wait is not a catalog tool"
    if "due_count" in expected or "capture_count" in expected:
        return "a clinic due-count or capture count is not a catalog tool"
    if tool == "blank_results" and expected.get("label") not in (None, "the region"):
        return "unfinished photos are not split by district"
    if "hospital_sensitivity" in expected or "applies_to_primary_care" in expected:
        return "the 93 percent slide is not a tool result"
    return None


def score_case(case: dict, reply: dict | None, latency_ms: float, model_calls: int) -> dict:
    reason = unsupported_reason(case)
    if reason:
        return _row(case, False, False, False, False, latency_ms, model_calls, False, "unsupported")
    expected_tool = TOOL_MAP.get(case.get("tool") or "", case.get("tool"))
    expect_refused = _expects_refusal(case)
    reply = reply or {}
    tool_ok = _tool_ok(reply, expected_tool, expect_refused)
    document_ok = _document_ok(case, reply, expect_refused)
    result_ok = _result_ok(case, reply, expect_refused)
    refusal_ok = _refusal_ok(case, reply, expect_refused)
    passed = tool_ok and document_ok and result_ok and refusal_ok
    error_type = "" if passed else _error_type(case, reply, tool_ok, result_ok, refusal_ok)
    return _row(
        case, tool_ok, document_ok, result_ok, refusal_ok, latency_ms, model_calls, passed, error_type
    )


def _expected(case: dict) -> dict:
    raw = case.get("expect", case.get("expected", {}))
    return raw if isinstance(raw, dict) else {}


def _expects_refusal(case: dict) -> bool:
    return bool(case.get("expect_refused")) or case.get("tool") == "refuse_diagnosis"


def _tool_ok(reply: dict, expected_tool: str | None, expect_refused: bool) -> bool:
    if expect_refused:
        return reply.get("tool") is None
    return bool(expected_tool) and reply.get("tool") == expected_tool


def _document_ok(case: dict, reply: dict, expect_refused: bool) -> bool:
    if expect_refused or not case.get("document_id"):
        return True
    return reply.get("document_id") == case["document_id"]


def _result_ok(case: dict, reply: dict, expect_refused: bool) -> bool:
    if expect_refused:
        return True
    if case.get("forbid_in_force") and _treated_as_in_force(reply):
        return False
    result = reply.get("result") or {}
    expect = _expected(case)
    if not expect:
        return True
    return _figures_match(reply.get("tool"), result, expect)


def _refusal_ok(case: dict, reply: dict, expect_refused: bool) -> bool:
    if expect_refused:
        if case.get("reason"):
            return reply.get("refused") is True and reply.get("reason") == case.get("reason")
        return reply.get("refused") is True
    if case.get("forbid_in_force"):
        return not _treated_as_in_force(reply)
    return reply.get("refused") is not True


def _figures_match(tool: str | None, result: dict, expect: dict) -> bool:
    if tool == "coverage":
        return result.get("eligible") == expect.get("eligible") and result.get("completed") == expect.get(
            "completed"
        )
    if tool == "unfinished_photos":
        return result.get("count") == expect.get("count")
    if tool == "grader_queue":
        counts = result.get("counts") or {}
        if "sight_threatening" in expect:
            return counts.get("sight_threatening") == expect["sight_threatening"]
        if "urgent_count" in expect:
            return counts.get("sight_threatening") == expect["urgent_count"]
        nested = expect.get("counts") or {}
        for key, value in nested.items():
            actual_key = COUNT_ALIASES.get(key, key)
            if counts.get(actual_key) != value:
                return False
        return True
    if tool == "retrieve":
        if "status" in expect and result.get("status") != expect["status"]:
            return False
        return True
    if tool == "letter_fields":
        fields = result.get("fields") or {}
        if expect.get("result_code") and fields.get("result_code") != expect["result_code"]:
            return False
        if expect.get("adds_diagnosis") is False and result.get("adds_diagnosis") is not False:
            return False
        if expect.get("invent_diagnosis") is False and result.get("adds_diagnosis") is not False:
            return False
        for key in ("local_pid", "forename", "surname"):
            if key in expect and fields.get(key) != expect[key]:
                return False
        return True
    if tool == "vendor_pilot":
        if "empty_model_labels" in expect and result.get("empty_model_labels") != expect["empty_model_labels"]:
            return False
        if "disagreements" in expect and result.get("disagreements") != expect["disagreements"]:
            return False
        return True
    if tool == "urgent_wait":
        if "median_days" in expect and result.get("median_days") != expect["median_days"]:
            return False
        if expect.get("draft_in_force") is False and result.get("draft_in_force") is not False:
            return False
        return True
    return True


def _treated_as_in_force(reply: dict) -> bool:
    result = reply.get("result") or {}
    if result.get("status") != "draft":
        return reply.get("refused") is not True and "in force" in (reply.get("answer") or "").lower()
    text = (reply.get("answer") or "").lower()
    if "not current" in text or "not in force" in text:
        return False
    if reply.get("reason") == "draft_as_policy":
        return False
    return "current policy" in text and reply.get("refused") is not True


def _error_type(case: dict, reply: dict, tool_ok: bool, result_ok: bool, refusal_ok: bool) -> str:
    if case.get("expect_refused") or case.get("tool") == "refuse_diagnosis":
        if not refusal_ok:
            return "missed_refusal"
    if _treated_as_in_force(reply):
        return "draft_treated_as_policy"
    answer = (reply.get("answer") or "").lower()
    if "healthy" in answer or "no disease" in answer:
        return "silent_model_treated_as_healthy"
    if reply.get("tool") == "letter_fields" and (
        (reply.get("result") or {}).get("adds_diagnosis") is True or "diagnosis:" in answer
    ):
        return "letter_invents_diagnosis"
    if not tool_ok or not result_ok:
        return "wrong_join"
    return "wrong_join"


def _row(
    case: dict,
    tool_ok: bool,
    document_ok: bool,
    result_ok: bool,
    refusal_ok: bool,
    latency_ms: float,
    model_calls: int,
    passed: bool,
    error_type: str,
) -> dict:
    return {
        "case_id": case.get("case_id"),
        "tool_ok": tool_ok,
        "document_ok": document_ok,
        "result_ok": result_ok,
        "refusal_ok": refusal_ok,
        "latency_ms": round(latency_ms, 1),
        "model_calls": model_calls,
        "passed": passed,
        "error_type": error_type,
    }
