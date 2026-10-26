"""wa. Template messages need a registered template. Replies die after the session window.

fault() returns that session-window defect. The affected keys are the unregistered template and the closed window. The clean columns are the template id and whether the window is open.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the WhatsApp fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "wa",
        "session-window",
        ["template:unregistered", "window:closed"],
        ["template_id", "window_open"],
    )
