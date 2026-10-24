"""chk-w1-repo. Paths and scan results only. The watermark value is not printed."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

FIELDS = ("Requester", "Data", "Purpose", "Classification")
REQUIRED = (
    "app.py",
    "scan.py",
    "Dockerfile",
    "compose.yaml",
    "deploy/namespace.yaml",
    ".github/workflows/ci.yml",
    "policy/pol-assistant-use.md",
    "tests/test_health.py",
    ".gitignore",
)


def access_problems(text: str) -> list[str]:
    problems = []
    for field in FIELDS:
        found = re.search(rf"^- {field}:\s*(.*)$", text, re.MULTILINE)
        if not found or not found.group(1).strip():
            problems.append(f"access request is missing {field}")
    return problems


def repo_problems(work: Path, canary: str) -> list[str]:
    problems = [f"missing {relative}" for relative in REQUIRED if not (work / relative).is_file()]
    gitignore = work / ".gitignore"
    if gitignore.is_file() and "credentials/" not in gitignore.read_text(encoding="utf-8"):
        problems.append(".gitignore must ignore credentials/")
    policy = work / "policy" / "pol-assistant-use.md"
    if policy.is_file() and "doc_id: pol-assistant-use" not in policy.read_text(encoding="utf-8"):
        problems.append("assistant-use rule is not the cluster document")
    workflow = work / ".github" / "workflows" / "ci.yml"
    if workflow.is_file():
        workflow_text = workflow.read_text(encoding="utf-8")
        if "scan.py" not in workflow_text or "evaluation-gate" not in workflow_text:
            problems.append("ci workflow is missing the scan or the evaluation-gate placeholder")
    credentials = work / "credentials" / "dev.json"
    if not credentials.is_file():
        problems.append("credentials/dev.json is missing")
    else:
        watermark = str(json.loads(credentials.read_text(encoding="utf-8")).get("watermark", ""))
        if watermark != canary:
            problems.append("credentials do not match this profile")
    request = work / "access-request.md"
    if not request.is_file():
        problems.append("access-request.md is missing")
    else:
        problems.extend(access_problems(request.read_text(encoding="utf-8")))
    problems.extend(_command(work, [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"], "health test"))
    problems.extend(_command(work, [sys.executable, "scan.py"], "secret scan"))
    return problems


def _command(work: Path, args: list[str], label: str) -> list[str]:
    completed = subprocess.run(args, cwd=work, capture_output=True, text=True)
    if completed.returncode == 0:
        return []
    return [f"{label} failed"]
