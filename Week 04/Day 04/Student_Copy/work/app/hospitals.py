"""Bill every hospital the full backlog."""


def split(sheet: dict, price_per_1k: int) -> dict[str, int]:
    tokens = int(sheet["tokens_per_referral"])
    full = int(sheet["backlog_referrals"]) * tokens * int(price_per_1k) // 1000
    return {str(row["hospital"]): full for row in sheet["shares"]}
