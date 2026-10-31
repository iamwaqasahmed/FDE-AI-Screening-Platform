"""INV-07. signal() is shown a stale document and a merely hot host."""

from __future__ import annotations

from pathlib import Path

from access.checks.runtime import load_callable
from access.sealed_holdouts import SIGNALS
from access.sealed_release import SIGNAL_PAGE


def grade_signal(path: Path) -> list[str]:
    fn, problems = load_callable(path, "signal")
    if fn is None:
        return problems
    for obs in SIGNALS:
        try:
            got = fn(obs)
        except Exception:
            problems.append(f"the signal function raised on {obs['id']}")
            continue
        if not isinstance(got, dict):
            problems.append(f"the signal function returned no record for {obs['id']}")
            continue
        problems.extend(_judge(obs, got))
    return problems


def _judge(obs: dict, got: dict) -> list[str]:
    problems: list[str] = []
    stale = obs["served_version"] != obs["in_force_version"]
    if stale and got.get("page_on") != SIGNAL_PAGE:
        problems.append("the page follows the host while the served document is stale")
    if not stale and got.get("page_on") not in (None, "none"):
        problems.append("a current document was paged as if it were stale")
    if got.get("shadow_can_write") is not False:
        problems.append("shadow traffic can write")
    if got.get("prompt_in_span") is not False:
        problems.append("the span carries the sentence")
    if got.get("flush_all_documents") is not False:
        problems.append("flushing every document is the signal")
    return problems
