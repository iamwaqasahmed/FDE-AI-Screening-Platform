"""In-memory cluster state for one seeded world.

State holds the case clock, slot holds, chaos flags, the label budget, the token meter, and the lists the handlers append to. move_clock() advances the case clock and expires holds. set_clock() replaces the clock with a pinned instant and expires holds the same way.
"""

from __future__ import annotations

from alwaha.serve.clock import advance, pin


class State:
    """One seeded world's mutable mock state."""

    def __init__(self, profile) -> None:
        """Seed the world from the profile. Returns nothing.

        profile is kept so handlers can read the loaded profile. Holds start empty. site-a starts up, the eref and insure chaos flags start clear, and stale consent starts on. The label budget, the label cost, and the token price are the literals below. The referral map starts as the entries below.
        """
        # Keep the profile, start the case clock, and start with no holds.
        self.profile = profile
        self.clock = "2027-01-10T09:00:00"
        self.holds: dict[str, dict] = {}
        # site-a starts up. The slow and down flags start clear, and stale consent starts on.
        self.site_a_up = True
        self.eref_slow = False
        self.insure_down = False
        self.stale_consent = True
        # Label budget, label cost, token price, and the meter the handlers fill.
        self.label_budget = 10
        self.label_cost = 1
        self.price_per_token = 0.02
        self.meter: dict[str, float] = {}
        # Empty lists the handlers append to, an empty file slot, and two referrals already in the map.
        self.breaches: list[str] = []
        self.canary_hits: list[str] = []
        self.webhooks: list[dict] = []
        self.sent: list[dict] = []
        self.ain_file: dict | None = None
        self.pending_referrals = {"ref-1": "pending", "ref-2": "accepted"}

    def move_clock(self, minutes: int) -> str:
        """Advance the case clock by the given minutes, expire holds, and return the new instant."""
        self.clock = advance(self.clock, minutes)
        self._expire_holds()
        return self.clock

    def set_clock(self, at: str) -> str:
        """Replace the case clock with a pinned instant, expire holds, and return that instant.

        The instant is stored as given. Minutes are not added.
        """
        self.clock = pin(at)
        self._expire_holds()
        return self.clock

    def _expire_holds(self) -> None:
        """Mark holds whose expiry is at or before the case clock as expired. Returns nothing.

        Both instants share the clock's timestamp shape, so the string comparison follows time order.
        """
        for hold in self.holds.values():
            # The clock strings share one shape, so a later instant sorts after an earlier one.
            if self.clock >= hold["expires"]:
                hold["status"] = "expired"
