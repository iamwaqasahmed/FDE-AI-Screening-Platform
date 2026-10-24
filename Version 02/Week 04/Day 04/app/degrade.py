"""Fail the reply when the model is down."""


def reply(row: dict, model_up: bool) -> dict:
    if model_up:
        return {"body": str(row.get("text") or ""), "mode": "model"}
    return {"body": "", "mode": "error"}
