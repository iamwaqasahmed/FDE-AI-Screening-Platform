# 04 — Words

Read this page once. You will look back at it while you replace the shell. You do not need to memorize it. You do not paste anything on this page, and you do not run a command. When a later chapter uses a word, come back to that row. Then go to [chapter 05](05-the-sprint.md).

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself. This page does not type a hash, a token, or the quota number. Those values stay in the files [chapter 03](03-the-standard.md) already opened.

## The service

| Word | Meaning |
| --- | --- |
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population. This client is the Al-Waha Health Cluster |
| Patient access | Referrals, appointments, reminders, and the phone line. The assistant you are building sits on that service |
| Referral | A request from a local clinic for a hospital appointment. Booking that appointment from chat waits |
| Patient | The person the referral is about |
| Phone line | The way most families still reach the cluster |
| Chief Information Security Officer | [Omar Al-Zahrani](packet/kickoff/personas/ciso.md). His id is `ciso`. Today's drop is from him. You do not interview him today |
| Private cloud | The cluster's own cloud. [zones.md](packet/kickoff/world/zones.md) calls it `zone-private`. Site-a and site-b sit there |
| Public cloud | The zone named `zone-public`. `ext-large` sits there |
| `zone-hospital` | The hospital data centers. Not today's URL |
| URL | `https://assistant.site-a.alwaha.internal`. [guide.md](packet/release/endpoint/guide.md) states it. Chapter 09 copies that address onto the deployment note |
| Namespace | The team folder for the manifest. The guide names it `ns-team` |
| `ep-local-small` | The private endpoint id. The router returns this id |
| `local-small` | The model that serves the assistant, in `zone-private` |
| `ext-large` | The external model. Patient data stays off it. The shell router still points there |
| `local-embed` | Another approved model on the register. The probe does not select it |
| `local-smallx` | The near name in [candidate.json](packet/release/fixtures/candidate.json). Status `unregistered`. Not a registration |

## The register and the credentials

| Word | Meaning |
| --- | --- |
| Register | [models.json](packet/release/registry/models.json). Each row has `hash`, `id`, `status`, and `zone`. The `local-small` rows also have `prompt` |
| Hash | The `hash` field on a register row. The probe reports the hash from the approved `local-small` row. You read it from the file. You do not type it |
| Approved | `status` `approved`. The probe uses this row for `local-small` |
| Previous | `status` `previous` on the other `local-small` row. A rollback changes the served hash to that row. The probe does not report it today |
| Prompt | `p1` on the approved row. `p0` on the previous row. The probe reports the approved prompt |
| Candidate | The unregistered near name. The shell probe reports its hash. The filled probe does not |
| Credential | The `endpoint` field in a credential file. [dev.json](packet/release/credentials/dev.json) and [prod.json](packet/release/credentials/prod.json) each have `endpoint`, `env`, and `registry` |
| Dev | The dev environment. Its credential file is `credentials/dev.json` |
| Prod | The prod environment. Its credential file is `credentials/prod.json`. Prod does not read the dev file |
| Quota | The `requests` field in [quota.json](packet/release/registry/quota.json). Read the number there. This page does not type it. A request over that count waits. It does not spill onto `ext-large` |
| Health probe | `GET /v1/health`. [health.yaml](packet/release/openapi/health.yaml) names the call `readHealth`. The body reports the registered hash, the prompt version, and the endpoint dependency |
| National id | An identifier that must not remain on a deploy log line. [log.json](packet/release/fixtures/log.json) carries one, and then a watermark. You do not copy that file |
| Watermark | The mark on the deploy log. The check message does not print it. A copy of `log.json` in `work/` fails the check |

## The image and the pipeline

| Word | Meaning |
| --- | --- |
| Image | The packaged program a Dockerfile builds. Week 1 Day 1 left a Dockerfile in the folder and did not build it. Today you still do not start a cluster. You change the account that image would run as |
| Container | One running copy of that image. [pol-deploy.md](packet/release/standards/pol-deploy.md) rejects a container whose account is root |
| Root | The account in [root.json](packet/release/fixtures/root.json). The shell image still uses it. The filled image does not |
| Non-root | The container user is not root. `pol-deploy` names this check. The deployment note uses this word |
| `USER 1000` | The last account line on the filled Dockerfile. `1000` is not root |
| Admission | [admit.py](packet/app/admit.py) decides whether an image is accepted. The shell accepts every image. The filled copy rejects root and a logged national id |
| Manifest | [deployment.yaml](packet/deploy/deployment.yaml). The shell has no team namespace and no health probe. The filled copy sets `ns-team`, refuses a root account, and calls `/v1/health` |
| Readiness | The probe the manifest calls before traffic arrives. The path is `/v1/health` |
| CI | The workflow. The packet copy in [ci.yml](packet/.github/workflows/ci.yml) does not run the suite. Chapter 08 adds that step on the work copy only |
| Suite | The tests under `work/tests`, together with the four app files they call |
| Shell | The starter copy in `packet/`. It still accepts root, still reports the candidate hash, still routes to `ext-large`, and still reads the dev credential for prod |
| `practice` | The shared classroom world. The build in chapter 01 uses it |
| `rel-w2d4` | Today's file drop |

## The pages

| Word | Meaning |
| --- | --- |
| Sprint | The order of the work. The deploy comes before the readout |
| Readout | The meeting booked after the deploy. It is the Later line of the sprint. It is not the steering page from Week 1 Day 5. You do not open that file today |
| Deployment note | [deployment.md](work/deployment.md). The headings are URL, Zone, Probe, Credentials, Monitoring, Boundary, and Operator steps |
| Zone row | [zones.md](work/zones.md). The columns are `surface` and `zone`. The surface cell is `url` |
| Operator steps | How someone reads the health probe with the prod credential |
| Monitoring | Request rate, error rate, and model latency. The rest of the operations stack waits until Week 4 |
| Boundary | A clinician assigns clinical urgency. Patient data stays off `ext-large` |
| Clinician | The person who assigns clinical urgency. The assistant does not |
| `pol-deploy` | The checklist id. Chapter 09 cites it |
| Citation | A source the deployment note names. `endpoint/guide.md` is one. `ciso` is another |
| Rollback | A change of the served model hash back to the previous registered hash. It does not rewrite patient records. The check does not read a rollback page. Chapter 10 answers what a rollback changes |
| Provenance | A label on the image. The check does not read a provenance page |
| Limits | Cpu and memory on the manifest. The check does not read a limits page |
| Quota note | A page about waiting when the request count is over the quota. The check does not read it |

## What the check will see

| Piece | What you should see |
| --- | --- |
| Probe | The approved `local-small` hash and prompt, with `endpoint` in the dependencies |
| Image | `USER 1000` on the Dockerfile. Root is rejected by admission |
| Log | The national id is removed from the emitted line. `log.json` stays in the pack |
| Credentials | Prod reads `prod.json`. Dev reads `dev.json` |
| Router | `ep-local-small`, `local-small`, and `zone-private` |
| Manifest | Namespace `ns-team`, a readiness call to `/v1/health`, and a non-root account flag |
| Pipeline | The work workflow runs `unittest` on `tests` |
| Demo | `root image: rejected`, then `registered image: accepted` |
| Pages | The URL on `zone-private`. The deploy before the readout. Monitoring names Week 4. A clinician assigns urgency |

The hash, the two credentials, and the quota number stay in the pack files. This page does not store them.

## A plain reading

On Week 1 Day 1 the folder held a Dockerfile. That file was the shape of a later deploy. You did not build it. Today is that later deploy, as files the check can read. You still do not start a cluster, and you do not apply the manifest to a live namespace.

An image is the packaged program that Dockerfile would build. A container is one running copy of the image. The shell image uses the root account. The filled image ends on `USER 1000`. Admission rejects root. The manifest tells the namespace to call `/v1/health` before it sends traffic.

On Week 2 Day 1 the stand-in health body put the model id `local-small` in a field named `model_hash`. Today's register keeps the id and the hash as two fields. The probe reports the hash from the approved `local-small` row. The previous `local-small` row stays on the register. A rollback would serve that previous hash. It would not rewrite patient records. The probe does not report the previous row today.

Readout on this page is a meeting you book after the deploy. It is the sprint's Later line. It is not the steering page you wrote on Week 1 Day 5.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
