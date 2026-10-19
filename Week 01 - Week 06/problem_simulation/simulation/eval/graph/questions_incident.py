"""The bureau incident, the 2025 file, the catalogue, and the freeze."""

from __future__ import annotations

from simulation.eval.graph.question import cite, make


def cases(world: dict, items: dict) -> list[dict]:
    precedent, window, agreement = items["precedent"], items["resend_window"], items["bureau_agreement"]
    catalogue = items["catalogue_lineage"]
    specs = [
        ("incident-precedent",
         "The week 4 bureau notice describes a queue failure and automatic retries. Which earlier incident had that cause, and on what dates did it start and end?",
         {"ref": precedent["ref"], "start": precedent["start"], "end": precedent["end"]},
         "notice-inc-0233", ["INC-0233", "notice-inc-0233"]),
        ("incident-copies",
         "How many rows in the March 2025 letter incident file are a second copy of a row already in that file?",
         {"count": precedent["second_copies"]}, "incident-letter-2025", ["incident-letter-2025", "incident_2025-03.csv"]),
        ("incident-migration",
         "On what date did the letter bureau platform migration finish?",
         {"date": _migration_end()}, "notice-chg-0158", ["CHG-0158", "notice-chg-0158"]),
        ("incident-lineage",
         "Which dataset feeds the letter dispatch dataset, and when was that lineage last verified?",
         {"upstream": catalogue["upstream"], "verified": catalogue["verified"]}, "", ["letters_dispatch", "grader_workbook"]),
        ("incident-grain",
         "The catalogue says the letter dispatch dataset has one row per letter. Does that hold for the week 4 dispatch file?",
         {"holds": False}, "", ["letters_dispatch"]),
        ("incident-freeze",
         "Which freeze blocks letter template changes over the new year, and what is the last letters release window before it starts?",
         {"freeze": window["freeze"], "last_window": window["last_before"]}, "", ["FRZ-0302"]),
        ("incident-zone",
         "Which trust zone is the letter bureau in, and which data sharing agreement covers it?",
         {"zone": agreement["zone"], "agreement": agreement["document_id"]}, "dsa-postright-2020",
         ["letters", "dsa-postright-2020"]),
        ("incident-deadline",
         "The bureau keeps letter data for ninety days after dispatch. For a letter dispatched on the last day of the week 4 window, what is the last date the authority can still reconcile it?",
         {"deadline": agreement["evidence_deadline"]}, "dsa-postright-2020", ["dsa-postright-2020"]),
    ]
    return [_row(world, *spec) for spec in specs]


def _row(world: dict, case_id: str, question: str, expected: dict, citation_id: str, visit: list[str]) -> dict:
    citation = cite(world["catalog"][citation_id]) if citation_id else {}
    return make(case_id, question, expected, "value", "incident", tuple(expected), citation, "multi_hop", visit)


def _migration_end() -> str:
    from simulation.world.clock import BUREAU_MIGRATION_END, iso
    return iso(BUREAU_MIGRATION_END)
