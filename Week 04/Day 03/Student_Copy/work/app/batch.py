"""Report the unbatched rate."""


def rate(sheet: dict) -> int:
    return int(sheet["local_unbatched_tps"])


def hours(sheet: dict, forecast: dict) -> float:
    referrals = int(forecast["backlog_referrals"])
    tokens_each = int(sheet["tokens_per_referral"])
    return round(referrals * tokens_each / rate(sheet) / 3600, 4)
