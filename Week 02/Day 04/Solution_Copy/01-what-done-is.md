# 01 — What done is

This page is the map. The day is finished by the sprint, the admission code, the probe, the router, the credentials, the four tests, the image, the manifest, the work pipeline, the deployment note, the zone row, the operator steps, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | The deploy comes first. The readout is later. Explained in [chapter 02](02-the-sprint.md) |
| [app/admit.py](work/app/admit.py) | Rejects root and drops a national id from the log. Explained in [chapter 03](03-the-image.md) |
| [app/health.py](work/app/health.py) | Reports the approved `local-small` hash. Explained in [chapter 04](04-the-probe.md) |
| [app/router.py](work/app/router.py) | Stays on `ep-local-small` in `zone-private`. Explained in [chapter 05](05-the-endpoint.md) |
| [app/secrets.py](work/app/secrets.py) | Prod reads the prod credential file. Explained in chapter 05 |
| [tests/test_admit.py](work/tests/test_admit.py) | Root and `0` are rejected. A clean account is accepted. The stand-in id leaves the line |
| [tests/test_health.py](work/tests/test_health.py) | The approved row wins over the previous row and over the candidate |
| [tests/test_router.py](work/tests/test_router.py) | Prod and dev both use the private endpoint |
| [tests/test_secrets.py](work/tests/test_secrets.py) | The two stand-in credentials stay apart |
| [deploy/Dockerfile](work/deploy/Dockerfile) | The last account line is `USER 1000`. Explained in chapter 03 |
| [deploy/deployment.yaml](work/deploy/deployment.yaml) | Namespace `ns-team`, a non-root account flag, and readiness on `/v1/health`. Explained in chapter 04 |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | Runs the suite. The packet copy does not. Explained in chapter 05 |
| [deployment.md](work/deployment.md) | The URL, the zone, the probe, the credentials, monitoring, the boundary, and the operator steps. Explained in [chapter 06](06-the-pages.md) |
| [zones.md](work/zones.md) | The surface `url` is in `zone-private` |
| [operators.md](work/operators.md) | Read the health probe with the prod credential |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 07](07-knowledge.md) |
| [provenance.md](work/provenance.md) | A later reading. The check does not read this file |
| [limits.md](work/limits.md) | A later reading. The check does not read this file |
| [rollback.md](work/rollback.md) | A later reading. The check does not read this file |
| [quota.md](work/quota.md) | A later reading. The check does not read this file |
| [ciso.notes.md](work/interviews/ciso.notes.md) | What the security officer says. The check does not read it |

The check prints `passed` when the probe reports the approved hash and prompt with the endpoint dependency, root and a logged national id are rejected, a clean account is accepted, prod and dev read different credential files, the router names the private endpoint, the image account is not root, the manifest is in the team namespace with a health probe and a non-root flag, the workflow runs the suite, the deployment note carries the required facts and a citation, urgency stays with a clinician, patient data stays off `ext-large`, the zone row is present, the operator steps name health and prod, the sprint puts the deploy before the readout, and both knowledge answers are present.

The deploy log is not in this folder. A copy of it here would fail the check. The message does not print the watermark.

Next: [02 — The sprint](02-the-sprint.md).
