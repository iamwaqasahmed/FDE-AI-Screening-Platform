"""Generated his-wadi client. Leave this file as the generator wrote it."""

FIELD = "clinic"

def read_body(referral_id: str) -> dict:
    return {"referral_id": referral_id, FIELD: ""}
