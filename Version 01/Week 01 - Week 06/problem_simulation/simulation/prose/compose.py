"""Pick the body for a spec: cached LLM prose if it verifies, otherwise the seeded template draft."""

from __future__ import annotations

import hashlib
import random
from collections import Counter
from typing import Callable

from simulation.prose import cache
from simulation.prose.spec import FactSpec
from simulation.prose.verify import ProseError, problems, verify

Draft = Callable[[FactSpec, random.Random], str]
STATS: Counter = Counter()
SPECS: dict[str, FactSpec] = {}
DRAFTS: dict[str, Draft] = {}


def compose(spec: FactSpec, draft: Draft) -> str:
    SPECS[spec.doc_id] = spec
    DRAFTS[spec.doc_id] = draft
    cached = cache.read(spec)
    if cached is not None:
        if not problems(spec, cached):
            STATS["cached"] += 1
            return cached.strip()
        STATS["cached_rejected"] += 1
    text = draft(spec, seeded(spec.doc_id)).strip()
    try:
        verify(spec, text)
    except ProseError as error:
        raise ProseError(f"Template draft failed its own spec. {error}") from error
    STATS["draft"] += 1
    return text


def seeded(key: str) -> random.Random:
    from simulation.world.clock import SEED

    digest = hashlib.sha256(f"{SEED}:{key}".encode()).digest()
    return random.Random(int.from_bytes(digest[:8], "big"))


def summary() -> str:
    return ", ".join(f"{name} {count}" for name, count in sorted(STATS.items())) or "no prose"
