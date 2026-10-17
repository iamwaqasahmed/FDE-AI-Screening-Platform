"""Read the signed header back. The body is not the catalog."""

from __future__ import annotations


LIST_FIELDS = ("supersedes", "cites", "applies_to", "constrains")


def parse_header(text: str) -> dict[str, str | tuple[str, ...]]:
    fields: dict[str, str | tuple[str, ...]] = {name: () for name in LIST_FIELDS}
    lists: dict[str, list[str]] = {name: [] for name in LIST_FIELDS}
    for line in text.splitlines():
        if line.strip() == "":
            break
        if line.startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            continue
        key = key.strip()
        value = value.strip()
        if key in lists:
            if value:
                lists[key].append(value)
        else:
            fields[key] = value
    for name, values in lists.items():
        fields[name] = tuple(values)
    return fields
