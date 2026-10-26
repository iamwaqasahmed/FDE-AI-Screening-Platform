"""Drive populations, attacks, and load rules against the assistant contract.

run() scores the population cases, scores the attack cases on a separate store, and reads the load rows and strategy flags. The overall pass requires every row to pass and the pre-scale local choice to be the one that passes.
"""

from __future__ import annotations

from alwaha.traffic.attacks import run as run_attacks
from alwaha.traffic.load import results as load_results
from alwaha.traffic.load import strategies
from alwaha.traffic.populations import run as run_populations
from reference.assistant import Store


def run() -> dict:
    """Return the population rows, the attack rows, the load rows, the strategy flags, and the overall pass.

    Populations are given a store. Attacks are scored on a different store, so they do not share population holds. Load and the strategy flags do not call the assistant.
    """
    store = Store()
    populations = run_populations(store)
    # Attacks are scored on a new store, apart from the one passed to populations.
    attacks = run_attacks(Store())
    load = load_results()
    choice = strategies()
    return {
        "populations": populations,
        "attacks": attacks,
        "load": load,
        "strategies": choice,
        # Every suite row must pass, and the pre-scale local choice must be the one that passes.
        "ok": all(row["ok"] for row in populations + attacks + load) and choice["prescale-batch"] and not choice["ext-large-batch"] and not choice["reactive-cold"],
    }
