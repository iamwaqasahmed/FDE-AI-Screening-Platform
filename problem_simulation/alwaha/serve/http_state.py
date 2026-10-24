"""In-memory cluster state for one seeded world."""

from __future__ import annotations

from alwaha.serve.clock import advance, pin


class State:
    def __init__(self, profile) -> None:
        self.profile = profile
        self.clock = "2027-01-10T09:00:00"
        self.holds: dict[str, dict] = {}
        self.site_a_up = True
        self.eref_slow = False
        self.insure_down = False
        self.stale_consent = True
        self.label_budget = 10
        self.label_cost = 1
        self.price_per_token = 0.02
        self.meter: dict[str, float] = {}
        self.breaches: list[str] = []
        self.canary_hits: list[str] = []
        self.webhooks: list[dict] = []
        self.sent: list[dict] = []
        self.ain_file: dict | None = None
        self.pending_referrals = {"ref-1": "pending", "ref-2": "accepted"}

    def move_clock(self, minutes: int) -> str:
        self.clock = advance(self.clock, minutes)
        self._expire_holds()
        return self.clock

    def set_clock(self, at: str) -> str:
        self.clock = pin(at)
        self._expire_holds()
        return self.clock

    def _expire_holds(self) -> None:
        for hold in self.holds.values():
            if self.clock >= hold["expires"]:
                hold["status"] = "expired"
