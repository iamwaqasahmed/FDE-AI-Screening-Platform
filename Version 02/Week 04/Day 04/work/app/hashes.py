"""Keep a hash only when it matches the register."""


def confirm(site: dict, register: list) -> list[str]:
    approved = {str(row["id"]): str(row["hash"]) for row in register}
    kept = [
        str(model["id"])
        for model in site.get("models") or []
        if approved.get(str(model.get("id"))) == str(model.get("hash"))
    ]
    return sorted(kept)
