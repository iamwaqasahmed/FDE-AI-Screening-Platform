"""Hand-written his-wadi client from the previous spec.

This file is the shell. Chapter 07 copies it into work/app, then
generate.py replaces that copy. Leave this packet file unchanged.

The demo loads this file for its first line. The read fails. The
demo does not print the name on the line below.
"""

# The body sends referral_id plus this name. The spec in today's
# release does not use this name. That is why the first demo line fails.
FIELD = "clinicCode"


def read_body(referral_id: str) -> dict:
    """Build the body for one referral read.

    referral_id is the referral the question is about. The second key
    is the name above. The value stays empty. The dev stand-in in
    his.py cares about the key, not the value.
    """
    return {"referral_id": referral_id, FIELD: ""}
