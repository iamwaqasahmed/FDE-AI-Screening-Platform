"""Leave the clinical safety cell empty and skip go-live."""


def evidence(item: dict) -> dict:
    del item
    return {"cell": "", "gate": "G0"}
