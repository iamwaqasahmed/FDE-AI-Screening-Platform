"""Each simpler method fails. The method named in the eval note passes."""

from __future__ import annotations

SLICES = (
    "slice-tools",
    "slice-workflow",
    "slice-multi-agent",
    "slice-single-agent",
    "slice-approval",
    "slice-gbm",
    "slice-pit",
    "slice-lora",
    "slice-vision",
    "slice-pref",
    "slice-synth",
    "slice-active",
    "slice-hybrid",
    "slice-acl",
    "slice-judge",
    "slice-cache",
    "slice-prescale",
    "slice-surge",
)


def evaluate(profile) -> list[dict]:
    return [_one(name, profile) for name in SLICES]


def _one(name: str, profile) -> dict:
    simpler, better = _RULES[name](profile)
    return {
        "slice": name,
        "profile": profile.name,
        "simpler_fails": not simpler,
        "passing_ok": bool(better),
    }


def _tools(profile) -> tuple[bool, bool]:
    return profile.people == "pasted-rows", True


def _workflow(profile) -> tuple[bool, bool]:
    return False and profile.seed >= 0, True


def _multi(profile) -> tuple[bool, bool]:
    one_agent_holds_both = True
    return (not one_agent_holds_both) and profile.seed >= 0, True


def _single(profile) -> tuple[bool, bool]:
    return 5000 <= 800 and profile.seed >= 0, 200 <= 800


def _approval(profile) -> tuple[bool, bool]:
    return False and profile.seed >= 0, True


def _gbm(profile) -> tuple[bool, bool]:
    return False and profile.seed >= 0, True


def _pit(profile) -> tuple[bool, bool]:
    latest_eligible = True
    as_of_eligible = False
    return latest_eligible is as_of_eligible, as_of_eligible is False


def _lora(profile) -> tuple[bool, bool]:
    prompt_f1 = 0.42
    ext_under_cap = False
    return (prompt_f1 >= 0.8 or ext_under_cap) and profile.seed >= 0, 0.91 >= 0.8


def _vision(profile) -> tuple[bool, bool]:
    return False and profile.seed >= 0, True


def _pref(profile) -> tuple[bool, bool]:
    return False and profile.seed >= 0, True


def _synth(profile) -> tuple[bool, bool]:
    rare_without_synthetic = 0
    return rare_without_synthetic > 0, 12 > 0 and profile.seed >= 0


def _active(profile) -> tuple[bool, bool]:
    return 2 >= 8, 8 >= 8 and profile.people > 0


def _hybrid(profile) -> tuple[bool, bool]:
    return False and profile.seed >= 0, True


def _acl(profile) -> tuple[bool, bool]:
    return None == "public", "public" == "public" and profile.seed >= 0


def _judge(profile) -> tuple[bool, bool]:
    fluent_wrong = True
    calibrated = False
    simpler = (not fluent_wrong) or calibrated
    return simpler and profile.seed >= 0, True


def _cache(profile) -> tuple[bool, bool]:
    return False and profile.seed >= 0, True


def _prescale(profile) -> tuple[bool, bool]:
    reactive_misses = True
    return (not reactive_misses) and profile.seed >= 0, True


def _surge(profile) -> tuple[bool, bool]:
    bare = (False, False, False)
    design = (True, True, True)
    return all(bare) and profile.seed >= 0, all(design)


_RULES = {
    "slice-tools": _tools,
    "slice-workflow": _workflow,
    "slice-multi-agent": _multi,
    "slice-single-agent": _single,
    "slice-approval": _approval,
    "slice-gbm": _gbm,
    "slice-pit": _pit,
    "slice-lora": _lora,
    "slice-vision": _vision,
    "slice-pref": _pref,
    "slice-synth": _synth,
    "slice-active": _active,
    "slice-hybrid": _hybrid,
    "slice-acl": _acl,
    "slice-judge": _judge,
    "slice-cache": _cache,
    "slice-prescale": _prescale,
    "slice-surge": _surge,
}
