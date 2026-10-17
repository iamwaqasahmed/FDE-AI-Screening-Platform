"""The rubric the judge calibration labels follow, written to eval/judge_rubric.md."""

from __future__ import annotations

from simulation.ml.judge_answers import TOLERANCE, VARIANTS

RUBRIC = """# Judge rubric for written answers

Each row in `judge_calibration.jsonl` is one written answer to an ML, discovery, or governance question.
The `gold` block holds the value, the numeric tolerance, the required caveat, and the source.
A judge is trusted only when its scores match the human-style `label` block on this set.

## Scores

| Score | Meaning |
|---|---|
| 5 | The main value is within tolerance, every supporting value is right, the required caveat is stated, and a source is cited. |
| 4 | As for 5, but no source is cited. |
| 3 | The main value is right, but the required caveat is missing or a supporting value is wrong. |
| 2 | The value is right, but the answer draws a conclusion the evidence does not support (over-claiming). Over-claiming caps the score at 2 whatever else is right. |
| 1 | The main value contradicts gold (a hallucinated number or the wrong categorical answer). A wrong main value caps the score at 1. |

## Rules

- Pass means score 4 or 5. Everything else fails.
- Apply the caps in order: a wrong main value first, then over-claiming, then a missing caveat or wrong supporting value, then the citation.
- Tolerance: {tolerance}. Rates and AUCs are compared after rounding to two decimals; counts and text must match exactly.
- A caveat counts as present when its substance is stated, not only its exact words.
- Do not reward length, confidence, or hedging. Do not penalise a correct answer for being short.
- Reasons list every rule the answer met or broke, using the phrases in the label block.

## Variant key

{variants}
"""


def rubric_text() -> str:
    tolerance = ", ".join(f"{kind} {value}" for kind, value in TOLERANCE.items())
    variants = "\n".join(f"- `{name}`: score {score}" for name, score in VARIANTS)
    return RUBRIC.format(tolerance=tolerance, variants=variants)
