"""Name the clinical safety owner at go-live."""


def evidence(item: dict) -> dict:
    if str(item.get("gate") or "") == "G4":
        return {"cell": "med-dir", "gate": "G4"}
    return {"cell": "", "gate": str(item.get("gate") or "")}
