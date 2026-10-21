"""Architecture and governance cases: zones, DR tiers, threats, access, the model register, the catalogue, and load figures."""

from __future__ import annotations

import pandas as pd

from simulation.architecture.model_register import approved_for, monthly_cost
from simulation.architecture.threats import MUST_MENTION
from simulation.estate.eval_common import ARCH_ROLES, ask

A = "handover/architecture"
COMPONENTS, REGISTER, CATALOGUE = f"{A}/components.csv", f"{A}/model_register.csv", f"{A}/data_catalogue.csv"
IDENTITY, AUDIT = "handover/identity/accounts.csv", "handover/audit/record_reads.jsonl"
NOTE_TOKENS, SUMMARY_TOKENS = 400, 80


def architecture_cases(world: dict) -> list[dict]:
    files, gold = world["files"], world["gold"]
    return (_components(files[COMPONENTS]) + _threats(gold) + _access(gold) + _models(files) + _catalogue(gold)
            + _load(files))


def _components(components: pd.DataFrame) -> list[dict]:
    tiers = components.set_index("component")["dr_tier"]
    fhir = sorted(components.loc[components["protocol"].str.contains("FHIR"), "component"])
    no_backup = sorted(components.loc[components["dr_tier"] == 4, "component"])
    return [
        ask("dr-tiers", "What recovery tier are booking and the registry in?", {"booking": int(tiers["booking"]), "registry": int(tiers["registry"])},
            "architecture", ARCH_ROLES, (COMPONENTS,), "lookup"),
        ask("no-backup", "Which components have no backup?", {"components": no_backup}, "architecture", ARCH_ROLES, (COMPONENTS,),
            "lookup", kind="set"),
        ask("fhir", "Which components speak FHIR today?", {"components": fhir}, "architecture", ARCH_ROLES, (COMPONENTS,), "lookup",
            kind="set"),
        ask("lab-protocol", "How does the HbA1c lab feed reach the authority?",
            {"protocol": components.set_index("component").loc["lab", "protocol"], "via": "integration-engine"},
            "architecture", ARCH_ROLES, (COMPONENTS,), "lookup"),
    ]


def _threats(gold: dict) -> list[dict]:
    threats = {item["threat_id"]: item for item in gold["threats"]}
    sources = (COMPONENTS, IDENTITY, "handover/identity/role_mappings.csv", "handover/service_desk/tickets.csv")
    return [
        ask("threat-callback", "Which data path crosses trust zones on its way to the grader workbench, and through which zones?",
            {"components": threats["T1"]["components"], "zones": threats["T1"]["zones"]}, "architecture", ARCH_ROLES, (COMPONENTS,)),
        ask("threat-service-account", "Which service account holds more rights than it needs, and which role is excess?",
            {"account_id": threats["T2"]["account_id"], "role": threats["T2"]["excess_role"]}, "architecture", ARCH_ROLES, sources[1:3]),
        ask("threat-model", "List the threats a current-state threat model must find.",
            {"must_mention": [MUST_MENTION[key] for key in sorted(threats)] + [threats["T2"]["account_id"]],
             "threat_ids": sorted(threats)},
            "architecture", ARCH_ROLES, sources, "written", kind="written"),
    ]


def _access(gold: dict) -> list[dict]:
    stale = sorted(item["account_id"] for item in gold["stale_access"])
    flagged = pd.DataFrame(gold["inappropriate_access"])
    return [
        ask("stale-accounts", "Which accounts still have access they should have lost?", {"account_ids": stale},
            "architecture", ARCH_ROLES, (IDENTITY, "handover/identity/role_mappings.csv", "handover/workforce/staff.csv"), "analysis",
            kind="set"),
        ask("inappropriate-reads", "During the access review window, which account read records without a care relationship, and how many reads?",
            {"account_id": str(flagged["account_id"].iloc[0]), "reads": int(len(flagged)), "ref": "INC-0262"},
            "architecture", ARCH_ROLES, (AUDIT, IDENTITY), "analysis"),
        ask("inappropriate-records", "How many distinct records were read inappropriately?", {"count": int(flagged["booking_id"].nunique())},
            "architecture", ARCH_ROLES, (AUDIT,), "analysis"),
    ]


def _models(files: dict) -> list[dict]:
    register = files[REGISTER]
    sensitive = approved_for(register, "official-sensitive")
    public_only = register.loc[register["approved_classifications"] == "public", "model_id"].tolist()
    generation = sensitive[sensitive["task"] == "generation"]
    cheapest = generation.sort_values(["cost_per_1k_input_gbp", "model_id"]).iloc[0]
    fast = sorted(generation.loc[generation["latency_p95_ms"] <= 1000, "model_id"])
    calls = files["truth/estate/call_reasons.parquet"]
    monthly_calls = calls["call_date"].str[:7].value_counts().sort_index().tail(12).mean()
    large = register.set_index("model_id").loc["M04"]
    cost = monthly_cost(large, monthly_calls * NOTE_TOKENS, monthly_calls * SUMMARY_TOKENS)
    return [
        ask("models-sensitive", "Which approved models may process official-sensitive data?", {"model_ids": sorted(sensitive["model_id"])},
            "architecture", ARCH_ROLES, (REGISTER,), "lookup", kind="set"),
        ask("models-public-only", "Which model is approved for public data only?", {"model_ids": public_only},
            "architecture", ARCH_ROLES, (REGISTER,), "lookup", kind="set"),
        ask("models-cheapest", "What is the cheapest text-generation model per 1,000 input tokens approved for official-sensitive data?",
            {"model_id": cheapest["model_id"]}, "architecture", ARCH_ROLES, (REGISTER,), "lookup"),
        ask("models-fast", "Which official-sensitive text-generation models meet a p95 latency of one second?", {"model_ids": fast},
            "architecture", ARCH_ROLES, (REGISTER,), "lookup", kind="set"),
        ask("models-note-cost", f"At {NOTE_TOKENS} input and {SUMMARY_TOKENS} output tokens per note, what would summarising a month of "
            "call notes on M04 cost, using the last twelve months' average volume?",
            {"monthly_gbp": cost, "calls_per_month": round(float(monthly_calls), 1)}, "architecture", ARCH_ROLES,
            (REGISTER, "handover/call_centre/export"), "analysis"),
    ]


def _catalogue(gold: dict) -> list[dict]:
    stale = sorted(f"{item['dataset']}.{item['column']}" for item in gold["catalogue_stale"])
    return [
        ask("catalogue-2021", "Which catalogued column changed meaning in 2021 without a catalogue update?",
            {"column": "lab_hba1c.value", "ref": "CHG-0120"}, "architecture", ARCH_ROLES, (CATALOGUE, "handover/lab/hba1c_results.csv")),
        ask("catalogue-stale", "Which catalogue entries no longer describe the data?", {"entries": stale},
            "architecture", ARCH_ROLES, (CATALOGUE, f"{A}/lineage.csv"), "analysis", kind="set"),
    ]


def _load(files: dict) -> list[dict]:
    receipts = files["handover/sms/receipts.jsonl"]
    per_hour = receipts["receipt_at"].str[:13].value_counts()
    reads = files[AUDIT]
    per_day = reads["read_at"].str[:10].value_counts()
    return [
        ask("load-sms", "What is the peak number of SMS receipts in one hour?", {"count": int(per_hour.max())},
            "architecture", ARCH_ROLES, ("handover/sms/receipts.jsonl",), "analysis"),
        ask("load-audit", "What is the peak number of record reads in one day in the audit log?", {"count": int(per_day.max())},
            "architecture", ARCH_ROLES, (AUDIT,), "analysis"),
    ]
