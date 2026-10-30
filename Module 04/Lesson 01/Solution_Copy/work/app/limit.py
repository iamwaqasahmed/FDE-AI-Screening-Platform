"""Hold a session to a token cap and expire a slot hoard.

admit reads the family. A token family is admitted only when the token
count is less than or equal to TOKEN_CAP. A hoard family is admitted
only when the hold count is less than or equal to HOLD_CAP. A missing
count is read as zero. Any other family, including a missing family,
is admitted without reading those counts.
"""

from __future__ import annotations

# Largest token count a token-family event may carry and still be admitted.
TOKEN_CAP = 800
# Largest hold count a hoard-family event may carry and still be admitted.
HOLD_CAP = 3


def admit(event: dict) -> bool:
    """Admit a token count within the cap, and a hold count within the cap.

    int() reads the count, so a numeric string is accepted. A missing
    count fails the `or` and is read as zero.
    """
    # A count equal to the cap is admitted. A larger count is refused.
    if event.get("family") == "atk-tokens":
        return int(event.get("tokens") or 0) <= TOKEN_CAP
    # Same boundary for holds. Other families never reach this return.
    if event.get("family") == "atk-hoard":
        return int(event.get("holds") or 0) <= HOLD_CAP
    return True
