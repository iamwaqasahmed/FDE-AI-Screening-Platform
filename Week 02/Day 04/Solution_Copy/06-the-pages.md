# 06 — The pages

Open the finished [zones.md](work/zones.md), [operators.md](work/operators.md), and [deployment.md](work/deployment.md) and put them beside yours.

[zones.md](sources/kickoff/world/zones.md) names `zone-private` as the private cloud, site-a and site-b. [guide.md](sources/release/endpoint/guide.md) puts the URL `https://assistant.site-a.alwaha.internal` in that zone, on model `local-small`. The zone table has columns `surface` and `zone`. The row is `url` and `zone-private`. The pipes stay. While the blank table is the file that runs, the check says `the url is not in zone-private`.

[operators.md](work/operators.md) says to read the health probe with the prod credential. While the blank steps are the file that runs, the check says `the operator steps are missing`.

[deployment.md](work/deployment.md) has the headings URL, Zone, Probe, Credentials, Monitoring, Boundary, and Operator steps. It cites `ciso` and `endpoint/guide.md`, and it names `pol-deploy`. The probe section says `GET /v1/health` reports the registered hash for `local-small`, and that the container user is `non-root`. It does not say the container runs as root. `admit.py` may still contain `root` on the line that rejects that account. That line is the rejection. It is not a claim on this page.

Credentials say dev and prod differ, and each stays in its own file. Monitoring names request rate, error rate, and model latency, and it says the rest waits until Week 4. [starter.md](sources/release/dashboard/starter.md) is that list. Boundary says a clinician assigns clinical urgency, and PHI stays off `ext-large`. [endpoint.yaml](sources/release/openapi/endpoint.yaml) says a request over the quota waits and does not spill onto `ext-large`. The quota number stays in [quota.json](sources/release/registry/quota.json). This page does not type it.

While the blank note is the file that runs, the check says the deployment note does not leave urgency with a clinician, does not keep patient data off the external model, is missing a required fact, and does not cite a source. The missing-fact message does not name the fact. A page that says the container runs as root fails with `the deployment note contains a banned sentence`.

[provenance.md](work/provenance.md), [limits.md](work/limits.md), [rollback.md](work/rollback.md), and [quota.md](work/quota.md) are in this folder. The check does not read them. [pol-deploy.md](sources/release/standards/pol-deploy.md) still lists provenance and resource limits. The manifest in chapter 04 already sets the cpu and memory limits. The check looks for the namespace, the probe, and the non-root flag. It does not grade those two notes.

Next: [07 — Knowledge](07-knowledge.md).
