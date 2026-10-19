"""The CDO's board paper. The PDF's cost table carries the full-rollout vendor fee; the Markdown export drops it."""

from __future__ import annotations

from datetime import timedelta

from simulation.corpus.add import Extra, add_document
from simulation.stakeholders.queries import summary_for
from simulation.world.engagement import KICKOFF, PILOT_DATE_ORIGINAL, PILOT_DATE_REQUESTED
from simulation.world.staff import name

DOC_ID = "board-paper-2026-09-ai-screening"
FAMILY = "board-papers"
TITLE = "Board paper: AI in diabetic eye screening"


def _body() -> str:
    return "\n\n".join([
        f"Author: {name('cdo')}, Chief Digital Officer.",
        "## Purpose",
        "The board is asked to note progress on the vendor pilot and to support expanding the vendor model to every "
        "screening site.",
        "## Background",
        "Grading capacity has not kept pace with demand. The vendor pilot has scored primary-care and outreach captures "
        "since it began. The vendor reports accuracy above ninety percent.",
        "## Proposal",
        f"Bring the pilot date forward from {PILOT_DATE_ORIGINAL.isoformat()} to {PILOT_DATE_REQUESTED.isoformat()} and "
        "extend the contract to hospital sites.",
        "## Costs",
        "Costs are set out in the attached table.",
        "## Risks",
        "Information governance review is in progress. A clinical safety owner will be appointed.",
    ])


def _table(summary: dict) -> tuple[list[list[str]], dict]:
    vendor = next(row for row in summary["opportunities"] if row["key"] == "vendor_model_expansion")
    fee = int(vendor["running_cost_gbp"])
    claimed = int(vendor["claimed_annual_gbp"])
    table = [
        ["Item", "Annual amount (GBP)", "Basis"],
        ["Vendor fee, all sites", f"{fee}", "Contract fee per scored image, all reads"],
        ["Claimed annual benefit", f"{claimed}", "Vendor proposal"],
        ["Hospital reads in scope", f"{int(summary['volumes']['hospital_reads'])}", "Not covered by the DPIA"],
    ]
    fact = {"doc_id": DOC_ID, "field": "vendor_fee_all_sites_gbp", "value": fee, "in_markdown": False,
            "also_table_only": {"claimed_annual_benefit_gbp": claimed,
                                "hospital_reads_per_year": int(summary["volumes"]["hospital_reads"])}}
    return table, fact


def add_board_paper(world: dict) -> dict:
    table, fact = _table(summary_for(world))
    add_document(world, DOC_ID, FAMILY, TITLE, _body(), KICKOFF - timedelta(days=12),
                 extra=Extra(original="pdf", table=table, meta={"author": "cdo"}))
    world.setdefault("gold", {})["board_paper_table"] = fact
    return fact
