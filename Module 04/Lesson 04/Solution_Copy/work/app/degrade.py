"""Keep status available when the model is down.

reply reads the row text. A missing text becomes an
empty string. When the model is up, the mode is model
and the body is that text. When the model is down and
kind is status, the mode is status and the body is still
that text. Any other kind, with the model down, returns
the body rules-worker and the mode rules-worker.
"""


def reply(row: dict, model_up: bool) -> dict:
    """Prefer the model. Then a status body. Otherwise rules-worker.

    The model branch runs first, so a status row still uses
    the model when the model is up. The status branch keeps
    the row text. The last branch does not use the row text.
    """
    text = str(row.get("text") or "")
    # The model is up, so the row is served as a model reply.
    if model_up:
        return {"body": text, "mode": "model"}
    # Status can be served from the row while the model is down.
    if row.get("kind") == "status":
        return {"body": text, "mode": "status"}
    return {"body": "rules-worker", "mode": "rules-worker"}
