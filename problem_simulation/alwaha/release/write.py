"""Write the rel-w1d1 pack and the facilitator truth beside it."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from alwaha.config.profile import Profile
from alwaha.corpus.texts import access_form, assistant_use, fact_problems, minutes, postmortem, sample_letter, stage_gate, zones_page
from alwaha.engagement.personas import load_personas
from alwaha.paths import STARTER_ROOT
from alwaha.release.fingerprint import fingerprint

RELEASE = "rel-w1d1"
SAMPLE_MARKER = "SAMPLE-REFERRAL-ALWAHA"


def reset(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _persona_page(data: dict) -> str:
    card = data["card"]
    goals = "\n".join(f"- {goal}" for goal in card["goals"])
    return f"# {card['name']}\n\nRole: {card['role']}\n\n{card['says_first']}\n\nGoals:\n\n{goals}\n"


def _release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w1d1

From: the office of the Chief Digital and Transformation Officer
Case date: 2027-01-10

This is the kickoff. Dev credentials are watermarked. They are not a grant of the full history. The day notes are [Week 1, Day 1](../../Week%2001/Day%2001/README.md).

Files:

{listed}
"""


def _truth_payload(personas: dict[str, dict], canary: str) -> dict:
    payload = {}
    for key, data in personas.items():
        payload[key] = {
            "id": key,
            "must_surface": list(data["must_surface"]),
            "banned": list(data["banned"]),
            "facts": data["facts"],
            "tree": [
                {"node_id": node.node_id, "keywords": list(node.keywords), "answer": node.answer, "releases": list(node.releases), "parent": node.parent}
                for node in data["tree"]
            ],
            "card": {**data["card"], "goals": list(data["card"]["goals"])},
        }
    payload["canary"] = canary
    return payload


def copy_starter(destination: Path) -> None:
    shutil.copytree(
        STARTER_ROOT,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache"),
        dirs_exist_ok=True,
    )


def write_release(profile: Profile, pack: Path, truth: Path) -> str:
    if not STARTER_ROOT.is_dir():
        raise SystemExit(f"Starter template is missing at {STARTER_ROOT}.")
    minutes_text, postmortem_text = minutes(), postmortem()
    problems = fact_problems(minutes_text, postmortem_text)
    if problems:
        raise SystemExit("Corpus facts: " + "; ".join(problems))
    personas = load_personas()
    canary = profile.canary()
    reset(pack)
    reset(truth)
    documents = {
        "corpus/pol-stage-gate.md": stage_gate(),
        "corpus/pol-assistant-use.md": assistant_use(),
        "corpus/doc-postmortem-2023.md": postmortem_text,
        "corpus/doc-minutes-2023-11.md": minutes_text,
        "forms/access-request.md": access_form(),
        "sample/referral-letter.md": sample_letter(canary),
        "world/zones.md": zones_page(),
    }
    for key in sorted(personas):
        documents[f"personas/{key}.md"] = _persona_page(personas[key])
    for relative, text in documents.items():
        _write(pack / relative, text)
    credentials = {
        "profile": profile.name,
        "token": profile.token(),
        "watermark": canary,
        "scope": "watermarked-dev-sample",
        "history": "not-included",
    }
    _write(pack / "credentials" / "dev.json", json.dumps(credentials, indent=2) + "\n")
    copy_starter(pack / "starter")
    rule = pack / "starter" / "policy" / "pol-assistant-use.md"
    if rule.read_text(encoding="utf-8") != assistant_use():
        raise SystemExit("starter/policy/pol-assistant-use.md does not match the corpus document.")
    names = sorted(path.relative_to(pack).as_posix() for path in pack.rglob("*") if path.is_file())
    names.append("README.md")
    _write(pack / "README.md", _release_note(sorted(names)))
    _write(truth / "personas.json", json.dumps(_truth_payload(personas, canary), indent=2) + "\n")
    _write(truth / "canary.txt", canary + "\n")
    digest = fingerprint(pack, truth)
    _write(truth / "fingerprint.txt", digest + "\n")
    return digest
