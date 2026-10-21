"""One ask: call the agent, append the access log, append the result file."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from screening_agent.loop import ask
from screening_service.model import ScriptedModel

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".dcm", ".tif", ".tiff"}


def serve(
    who: str,
    question: str,
    log_path: Path,
    result_path: Path,
    model=None,
) -> dict:
    if not who.strip():
        raise ValueError("who is required.")
    reply = ask(question, model or ScriptedModel())
    reply = _without_diagnosis(reply)
    _append_log(log_path, who, question, reply)
    _append_result(result_path, reply)
    return reply


def _without_diagnosis(reply: dict) -> dict:
    result = reply.get("result")
    if isinstance(result, dict) and result.get("adds_diagnosis"):
        result = dict(result)
        result["adds_diagnosis"] = False
        reply = dict(reply)
        reply["result"] = result
    answer = reply.get("answer") or ""
    if "diagnosis:" in answer.lower():
        reply = dict(reply)
        reply["answer"] = "A letter may repeat a grader code. It must not contain a diagnosis."
    return reply


def _append_log(path: Path, who: str, question: str, reply: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = {
        "time": datetime.now(timezone.utc).isoformat(),
        "who": who,
        "question": question,
        "tool": reply.get("tool"),
        "document_id": reply.get("document_id"),
        "refused": reply.get("refused"),
    }
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(line) + "\n")


def _append_result(path: Path, reply: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(reply) + "\n")
