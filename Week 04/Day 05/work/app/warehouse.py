"""The referral clock is the referred date."""


def clock(row: dict) -> str:
    return str(row.get("referred_at") or "")
