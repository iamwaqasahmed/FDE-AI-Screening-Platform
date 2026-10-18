"""Score the Dockerfile and the three YAML records."""

from __future__ import annotations

import re

import yaml

from simulation.eval.handoff.bars import FACT_BAR
from simulation.eval.handoff.prose import has_rate, passed, score_text

MODEL_ID = re.compile(r"\bM\d+\b")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def score_dockerfile(text: str, gold: dict) -> dict:
    spec = gold["records"]["dockerfile"]
    reasons = []
    if not text.strip():
        return {"ok": False, "reasons": ["missing"]}
    for line in text.splitlines():
        stripped = line.strip()
        upper = stripped.upper()
        if upper.startswith("COPY") and any(token in stripped for token in spec["banned_copy"]):
            reasons.append("copy")
        if upper.startswith(("ENV ", "ARG ")) and _secret(stripped, spec["secret"]):
            reasons.append("secret")
    lowered = text.lower()
    if spec["banned_host"] in lowered or spec["banned_prefix"] in lowered:
        reasons.append("model")
    reasons += [model for model in MODEL_ID.findall(text) if model not in spec["allowed_models"]]
    return {"ok": not reasons, "reasons": reasons}


def score_contract(text: str, gold: dict) -> dict:
    spec = gold["records"]["contract"]
    loaded = _load(text)
    missing = [field for field in spec["fields"] if field not in loaded]
    prose = score_text(text, spec["facts"], spec["forbidden"])
    prose["missing"] = missing
    prose["ok"] = not missing and _contract_values(loaded, spec) and passed(prose, FACT_BAR)
    return prose


def score_transparency(text: str, gold: dict) -> dict:
    spec = gold["records"]["transparency"]
    loaded = _load(text)
    missing = [field for field in spec["fields"] if field not in loaded]
    terms = [term for term in spec["forbidden_terms"] if term.lower() in text.lower()]
    ok = not missing and not terms and _transparency_values(loaded, spec)
    return {"ok": ok, "missing": missing, "terms": terms, "coverage": 1.0 if ok else 0.0, "forbidden": terms}


def score_model_card(text: str, gold: dict) -> dict:
    spec = gold["records"]["model_card"]
    loaded = _load(text)
    missing = [field for field in spec["fields"] if field not in loaded]
    prose = score_text(text, spec["facts"], spec["forbidden"])
    numbers = [number for number in spec["numbers"] if not has_rate(text, float(number), spec["tolerance"])]
    sites = [site for site in spec["sites"] if site.lower() not in text.lower()]
    drift = spec["drift_site"].lower() in text.lower()
    prose["missing"] = missing
    prose["ok"] = not missing and not numbers and not sites and drift and passed(prose, FACT_BAR)
    return prose


def _contract_values(loaded: dict, spec: dict) -> bool:
    models = loaded.get("models")
    listed = models if isinstance(models, list) else [models]
    writes = loaded.get("writes")
    empty = writes in ([], None, "")
    account = str(loaded.get("account", "")).strip()
    owner = str(loaded.get("owner", "")).strip()
    return (
        str(loaded.get("service", "")).strip() == spec["service"]
        and str(loaded.get("zone", "")).strip() == spec["zone"]
        and empty
        and bool(listed)
        and all(str(model) in spec["sensitive_models"] for model in listed)
        and account not in {"", spec["banned_account"]}
        and owner in spec["owners"]
    )


def _transparency_values(loaded: dict, spec: dict) -> bool:
    sites = loaded.get("sites_in_scope")
    listed = sites if isinstance(sites, list) else []
    start = str(loaded.get("start_date") or "")
    return (
        str(loaded.get("owner", "")).strip() == spec["owner"]
        and spec["supplier"].lower() in str(loaded.get("supplier", "")).lower()
        and str(loaded.get("tier", "")).strip() in {spec["tier"], f"{spec['tier']}.0"}
        and spec["classification"] in str(loaded.get("data_classification", "")).lower()
        and spec["region_token"] in str(loaded.get("hosting_region", "")).lower()
        and set(map(str, listed)) == set(spec["sites"])
        and not DATE.search(start)
        and spec["human"] in str(loaded.get("human_in_the_loop", "")).lower()
        and spec["contact"] in str(loaded.get("contact_for_challenge", "")).lower()
    )


def _secret(line: str, words: list[str]) -> bool:
    name = line.split(None, 1)[1].split("=", 1)[0].strip()
    return any(word in name.lower() for word in words)


def _load(text: str) -> dict:
    try:
        loaded = yaml.safe_load(text) if text.strip() else {}
    except yaml.YAMLError:
        return {}
    return loaded if isinstance(loaded, dict) else {}
