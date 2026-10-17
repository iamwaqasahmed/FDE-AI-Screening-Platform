"""Approved model register: on-premises open-weight models under a GPU quota, and cloud models limited by residency."""

from __future__ import annotations

import pandas as pd

PUBLIC = "public"
OFFICIAL = "public;official"
SENSITIVE = "public;official;official-sensitive"
COLUMNS = ["model_id", "name", "family", "deployment", "region", "data_residency", "approved_classifications",
           "cost_per_1k_input_gbp", "cost_per_1k_output_gbp", "latency_p50_ms", "latency_p95_ms", "context_tokens",
           "gpu_quota_hours_month", "status"]
MODELS = (
    ("M01", "Open-weight 70B instruct", "open-weight", "on-prem", "authority data centre", "UK", SENSITIVE, 0.0009, 0.0009, 1400, 4200, 32_000, 600),
    ("M02", "Open-weight 8B instruct", "open-weight", "on-prem", "authority data centre", "UK", SENSITIVE, 0.0002, 0.0002, 300, 900, 16_000, 200),
    ("M03", "Open-weight embedding base", "open-weight", "on-prem", "authority data centre", "UK", SENSITIVE, 0.00005, 0.0, 40, 120, 8_000, 80),
    ("M04", "Cloud LLM large", "commercial", "cloud", "UK South", "UK", SENSITIVE, 0.0025, 0.0100, 900, 2600, 128_000, 0),
    ("M05", "Cloud LLM small", "commercial", "cloud", "UK South", "UK", OFFICIAL, 0.00015, 0.0006, 350, 1100, 128_000, 0),
    ("M06", "Cloud LLM frontier", "commercial", "cloud", "US East", "US", PUBLIC, 0.0120, 0.0360, 1800, 6000, 200_000, 0),
    ("M07", "Cloud LLM EU", "commercial", "cloud", "EU West", "EU", OFFICIAL, 0.0008, 0.0024, 700, 2100, 64_000, 0),
)


def model_register() -> pd.DataFrame:
    frame = pd.DataFrame([list(model) + ["approved"] for model in MODELS], columns=COLUMNS)
    frame.insert(3, "task", ["embedding" if "embedding" in label else "generation" for label in frame["name"]])
    return frame


def approved_for(frame: pd.DataFrame, classification: str) -> pd.DataFrame:
    return frame[frame["approved_classifications"].str.split(";").map(lambda allowed: classification in allowed)]


def monthly_cost(row: pd.Series, input_tokens: float, output_tokens: float) -> float:
    return round(float(input_tokens / 1000 * row["cost_per_1k_input_gbp"] + output_tokens / 1000 * row["cost_per_1k_output_gbp"]), 2)
