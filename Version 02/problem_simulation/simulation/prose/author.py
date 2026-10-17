"""The only module that calls a language model. Run it as a separate command, then commit the cache.

Any OpenAI-compatible chat endpoint works. See settings.py for where the URL, key, and model come from.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.request

from simulation.prose import cache
from simulation.prose.compose import seeded
from simulation.prose.settings import settings
from simulation.prose.spec import FactSpec
from simulation.prose.verify import problems

SYSTEM = (
    "You write realistic internal documents for a fictional regional health authority. "
    "You are given a list of facts and a rough draft. Rewrite the draft as natural, varied, professional prose "
    "in the requested style. Rules: use every fact value exactly as written, character for character. "
    "Do not add any number, date, identifier, or person, site, or company name that is not in the facts. "
    "Write dates exactly as given. Do not use numbered lists or section numbers. Return Markdown body text only, "
    "with no title line."
)


def prompt(spec: FactSpec, draft: str) -> str:
    lines = [f"Document: {spec.title}", f"Style: {spec.style}", f"Length: about {spec.length_words} words"]
    if spec.sections:
        lines.append("Sections, as Markdown level-2 headings: " + "; ".join(spec.sections))
    lines.append("Facts:")
    lines.extend(f"- {fact.key}: {fact.value}" for fact in spec.facts)
    lines.append("Draft:")
    lines.append(draft)
    return "\n".join(lines)


def call_model(user: str) -> str:
    config = settings()
    if not config.key:
        raise SystemExit("No LLM key. Set HARTLAND_LLM_KEY or OPENAI_API_KEY, or put it in a .env file.")
    body = {"model": config.model, "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]}
    request = urllib.request.Request(
        config.url + "/chat/completions", data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {config.key}", "Content-Type": "application/json"},
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                payload = json.loads(response.read().decode())
            return payload["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as error:
            if error.code not in (429, 500, 502, 503) or attempt == 3:
                raise SystemExit(f"LLM call failed: HTTP {error.code} {error.read().decode()[:300]}") from error
            time.sleep(2 ** attempt * 5)
    raise SystemExit("LLM call failed after retries.")


def author(spec: FactSpec, draft_fn, attempts: int = 3) -> tuple[bool, list[str]]:
    draft = draft_fn(spec, seeded(spec.doc_id))
    issues: list[str] = []
    for _ in range(attempts):
        text = call_model(prompt(spec, draft) + ("\nFix these problems: " + "; ".join(issues) if issues else ""))
        issues = problems(spec, text)
        if not issues:
            cache.write(spec, text)
            return True, []
    return False, issues
