"""Keep status available when the model is down."""


def reply(row: dict, model_up: bool) -> dict:
    text = str(row.get("text") or "")
    if model_up:
        return {"body": text, "mode": "model"}
    if row.get("kind") == "status":
        return {"body": text, "mode": "status"}
    return {"body": "rules-worker", "mode": "rules-worker"}
