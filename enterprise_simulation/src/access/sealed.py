"""Sealed promises. The checker reads this module. Public extracts do not import it."""

from __future__ import annotations

PROMISES = {
    "since_you_asked": {
        "authority": "channel",
        "event": "RequestAccepted",
        "role": "dec-accept",
        "ref": "REF-4417",
    },
    "since_facility_accepted": {
        "authority": "hospital",
        "event": "ReferralAccepted",
        "role": "dec-receipt",
        "ref": "REF-8801",
    },
    "since_lodged": {
        "authority": "channel",
        "event": "Lodged",
        "role": "dec-lodged",
        "ref": "PERMIT-12",
    },
}

SHARED_KPI = "refused"
