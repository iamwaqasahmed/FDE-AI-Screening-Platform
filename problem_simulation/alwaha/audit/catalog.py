"""Foundation and advanced checks, pointed at each day's filled work copy.

Each job is a check name, a release id, and the work directory that check reads. An empty release id means the checker supplies its own default. The same check name can appear on more than one day, with a different release id and a different directory.
"""

from __future__ import annotations

from alwaha import paths

M01_L01 = paths.M01_L01_WORK


def jobs() -> list[tuple[str, str, object]]:
    """Return the check name, release id, and work directory for every readiness job."""
    return [
        # Module 1. An empty release id means the checker supplies its own default.
        ("repo", "", M01_L01),
        ("interview", "", M01_L01),
        ("approach", "", paths.M01_L02_WORK),
        ("brief", "", paths.M01_L02_WORK),
        ("events", "", paths.M01_L03_WORK),
        ("agent", "", paths.M01_L04_WORK),
        ("trajectory", "", paths.M01_L04_WORK),
        ("agent", "rel-m01-l05", paths.M01_L05_WORK),
        ("trajectory", "rel-m01-l05", paths.M01_L05_WORK),
        ("design", "", paths.M01_L05_WORK),
        ("readout", "", paths.M01_L05_WORK),
        ("individual", "", paths.M01_L05_WORK),
        # Module 2. The same check name can point at a later day with a new release id.
        ("auth", "rel-m02-l01", paths.M02_L01_WORK),
        ("journey", "rel-m02-l01", paths.M02_L01_WORK),
        ("journey", "rel-m02-l02", paths.M02_L02_WORK),
        ("tests", "rel-m02-l03", paths.M02_L03_WORK),
        ("ux", "rel-m02-l03", paths.M02_L03_WORK),
        ("deploy", "rel-m02-l04", paths.M02_L04_WORK),
        ("deploy", "rel-m02-l05", paths.M02_L05_WORK),
        ("journey", "rel-m02-l05", paths.M02_L05_WORK),
        ("readout", "rel-m02-l05", paths.M02_L05_WORK),
        ("individual", "rel-m02-l05", paths.M02_L05_WORK),
        # Module 2, from the identity work through the module readout.
        ("identity", "rel-m03-l01", paths.M03_L01_WORK),
        ("labels", "rel-m03-l01", paths.M03_L01_WORK),
        ("synthetic", "rel-m03-l01", paths.M03_L01_WORK),
        ("model", "rel-m03-l02", paths.M03_L02_WORK),
        ("lora", "rel-m03-l02", paths.M03_L02_WORK),
        ("rag", "rel-m03-l03", paths.M03_L03_WORK),
        ("hybrid", "rel-m03-l03", paths.M03_L03_WORK),
        ("acl", "rel-m03-l03", paths.M03_L03_WORK),
        ("eval", "rel-m03-l04", paths.M03_L04_WORK),
        ("judge", "rel-m03-l04", paths.M03_L04_WORK),
        ("eval", "rel-m03-l05", paths.M03_L05_WORK),
        ("rcp", "rel-m03-l05", paths.M03_L05_WORK),
        ("readout", "rel-m03-l05", paths.M03_L05_WORK),
        ("individual", "rel-m03-l05", paths.M03_L05_WORK),
        # Module 2, from the red-team work through the final readout.
        ("redteam", "rel-m04-l01", paths.M04_L01_WORK),
        ("privacy", "rel-m04-l01", paths.M04_L01_WORK),
        ("access", "rel-m04-l01", paths.M04_L01_WORK),
        ("fair", "rel-m04-l01", paths.M04_L01_WORK),
        ("incident", "rel-m04-l02", paths.M04_L02_WORK),
        ("cache", "rel-m04-l02", paths.M04_L02_WORK),
        ("slo", "rel-m04-l03", paths.M04_L03_WORK),
        ("surge", "rel-m04-l03", paths.M04_L03_WORK),
        ("slo", "rel-m04-l04", paths.M04_L04_WORK),
        ("integrate", "rel-m04-l05", paths.M04_L05_WORK),
        ("ops", "rel-m04-l05", paths.M04_L05_WORK),
        ("rcp", "rel-m04-l05", paths.M04_L05_WORK),
        ("readout", "rel-m04-l05", paths.M04_L05_WORK),
        ("individual", "rel-m04-l05", paths.M04_L05_WORK),
    ]
