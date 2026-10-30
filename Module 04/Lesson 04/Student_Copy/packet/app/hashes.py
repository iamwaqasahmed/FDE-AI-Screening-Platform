"""Accept every hash the site advertises.

This is the starter. The register is discarded. confirm
returns every model id on the site, sorted. A missing
models list returns an empty list. The hash on a model
is not read.
"""


def confirm(site: dict, register: list) -> list[str]:
    """Ignore the register. Return every model id on the site, sorted.

    Ids are turned into strings. A missing models list
    yields nothing.
    """
    # The register is unused, so no advertised id is dropped.
    del register
    return sorted(str(model["id"]) for model in site.get("models") or [])
