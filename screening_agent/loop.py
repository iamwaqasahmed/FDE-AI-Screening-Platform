"""Run a model against the catalog. Answers are copied from tool results."""

from __future__ import annotations

import json
from typing import Protocol

from screening_agent.catalog import call_tool, openai_tools

SITES = (
    "Hill Counties Health Centre",
    "Oakridge Primary Care",
    "North City Eye Clinic",
)
MAX_STEPS = 4


class Model(Protocol):
    def complete(self, messages: list[dict], tools: list[dict]) -> dict:
        """Return a tool call or a final sentence."""


def ask(question: str, model: Model) -> dict:
    reason = _question_refusal(question)
    if reason:
        return _refusal(reason, _refusal_sentence(reason))
    messages = [
        {"role": "system", "content": _SYSTEM},
        {"role": "user", "content": question},
    ]
    tool_name = None
    tool_result = None
    for step in range(MAX_STEPS):
        decision = model.complete(messages, openai_tools())
        if decision.get("type") == "tool":
            tool_name = decision["name"]
            arguments = decision.get("arguments") or {}
            tool_result = call_tool(tool_name, arguments)
            call_id = f"call_{step}"
            messages.append(
                {
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [
                        {
                            "id": call_id,
                            "type": "function",
                            "function": {
                                "name": tool_name,
                                "arguments": json.dumps(arguments),
                            },
                        }
                    ],
                }
            )
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call_id,
                    "content": json.dumps(tool_result),
                }
            )
            continue
        if tool_result is None:
            return _refusal("no_tool", "No tool ran, so there is no result to repeat.")
        answer = decision.get("answer") or ""
        if _claims_draft_is_current_policy(tool_name, tool_result, answer):
            return {
                "answer": _refusal_sentence("draft_as_policy"),
                "tool": tool_name,
                "document_id": tool_result.get("document_id"),
                "result": tool_result,
                "refused": True,
                "reason": "draft_as_policy",
            }
        return {
            "answer": _answer_from_tool(question, tool_name, tool_result),
            "tool": tool_name,
            "document_id": tool_result.get("document_id"),
            "result": tool_result,
            "refused": False,
            "reason": None,
        }
    return _refusal("no_tool", "No tool ran, so there is no result to repeat.")


def _question_refusal(question: str) -> str | None:
    text = question.lower()
    if "retina" in text or "diagnos" in text:
        return "diagnosis"
    if "without a grader" in text:
        return "unsigned_referral"
    return None


def _claims_draft_is_current_policy(tool_name: str | None, result: dict | None, answer: str) -> bool:
    if tool_name != "retrieve" or not result or result.get("status") != "draft":
        return False
    text = answer.lower()
    if "not current" in text or "not in force" in text:
        return False
    return "current policy" in text


def _answer_from_tool(question: str, tool_name: str, result: dict) -> str:
    scope = ""
    if any(site.lower() in question.lower() for site in SITES):
        named = ", ".join(SITES)
        scope = f" Scope: {named}. The tools do not return a separate count per clinic."
    if tool_name == "coverage":
        return (
            f"Eligible people: {result['eligible']}. "
            f"Completed screens: {result['completed']}.{scope}"
        )
    if tool_name == "grader_queue":
        count = result["counts"]["sight_threatening"]
        return f"Sight-threatening cases: {count}.{scope}"
    if tool_name == "letter_fields":
        code = result["fields"].get("result_code", "")
        return f"Result code: {code}."
    if tool_name == "retrieve":
        return f"Status: {result['status']}. Document: {result['document_id']}."
    return f"Tool {tool_name} returned a result.{scope}"


def _refusal(reason: str, answer: str) -> dict:
    return {
        "answer": answer,
        "tool": None,
        "document_id": None,
        "result": None,
        "refused": True,
        "reason": reason,
    }


def _refusal_sentence(reason: str) -> str:
    sentences = {
        "diagnosis": "A grader signs any grade. This drop has no retinal image to read.",
        "unsigned_referral": "A grader has not signed this referral, so none is written.",
        "draft_as_policy": "The 14-day pathway is a draft. It is not current policy.",
        "no_tool": "No tool ran, so there is no result to repeat.",
    }
    return sentences[reason]


_SYSTEM = (
    "You are the Hartland screening agent. Call one catalogued tool for a count or a rule. "
    "Repeat that tool result. Do not invent numbers, diagnoses, or referrals. "
    "A draft document is not current policy."
)
