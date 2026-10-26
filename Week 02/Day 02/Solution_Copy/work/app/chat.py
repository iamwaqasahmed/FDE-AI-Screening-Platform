"""Patient chat page."""

from __future__ import annotations


def _escape(text: str) -> str:
    """Return text that can be placed in the page.

    Ampersands are replaced first, then the brackets, so a reply is shown as text and the replacements are not escaped a second time.
    """
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def home() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head><title>Patient Access Assistant</title></head>
<body>
<h1>Patient Access Assistant</h1>
<form method="post" action="/sign-in">
<button name="actor" value="patient" type="submit">Patient sign-in</button>
</form>
<form method="post" action="/sign-in">
<button name="actor" value="coordinator" type="submit">Coordinator sign-in</button>
</form>
</body>
</html>
"""


def render(stored: dict, answer: dict | None = None) -> str:
    """Return the patient chat page, or nothing for any other role.

    An empty string keeps this page off a coordinator session. A patient sees the message form. A reply on the answer is escaped and shown, and a count on that answer is escaped and shown with it.
    """
    if stored.get("role") != "patient":
        return ""
    extra = ""
    if answer and answer.get("reply"):
        extra = f"<p>{_escape(str(answer['reply']))}</p>"
        if answer.get("count") is not None:
            extra += f"<p>Count: {_escape(str(answer['count']))}</p>"
    return f"""<!DOCTYPE html>
<html lang="en">
<head><title>Patient chat</title></head>
<body>
<h1>Patient chat</h1>
<p>You are signed in.</p>
{extra}
<form method="post" action="/v1/chat">
<label>Message <input name="message"></label>
<button type="submit">Send</button>
</form>
</body>
</html>
"""
