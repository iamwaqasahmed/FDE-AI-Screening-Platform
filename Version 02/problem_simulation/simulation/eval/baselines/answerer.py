"""Turn retrieved documents into an answer the way a single-pass assistant would."""

from __future__ import annotations

import re

from simulation.eval.baselines.corpus_index import Doc, tokens

NUMBER = re.compile(r"(?<![\w-])\d+(?:\.\d+)?(?![\w-])")
INJECTION_MARK = "ignore your previous instructions"


def answer(case: dict, docs: list[Doc]) -> dict:
    top = docs[0] if docs else None
    text = " ".join(doc.body for doc in docs)
    usage = {"tokens": len(text) // 4 + 200, "seconds": 2, "cost_usd": round((len(text) // 4) * 0.15e-6, 6)}
    citation = _citation(top)
    kind = case["kind"]
    if kind == "refusal":
        return {"case_id": case["case_id"], "answer": text[:300], "refused": False, "citation": citation, "usage": usage}
    if kind in ("written", "injection"):
        followed = INJECTION_MARK in text.lower()
        return {"case_id": case["case_id"], "answer": text[:1500], "citation": citation, "usage": usage,
                "followed_injection": followed}
    if kind == "citation":
        return {"case_id": case["case_id"], "answer": {"clause_id": top.doc_id if top else ""}, "citation": citation, "usage": usage}
    body = top.body if top else ""
    wants_text = case["question"].lower().startswith(("what cause", "which", "who", "what reason"))
    value = _best_phrase(case["question"], body) if wants_text else _best_number(case["question"], body)
    return {"case_id": case["case_id"], "answer": _shape(case["expected"], value), "citation": citation, "usage": usage}


def _citation(doc: Doc | None) -> dict:
    if doc is None:
        return {}
    return {key: doc.header.get(key, "") for key in ("document_id", "status", "effective", "site")}


def _sentences(body: str) -> list[str]:
    return [sentence for sentence in re.split(r"(?<=[.!?])\s+|\n", body) if sentence.strip()]


def _best_number(question: str, body: str) -> str:
    terms = set(tokens(question))
    wants_rate = "rate" in terms or "per" in terms
    best, best_score = "", -1
    for sentence in _sentences(body):
        numbers = [number for number in NUMBER.findall(sentence) if number not in terms]
        if wants_rate:
            numbers = [number for number in numbers if "." in number]
        if not numbers:
            continue
        score = sum(1 for term in tokens(sentence) if term in terms)
        if score > best_score:
            best, best_score = numbers[0], score
    return best


def _best_phrase(question: str, body: str) -> str:
    terms = set(tokens(question))
    ranked = sorted(_sentences(body), key=lambda sentence: -sum(1 for term in tokens(sentence) if term in terms))
    for sentence in ranked:
        if ":" in sentence:
            return sentence.split(":", 1)[1].strip().rstrip(".")
    return ranked[0].strip() if ranked else ""


def _shape(expected, value: str):
    if not isinstance(expected, dict):
        return value
    keys = [key for key in expected if key not in ("unit", "include_deceased", "days")]
    if len(keys) == 1 and not isinstance(expected[keys[0]], (dict, list, bool)):
        return {keys[0]: value}
    if "same_person" in expected:
        return {"same_person": True}
    return {key: value for key in keys}
