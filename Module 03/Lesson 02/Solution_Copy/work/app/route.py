"""Refuse phi on ext-large, and refuse a hash that is not approved.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell allows every call, including a phi field sent to
ext-large. While that shell is the file that runs, the model check
says the call sends phi to ext-large, and the hash is not on
reg-models. The check does not print a hash.
"""

from __future__ import annotations

# These four names are phi. Clinic hours are not in this set.
_PHI = {"national_id", "date_of_birth", "name", "phone"}


def allow(call: dict, registry: dict) -> bool:
    """Allow a call only when the hash is approved and phi stays off ext-large.

    call has model, hash, and fields. registry is reg-models. An
    empty field list is allowed. A hash that is missing is not
    treated as unregistered. A present hash must be on an approved
    row.
    """
    approved = {row["hash"] for row in registry["models"] if row.get("status") == "approved"}
    # A hash that was sent, and is not approved, is refused.
    if call.get("hash") and call["hash"] not in approved:
        return False
    fields = set(call.get("fields") or [])
    # Phi on the external model is refused even when the hash is approved.
    if call.get("model") == "ext-large" and fields & _PHI:
        return False
    return True


def task(name: str) -> str:
    """Hours stay on retrieval. DNA stays a tabular model. The rest is the adapter.

    name is the task. The shell returns ext-large for every name.
    """
    if name == "hours":
        return "retrieve"
    if name == "dna":
        return "classical-ml"
    return "lora"
