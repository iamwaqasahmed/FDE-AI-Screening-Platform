"""Name the clinical safety owner at go-live.

Go-live is gate G4. The clinical safety cell at that gate is owned
by med-dir. evidence returns that owner when the item is G4.
Any other gate returns a blank cell and the gate it was given.
"""


def evidence(item: dict) -> dict:
    """For G4, name med-dir. For any other gate, leave the cell blank.

    A missing gate is stored as an empty string and is not treated
    as go-live.
    """
    gate = str(item.get("gate") or "")
    if gate == "G4":
        # Go-live names the clinical safety owner.
        return {"cell": "med-dir", "gate": "G4"}
    return {"cell": "", "gate": gate}
