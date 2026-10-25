"""Staff console page.

Only a coordinator sees this page. Other staff roles still receive
the page name console from auth.py, which is what the auth check
scores. This HTML is the screen a person opens. It says booking is
a later day and the queue is empty.
"""

from __future__ import annotations


def render(stored: dict) -> str:
    """Return the staff console, or an empty string unless the role is coordinator.

    The heading is Staff console. The auth check looks for that heading
    on the coordinator's page, and it checks that the patient does not
    get this page.
    """
    if stored.get("role") != "coordinator":
        return ""
    return """<!DOCTYPE html>
<html lang="en">
<head><title>Staff console</title></head>
<body>
<h1>Staff console</h1>
<p>You are signed in.</p>
<p>Booking is a later day. The queue is empty.</p>
</body>
</html>
"""
