"""Comparisons for answers a person wrote."""

from __future__ import annotations

from course.checks.rules import close, same_set


def same(answer, expected) -> bool:
    if isinstance(expected, dict):
        return isinstance(answer, dict) and all(key in answer and same(answer[key], expected[key]) for key in expected)
    if isinstance(expected, list):
        return same_set(answer if isinstance(answer, list) else [], expected)
    if isinstance(expected, bool):
        return answer is expected
    return answer == expected


def near(answer, expected, tolerance: float) -> bool:
    return close(answer, expected, tolerance, relative=False)
