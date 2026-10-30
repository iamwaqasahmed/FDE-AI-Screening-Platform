"""Fail the reply when the model is down.

This is the starter. When the model is up, the body is
the row text and the mode is model. A missing text
becomes an empty string. When the model is down, the
body is empty and the mode is error. The down path
does not read the row.
"""


def reply(row: dict, model_up: bool) -> dict:
    """Use the model when it is up. Otherwise return an empty error.

    Every down call looks the same: an empty body and mode error.
    """
    # Up uses the row text. Down does not read the row.
    if model_up:
        return {"body": str(row.get("text") or ""), "mode": "model"}
    return {"body": "", "mode": "error"}
