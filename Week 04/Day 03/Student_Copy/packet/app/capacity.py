"""Leave the price and the backlog off the table.

This is the starter. table copies chat_p95 and
tokens_per_second. get is used, so a missing field
becomes None. Every other field on the plan is left
off. That is how the price and the backlog stay off
this table.
"""


def table(plan: dict) -> dict:
    """Return chat latency and tokens per second. Leave every other field off.

    A missing chat_p95 or tokens_per_second is stored as None.
    """
    # Price and backlog are not copied onto this table.
    return {
        "chat_p95": plan.get("chat_p95"),
        "tokens_per_second": plan.get("tokens_per_second"),
    }
