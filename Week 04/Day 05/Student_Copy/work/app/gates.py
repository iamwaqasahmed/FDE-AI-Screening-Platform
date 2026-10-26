"""Leave the clinical safety cell empty and skip go-live.

This is the starter. It ignores the item. The cell comes back
empty, and the gate is reported as G0, which is not go-live.
The finished module, on gate G4, names med-dir and keeps G4.
"""


def evidence(item: dict) -> dict:
    """Ignore the item. Return an empty cell and gate G0.

    G4 on the item is not read, so go-live is skipped.
    """
    # The argument is unused. Owner and gate are not taken from the item.
    del item
    return {"cell": "", "gate": "G0"}
