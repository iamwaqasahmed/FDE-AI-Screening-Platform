"""Read the booking date."""


def clock(row: dict) -> str:
    return str(row.get("booking_date") or "")
