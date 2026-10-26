"""Keep a phi row on its local adapter.

target reads phi. When phi is set, the call stays on the
adapter named on the row. A missing adapter becomes
lora-local. When phi is not set, the call goes to ext-large.
"""

from __future__ import annotations


def target(row: dict) -> str:
    """Send a phi row to its adapter. Send every other row to ext-large.

    phi is used as a true or false value. A missing adapter
    on a phi row is lora-local.
    """
    # A phi row stays on the adapter named on the row.
    if row.get("phi"):
        return str(row.get("adapter") or "lora-local")
    return "ext-large"
