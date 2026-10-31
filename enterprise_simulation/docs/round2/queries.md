# Query helpers

`by_ref` and `site_feeds` read extract rows. Each call returns a new collection and leaves its inputs unchanged.

## by_ref

`by_ref(bundle, ref)` takes the extract map. A name points at a list of row objects, or at one object.

A list contributes each object in order. Objects nested inside that row stay on the row, and `payload.ref` is read there. An object extract is itself a candidate row. Lists on that object are walked the same way. Nested objects other than `payload` are walked the same way, so a grouped extract still yields the rows inside it. Bundle key order is preserved.

A row is a hit when `ref` equals any of these:

- the row's `ref`
- the stream ref: `stream_id`, `stream_ref`, a string `stream`, or `stream.ref` when `stream` is an object
- `payload.ref`

A row that has no top-level `ref` stays in the walk. That missing field is skipped, and the stream ref and `payload.ref` are still compared. A row that matches none of the three is omitted from `hits`.

The result is `{"ref": ref, "hits": [{"extract": name, "row": row}, ...]}`. Each `row` is the original object.

## site_feeds

`site_feeds(hospital_rows)` keeps rows whose `kind` is `nightly_file` or `event`.

Each kept row is appended to one list. The keys, always present, are `cascade-seattle`, `cedar-ridge`, `fraser-burnaby`, and `other`.

The site is `payload.site` when that value is a non-empty string. Otherwise it is `row.site`. One of the three named sites becomes the key. Any other string, and a missing site, uses `other`.

When `payload.site` and `row.site` differ, the payload site is the only destination. Order inside a key follows the input list.
