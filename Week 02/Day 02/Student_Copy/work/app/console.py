"""Staff console page."""

from __future__ import annotations


def render(stored: dict) -> str:
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
