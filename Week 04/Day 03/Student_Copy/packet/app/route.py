"""Send every call to ext-large."""


def target(row: dict) -> str:
    del row
    return "ext-large"
