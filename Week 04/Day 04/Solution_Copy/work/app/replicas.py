"""Place every replica behind the balancer."""


def placed(sites: dict) -> list[str]:
    return sorted(str(row["id"]) for row in sites.get("sites") or [])
