"""Pure lookups over the student extract bundle."""

from __future__ import annotations

_SITES = ("cascade-seattle", "cedar-ridge", "fraser-burnaby", "other")
_NAMED_SITES = _SITES[:-1]
_FEED_KINDS = ("nightly_file", "event")


def by_ref(bundle: dict, ref: str) -> dict:
    """Return rows whose ref, stream ref, or payload.ref equals ref."""
    hits = [
        {"extract": name, "row": row}
        for name, body in bundle.items()
        for row in _rows(body)
        if _matches(row, ref)
    ]
    return {"ref": ref, "hits": hits}


def site_feeds(hospital_rows: list[dict]) -> dict:
    """Place each nightly file and event under exactly one site key."""
    feeds = {site: [] for site in _SITES}
    for row in hospital_rows:
        if isinstance(row, dict) and row.get("kind") in _FEED_KINDS:
            feeds[_site_key(row)].append(row)
    return feeds


def _rows(body: object):
    if isinstance(body, list):
        yield from _list_rows(body)
        return
    if isinstance(body, dict):
        yield from _dict_rows(body)


def _list_rows(items: list):
    for item in items:
        if isinstance(item, dict):
            yield item


def _dict_rows(obj: dict):
    yield obj
    for key, value in obj.items():
        if key == "payload":
            continue
        if isinstance(value, list):
            yield from _list_rows(value)
        elif isinstance(value, dict):
            yield from _dict_rows(value)


def _matches(row: dict, ref: str) -> bool:
    if row.get("ref") == ref or _stream_hit(row, ref):
        return True
    payload = row.get("payload")
    return isinstance(payload, dict) and payload.get("ref") == ref


def _stream_hit(row: dict, ref: str) -> bool:
    if row.get("stream_id") == ref or row.get("stream_ref") == ref:
        return True
    stream = row.get("stream")
    if stream == ref:
        return True
    return isinstance(stream, dict) and stream.get("ref") == ref


def _site_key(row: dict) -> str:
    site = _site_text(_payload_site(row))
    if site is None:
        site = _site_text(row.get("site"))
    if site in _NAMED_SITES:
        return site
    return "other"


def _payload_site(row: dict):
    payload = row.get("payload")
    if isinstance(payload, dict):
        return payload.get("site")
    return None


def _site_text(value: object) -> str | None:
    if isinstance(value, str) and value:
        return value
    return None
