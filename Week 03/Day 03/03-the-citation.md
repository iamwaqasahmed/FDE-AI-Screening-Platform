# The citation

A document binds only when its status is `in_force`, the case date sits inside the effective window, and the site is cluster-wide or matches. A draft stays searchable. A draft is not citable. An unauthorized document is not citable.

The shell filter keeps every audience, so a patient can be shown a staff leaflet. The shell bind restarts an in-flight referral on v4 and treats every v4 as in force, including a specialty the notice does not name. The shell cite returns the nearest chunk. The shell sync rebuilds the snapshot and ignores `document.changed`.

The copy filters by status, date, site, and audience. A patient sees `public`. Staff see `public` and `staff`. `restricted` stays off both of those paths. An in-flight referral keeps the criteria version it started on. v4 is `endo`, `ophth`, and `card` only. When nothing binds, the answer refuses.

The product manager copies [templates/refusal.md](templates/refusal.md) to `work/refusal.md`. One sentence for no document in force. One sentence for a document the asker cannot see.

The architect copies [templates/audience.md](templates/audience.md) to `work/audience.md` and fills the three rows.

`vision.py` reads the transcription in [photos/prep.json](../../data/rel-w3d3/photos/prep.json). The export omits the clause. `conflict.py` names the cluster window and the `h-safra` window, and the cluster window wins. `catalog.py` answers from [catalog/service-catalog.json](../../data/rel-w3d3/catalog/service-catalog.json), not from a leaflet. Those three are the advanced path. The three checks do not require them.
