"""The CDO office roadmap, and the board note whose priorities disagree with it."""

from __future__ import annotations

from datetime import date

import pandas as pd

from simulation.corpus.add import Extra, add_document
from simulation.delivery.plan import PILOT_CONTRACT_VALUE, frozen
from simulation.world.engagement import PILOT_DATE_ORIGINAL
from simulation.world.staff import name

ROADMAP_DOC = "delivery-roadmap-2026"
BOARD_DOC = "delivery-board-priorities-2026-09"
FREEZE_SYSTEMS = {"RM-01": "registry", "RM-05": "letters"}


def _items() -> tuple[tuple, ...]:
    return (
        ("RM-01", "Registry schema v3 interface", name("integration_lead"), "2026-12-01", "P1", "", ""),
        ("RM-02", "Vendor pilot contract (direct award as a variation)", name("procurement_lead"), "2026-12-15", "P1", "G2",
         str(PILOT_CONTRACT_VALUE)),
        ("RM-03", "AI triage pilot live at primary-care sites", name("cdo"), PILOT_DATE_ORIGINAL.isoformat(), "P1",
         "RM-01 RM-02 RM-09", ""),
        ("RM-04", "Booking platform stabilisation", name("programme_manager"), "2027-03-31", "P3", "", ""),
        ("RM-05", "Letter template refresh", name("programme_manager"), "2026-12-16", "P2", "", ""),
        ("RM-06", "Warehouse eligibility fix", name("enterprise_architect"), "2027-02-26", "P2", "", ""),
        ("RM-07", "Grader capacity plan", name("lead_grader"), "2027-01-29", "P2", "", ""),
        ("RM-08", "Patient portal accessibility audit", name("product_owner"), "2027-03-15", "P3", "RM-05", ""),
        ("RM-09", "Clinical safety case", "", "2027-01-15", "P1", "", ""),
        ("RM-10", "Benefits baseline", name("finance_head"), "2027-04-30", "P3", "", ""),
    )


BOARD_PRIORITIES = {"RM-03": "P2", "RM-04": "P1", "RM-05": "P1"}


def roadmap_frame() -> pd.DataFrame:
    rows = []
    for item_id, title, owner, target, priority, depends, value in _items():
        day = date.fromisoformat(target)
        rows.append({"item_id": item_id, "item": title, "owner": owner, "quarter": f"{day.year} Q{(day.month - 1) // 3 + 1}",
                     "target_date": target, "priority": priority, "depends_on": depends, "estimated_value_gbp": value})
    return pd.DataFrame(rows)


def roadmap_gold(frame: pd.DataFrame) -> dict:
    conflicts = [{"item_id": item, "roadmap": frame.set_index("item_id").loc[item, "priority"], "board": board}
                 for item, board in sorted(BOARD_PRIORITIES.items())]
    targets = frame.set_index("item_id")["target_date"]
    impossible = [{"item_id": item, "target_date": targets[item], "freeze": frozen(system, date.fromisoformat(targets[item]))}
                  for item, system in sorted(FREEZE_SYSTEMS.items())]
    return {"conflicts": conflicts, "frozen_targets": [row for row in impossible if row["freeze"]],
            "unowned": sorted(frame.loc[frame["owner"] == "", "item_id"]), "board_doc": BOARD_DOC, "roadmap_doc": ROADMAP_DOC}


def add_roadmap_docs(world: dict, frame: pd.DataFrame) -> None:
    table = [list(frame.columns), *frame.astype(str).values.tolist()]
    lines = [f"{row.item_id}: {row.item}. Target {row.target_date}, priority {row.priority}."
             + (f" Depends on {row.depends_on}." if row.depends_on else "") for row in frame.itertuples(index=False)]
    body = ("Roadmap from the office of the Chief Digital Officer. The workbook is the master copy.\n\n" + "\n\n".join(lines))
    add_document(world, ROADMAP_DOC, "delivery", "Digital roadmap 2026 to 2027", body, date(2026, 9, 1),
                 extra=Extra(original="xlsx", table=table, meta={"owner": name("cdo")}))
    board = "\n\n".join(
        f"{item} is agreed at priority {priority}." for item, priority in sorted(BOARD_PRIORITIES.items())
    )
    body = ("The programme board reviewed delivery priorities after the summer complaints. "
            "Booking stability and the referral letter come first. The AI pilot follows once those are steady.\n\n" + board)
    add_document(world, BOARD_DOC, "delivery", "Programme board priorities, September 2026", body, date(2026, 9, 24),
                 extra=Extra(original="pdf", cites=(ROADMAP_DOC,)))
