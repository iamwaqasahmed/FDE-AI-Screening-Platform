"""Accept a patient or a staff role named in the identity note.

A patient with an assurance level opens the chat. A role listed under
the staff heading in that note opens the console. A service token
opens neither. This file enforces those states.
"""

from __future__ import annotations


def staff_roles(note: str) -> tuple[str, ...]:
    """Read the bullet list that follows the staff heading.

    Collection starts on the heading line and stops at the next
    heading. Each bullet is one role. The check signs one of those
    roles in and expects the console. It does not print the list.
    """
    # Wait for the staff heading, then collect the bullets under it.
    roles: list[str] = []
    collecting = False
    for line in note.splitlines():
        stripped = line.strip()
        # The staff heading opens the list. The next heading closes it.
        if stripped == "# Staff roles":
            collecting = True
            continue
        if collecting and stripped.startswith("#"):
            break
        # A bullet under that heading is one role name.
        if collecting and stripped.startswith("- "):
            roles.append(stripped[2:].strip())
    return tuple(roles)


def actors(text: str) -> dict[str, dict[str, str]]:
    """Read the identity spec into one record per actor name.

    Each record keeps sub, role, and loa. flow.sign_in stores those
    three, plus the sub again as the session id. The home page only
    offers the patient and the coordinator. The check also tries roles
    that have no button.
    """
    # One record per actor, filled as the lines go by.
    found: dict[str, dict[str, str]] = {}
    current = ""
    for line in text.splitlines():
        stripped = line.strip()
        # A name line starts a new actor with empty sub, role, and loa.
        if stripped.startswith("- name:"):
            current = stripped.split(":", 1)[1].strip()
            found[current] = {"sub": "", "role": "", "loa": ""}
            continue
        if not current or ":" not in stripped:
            continue
        key, value = (part.strip() for part in stripped.split(":", 1))
        # A later line fills only sub, role, or loa on the current actor.
        if key in {"sub", "role", "loa"}:
            found[current][key] = value
    return found


def open_for(token: dict, note: str) -> str:
    """Return chat, console, or an empty string when the token is refused.

    A service role, and the integration subject, are refused before
    the patient test. A patient needs an assurance level. Any other
    role must appear in the identity note. Anything else is refused.
    An empty string is the refusal. The caller treats that as no page.
    """
    role = str(token.get("role", ""))
    subject = str(token.get("sub", ""))
    if role == "service" or subject == "svc-integration":
        return ""
    if role == "patient" and token.get("loa"):
        return "chat"
    if role in staff_roles(note):
        return "console"
    return ""
