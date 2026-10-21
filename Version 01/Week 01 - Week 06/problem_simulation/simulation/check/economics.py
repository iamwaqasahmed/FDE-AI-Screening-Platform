"""Economics invariants: the naive reminder estimate overstates, the flashy opportunity nets least, the graph is sound."""

from __future__ import annotations

from simulation.economics.budgets import NEW_CENTRES, OLD_CENTRES, financial_year
from simulation.economics.dependencies import edges, unlocks
from simulation.economics.opportunities import BLOCKERS, BY_KEY
from simulation.economics.reminder import reminder_gold
from simulation.world.clock import FINANCE_RECODE

FLASHY = "vendor_model_expansion"


def _opportunities(world: dict) -> list[dict]:
    return world["files"]["truth/economics/opportunities.json"]["opportunities"]


def check_reminder_trap(world: dict, errors: list[str]) -> None:
    fresh = reminder_gold(world["invitations"])
    stored = world["gold"].get("reminder_uplift", {})
    if fresh != stored:
        errors.append("Reminder gold does not match a recomputation from the invitations")
    if len(fresh["overstated_districts"]) < 2:
        errors.append(f"The naive before-and-after must overstate in at least two districts: {fresh['districts']}")


def check_flashy_nets_least(world: dict, errors: list[str]) -> None:
    rows = _opportunities(world)
    claimed = max(rows, key=lambda row: row["claimed_annual_gbp"])["key"]
    lowest = min(rows, key=lambda row: row["net_annual_gbp"])["key"]
    if claimed != FLASHY or lowest != FLASHY:
        errors.append(f"{FLASHY} should claim the most and net the least; largest claim {claimed}, lowest net {lowest}")


def check_value_ranges(world: dict, errors: list[str]) -> None:
    for row in _opportunities(world):
        low, high = row["value_range_gbp"]
        if not low <= row["net_annual_gbp"] <= high:
            errors.append(f"{row['key']}: net value outside its range")
        if row["blockers"] and not row["must_cite"]:
            errors.append(f"{row['key']}: a blocked opportunity needs must-cite facts")


def check_dependency_graph(world: dict, errors: list[str]) -> None:
    for edge in edges():
        known_source = edge["source"] in BY_KEY or edge["source"] in BLOCKERS
        if not known_source or edge["target"] not in BY_KEY:
            errors.append(f"Unknown node in dependency edge {edge}")
    for key in BY_KEY:
        if key in unlocks(key):
            errors.append(f"Dependency cycle through {key}")
    if len(unlocks("identity_resolution")) < 3 or len(unlocks("letter_bureau_fix")) < 2:
        errors.append("Identity and letters should unlock most of the other opportunities")
    if len(world["files"]["truth/economics/dependencies.csv"]) != len(edges()):
        errors.append("dependencies.csv does not match the graph")


def check_budget_recode(world: dict, errors: list[str]) -> None:
    budgets = world["files"]["engagement/economics/budgets.csv"]
    recode = financial_year(FINANCE_RECODE.isoformat())
    old = {code for code, _ in OLD_CENTRES.values()}
    new = {code for code, _ in NEW_CENTRES.values()}
    before = set(budgets.loc[budgets["financial_year"] < recode, "cost_centre"])
    after = set(budgets.loc[budgets["financial_year"] >= recode, "cost_centre"])
    if before - old or after - new:
        errors.append("Cost centres do not switch cleanly at the recode")


def check_public_files(world: dict, errors: list[str]) -> None:
    files = world["files"]
    for path in ("unit_costs.csv", "budgets.csv", "attendance_by_month.csv"):
        if f"engagement/economics/{path}" not in files:
            errors.append(f"Missing engagement/economics/{path}")
    monthly = files.get("engagement/economics/attendance_by_month.csv")
    if monthly is not None and int(monthly["invited"].sum()) != len(world["invitations"]):
        errors.append("Monthly attendance does not add up to the invitations")


CHECKS = [
    ("economics reminder naive overstates", check_reminder_trap),
    ("economics flashy opportunity nets least", check_flashy_nets_least),
    ("economics value ranges", check_value_ranges),
    ("economics dependency graph", check_dependency_graph),
    ("economics budget recode", check_budget_recode),
    ("economics public files", check_public_files),
]
