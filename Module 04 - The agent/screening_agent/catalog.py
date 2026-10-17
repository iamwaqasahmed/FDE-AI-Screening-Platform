"""The only functions the model is allowed to call."""

from __future__ import annotations

from screening_retrieval.retrieve import retrieve
from screening_tools import (
    coverage,
    grader_queue,
    letter_fields,
    letter_timing,
    unfinished_photos,
    urgent_wait,
    vendor_pilot,
)

CATALOG = [
    {
        "name": "coverage",
        "description": "Who is eligible, and who has a completed screen. Optional district.",
        "parameters": {
            "type": "object",
            "properties": {"district": {"type": "string"}},
        },
    },
    {
        "name": "unfinished_photos",
        "description": "How many people have a photo and no result code.",
        "parameters": {"type": "object", "properties": {}},
    },
    {
        "name": "grader_queue",
        "description": "Counts for unfinished, unreadable, mild referable, and sight-threatening piles.",
        "parameters": {"type": "object", "properties": {}},
    },
    {
        "name": "urgent_wait",
        "description": "Median days from an urgent result to a specialist visit. The 14-day rule is a draft.",
        "parameters": {"type": "object", "properties": {}},
    },
    {
        "name": "letter_timing",
        "description": "Median days from photo to letter for completed screens that have a letter.",
        "parameters": {"type": "object", "properties": {}},
    },
    {
        "name": "vendor_pilot",
        "description": "Empty model labels and disagreements on the pilot file.",
        "parameters": {"type": "object", "properties": {}},
    },
    {
        "name": "letter_fields",
        "description": "Fields one letter may contain. Does not write a diagnosis or a referral.",
        "parameters": {
            "type": "object",
            "properties": {"local_pid": {"type": "string"}},
            "required": ["local_pid"],
        },
    },
    {
        "name": "retrieve",
        "description": "Which written rule applies, and whether that document is in force or a draft.",
        "parameters": {
            "type": "object",
            "properties": {"question": {"type": "string"}},
            "required": ["question"],
        },
    },
]

_CALLS = {
    "coverage": lambda arguments: coverage(district=arguments.get("district") or None),
    "unfinished_photos": lambda arguments: unfinished_photos(),
    "grader_queue": lambda arguments: grader_queue(),
    "urgent_wait": lambda arguments: urgent_wait(),
    "letter_timing": lambda arguments: letter_timing(),
    "vendor_pilot": lambda arguments: vendor_pilot(),
    "letter_fields": lambda arguments: letter_fields(arguments["local_pid"]),
    "retrieve": lambda arguments: retrieve(arguments.get("question") or ""),
}


def openai_tools() -> list[dict]:
    return [
        {
            "type": "function",
            "function": {
                "name": spec["name"],
                "description": spec["description"],
                "parameters": spec["parameters"],
            },
        }
        for spec in CATALOG
    ]


def call_tool(name: str, arguments: dict) -> dict:
    if name not in _CALLS:
        raise KeyError(name)
    return _CALLS[name](arguments or {})
