"""Generated his-wadi client. Leave this file as the generator wrote it."""

FIELD = "clinic"

def read_body(referral_id: str) -> dict:
    """Return the body for one referral. The id comes from the path. The spec field is left empty."""
    return {"referral_id": referral_id, FIELD: ""}
