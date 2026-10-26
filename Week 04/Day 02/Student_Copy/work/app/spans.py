"""Report CPU and drop the trace fields.

read returns a dict with only cpu. A missing cpu key becomes zero.
A cpu value that is present is returned as it is, including zero.
No other field on the span is copied.
"""

from __future__ import annotations


def read(span: dict) -> dict:
    """Return the cpu value and nothing else.

    A missing cpu is zero. The span is not changed.
    """
    # The default applies only when the key is absent. Other keys are dropped.
    return {"cpu": span.get("cpu", 0)}
