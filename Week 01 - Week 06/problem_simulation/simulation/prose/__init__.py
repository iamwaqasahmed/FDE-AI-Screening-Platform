"""Prose pipeline: the generator decides every fact, a writer only adds sentences around them.

Use `compose(spec, draft)` from a document family. It returns verified body text: cached LLM prose
when the cache holds this exact spec, otherwise the family's seeded template draft.
"""

from simulation.prose.compose import compose
from simulation.prose.spec import Fact, FactSpec

__all__ = ["Fact", "FactSpec", "compose"]
