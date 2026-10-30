"""Put the blocked problem first.

This is the starter. It ignores the rows and always returns
p-triage. That problem still has a blocker, so it cannot open.
The finished module walks the rows and returns the first id
whose blocker list is empty.
"""


def first(rows: list) -> str:
    """Ignore the model and return the blocked problem.

    The rows are discarded. The caller always hears the same id.
    """
    # The argument is unused. Order and blockers are not read.
    del rows
    return "p-triage"
