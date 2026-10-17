"""Discovery questions over opportunity values, dependencies, unit costs, budgets, and the reminder baseline trap."""

from __future__ import annotations

from simulation.economics.costs import cost
from simulation.economics.dependencies import prerequisites
from simulation.economics.opportunities import BY_KEY
from simulation.eval.case_format import make_case
from simulation.stakeholders.queries import summary_for
from simulation.world.clock import FINANCE_RECODE, REMINDER_CHANGE

DISCOVERY = ("consultant", "pm", "data_science")


def _case(name: str, question: str, expected: dict, **tags) -> dict:
    tags.setdefault("outcome", "discovery")
    tags.setdefault("roles", DISCOVERY)
    tags.setdefault("surfaces", ("economics",))
    return make_case(f"economics-{name}", question, expected, **tags)


def reminder_cases(world: dict) -> list[dict]:
    gold = world["gold"]["reminder_uplift"]
    cases = []
    for district, row in gold["districts"].items():
        cases.append(_case(f"reminder-{district.lower().replace(' ', '-')}",
                           f"By how much did the reminder change of {REMINDER_CHANGE.isoformat()} raise attendance in "
                           f"{district}? Give the true uplift and the naive before-and-after figure.",
                           {"true_uplift": row["true_uplift"], "naive_before_after": row["naive_before_after"],
                            "naive_overstates": row["overstated_by"] > 0},
                           roles=("data_science",), budget="analysis", surfaces=("economics", "sms", "booking")))
    cases.append(_case("reminder-written", "Explain to the programme board why the attendance rise after the reminder "
                       "change is not the reminder's effect.",
                       {"must_mention": ["no control group", "seasonality", "the uplift differs by district",
                                         f"the naive estimate overstates in {', '.join(gold['overstated_districts'])}"],
                        "must_not_claim": ["The reminder caused the whole rise in attendance"]},
                       outcome="consulting", budget="written", kind="written"))
    return cases


def value_cases(summary: dict) -> list[dict]:
    cases = []
    for row in summary["opportunities"]:
        cases.append(_case(f"value-{row['key'].replace('_', '-')}",
                           f"What is a defensible annual net value range for '{row['title']}', and what must a ranking cite?",
                           {"value_range_gbp": row["value_range_gbp"], "net_annual_gbp": row["net_annual_gbp"],
                            "blockers": row["blockers"], "must_cite": row["must_cite"]},
                           budget="analysis", surfaces=("economics", "corpus", "stakeholders")))
    return cases


def graph_cases() -> list[dict]:
    cases = [_case(f"depends-{key.replace('_', '-')}", f"What has to be in place before '{BY_KEY[key].title}'?",
                   {"prerequisites": prerequisites(key)}, budget="multi_hop")
             for key in ("dna_prediction", "reminder_targeting", "call_deflection")]
    cases += [_case(f"blocked-{key.replace('_', '-')}", f"What blocks '{BY_KEY[key].title}' today?",
                    {"blockers": list(BY_KEY[key].blockers)}, outcome="delivery", roles=("pm", "consultant"),
                    budget="multi_hop") for key in ("vendor_model_expansion", "fast_track_scheduling")]
    return cases


def ranking_case(summary: dict) -> dict:
    return _case("ranking", "Rank the eight opportunities for the steering group and justify the order.",
                 {"must_mention": ["identity resolution and the letter fix unlock most of the others",
                                   "vendor model expansion is blocked by the DPO restriction and the missing safety owner",
                                   f"{summary['net_rank'][0].replace('_', ' ')} has the highest net value"],
                  "must_not_claim": ["Vendor model expansion should come first"],
                  "must_not_rank_first": ["vendor_model_expansion"]},
                 outcome="consulting", budget="written", kind="written")


def lookup_cases(world: dict, summary: dict) -> list[dict]:
    budgets = world["files"]["engagement/economics/budgets.csv"]
    agency = budgets[(budgets["financial_year"] == "2025-26") & (budgets["cost_centre"] == "SCR-215")]
    monthly = world["files"]["engagement/economics/attendance_by_month.csv"]
    by_month = monthly.assign(m=monthly["month"].str.slice(5, 7)).groupby("m")["attendance_rate"].mean()
    harm = summary["volumes"]["harm"]
    return [
        _case("unit-dna", "What does one missed screening slot cost?", {"gbp": cost("dna_slot")}, roles=("pm",)),
        _case("unit-call", "What does one contact-centre call cost?", {"gbp": cost("call")}, roles=("pm",)),
        _case("unit-vendor", "What does the vendor charge per scored image?", {"gbp": cost("vendor_read_fee")},
              roles=("pm", "consultant")),
        _case("agency-actual", "What did agency grading actually cost in financial year 2025-26?",
              {"gbp": float(agency["actual_gbp"].sum())}, roles=("pm", "data_engineering"), budget="multi_hop"),
        _case("recode", "Letter spend seems to vanish after 2022-23. Why?",
              {"recoded_on": FINANCE_RECODE.isoformat(), "old_code": "4430", "new_code": "SCR-230",
               "merged_with": "SMS gateway"}, roles=("pm", "data_engineering"), budget="multi_hop"),
        _case("harm-cause", "Over the last three years, which delay cause carries the most harm-weighted cost?",
              {"cause": max(sorted(harm), key=lambda key: harm[key]["harm_gbp"])}, roles=("data_science",),
              budget="analysis", surfaces=("economics", "grader", "letters", "ophthalmology")),
        _case("never-graded", "How many encounters a year never reach a grader, and which opportunity addresses them?",
              {"per_year": harm["never_graded"]["encounters"], "opportunity": "identity_resolution"},
              roles=DISCOVERY + ("data_engineering",), budget="analysis", surfaces=("economics", "grader", "shared")),
        _case("costliest", "Which problem theme costs the service most each year?",
              {"theme": summary["costliest_problem"], "gbp": summary["problem_costs"][summary["costliest_problem"]]},
              budget="analysis"),
        _case("season-low", "In which calendar month is attendance lowest on average?",
              {"month": int(by_month.idxmin())}, roles=("data_science",), budget="multi_hop"),
        _case("letter-case", "Write the economic case for fixing the letter bureau.",
              {"must_mention": [f"net value about {int(next(r for r in summary['opportunities'] if r['key'] == 'letter_bureau_fix')['net_annual_gbp'])} pounds a year",
                                "it unlocks call deflection and reminder targeting", "low regulatory risk"],
               "must_not_claim": ["Call deflection savings add to the letter fix savings"]},
              outcome="discovery", budget="written", kind="written"),
    ]


def cases(world: dict) -> list[dict]:
    summary = summary_for(world)
    return (reminder_cases(world) + value_cases(summary) + graph_cases() + [ranking_case(summary)]
            + lookup_cases(world, summary))
