"""itsm. The cause of a feed gap sits in a ticket, among routine tickets. Ramadan week is a freeze."""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    return record(
        "itsm",
        "cause-in-ticket",
        ["ticket:feed-gap", "freeze:ramadan"],
        ["ticket_id", "cause_id"],
    )
