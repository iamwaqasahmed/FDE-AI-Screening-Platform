"""A chase letter, the clinic it came from, and the clause in force on that date."""

from __future__ import annotations

from simulation.eval.graph.bars import PATH_QUESTIONS
from simulation.eval.graph.cohort import binding, clinic_class
from simulation.eval.graph.question import cite, make

COPIES = (0, 1, 2)
CLINICS = ("ncec-after", "ncec-before", "harbour-after", "harbour-before", "other", "blank")


def cases(world: dict, linked: dict) -> list[dict]:
    frame = linked["chase"].dropna(subset=["request_id"]).copy()
    frame["clinic"] = [clinic_class(row.hospital, str(row.referred), row.mrn) for row in frame.itertuples(index=False)]
    picked = _pick(frame)
    return [_case(world, row, index) for index, row in enumerate(picked)]


def _pick(frame) -> list:
    chosen, seen = [], set()
    for clinic in CLINICS:
        for copies in COPIES:
            pool = frame[(frame["clinic"] == clinic) & (frame["copies"] == copies)].sort_values("local_pid")
            if pool.empty:
                continue
            row = pool.iloc[0]
            chosen.append(row)
            seen.add(row.request_id)
    rest = frame[~frame["request_id"].isin(seen)].sort_values(["clinic", "local_pid"])
    for row in rest.itertuples(index=False):
        if len(chosen) >= PATH_QUESTIONS:
            break
        chosen.append(row)
    return chosen[:PATH_QUESTIONS]


def _case(world: dict, row, index: int) -> dict:
    clause = binding(str(row.hospital), str(row.referred), str(row.mrn))
    document = world["catalog"][clause.document_id]
    limit = "" if clause.days is None else int(clause.days)
    question = (
        f"Local id {row.local_pid} was sent a chase letter in the bureau window. "
        f"Which document binds specialist review at the referring clinic on {str(row.referred)[:10]}, "
        "and how many times was that request dispatched? Use the document id as clause_id. "
        "Leave limit blank when the text sets no clock. copies is 0 when nothing was dispatched."
    )
    visit = [str(row.request_id), clause.document_id]
    if row.mrn:
        visit.append(str(row.mrn))
    expected = {"clause_id": clause.document_id, "limit": limit, "copies": int(row.copies)}
    return make(f"path-{index:02d}", question, expected, "value", "path", ("clause_id", "limit", "copies"),
                cite(document), "multi_hop", visit)

