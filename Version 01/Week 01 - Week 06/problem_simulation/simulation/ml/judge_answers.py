"""Written answers of controlled quality about each fact, labelled by the rubric in eval/judge_rubric.md."""

from __future__ import annotations

import numpy as np

from simulation.ml.judge_facts import Fact

VARIANTS = (
    ("correct_full", 5),
    ("correct_full_reordered", 5),
    ("correct_uncited", 4),
    ("partially_correct", 3),
    ("missing_caveat", 3),
    ("over_claiming", 2),
    ("over_claiming_uncited", 2),
    ("hallucinated_number", 1),
)
REASONS = {
    "correct_full": ["value matches gold", "required caveat present", "source cited"],
    "correct_full_reordered": ["value matches gold", "required caveat present", "source cited"],
    "correct_uncited": ["value matches gold", "required caveat present", "no source cited"],
    "partially_correct": ["main value matches gold", "supporting value is wrong"],
    "missing_caveat": ["value matches gold", "required caveat missing"],
    "over_claiming": ["value matches gold", "conclusion not supported by the evidence"],
    "over_claiming_uncited": ["value matches gold", "conclusion not supported by the evidence", "required caveat missing", "no source cited"],
    "hallucinated_number": ["value contradicts gold"],
}
OPENERS = ("The answer is", "From the data, it is", "My finding is", "Working it through, the figure is")
TOLERANCE = {"rate": 0.01, "auc": 0.01, "count": 0, "text": 0}


def show(kind: str, value) -> str:
    if kind in ("rate", "auc"):
        return f"{float(value):.2f}"
    if kind == "count":
        return str(int(value))
    return str(value)


def wrong(kind: str, value, text: str, rng: np.random.Generator) -> str:
    if kind == "text":
        return text
    if kind == "count":
        return str(int(round(int(value) * rng.uniform(1.25, 1.6))) + 1)
    step = rng.uniform(0.08, 0.2) * (1 if float(value) < 0.5 else -1)
    return f"{min(max(float(value) + step, 0.01), 0.99):.2f}"


def secondary_kind(fact: Fact) -> str:
    return fact.kind if isinstance(fact.secondary, (int, float)) and fact.kind != "text" else "text"


def answer_row(fact: Fact, variant: str, score: int, rng: np.random.Generator) -> dict:
    value = show(fact.kind, fact.value)
    second = show(secondary_kind(fact), fact.secondary)
    if variant == "hallucinated_number":
        value = wrong(fact.kind, fact.value, fact.wrong_text, rng)
    if variant == "partially_correct":
        second = wrong(secondary_kind(fact), fact.secondary, fact.secondary_wrong_text or "unknown", rng)
    return {
        "fact_id": fact.fact_id,
        "category": fact.category,
        "question": fact.question,
        "reference_answer": _text(fact, show(fact.kind, fact.value), show(secondary_kind(fact), fact.secondary), "correct_full"),
        "answer": _text(fact, value, second, variant, OPENERS[int(rng.integers(len(OPENERS)))]),
        "variant": variant,
        "gold": {"value": show(fact.kind, fact.value), "tolerance": TOLERANCE[fact.kind], "caveat": fact.caveat, "source": fact.source},
        "label": {"score": score, "pass": score >= 4, "reasons": REASONS[variant]},
    }


def _text(fact: Fact, value: str, second: str, variant: str, opener: str = OPENERS[0]) -> str:
    main = f"{opener} {value}, with {fact.secondary_label} {second}."
    cite = f" Source: {fact.source}."
    caveat = f" Note that {fact.caveat}."
    if variant == "correct_full_reordered":
        return f"Checked against {fact.source}: {fact.secondary_label} is {second} and the answer is {value}. Caveat: {fact.caveat}."
    if variant == "correct_uncited":
        return main + caveat
    if variant == "missing_caveat":
        return main + cite
    if variant == "over_claiming":
        return main + caveat + f" Overall, {value}, {fact.overclaim}." + cite
    if variant == "over_claiming_uncited":
        return f"It is {value}, {fact.overclaim}."
    return main + caveat + cite


def calibration_rows(facts: list[Fact], rng: np.random.Generator) -> list[dict]:
    rows = []
    for fact in facts:
        for variant, score in VARIANTS:
            row = answer_row(fact, variant, score, rng)
            rows.append(dict(answer_id=f"judge-{len(rows) + 1:04d}", **row))
    order = rng.permutation(len(rows))
    return [rows[index] for index in order]
