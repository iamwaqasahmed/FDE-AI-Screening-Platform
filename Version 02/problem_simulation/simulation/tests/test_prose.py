"""Prose pipeline: drafts verify, extra facts are caught, every format renders."""

from __future__ import annotations

from simulation.prose import FactSpec, compose
from simulation.prose.formats.render import FORMATS, render
from simulation.prose.spec import facts
from simulation.prose.verify import problems

SPEC = FactSpec("t-1", "test", "Test note", facts(count="1,250", date="2025-03-03", site="Harbour Eye Clinic"))


def _draft(spec, rng):
    return f"The bureau logged {spec.value('count')} letters on {spec.value('date')} at {spec.value('site')}."


def test_draft_verifies():
    assert "1,250" in compose(SPEC, _draft)


def test_extra_facts_are_caught():
    text = (
        "The bureau logged 1,250 letters on 2025-03-03 at Harbour Eye Clinic and 17 more, "
        "per J. Whitfield on 2025-04-01 ref INC-0042."
    )
    found = " ".join(problems(SPEC, text))
    for token in ("17", "J. Whitfield", "2025-04-01", "INC-0042"):
        assert token in found


def test_missing_fact_is_caught():
    assert any("missing" in issue for issue in problems(SPEC, "Nothing to see."))


def test_formats_render():
    for kind in FORMATS:
        data = render(kind, "t-1", "Test", compose(SPEC, _draft), [["a", "b"], ["1", "2"]])
        assert len(data) > 200


if __name__ == "__main__":
    for name, function in list(globals().items()):
        if name.startswith("test_"):
            function()
            print("ok", name)
