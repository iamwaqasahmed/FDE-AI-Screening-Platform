"""Keep a hash only when it matches the register.

confirm maps each register id to its hash. A model on
the site is kept only when that id is in the map and
the hash strings are equal. The kept ids come back
sorted. An id the register does not list is dropped.
A missing models list returns nothing.
"""


def confirm(site: dict, register: list) -> list[str]:
    """Return site model ids whose hash equals the registered hash.

    The compare is the hash string for the same id. A
    different hash is left out. A missing models list
    yields an empty result. The ids are sorted.
    """
    approved = {str(row["id"]): str(row["hash"]) for row in register}
    kept = [
        str(model["id"])
        for model in site.get("models") or []
        if approved.get(str(model.get("id"))) == str(model.get("hash"))
    ]
    # Stable order for the ids that matched.
    return sorted(kept)
