"""Scripted model for a cold start. No API key."""

from __future__ import annotations


class ScriptedModel:
    def complete(self, messages: list[dict], tools: list[dict]) -> dict:
        question = _question(messages)
        if messages and messages[-1].get("role") == "tool":
            if "14" in question and "day" in question:
                return {"type": "final", "answer": "The 14-day pathway is not current policy."}
            return {"type": "final", "answer": "Use the tool result."}
        lowered = question.lower()
        if "14" in lowered and "day" in lowered:
            return {"type": "tool", "name": "retrieve", "arguments": {"question": question}}
        if "eligible" in lowered or "completed" in lowered or "how many" in lowered:
            return {"type": "tool", "name": "coverage", "arguments": {}}
        return {"type": "tool", "name": "retrieve", "arguments": {"question": question}}


def _question(messages: list[dict]) -> str:
    for message in messages:
        if message.get("role") == "user":
            return str(message.get("content") or "")
    return ""
