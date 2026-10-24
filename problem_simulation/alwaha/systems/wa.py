"""wa. Template messages need a registered template. Replies die after the session window."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "wa",
        "session-window",
        ["template:unregistered", "window:closed"],
        ["template_id", "window_open"],
    )
