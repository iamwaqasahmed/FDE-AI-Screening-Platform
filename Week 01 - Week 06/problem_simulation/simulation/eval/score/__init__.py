"""Score answers against gold cases: values, citations, refusals, written fact lists, injection, and budget."""

from simulation.eval.score.case import score_case
from simulation.eval.score.slices import summarise

__all__ = ["score_case", "summarise"]
