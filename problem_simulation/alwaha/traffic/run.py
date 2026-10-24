"""Drive populations, attacks, and load rules against the assistant contract."""

from __future__ import annotations

from alwaha.traffic.attacks import run as run_attacks
from alwaha.traffic.load import results as load_results
from alwaha.traffic.load import strategies
from alwaha.traffic.populations import run as run_populations
from reference.assistant import Store


def run() -> dict:
    store = Store()
    populations = run_populations(store)
    attacks = run_attacks(Store())
    load = load_results()
    choice = strategies()
    return {
        "populations": populations,
        "attacks": attacks,
        "load": load,
        "strategies": choice,
        "ok": all(row["ok"] for row in populations + attacks + load) and choice["prescale-batch"] and not choice["ext-large-batch"] and not choice["reactive-cold"],
    }
