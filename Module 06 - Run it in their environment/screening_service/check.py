"""Cold-start checks: log, result file, no images, Dockerfile boundary."""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from screening_service.service import IMAGE_SUFFIXES, serve

REPO_ROOT = Path(__file__).resolve().parents[2]
DOCKERFILE = REPO_ROOT / "Dockerfile"
FORBIDDEN = (".env", "data/truth", "data/eval")
COVERAGE = "How many eligible people are there?"
POLICY = "What is the current rule for who counts as screened?"


def main() -> None:
    errors: list[str] = []
    with tempfile.TemporaryDirectory() as raw:
        root = Path(raw)
        log_path = root / "access.log"
        result_path = root / "results.jsonl"
        first = serve("clinic nurse", COVERAGE, log_path, result_path)
        second = serve("screening director", POLICY, log_path, result_path)
        _check_replies(first, second, errors)
        _check_files(root, log_path, result_path, errors)
    _check_dockerfile(errors)
    if errors:
        raise SystemExit("Service check failed:\n- " + "\n- ".join(errors))
    print("Service check passed.")


def _check_replies(first: dict, second: dict, errors: list[str]) -> None:
    if first.get("tool") != "coverage" or (first.get("result") or {}).get("eligible") != 84120:
        errors.append(f"coverage run {first}")
    if second.get("tool") != "retrieve" or (second.get("result") or {}).get("status") != "in_force":
        errors.append(f"retrieval run {second}")
    for reply in (first, second):
        if "diagnosis:" in (reply.get("answer") or "").lower():
            errors.append("reply added a diagnosis")
        result = reply.get("result") or {}
        if result.get("adds_diagnosis") is True:
            errors.append("letter result adds a diagnosis")


def _check_files(root: Path, log_path: Path, result_path: Path, errors: list[str]) -> None:
    log_lines = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines()]
    callers = {line["who"] for line in log_lines}
    tools = {line["tool"] for line in log_lines}
    if callers != {"clinic nurse", "screening director"}:
        errors.append(f"access log callers {callers}")
    if tools != {"coverage", "retrieve"}:
        errors.append(f"access log tools {tools}")
    results = [json.loads(line) for line in result_path.read_text(encoding="utf-8").splitlines()]
    if len(results) != 2:
        errors.append(f"result file has {len(results)} lines")
    secret = os.environ.get("OPENAI_API_KEY", "")
    blob = log_path.read_text(encoding="utf-8") + result_path.read_text(encoding="utf-8")
    if secret and secret in blob:
        errors.append("run output contains the API key")
    images = [path.name for path in root.rglob("*") if path.suffix.lower() in IMAGE_SUFFIXES]
    if images:
        errors.append(f"run directory contains images: {images}")


def _check_dockerfile(errors: list[str]) -> None:
    if not DOCKERFILE.is_file():
        errors.append("Dockerfile is missing")
        return
    text = DOCKERFILE.read_text(encoding="utf-8")
    for forbidden in FORBIDDEN:
        if forbidden in text:
            errors.append(f"Dockerfile mentions {forbidden}")


if __name__ == "__main__":
    main()
