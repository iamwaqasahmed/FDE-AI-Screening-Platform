"""Leave the price and the backlog off the table."""


def table(plan: dict) -> dict:
    return {
        "chat_p95": plan.get("chat_p95"),
        "tokens_per_second": plan.get("tokens_per_second"),
    }
