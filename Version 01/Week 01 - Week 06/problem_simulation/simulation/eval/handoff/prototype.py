"""What the Week 00 - Self Paced container still does that the standards forbid."""

from __future__ import annotations

import re
from datetime import timedelta

import yaml

from simulation.architecture.model_register import MODELS
from simulation.eval.handoff.bars import (
    BANNED_ACCOUNT,
    DOCKERFILE,
    MODEL_PY,
    RUN_PY,
    SERVICE_ID,
    SERVICE_PY,
    TOKENS,
)
from simulation.world.engagement import OWNER_NAMED


def facts() -> dict:
    for path in (DOCKERFILE, MODEL_PY, SERVICE_PY, RUN_PY, TOKENS):
        if not path.is_file():
            raise FileNotFoundError(path)
    dockerfile, model, service, run = (path.read_text(encoding="utf-8") for path in (DOCKERFILE, MODEL_PY, SERVICE_PY, RUN_PY))
    default = _default(model)
    copies = _copies(dockerfile)
    logs_question = '"question": question' in service
    sign_in = "Authorization" in service or "Authorization" in run
    on_register = default in {row[0] for row in MODELS} or default in {row[1] for row in MODELS}
    return {
        "prototype_gaps": {
            "copies": copies,
            "default_model": default,
            "model_host": "api.openai.com" if "api.openai.com" in model else "",
            "on_register": on_register,
            "logs_question": logs_question,
            "sign_in": sign_in,
            "gaps": _gaps(copies, on_register, logs_question, sign_in),
            "replace_with": _cheapest(),
        },
        "production_account": _account(),
    }


def _copies(dockerfile: str) -> list[str]:
    found = []
    for line in dockerfile.splitlines():
        if not line.strip().upper().startswith("COPY"):
            continue
        for token in re.findall(r"data/[\w./-]+|\.env", line):
            cleaned = token.rstrip("/")
            if cleaned not in found:
                found.append(cleaned)
    return found


def _default(model: str) -> str:
    match = re.search(r'DEFAULT_MODEL = "([^"]+)"', model)
    if not match:
        raise ValueError("Week 00 - Self Paced model adapter has no DEFAULT_MODEL")
    return match.group(1)


def _gaps(copies: list[str], on_register: bool, logs_question: bool, sign_in: bool) -> list[dict]:
    found = []
    if copies:
        found.append({"gap": "data_in_image", "standard": "data-classification-policy"})
    if not on_register:
        found.append({"gap": "model_off_register", "standard": "cloud-policy"})
    if logs_question:
        found.append({"gap": "question_in_log", "standard": "security-logging-standard"})
        found.append({"gap": "local_log", "standard": "security-logging-standard"})
    if not sign_in:
        found.append({"gap": "no_sign_in", "standard": "security-authentication-standard"})
    return found


def _cheapest() -> str:
    generators = [row for row in MODELS if "official-sensitive" in row[6] and "embedding" not in row[1]]
    return min(generators, key=lambda row: (row[7], row[0]))[0]


def _account() -> dict:
    rows = yaml.safe_load(TOKENS.read_text(encoding="utf-8"))["tokens"]
    discovery = next(row for row in rows if row["client"] == BANNED_ACCOUNT)
    expires = str(discovery["expires"])
    end = (OWNER_NAMED + timedelta(days=4)).isoformat()
    return {
        "client": discovery["client"],
        "expires": expires,
        "expires_this_week": OWNER_NAMED.isoformat() <= expires <= end,
        "standard": "security-authentication-standard",
        "production_client_exists": any(row["client"] == SERVICE_ID for row in rows),
    }
