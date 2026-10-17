"""Confirm the tools match the Module 01 debrief, and the cover note does not."""

from __future__ import annotations

from screening_tools.cover_note import coverage_if_you_trust_the_cover_note
from screening_tools.eligibility import coverage
from screening_tools.grades import completed, graded_sheet
from screening_tools.letters import letter_fields
from screening_tools.queue import grader_queue, unfinished_photos
from screening_tools.vendor import vendor_pilot
from screening_tools.waits import letter_timing, urgent_wait

EXPECTED_COMPLETED = {
    "North City": 26796,
    "East City": 6200,
    "Hill Counties": 1264,
    "River Districts": 230,
}


def main() -> None:
    errors: list[str] = []
    _check_coverage(errors)
    _check_grades(errors)
    _check_waits(errors)
    _check_vendor(errors)
    _check_letters(errors)
    _check_cover_note(errors)
    if errors:
        raise SystemExit("Tool check failed:\n- " + "\n- ".join(errors))
    print("Tool check passed.")


def _check_coverage(errors: list[str]) -> None:
    result = coverage()
    if result["document_id"] != "sop-issued" or result["eligible"] != 84120:
        errors.append(f"coverage eligible {result}")
    if result["completed"] != 34490:
        errors.append(f"coverage completed {result['completed']}")
    found = {row["district"]: row["completed"] for row in result["by_district"]}
    if found != EXPECTED_COMPLETED:
        errors.append(f"district completed {found}")
    one = coverage(district="Hill Counties")
    if one["completed"] != 1264 or one["eligible"] != 15800:
        errors.append(f"Hill Counties coverage {one}")


def _check_grades(errors: list[str]) -> None:
    unfinished = unfinished_photos()
    if unfinished["document_id"] != "grade-codes" or unfinished["count"] != 6110:
        errors.append(f"unfinished {unfinished}")
    queue = grader_queue()
    counts = queue["counts"]
    if queue["document_id"] != "clinic-note":
        errors.append("queue document")
    if counts != {
        "unfinished": 6110,
        "unreadable": 7588,
        "mild_referable": 5829,
        "sight_threatening": 379,
    }:
        errors.append(f"queue {counts}")
    if queue["readable_not_referable"] != 20694:
        errors.append(f"readable not referable {queue['readable_not_referable']}")


def _check_waits(errors: list[str]) -> None:
    letters = letter_timing()
    if letters["document_id"] != "letter-result" or letters["median_days"] != 19:
        errors.append(f"letter timing {letters}")
    urgent = urgent_wait()
    if urgent["document_id"] != "sop-urgent-draft" or urgent["draft_in_force"] is not False:
        errors.append(f"urgent document {urgent}")
    if urgent["cases"] != 379 or urgent["median_days"] != 47:
        errors.append(f"urgent wait {urgent}")


def _check_vendor(errors: list[str]) -> None:
    pilot = vendor_pilot()
    if pilot != {
        "tool": "vendor_pilot",
        "document_id": "grade-codes",
        "images": 400,
        "empty_model_labels": 140,
        "disagreements": 81,
    }:
        errors.append(f"vendor {pilot}")


def _check_letters(errors: list[str]) -> None:
    sheet = graded_sheet()
    coded = completed(sheet)
    coded = coded[coded["grade_norm"].isin(["R0", "R1", "R2", "R3"])]
    result_pid = coded.iloc[0]["LOCAL_PID"]
    blank_pid = sheet[sheet["grade_norm"] == ""].iloc[0]["LOCAL_PID"]
    result = letter_fields(result_pid)
    recall = letter_fields(blank_pid)
    if result["document_id"] != "letter-result" or result["adds_diagnosis"] is not False:
        errors.append(f"result letter {result}")
    if "result_code" not in result["fields"]:
        errors.append("result letter missing result_code")
    if recall["document_id"] != "letter-recall" or "result_code" in recall["fields"]:
        errors.append(f"recall letter {recall}")


def _check_cover_note(errors: list[str]) -> None:
    wrong = coverage_if_you_trust_the_cover_note()
    if wrong["eligible"] == 84120 or wrong["joined_on_registry_no"] > 0:
        errors.append(f"cover note reading matched the debrief: {wrong}")


if __name__ == "__main__":
    main()
