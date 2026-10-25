# 04 — The probe

Open the finished [health.py](work/app/health.py), [test_health.py](work/tests/test_health.py), and [deployment.yaml](work/deploy/deployment.yaml) and put them beside yours.

[models.json](sources/release/registry/models.json) has two `local-small` rows. The approved row carries prompt `p1`. The previous row carries prompt `p0`. `ext-large` is approved on `zone-public`. `local-embed` is approved on `zone-private`. The function keeps the row whose id is `local-small` and whose status is `approved`. It reports that hash and that prompt, and it lists `endpoint` in the dependencies.

`candidate` stays on the function line. The body does not read it. [candidate.json](sources/release/fixtures/candidate.json) is the near name `local-smallx`, status `unregistered`. That hash is not a registration.

The test stand-ins are `sha256:old`, `sha256:good`, and `sha256:near`. They are not the hashes in the register file. The previous stand-in comes first and is skipped. The approved stand-in is the one the body reports.

[guide.md](sources/release/endpoint/guide.md) names the namespace `ns-team` and the call `GET /v1/health`. The manifest sets that namespace, sets `runAsNonRoot`, and points readiness at `/v1/health`. Cpu and memory limits are set. [pol-deploy.md](sources/release/standards/pol-deploy.md) lists those checks. The image name `patient-access-assistant` stays. That is expected.

The shell probe returns `candidate["hash"]` and an empty dependency list. The shell manifest has no namespace line and no probe. While that shell is the file that runs, the check says `the health probe does not report the registered hash`, `the manifest is not in the team namespace`, `the health probe is missing`, and `the image runs as root`. The hash message does not name the hash.

Next: [05 — The endpoint](05-the-endpoint.md).
