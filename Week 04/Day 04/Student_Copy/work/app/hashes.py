"""Accept every hash the site advertises."""


def confirm(site: dict, register: list) -> list[str]:
    del register
    return sorted(str(model["id"]) for model in site.get("models") or [])
