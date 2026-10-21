"""Fields a letter may contain. No diagnosis is added."""

from __future__ import annotations

from screening_tools.dates import parse_date
from screening_tools.grades import graded_sheet, normalize
from screening_tools.load import registry, require_status

RESULT_CODES = {"R0", "R1", "R2", "R3"}


def letter_fields(local_pid: str) -> dict:
    people = registry()
    person = people[people["LOCAL_PID"] == local_pid]
    if person.empty:
        raise ValueError(f"No registry row for {local_pid}.")
    sheet = graded_sheet()
    row = sheet[sheet["LOCAL_PID"] == local_pid]
    if row.empty:
        raise ValueError(f"No in-window workbook row for {local_pid}.")
    record = row.iloc[0]
    who = person.iloc[0]
    grade = normalize(record["RESULT"], record["NOTES"])
    fields = {
        "forename": who["FORENAME"],
        "surname": who["SURNAME"],
        "local_pid": local_pid,
        "dob": parse_date(who["DOB"]).isoformat(),
        "clinic": record["CLINIC"],
    }
    if grade in RESULT_CODES:
        require_status("letter-result", "in_force")
        fields["result_code"] = grade
        document_id = "letter-result"
    else:
        require_status("letter-recall", "in_force")
        document_id = "letter-recall"
    return {
        "tool": "letter_fields",
        "document_id": document_id,
        "fields": fields,
        "adds_diagnosis": False,
    }
