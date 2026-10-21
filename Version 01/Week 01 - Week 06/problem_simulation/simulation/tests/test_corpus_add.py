"""Any stage can register a document with an original file and gold spans."""

from __future__ import annotations

from datetime import date

from simulation.corpus.add import Extra, add_composed, add_document, pii_spans
from simulation.prose import FactSpec
from simulation.prose.spec import facts


def test_add_document_with_original_and_pii():
    world = {"files": {}, "gold": {}}
    body = "Call Jo Bloggs on 07700 900123 about the letter."
    extra = Extra(original="pdf", pii=pii_spans(body, {"name": "Jo Bloggs", "phone": "07700 900123"}), injection="x")
    path = add_document(world, "complaint-0001", "complaints", "Complaint", body, date(2024, 1, 2), extra=extra)
    assert path == "complaints/complaint-0001.md"
    assert "corpus/complaints/originals/complaint-0001.pdf" in world["files"]
    span = world["gold"]["pii"][0]
    assert world["rendered"]["complaint-0001"][span["start"]:span["end"]] == span["value"]
    assert world["corpus_meta"]["complaint-0001"]["original"].endswith(".pdf")


def test_add_composed():
    world = {"files": {}, "gold": {}}
    spec = FactSpec("memo-1", "memos", "Memo", facts(day="2024-02-01"))
    add_composed(world, spec, lambda s, r: f"Effective {s.value('day')}.", date(2024, 2, 1))
    assert "Effective 2024-02-01." in world["rendered"]["memo-1"]


if __name__ == "__main__":
    test_add_document_with_original_and_pii()
    test_add_composed()
    print("ok")
