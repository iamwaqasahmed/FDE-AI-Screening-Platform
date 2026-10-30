"""chk-repo. Paths and scan results only. The watermark value is not printed.

This check grades the repository shape: required paths, the ignore rule, the policy document, the workflow, the credential file, the access request, the health test, and the secret scan. The watermark value is compared and not printed. Command output is not included in a failure.
"""

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
    """Return a miss for each access-request field that is missing or blank.

    The field must be a markdown bullet with that label. A present label with an empty value still fails.
    """
    problems = []
    for field in FIELDS:
        found = re.search(rf"^- {field}:\s*(.*)$", text, re.MULTILINE)
        # A missing bullet and a bullet with an empty value are the same miss.
        if not found or not found.group(1).strip():
            problems.append(f"access request is missing {field}")
    return problems


def repo_problems(work: Path, canary: str) -> list[str]:
    """Return the repository misses.

    Each required path that is not a file is named. The ignore file, the policy, the workflow, the credential file, and the access request are graded only when they exist, because a missing path is already reported. The credential watermark must equal the profile token and is not printed. The health test and the secret scan run last. Their output is discarded. Only the pass or fail is kept.
    """
    problems = [f"missing {relative}" for relative in REQUIRED if not (work / relative).is_file()]
    gitignore = work / ".gitignore"
    # The ignore rule is graded only when the file exists. A missing file is already in the required-path list.
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
        # The token is compared and not printed. A mismatch means these credentials belong to another profile.
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
    """Return nothing when the command exits cleanly, otherwise one failure labeled with the given name.

    The process output is captured and not returned, so a scan miss does not echo a secret.
    """
    completed = subprocess.run(args, cwd=work, capture_output=True, text=True)
    # A clean exit adds no miss. The captured output is thrown away.
    if completed.returncode == 0:
        return []
    return [f"{label} failed"]
