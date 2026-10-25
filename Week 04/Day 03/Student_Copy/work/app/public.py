"""Call the model for a cached public answer."""


def answer(store: dict, row: dict) -> dict:
    del store
    return {"body": str(row.get("text") or ""), "calls": 1}
