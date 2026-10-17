"""A scripted model that chooses the catalog tool for a labeled question."""

from __future__ import annotations

import re

DISTRICTS = ("North City", "East City", "Hill Counties", "River Districts")


class RoutingModel:
    def complete(self, messages: list[dict], tools: list[dict]) -> dict:
        question = _question(messages)
        if messages and messages[-1].get("role") == "tool":
            if "14" in question and "day" in question:
                return {"type": "final", "answer": "The 14-day pathway is not current policy."}
            return {"type": "final", "answer": "Use the tool result."}
        if "14" in question and "day" in question:
            return {"type": "tool", "name": "retrieve", "arguments": {"question": question}}
        if "letter" in question.lower() and "LP" in question:
            return {
                "type": "tool",
                "name": "letter_fields",
                "arguments": {"local_pid": _local_pid(question)},
            }
        lowered = question.lower()
        if "model output" in lowered or "disagree" in lowered or "pilot" in lowered:
            return {"type": "tool", "name": "vendor_pilot", "arguments": {}}
        if "sight-threatening" in lowered or "queue" in lowered:
            return {"type": "tool", "name": "grader_queue", "arguments": {}}
        if "no result" in lowered:
            return {"type": "tool", "name": "unfinished_photos", "arguments": {}}
        district = _district(question)
        if district or "eligible" in lowered or "completed-screen" in lowered:
            arguments = {"district": district} if district else {}
            return {"type": "tool", "name": "coverage", "arguments": arguments}
        return {"type": "tool", "name": "retrieve", "arguments": {"question": question}}


class CountingModel:
    def __init__(self, inner) -> None:
        self.inner = inner
        self.calls = 0

    def complete(self, messages: list[dict], tools: list[dict]) -> dict:
        self.calls += 1
        return self.inner.complete(messages, tools)


def _question(messages: list[dict]) -> str:
    for message in messages:
        if message.get("role") == "user":
            return str(message.get("content") or "")
    return ""


def _local_pid(question: str) -> str:
    match = re.search(r"LP\d+", question)
    return match.group(0) if match else ""


def _district(question: str) -> str | None:
    for name in DISTRICTS:
        if name in question and f"{name} Eye Clinic" not in question:
            return name
    return None
