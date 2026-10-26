"""itsm. The cause of a feed gap sits in a ticket, among routine tickets. Ramadan week is a freeze.

fault() returns that hidden-cause defect. The affected keys are the feed-gap ticket and the freeze. The clean columns are the ticket id and the cause id.
"""

from alwaha.systems.record import record


def fault(_profile) -> dict:
    """Return the ticket-system fault record.

    The profile is unused because this defect does not change with the seed.
    """
    return record(
        "itsm",
        "cause-in-ticket",
        ["ticket:feed-gap", "freeze:ramadan"],
        ["ticket_id", "cause_id"],
    )
