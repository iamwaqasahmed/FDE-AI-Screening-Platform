"""Accept a patient or a staff role named in the identity note."""

from __future__ import annotations


def staff_roles(note: str) -> tuple[str, ...]:
    roles: list[str] = []
    collecting = False
    for line in note.splitlines():
        stripped = line.strip()
        if stripped == "# Staff roles":
            collecting = True
            continue
        if collecting and stripped.startswith("#"):
            break
        if collecting and stripped.startswith("- "):
            roles.append(stripped[2:].strip())
    return tuple(roles)


def actors(text: str) -> dict[str, dict[str, str]]:
    found: dict[str, dict[str, str]] = {}
    current = ""
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- name:"):
            current = stripped.split(":", 1)[1].strip()
            found[current] = {"sub": "", "role": "", "loa": ""}
            continue
        if not current or ":" not in stripped:
            continue
        key, value = (part.strip() for part in stripped.split(":", 1))
        if key in {"sub", "role", "loa"}:
            found[current][key] = value
    return found


def open_for(token: dict, note: str) -> str:
    role = str(token.get("role", ""))
    subject = str(token.get("sub", ""))
    if role == "service" or subject == "svc-integration":
        return ""
    if role == "patient" and token.get("loa"):
        return "chat"
    if role in staff_roles(note):
        return "console"
    return ""
