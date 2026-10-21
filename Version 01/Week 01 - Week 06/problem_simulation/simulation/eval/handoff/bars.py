"""Thresholds, columns, and paths for the Week 6 handoff."""

from __future__ import annotations

from pathlib import Path

ITEM_BAR = 0.8
ROLE_BAR = 0.6
FACT_BAR = 0.8
RATE_TOLERANCE = 0.01
HAZARD_NEED = 6
SERVICE_ID = "screening-agent"
ZONE = "authority"
BANNED_ACCOUNT = "discovery-team"
SENSITIVE_MODELS = ("M01", "M02", "M03", "M04")
IMAGE_MODELS = ("M01", "M02", "M04")
FLOW_COLUMNS = ("flow_id", "source", "target", "data", "allowed", "rule")
THREAT_COLUMNS = ("threat_id", "title", "components", "evidence", "standard", "live", "mitigation", "owner")
HAZARD_COLUMNS = ("hazard_id", "cause", "effect", "anchor", "evidence", "control", "control_owner", "signed_by")
CONTRACT_FIELDS = (
    "service", "zone", "dr_tier", "image", "data", "account", "owner", "scopes", "writes", "models",
    "logs", "audit", "sign_in", "incidents", "register", "fails_when",
)
DATA = (
    "photograph", "year_of_birth", "date_of_birth", "hospital_study", "vendor_score", "signed_grade",
    "local_id", "record_reference",
)
ALLOWED = ("yes", "no", "pending")

SIM = Path(__file__).resolve().parents[3]
REPO = SIM.parents[1]
WEEK00 = REPO / "Week 00 - Self Paced"
TOKENS = SIM / "serve" / "tokens.yaml"
SLOS = SIM / "serve" / "slos.yaml"
DOCKERFILE = WEEK00 / "Dockerfile"
MODEL_PY = WEEK00 / "Module 04 - The agent" / "screening_agent" / "openai_model.py"
SERVICE_PY = WEEK00 / "Module 06 - Run it in their environment" / "screening_service" / "service.py"
RUN_PY = WEEK00 / "Module 06 - Run it in their environment" / "screening_service" / "run.py"
