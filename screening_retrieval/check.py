"""Check the five corpus questions and the citation fields."""

from __future__ import annotations

from screening_retrieval.retrieve import retrieve

CASES = [
    {
        "question": "Who counts as screened?",
        "document_ids": {"sop-issued"},
        "status": "in_force",
    },
    {
        "question": "What does a blank result mean?",
        "document_ids": {"grade-codes"},
        "status": "in_force",
    },
    {
        "question": "Is the 14-day target current policy?",
        "document_ids": {"sop-urgent-draft"},
        "status": "draft",
    },
    {
        "question": "What may a letter say?",
        "document_ids": {"letter-result", "dpo-rule"},
        "status": "in_force",
    },
    {
        "question": "What must a model not do?",
        "document_ids": {"dpo-rule"},
        "status": "in_force",
    },
]


def main() -> None:
    errors: list[str] = []
    for case in CASES:
        result = retrieve(case["question"])
        _check_fields(case["question"], result, errors)
        if result.get("document_id") not in case["document_ids"]:
            errors.append(f"{case['question']} cited {result.get('document_id')}")
        if result.get("status") != case["status"]:
            errors.append(f"{case['question']} status {result.get('status')}")
    if errors:
        raise SystemExit("Retrieval check failed:\n- " + "\n- ".join(errors))
    print("Retrieval check passed.")


def _check_fields(question: str, result: dict, errors: list[str]) -> None:
    for field in ("document_id", "status", "filename", "passage"):
        if field not in result:
            errors.append(f"{question} missing {field}")
    if not str(result.get("passage", "")).strip():
        errors.append(f"{question} has an empty passage")


if __name__ == "__main__":
    main()
