"""Foundation and advanced checks, pointed at each day's filled work copy."""

from __future__ import annotations

from alwaha import paths

DAY1 = paths.DAY1_WORK


def jobs() -> list[tuple[str, str, object]]:
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
        ("deploy", "rel-w2d4", paths.W2D4_ROOT / "work"),
        ("deploy", "rel-w2d5", paths.W2D5_ROOT / "work"),
        ("journey", "rel-w2d5", paths.W2D5_ROOT / "work"),
        ("readout", "rel-w2d5", paths.W2D5_ROOT / "work"),
        ("individual", "rel-w2d5", paths.W2D5_ROOT / "work"),
        ("identity", "rel-w3d1", paths.W3D1_ROOT / "work"),
        ("labels", "rel-w3d1", paths.W3D1_ROOT / "work"),
        ("synthetic", "rel-w3d1", paths.W3D1_ROOT / "work"),
        ("model", "rel-w3d2", paths.W3D2_ROOT / "work"),
        ("lora", "rel-w3d2", paths.W3D2_ROOT / "work"),
        ("rag", "rel-w3d3", paths.W3D3_ROOT / "work"),
        ("hybrid", "rel-w3d3", paths.W3D3_ROOT / "work"),
        ("acl", "rel-w3d3", paths.W3D3_ROOT / "work"),
        ("eval", "rel-w3d4", paths.W3D4_ROOT / "work"),
        ("judge", "rel-w3d4", paths.W3D4_ROOT / "work"),
        ("eval", "rel-w3d5", paths.W3D5_ROOT / "work"),
        ("rcp", "rel-w3d5", paths.W3D5_ROOT / "work"),
        ("readout", "rel-w3d5", paths.W3D5_ROOT / "work"),
        ("individual", "rel-w3d5", paths.W3D5_ROOT / "work"),
        ("redteam", "rel-w4d1", paths.W4D1_ROOT / "work"),
        ("privacy", "rel-w4d1", paths.W4D1_ROOT / "work"),
        ("access", "rel-w4d1", paths.W4D1_ROOT / "work"),
        ("fair", "rel-w4d1", paths.W4D1_ROOT / "work"),
        ("incident", "rel-w4d2", paths.W4D2_ROOT / "work"),
        ("cache", "rel-w4d2", paths.W4D2_ROOT / "work"),
        ("slo", "rel-w4d3", paths.W4D3_ROOT / "work"),
        ("surge", "rel-w4d3", paths.W4D3_ROOT / "work"),
        ("slo", "rel-w4d4", paths.W4D4_ROOT / "work"),
        ("integrate", "rel-w4d5", paths.W4D5_ROOT / "work"),
        ("ops", "rel-w4d5", paths.W4D5_ROOT / "work"),
        ("rcp", "rel-w4d5", paths.W4D5_ROOT / "work"),
        ("readout", "rel-w4d5", paths.W4D5_ROOT / "work"),
        ("individual", "rel-w4d5", paths.W4D5_ROOT / "work"),
    ]
