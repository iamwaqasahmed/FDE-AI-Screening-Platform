# The endpoint

Point the router at `ep-local-small` for `local-small` on `zone-private`. Select the credential by environment. Prod does not read the dev file.

The architect copies [templates/zones.md](templates/zones.md) to `work/zones.md` and maps the URL onto `zone-private`. The surface cell is `url`.

The product manager copies [templates/operators.md](templates/operators.md) to `work/operators.md` and writes the steps to read the health probe with the prod credential.

Copy [templates/deployment.md](templates/deployment.md) to `work/deployment.md`. Fill URL, Zone, Probe, Credentials, Monitoring, Boundary, and Operator steps. Cite `ciso` or a file in the pack. Monitoring at this stage is request rate, error rate, and model latency. The rest waits until Week 4. A clinician assigns urgency. PHI stays off `ext-large`.

Four readings are advanced. They are not in today's check.

- Image provenance, in `work/provenance.md`.
- Resource limits, in `work/limits.md`.
- Rollback to the previous registered hash, in `work/rollback.md`.
- A request over the quota waits, in `work/quota.md`. It does not spill onto `ext-large`.
