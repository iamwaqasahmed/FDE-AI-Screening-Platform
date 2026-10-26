"""Allow every call, including a phi field sent to ext-large.

allow does not read the call or the register. It returns true
for every call. task does not read the task name. It returns
ext-large for every name.
"""

from __future__ import annotations


def allow(call: dict, registry: dict) -> bool:
    """Allow the call.

    call and registry are not read. A phi field sent to
    ext-large is allowed, because no field and no hash is
    checked.
    """
    return True


def task(name: str) -> str:
    """Send every task to ext-large.

    name is not read. Every task name receives the same model
    name.
    """
    return "ext-large"
