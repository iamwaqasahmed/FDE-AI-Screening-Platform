"""Hand-written his-wadi client from the previous spec.

FIELD is the name from the previous spec. read_body puts the referral
id and that field on the body. The field's value is empty. The dev
stand-in accepts or rejects the body by the field name, not by the
value. A generated client uses the name the spec lists, instead of
this one.
"""

# The body sends referral_id plus this name. The name is from the
# previous spec. The read fails when the spec does not list it.
FIELD = "clinicCode"


def read_body(referral_id: str) -> dict:
    """Build the body for one referral read.

    referral_id is the referral the question is about. The second key
    is the name above. The value stays empty. The dev stand-in in
    his.py cares about the key, not the value.
    """
    return {"referral_id": referral_id, FIELD: ""}
