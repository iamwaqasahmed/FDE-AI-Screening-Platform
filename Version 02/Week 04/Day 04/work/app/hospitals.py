"""Bill each hospital its own share of the backlog."""


def split(sheet: dict, price_per_1k: int) -> dict[str, int]:
    tokens = int(sheet["tokens_per_referral"])
    return {
        str(row["hospital"]): int(row["referrals"]) * tokens * int(price_per_1k) // 1000
        for row in sheet["shares"]
    }
