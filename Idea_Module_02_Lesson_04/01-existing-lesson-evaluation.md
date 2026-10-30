# 01 — Existing lesson evaluation

Lesson: Module 02 Lesson 04, release `rel-m02-l04`, check `chk-deploy`. Sources read: student chapters `00`–`10`, solution chapters and `work/`, `course_design/module-02.md`, `course_design/slides/module-02-lesson-04.md`, the curriculum map, `problem_simulation/alwaha/check/deploy_m02.py`, `notes_m02_l04.py`, `alwaha/engagement/m02_l04.py`, `tests/test_m02_l04.py`, `tests/test_m02_l04_checks.py`, `problem_simulation/host/compose.yaml`, design notes `04-systems-and-environments.md` and `08-live-services.md`, and `design/05-corpus.md` plus `traceability/module-02-trace.md`.

## What the syllabus says the day is

`course_design/module-02.md` states the syllabus line as containerizing and deploying AI applications with cloud-native workflows, and configuring model serving, inference endpoints, and environment management. The objective is narrower: the assistant answers on a private-cloud URL with a health probe and a named model hash. Concepts listed: images, probes, environments, the inference endpoint, `pol-deploy`. The lab is "build in CI, deploy to the team namespace, point the router at the endpoint, separate dev and prod secrets." The trap is a container running as root, or a log line with a national id. Advanced layer, in the same file and in `module-02-trace.md`: provenance, resource limits, rollback to the previous hash, GitOps, secrets handling.

The student background is more honest than the syllabus. Chapter `04-words.md` says Module 1 left a Dockerfile that was never built, and that today is "that later deploy, as files the check can read." The same page says the student still does not start a cluster and does not apply the manifest. `instructional/student-journey/lessons/m02_l04.md` records the engineering decision in one sentence: nothing is deployed to a live cluster. The slides tell the facilitator to demo a deploy rejected for a root user on `practice`. That demo is `python -m alwaha.demo.deploy`, and `test_m02_l04.py` locks its stdout to exactly `root image: rejected` then `registered image: accepted`. The demo runs the course's reference code. It does not build the student's Dockerfile.

**Verdict on the claim.** The day teaches the vocabulary of a private-cloud deploy and a checklist id. It does not containerize, deploy, serve a model, or run a probe. That gap is the thesis of this research. The vocabulary is worth keeping. The claim that the assistant is now on a URL is a sentence in `deployment.md`.

## What the student actually does

One person holds lead, AI, application, product, and architect. That constraint should stay. The graded path is a sequence of whole-file pastes:

| Order | File | What the paste does |
| --- | --- | --- |
| Sprint | `work/sprint.md` | "Build the image in CI and deploy it to the team namespace" before the readout |
| Image | `work/app/admit.py` | Reject `user` in `{root, 0}` and reject a log line that still contains `national_id`; `emitted_log` does `str.replace` |
| Image | `work/tests/test_admit.py` | Expects that behavior with stand-in `NID-sample` |
| Image | `work/deploy/Dockerfile` | `FROM python:3.12-slim`, `USER 1000`, `CMD ["python", "app.py"]` |
| Probe | `work/app/health.py` | Pick the register row `id == local-small` and `status == approved`; return `model_hash`, `prompt_version`, `dependencies: [endpoint]` |
| Probe | `work/deploy/deployment.yaml` | Namespace `ns-team`, `runAsNonRoot: true`, `readinessProbe` `httpGet` `/v1/health`, cpu `500m`, memory `512Mi` |
| Endpoint | `work/app/router.py` | Always return `ep-local-small`, `local-small`, `zone-private`; the `env` argument is deleted |
| Endpoint | `work/app/secrets.py` | `prod` reads `credentials/prod.json`, anything else reads `dev.json`, return the `endpoint` field |
| Endpoint | `work/.github/workflows/ci.yml` | Checkout, Python 3.12, `python -m unittest discover -s tests` |
| Pages | `zones.md`, `operators.md`, `deployment.md` | URL on `zone-private`; operator steps that mention health and prod; a note that cites `ciso` and `endpoint/guide.md` |
| Knowledge | `knowledge.md` | Line 1 contains `zone-private`. Line 2 contains `hash` |

Chapters 06–09 include the finished file under a Replace heading. A student who can copy a fenced block can pass without deciding anything. The words page already states the two rejection reasons, the approved row, `USER 1000`, `ns-team`, and `/v1/health` before the paste. The trainer chapter says the answers are in the solution chapters and that students were not asked to write provenance, limits, rollback, or quota pages. Those files exist in the solution (`provenance.md` is the sentence "The image carries a provenance label. Today's check does not read it.") and are unscored.

There is no interview on this day. `02-the-role.md` says the check does not read an interview note. The release test still carries a CISO script whose last turn asks whether patient data is in the integration-engine log. That question points at a real planted defect in design note 04: `int-engine` debug logs include PHI since change `CHG-2025-118`. The student never sees that defect. The trap they do see is a synthetic id inside `fixtures/log.json`, which they must not copy into `work/` because the file also holds the profile watermark.

## What `chk-deploy` scores

`deploy_m02.py` imports `admit`, `health`, `router`, and `secrets` from `work/app` and calls them. It does not listen on a port.

- **Health.** `health(register, candidate)` must return the gold approved hash, the gold prompt, and a dependencies list that contains the string `endpoint`. The candidate lookalike is passed in and the reference solution discards it. A wrong hash, a wrong prompt, and a missing dependency share one message: `the health probe does not report the registered hash`. The message does not name the hash. That secrecy is good. The probe is not HTTP.
- **Admission.** Four calls. Users `root` and `0` with a clean line must be rejected. User `1000` with a clean line must be accepted. User `1000` with the fixture log line must be rejected. `emitted_log` must not still contain the gold national id. The function under test is given the national id as an argument. The reference implementation deletes that substring.
- **Router.** `route("prod")` must equal gold endpoint, model, and zone.
- **Secrets.** `credential("dev", pack)` and `credential("prod", pack)` must equal the gold tokens, which are the `endpoint` fields `dev-` plus eight hex digits and `prod-` plus eight hex digits. Both JSON files are in the student packet. Chapter 03 prints them.
- **Dockerfile.** The last `USER` instruction is parsed with a regex. Missing `USER` counts as root. The last token must not be `root` or `0`. `USER app` passes the regex even if that name were uid 0 inside the image. The OCI config spec says a non-numeric user is resolved from the image's passwd data, and that an omitted `User` leaves the runtime user implementation-defined (`config.md` in the image spec). The grader's "no USER means root" matches common Docker behavior and is the right classroom default. It is a text rule, not a run of the image.
- **Manifest.** Substring search, not a YAML parse. The namespace string must appear. `readinessprobe` or `livenessprobe` must appear, and `/v1/health` must appear. `runasnonroot` must appear. A comment that contains those strings satisfies the check. Cpu and memory limits are in the solution manifest and are not read. `allowPrivilegeEscalation`, `capabilities.drop`, `seccompProfile`, `readOnlyRootFilesystem`, `runAsUser`, image digest, and `hostPath` are not read. The Pod Security Standards restricted profile requires the privilege-escalation, capability, seccomp, and non-root controls together. The solution manifest sets `runAsNonRoot: true` and resource limits only. Under the published restricted profile it is incomplete, and the grader cannot see the incompleteness.
- **Workflow.** The file must contain the substrings `unittest` and `tests`. There is no `docker build`, no digest, no signature, no deploy step. The sprint sentence still says the image is built in CI and deployed to the namespace.
- **Log copy.** Any file named `log.json` under `work/` fails as a watermarked sample. The message does not print the watermark.
- **Notes.** `notes_m02_l04.py` requires a citation (`ciso`, a doc id, or a pack path), a Boundary section that contains `clinician` and `urgency` and `ext-large`, a coverage share of required tokens, and a ban list that includes "the container runs as root", "prod uses the dev credential", "monitoring is complete", and "the integration-engine log is clean". Zones need a table row `url` / `zone-private`. Operators need both substrings `health` and `prod`. Sprint needs `deploy` or `pipeline` to appear before `readout`. Knowledge needs two numbered lines, `zone-private` on the first, `hash` on the second.

`pol-deploy` in the pack lists six checks: non-root, health probe, resource limits, no national id in a log line, image provenance, registered model hash. Design note `05-corpus.md` calls that list machine-checkable. The machine checks a subset, and it checks the subset as strings and function returns. Provenance is explicitly unread. Limits are present in YAML and unread. The registered hash is a 16-hex-digit prefix of a seed digest (`approved_hash` in `m02_l04.py`), prefixed with `sha256:`. An OCI image id and a cosign signature are over the full 64-hex digest. Teaching the short prefix as "the hash" will collide with the later habit of pinning `image@sha256:…`.

The solution manifest pins `image: patient-access-assistant:m01_l04`. That is a tag, and the tag text points at Module 1 Lesson 4. Nothing in the check looks at the image field.

## The traps, as implemented

**Root.** The shell Dockerfile ends `USER root`. The shell `admit` returns `accepted` for every call. The filled paste ends `USER 1000` and rejects the strings `root` and `0`. A numeric uid is the right direction: the OCI config field `User` accepts a uid, and Pod Security `runAsNonRoot: true` is how the cluster refuses uid 0 even when the image's `USER` is wrong. The lesson stops at the uid line. It does not create the user in the image, set ownership, drop capabilities, or set `allowPrivilegeEscalation: false`. `problem_simulation/host/compose.yaml` runs `python:3.12-slim` for `mocks` and `assistant` with no `user:` and no healthcheck, publishing 8080 and 8081. The course's own host stack does not apply the standard the student is told is in force. That is a useful contradiction to show a facilitator. It is a bad silent default if a later lesson says "the compose file is production."

**National id.** The generator builds `NID-` plus eight hex digits and embeds it in `fixtures/log.json` beside the canary. Prose must not contain it (`test_m02_l04.py`). The student function is then given that value so it can delete it. OWASP's logging cheat sheet says government identifiers and health data should not be recorded in the first place. A redaction function that must be told the identifier has already lost: the process held the value, and a second shape of the same value (split fields, a different fixture, an id inside a JSON body the logger also prints) survives `str.replace`. The integration-engine defect in design note 04 is the production-shaped version of this trap, and this lesson's ban list only forbids the sentence "the integration-engine log is clean." The student is rewarded for not claiming the log is clean, and is not shown the log.

## Contract the rest of the course thinks exists

Design note 08 requires `GET /v1/health` to report model hash, prompt version, and dependency status, and `POST /v1/chat` to return reply, citations, tool trace, and pending approval ids. The traffic simulator uses that contract. Lesson 4 implements the health shape as a pure function and does not implement chat. Monitoring is three words from `dashboard/starter.md`: request rate, error rate, model latency. The starter says the rest of the operations stack arrives in a later module. The solution `deployment.md` says it "waits until Module 2." The student is already in Module 2. The note is internally wrong, and a token check that wants the words "Module 2" in the Monitoring section will preserve the error if someone pastes the solution.

Quota lives in `quota.json` (`40 + seed % 17` in the generator; the committed practice picture in chapter 03 shows `requests: 47`). Over quota, the endpoint guide's companion OpenAPI says the request waits and does not spill onto `ext-large`. `router.py` ignores quota. `quota.md` in the solution is unread. Rollback is a knowledge sentence that contains the word `hash`. The previous register row is never served. Patient records are not in the exercise, so "a rollback does not rewrite patient records" is an untested sentence. It is still the right sentence. The check should bind it to a fixture file whose digest is unchanged when the served model digest changes.

Zones in `04-systems-and-environments.md` put `ext-large` on the public side via the external gateway, which meters tokens and fails a call whose prompt contains a `phi` field. The lesson's boundary section says PHI stays off `ext-large`. The router never has a path that could spill, so the boundary is a required phrase. Network policy is absent. Kubernetes documents that a `NetworkPolicy` does nothing until a plugin enforces it, and that pods are non-isolated until a policy selects them. The lesson has neither the object nor the caveat.

## What is already good

- The register distinguishes approved, previous, embed, external, and a lookalike name `local-smallx`. That is the right serving bug: a near name is not a registration.
- Dev and prod are different files, and the failure "prod uses the dev credential" is the right failure. The implementation then puts both files in the pack the student reads, which fails the twelve-factor litmus (a repo that could be opened without giving away credentials). The idea of separation should stay. The files-in-the-pack mechanism should go.
- The check refuses to echo the hash, the token, the quota, or the national id in failure text. Keep that property in any rebuilt grader.
- The watermark must not enter prompts, tickets, or `work/`. Keep that.
- Booking from chat still waits. The deploy day does not quietly start scheduling. Keep that boundary so Lesson 5's Ain file remains a change in scope.
- One person holds every role. Keep that. The role table can name platform, model owner, and security reviewer without inventing a second human.
- `pol-deploy` as a named checklist owned by `ciso` is the right artifact. It should become the spec the verifier enforces, including the rows the current check skips.

## Evaluation

| Question | Finding |
| --- | --- |
| Does the student leave with a running URL? | They leave with the string `https://assistant.site-a.alwaha.internal` in markdown. |
| Does a probe run? | A function returns a dict. Nothing calls `GET /v1/health`. |
| Is the model hash a digest a registry could pin? | It is a 16-hex prefix. The manifest uses a tag, `m01_l04`. |
| Is non-root admission control? | It is a uid string plus a substring `runasnonroot`. Restricted Pod Security is not met by the solution manifest. |
| Are secrets separated? | Two JSON files in the student pack, selected by `env == "prod"`. |
| Is CI a deploy pipeline? | It runs `unittest`. |
| Are provenance, limits, GitOps, and rollback taught? | They are named. Provenance and limits are unread notes. GitOps is absent. Rollback is the word `hash` on line 2 of `knowledge.md`. |
| Does the national-id trap match log hygiene? | It matches a substring delete of a value the function was given. |
| Can one student finish on a laptop? | Yes. The method is copying. The laptop never needs a cluster, which is the constraint to preserve while replacing the method. |

The day is a successful secret-keeping exercise and a successful vocabulary drill. It is a weak deployment exercise. The rebuild should keep the case, the check name, the five roles, and the refusal to print secrets, and should score behaviors the current string checks cannot see.
