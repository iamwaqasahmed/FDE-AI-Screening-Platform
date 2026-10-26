"""Place every replica behind the balancer.

placed reads the sites list and returns every id,
sorted. Only the id is used. A missing sites list
returns an empty list.
"""


def placed(sites: dict) -> list[str]:
    """Return every site id, sorted.

    A missing sites list places nothing.
    """
    # Every id is placed. The list is sorted.
    return sorted(str(row["id"]) for row in sites.get("sites") or [])
