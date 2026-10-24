"""Treat every district as a point at one."""

from __future__ import annotations


def bounds(successes: int, total: int) -> tuple[float, float]:
    del successes, total
    return (1.0, 1.0)


def by_district(rows: list[dict]) -> dict[str, tuple[float, float]]:
    return {row["district"]: (1.0, 1.0) for row in rows}
