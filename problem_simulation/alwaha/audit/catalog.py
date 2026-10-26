"""Foundation and advanced checks, pointed at each day's filled work copy.

Each job is a check name, a release id, and the work directory that check reads. An empty release id means the checker supplies its own default. The same check name can appear on more than one day, with a different release id and a different directory.
"""

from __future__ import annotations

from alwaha import paths

DAY1 = paths.DAY1_WORK


def jobs() -> list[tuple[str, str, object]]:
    """Return the check name, release id, and work directory for every readiness job."""
    return [
        ("repo", "", DAY1),
        ("interview", "", DAY1),
        ("approach", "", paths.DAY2_WORK),
        ("brief", "", paths.DAY2_WORK),
        ("events", "", paths.DAY3_WORK),
        ("agent", "", paths.DAY4_WORK),
        ("trajectory", "", paths.DAY4_WORK),
        ("agent", "rel-w1d5", paths.DAY5_WORK),
        ("trajectory", "rel-w1d5", paths.DAY5_WORK),
        ("design", "", paths.DAY5_WORK),
        ("readout", "", paths.DAY5_WORK),
        ("individual", "", paths.DAY5_WORK),
        ("auth", "rel-w2d1", paths.W2D1_WORK),
        ("journey", "rel-w2d1", paths.W2D1_WORK),
        ("journey", "rel-w2d2", paths.W2D2_WORK),
        ("tests", "rel-w2d3", paths.W2D3_WORK),
        ("ux", "rel-w2d3", paths.W2D3_WORK),
        ("deploy", "rel-w2d4", paths.W2D4_WORK),
        ("deploy", "rel-w2d5", paths.W2D5_WORK),
        ("journey", "rel-w2d5", paths.W2D5_WORK),
        ("readout", "rel-w2d5", paths.W2D5_WORK),
        ("individual", "rel-w2d5", paths.W2D5_WORK),
        ("identity", "rel-w3d1", paths.W3D1_WORK),
        ("labels", "rel-w3d1", paths.W3D1_WORK),
        ("synthetic", "rel-w3d1", paths.W3D1_WORK),
        ("model", "rel-w3d2", paths.W3D2_WORK),
        ("lora", "rel-w3d2", paths.W3D2_WORK),
        ("rag", "rel-w3d3", paths.W3D3_WORK),
        ("hybrid", "rel-w3d3", paths.W3D3_WORK),
        ("acl", "rel-w3d3", paths.W3D3_WORK),
        ("eval", "rel-w3d4", paths.W3D4_WORK),
        ("judge", "rel-w3d4", paths.W3D4_WORK),
        ("eval", "rel-w3d5", paths.W3D5_WORK),
        ("rcp", "rel-w3d5", paths.W3D5_WORK),
        ("readout", "rel-w3d5", paths.W3D5_WORK),
        ("individual", "rel-w3d5", paths.W3D5_WORK),
        ("redteam", "rel-w4d1", paths.W4D1_WORK),
        ("privacy", "rel-w4d1", paths.W4D1_WORK),
        ("access", "rel-w4d1", paths.W4D1_WORK),
        ("fair", "rel-w4d1", paths.W4D1_WORK),
        ("incident", "rel-w4d2", paths.W4D2_WORK),
        ("cache", "rel-w4d2", paths.W4D2_WORK),
        ("slo", "rel-w4d3", paths.W4D3_WORK),
        ("surge", "rel-w4d3", paths.W4D3_WORK),
        ("slo", "rel-w4d4", paths.W4D4_WORK),
        ("integrate", "rel-w4d5", paths.W4D5_WORK),
        ("ops", "rel-w4d5", paths.W4D5_WORK),
        ("rcp", "rel-w4d5", paths.W4D5_WORK),
        ("readout", "rel-w4d5", paths.W4D5_WORK),
        ("individual", "rel-w4d5", paths.W4D5_WORK),
    ]
