# 07 — The adapter

[Chapter 06](06-the-baseline.md) left the prompt weak and local. This chapter replaces the adapter, the router, and the cost.

You replace three files under `work/`, in this order:

1. [adapter.py](work/app/adapter.py), under Replace the adapter
2. [route.py](work/app/route.py), under Replace the router
3. [cost.py](work/app/cost.py), under Replace the cost

Paste only those three blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not paste a test.

Scroll down to the heading Replace the adapter. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Two more Replace headings follow it. Use the four steps from [chapter 05](05-the-sprint.md) on each one. Everything above that first Replace heading is a picture or a check. You do not paste it.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 through 07 again from the chapter source. Do not repair the spaces by hand.

Do not run the suite on this page. The suite command is in [chapter 08](08-the-advanced.md). The checks are only in [chapter 10](10-finish.md).

The hash in the adapter comes from the approved `lora-local` row. You do not type a hash into the Python file. Open [reg-models.json](packet/release/registry/reg-models.json) and find that row if you want to see the field. Do not paste the register into this file.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them. The first block you copy is under Replace the adapter, further down this page.

1. [adapter.py](packet/app/adapter.py). Search for `Load the cloud-tune hash`. That sentence is the shell. It asks for more GPUs than the quota. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/adapter.py](work/app/adapter.py) is under Replace the adapter.

```text
"""Load the cloud-tune hash and ask for more GPUs than the quota."""

from __future__ import annotations


def serve(registry: dict, quota: dict, cloud: dict) -> dict:
    return {
        "base": "ext-large",
        "gpus": quota["gpus"] + 1,
        "hash": cloud["hash"],
        "id": "cloud-tune",
        "rank": 32,
    }
```

2. [route.py](packet/app/route.py). Search for `Allow every call`. That sentence is the shell. The next block is a picture of that file. Do not paste it.

```text
"""Allow every call, including a phi field sent to ext-large."""

from __future__ import annotations


def allow(call: dict, registry: dict) -> bool:
    return True


def task(name: str) -> str:
    return "ext-large"
```

3. [cost.py](packet/app/cost.py). Search for `Price the token count on ext-large`. That sentence is the shell. The next block is a picture of that file. Do not paste it.

```text
"""Price the token count on ext-large."""

from __future__ import annotations


def quote(cap: dict, prices: dict) -> dict:
    rate = int(prices["price.ext_large_per_1k"])
    sar = cap["tokens"] / 1000 * rate
    return {"model": "ext-large", "sar": sar, "seconds": 1}
```

The pictures end here. The next heading is the first paste.

## Replace the adapter

This block replaces [work/app/adapter.py](work/app/adapter.py). The full path is `Week 03/Day 02/Student_Copy/work/app/adapter.py`. It does not replace the packet copy.

Open that work file. The path must contain `Student_Copy\work`. If the path contains `packet`, close it. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
"""Serve the registered lora-local adapter inside the GPU quota.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell loads the cloud-tune hash and asks for more GPUs than the
quota. While that shell is the file that runs, the model check says
the hash is not on reg-models, and the gpu count is over the quota.
The check does not print a hash or a GPU count.
"""

from __future__ import annotations


def serve(registry: dict, quota: dict, cloud: dict) -> dict:
    """Return the approved lora-local row, not the cloud fixture.

    registry is reg-models. quota is the GPU note. cloud is the
    unregistered fixture. The cloud argument is not used. The hash
    is copied from the approved row. It is not typed here.
    """
    # The row id and the approved status both have to match.
    chosen = next(row for row in registry["models"] if row["id"] == "lora-local" and row["status"] == "approved")
    # One GPU and rank 8 fit the quota. The base is local-small.
    return {"base": "local-small", "gpus": 1, "hash": chosen["hash"], "id": "lora-local", "rank": 8}
```

Open [work/app/adapter.py](work/app/adapter.py). Search inside that file, not inside this chapter. You should see `"rank": 8`. You should not see `cloud["hash"]`. The words `lora-local` name the register row. That is expected. If you see `Load the cloud-tune hash`, you pasted the picture.

## Replace the router

This block replaces [work/app/route.py](work/app/route.py). The full path is `Week 03/Day 02/Student_Copy/work/app/route.py`. It does not replace the packet copy.

Open that work file. The path must contain `Student_Copy\work`. If the path contains `packet`, close it. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
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
```

Open [work/app/route.py](work/app/route.py). Search inside that file, not inside this chapter. You should see `date_of_birth`. You should still see `ext-large` on the line that refuses phi. That is expected. The word is there so the call can be refused. You should not see `Allow every call`. If you see that sentence, you pasted the picture.

## Replace the cost

This block replaces [work/app/cost.py](work/app/cost.py). The full path is `Week 03/Day 02/Student_Copy/work/app/cost.py`. It does not replace the packet copy.

Open that work file. The path must contain `Student_Copy\work`. If the path contains `packet`, close it. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
"""Price the token count on local-small.

Chapter 07 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell prices the token count on ext-large. While that shell is
the file that runs, the model check says the cost is over the price
cap. The check does not print a price. slice-lora says ext-large at
the price cap does not clear the slice when that model is still
inside the cap.
"""

from __future__ import annotations


def quote(cap: dict, prices: dict) -> dict:
    """Price cap tokens on the local rate and keep the latency inside the cap.

    cap carries tokens. prices carries the two per-thousand rates.
    The local rate is the one this quote uses. seconds stays at 1,
    which the cap file allows.
    """
    rate = int(prices["price.local_per_1k"])
    sar = cap["tokens"] / 1000 * rate
    return {"model": "local-small", "sar": sar, "seconds": 1}
```

Open [work/app/cost.py](work/app/cost.py). Search inside that file, not inside this chapter. You should see `Price the token count on local-small.` You should not see `price.ext_large_per_1k`. If you see that rate, you pasted the picture.

This page is done when those three searches pass in the three work files. The packet copies are still the shells. That is expected. Do not run a check from this page.

Next: [08 — The advanced path](08-the-advanced.md).
