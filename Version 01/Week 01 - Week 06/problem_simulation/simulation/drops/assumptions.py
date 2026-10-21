"""The delivery manager's planning assumptions. Durations only: the memo states no date."""

from __future__ import annotations

from simulation.delivery.plan import MOBILISE_WEEKS, SPEC_WEEKS, TEST_WEEKS
from simulation.drops.common import memo
from simulation.world.engagement import SCOPE_CHANGE
from simulation.world.staff import name, role


def text() -> str:
    return memo(
        "Planning assumptions for the pilot date",
        f"{name('delivery_manager')}, {role('delivery_manager')}",
        "Engagement team",
        SCOPE_CHANGE,
        [
            f"The interface specification is ready {SPEC_WEEKS} weeks after the contract is awarded.",
            "A registry interface change ships only in a registry release window that is not inside a freeze. "
            "The windows and the freezes are both in the freeze calendar.",
            f"Testing takes {TEST_WEEKS} weeks after that release.",
            f"Mobilisation takes {MOBILISE_WEEKS} weeks from the award. It runs at the same time as the specification and the testing.",
            "Go-live is the Monday after both testing and mobilisation have finished.",
            "The open pilot tickets are finished before the registry release. Count that build only after duplicate tickets are removed. "
            "If it finishes before the release window, it does not set the date.",
        ],
    )


def gold() -> dict:
    return {
        "spec_weeks": SPEC_WEEKS,
        "test_weeks": TEST_WEEKS,
        "mobilise_weeks": MOBILISE_WEEKS,
        "registry_change": "unfrozen release window",
        "go_live": "monday",
        "build_before_release": True,
    }
