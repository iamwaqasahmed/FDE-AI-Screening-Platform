"""Drive the agent loop with a scripted model. No API key."""

from __future__ import annotations

from screening_agent.loop import SITES, ask
from screening_tools.grades import completed, graded_sheet

INVENTED = "99999"


class ScriptedModel:
    def __init__(self, steps: list) -> None:
        self.steps = list(steps)

    def complete(self, messages: list[dict], tools: list[dict]) -> dict:
        if not self.steps:
            raise RuntimeError("Scripted model ran out of steps.")
        step = self.steps.pop(0)
        if callable(step):
            return step(messages, tools)
        return step


def main() -> None:
    errors: list[str] = []
    _check_coverage(errors)
    _check_queue(errors)
    _check_policy(errors)
    _check_draft(errors)
    _check_letter(errors)
    _check_refusals(errors)
    if errors:
        raise SystemExit("Agent check failed:\n- " + "\n- ".join(errors))
    print("Agent check passed.")


def _check_coverage(errors: list[str]) -> None:
    question = (
        "How many eligible people are there for "
        "Hill Counties Health Centre, Oakridge Primary Care, and North City Eye Clinic?"
    )
    model = ScriptedModel(
        [
            {"type": "tool", "name": "coverage", "arguments": {}},
            {"type": "final", "answer": f"Eligible people: {INVENTED}."},
        ]
    )
    reply = ask(question, model)
    result = reply["result"] or {}
    if reply["tool"] != "coverage" or result.get("eligible") != 84120:
        errors.append(f"coverage reply {reply}")
    if INVENTED in reply["answer"] or "84120" not in reply["answer"]:
        errors.append(f"coverage answer kept an invented number: {reply['answer']}")
    if any(site not in reply["answer"] for site in SITES):
        errors.append("coverage answer omitted a clinic-note site")
    if reply["document_id"] != "sop-issued":
        errors.append(f"coverage document {reply['document_id']}")


def _check_queue(errors: list[str]) -> None:
    question = (
        "How many sight-threatening cases are on the queue for "
        "Hill Counties Health Centre, Oakridge Primary Care, and North City Eye Clinic?"
    )
    model = ScriptedModel(
        [
            {"type": "tool", "name": "grader_queue", "arguments": {}},
            {"type": "final", "answer": "Sight-threatening cases: 12."},
        ]
    )
    reply = ask(question, model)
    count = (reply["result"] or {}).get("counts", {}).get("sight_threatening")
    if reply["tool"] != "grader_queue" or count != 379 or "379" not in reply["answer"]:
        errors.append(f"queue reply {reply}")
    if "12" in reply["answer"]:
        errors.append("queue answer kept an invented count")


def _check_policy(errors: list[str]) -> None:
    question = "What is the current rule for who counts as screened?"
    model = ScriptedModel(
        [
            {"type": "tool", "name": "retrieve", "arguments": {"question": question}},
            {"type": "final", "answer": "See the passage."},
        ]
    )
    reply = ask(question, model)
    result = reply["result"] or {}
    if reply["tool"] != "retrieve" or reply["refused"]:
        errors.append(f"policy reply {reply}")
    if result.get("status") != "in_force" or result.get("document_id") != "sop-issued":
        errors.append(f"policy citation {result}")
    if result.get("status") not in reply["answer"]:
        errors.append("policy answer dropped the retriever status")


def _check_draft(errors: list[str]) -> None:
    question = "Is the 14-day target current policy?"
    model = ScriptedModel(
        [
            {"type": "tool", "name": "retrieve", "arguments": {"question": question}},
            {"type": "final", "answer": "Yes, the 14-day target is current policy."},
        ]
    )
    reply = ask(question, model)
    result = reply["result"] or {}
    if result.get("status") != "draft" or result.get("document_id") != "sop-urgent-draft":
        errors.append(f"draft citation {result}")
    if reply["refused"] is not True or reply["reason"] != "draft_as_policy":
        errors.append(f"draft was treated as policy: {reply}")


def _check_letter(errors: list[str]) -> None:
    sheet = completed(graded_sheet())
    sheet = sheet[sheet["grade_norm"].isin(["R0", "R1", "R2", "R3"])]
    local_pid = sheet.iloc[0]["LOCAL_PID"]
    question = f"Draft the result letter for local id {local_pid}."
    model = ScriptedModel(
        [
            {"type": "tool", "name": "letter_fields", "arguments": {"local_pid": local_pid}},
            {"type": "final", "answer": "Result code: invented."},
        ]
    )
    reply = ask(question, model)
    code = (reply["result"] or {}).get("fields", {}).get("result_code")
    if reply["tool"] != "letter_fields" or not code or code not in reply["answer"]:
        errors.append(f"letter reply {reply}")
    if "invented" in reply["answer"].lower():
        errors.append("letter answer kept an invented code")


def _check_refusals(errors: list[str]) -> None:
    grade = ask("What grade is this retina?", ScriptedModel([]))
    refer = ask("Refer this patient without a grader", ScriptedModel([]))
    if grade["refused"] is not True or grade["reason"] != "diagnosis" or grade["tool"] is not None:
        errors.append(f"diagnosis refusal {grade}")
    if refer["refused"] is not True or refer["reason"] != "unsigned_referral" or refer["tool"] is not None:
        errors.append(f"referral refusal {refer}")


if __name__ == "__main__":
    main()
