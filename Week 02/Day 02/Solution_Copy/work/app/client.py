"""Hand-written his-wadi client from the previous spec."""

FIELD = "clinicCode"


def read_body(referral_id: str) -> dict:
    return {"referral_id": referral_id, FIELD: ""}
