# 04 — Exercises, assessment, and instruction

Audience: one person, self-paced, the same five roles the lesson already assigns. Python is already installed by chapter 01. A cluster is not required. Docker, cosign, Syft, SOPS, Kyverno, and `kind` are optional and detected. If they are missing, the required tests still pass through the pack verifier and a hand-written `bom.json`.

## Prerequisites

From earlier lessons: zones, the idea of a registered model, the external model `ext-large` as a place patient data must not go, and the habit of leaving gold secrets out of prose. From this lesson's reading, before any paste: OCI `User`, the three Kubernetes probes, the restricted profile's non-root plus capability drop plus seccomp, SLSA L1 versus L2 in one paragraph, and NIM's two-phase air gap as a story. The reading cites the URLs in [02-industry-research.md](02-industry-research.md). It does not include a finished `promote.py`.

The student does not need Kubernetes experience to finish the required path. They need to read a short YAML skeleton and to fill Python functions that already have tests. That is the same skill as the current lesson. The difference is that the chapter no longer contains the answer.

## Self-paced constraints

- One laptop. Windows is the course's primary shell. Commands stay `python`. No `kind` install on the critical path. `kind` on Windows often needs a working container engine and an extra hour; that hour is the failure mode of Alternative B.
- No GPU, no NGC account, no Hugging Face token. The weight file is generated locally.
- No outbound network in Phase 2. The simulator enforces this in-process so the student does not have to disable a Wi-Fi adapter.
- Optional tools are tried with `shutil.which`. A missing binary prints `optional tool absent, using pack verifier` and continues.
- Secrets: the prod value is not in the student chapter and not in `zones/build`. The hospital injector is a file the check mounts only inside the graded hospital run. The student pack's current `credentials/prod.json` moves to the hidden side.
- The national id and the watermark stay hidden. Failure messages keep today's property: they name a reason code, not the secret.
- Time box: background and standard, then four coded exercises, then the note. A student who only finishes the HTTP probe and the logger has not passed. A student who cannot install Docker has not failed.
- One person holds every role. The role is a heading on the exercise, not a second account.

| Role | Exercise they own | What "done" is |
| --- | --- | --- |
| Lead | Sequence the promotion before the readout | `sprint.md` lists build, verify, promote, then readout |
| AI / model owner | Register binding and rollback | Approved digest is served; previous digest is the rollback; lookalike is rejected; appointment file digest unchanged |
| Application | Image user, HTTP probes, allow-list logger | `/live` and `/ready` behave; stdout has no fixture id |
| Platform | Manifest, network policy, CI | Restricted fields present; egress to `ext-large` denied; workflow runs the verifier |
| Security (`ciso`'s checklist) | Phase 2 gate and the note | `pol-deploy` rows are each either enforced or explicitly "not this lesson" |
| Product | Operator steps | How to call `/ready` with the prod injector, and what 503 means |

The security role is the same person. There is still no interview. The CISO drop remains the standard.

## Exercises

Skeletons live in `work/`. Tests live in `work/tests/` and are already the course's style (`unittest`). The student replaces function bodies. They do not replace tests except where an old test encodes the bad contract (`admit` taking a national id). Those tests are replaced with tests that call the new signature, and the chapter shows the test, not the implementation.

**E1 — Probe.** Implement `serve.py` with `GET /v1/health/live` and `GET /v1/health/ready`. Live returns 200 when the process is up, including when `weights.bin` is missing. Ready returns 503 until the loaded digest equals the approved row, then 200 with `model_hash`, `prompt_version`, and `dependencies`. Ready also returns 503 when the dependency `endpoint` is marked down. A startup counter is incremented while ready is 503; a liveness function that restarts during that window fails the test. This replaces `health()` returning a dict with no socket.

**E2 — Logger.** Implement `log_event(event: dict) -> str` with an allow-list. There is no `national_id` parameter. Tests feed events that contain the fixture id under extra keys. The returned line and the captured stdout omit it. A test imports the module source from disk and fails if the gold id or the watermark appears in `work/`. `str.replace` of a known id is not an acceptable implementation because the tests include a split form that replace will not see, and because the function is not given the id.

**E3 — Workload and egress.** Fill the skeleton manifest and network policy. The checker parses YAML (the course can use the stdlib and a tiny indentation-sensitive walk, or PyYAML if it is already a dependency; if neither is acceptable, parse the specific keys with a small dedicated reader already in the pack). Substring presence is not success. Include a bad fixture, `privileged: true` together with `runAsNonRoot: true`, which today's regex would accept and the new checker rejects.

**E4 — Promote.** Implement `promote(bundle, zone, network) -> str` for the rules in [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md). The air-gap case is mandatory: `network="airgap"` plus a bundle that contains a clear-text prod token, a keyless bundle with no offline proof, a lookalike row, a short 16-hex hash in `model_hash`, and a weights container limited to `512Mi`. Each returns its reason code. The happy path copies the bundle to `running/` and starts the server bound to localhost only.

**E5 — Note.** `deployment.md`, `zones.md`, `operators.md`, `sprint.md`, `knowledge.md`. Same headings as today, plus a Promotion section and an honest provenance sentence. Monitoring says the rest of the stack arrives in a later module. Knowledge line 1 names `zone-private`. Knowledge line 2 states that rollback changes the served digest and leaves the appointment fixture's digest unchanged. Operators name `/v1/health/ready`, 503, and the prod injector. They do not contain the token.

Optional stretch, after the check: if `docker` exists, build the Dockerfile and run it with `--user 1000` and a read-only root filesystem; if `syft` exists, replace the hand-written BOM; if `cosign` exists, sign the digest with `--tlog-upload=false` and verify with the key. The stretch cannot be the only way to pass.

## Assessment

Keep the command:

```text
python -m alwaha.check deploy --release rel-m02-l04 --work <work> --profile practice
```

Change `deploy_problems` so it scores the behaviors below. Keep the rule that the printed miss does not contain the hash, the token, the quota, or the national id.

| Miss text (stable, secret-free) | Condition |
| --- | --- |
| `the health probe does not report the registered hash` | `/ready` body digest or prompt mismatches, or ready is 200 while weights are absent |
| `the image runs as root` | Image config user is root, 0, or missing; or the manifest fails a restricted-profile field, not only `runAsNonRoot` |
| `a national id is in the deploy log` | Allow-list logger emits the fixture, or any file under `work/` contains it or the watermark |
| `prod uses the dev credential` | Air-gap promote reads the dev file, or the prod token appears in `zones/build` or the bundle in clear text |
| `the router leaves the private endpoint` | Route is not the private endpoint, including when the request count is over quota |
| `the manifest is not in the team namespace` | Namespace is not `ns-team` |
| `the health probe is missing` | Live or ready route missing, or the manifest probes the wrong path |
| `the pipeline is not in CI` | Workflow does not run the verifier tests. A file that merely contains the letters `unittest` is not enough |
| `the deploy rejected a registered image` | Happy-path bundle is rejected |
| `the url is not in zone-private` | Zone table unchanged from today |
| `promotion left the air gap open` | Air-gap mode accepted a bundle with a clear-text secret, a banned API-key name, or a keyless proof that needs the public log |
| `the sbom does not match the digest` | `bom.json` missing or inconsistent |
| `rollback rewrote patient state` | Appointment fixture digest changed |

Notes keep the citation, the clinician urgency sentence, and the `ext-large` boundary. Drop the ban that is only needed because the paste once said "the container runs as root." Add a ban on "monitoring is complete", "SLSA level 3", "HIPAA compliant", "PDPL compliant", and "the integration-engine log is clean."

`test_m02_l04.py` should grow fixtures for the bad bundles and should keep the existing guarantees: earlier releases are unchanged, the canary appears once, prose does not contain secrets, the demo does not print secrets. The demo should change. Today it prints the admission result before the student writes code. The new demo prints two HTTP status lines from the reference server (`live 200`, `ready 503`) on a bundle with weights withheld, and nothing else. That previews the probe split without previewing `promote.py`.

## Solution approach

The reference solution is the smallest Python that passes the table. It uses `hashlib` for digests, `http.server` for the probe, a dict allow-list for logs, and a YAML reader for the manifest. It calls `pack/tools/verify_sig.py` for the signature. It does not vendor cosign. The solution note's Promotion section names Path A and points at the NIM air-gap URL as the story of the two phases. The solution manifest's image field is a digest, not `patient-access-assistant:m01_l04`.

Facilitator traps to keep in the trainer chapter, still optional for the student:

- A manifest comment that contains `runAsNonRoot` while the field is false. The old checker passed. The new one fails.
- A logger that deletes the synthetic id and still prints the surrounding request body.
- A student who sets `USER 1000` and `privileged: true`.
- A student who copies `credentials/prod.json` into the bundle to "make prod work."

## Deletions inside the current chapters

Delete these as graded activities. Some can remain as a short "what we used to accept" sidebar in the trainer chapter.

- Whole-file paste of `admit.py`, `health.py`, `router.py`, `secrets.py`, `Dockerfile`, `deployment.yaml`, `ci.yml`, `sprint.md`, `zones.md`, `operators.md`, and `deployment.md`.
- `admit(user, log_line, national_id)` and `emitted_log` via `str.replace`.
- Grading `runasnonroot`, `unittest`, `tests`, `health`, `prod`, and `hash` as substrings.
- Unread `provenance.md` and `limits.md` that exist so a facilitator can say the check skips them. Either the verifier reads the control or the checklist row is marked "later."
- Truncated `sha256:` prefixes as the value `/ready` reports.
- Printing dev and prod endpoint tokens in chapter 03.
- The sprint claim that CI deploys to the namespace, until a workflow actually builds or, in this rebuild, runs the promotion verifier.
- The monitoring sentence that the rest of the stack waits until Module 2.
- The image tag `m01_l04`.
- A demo that only prints `root image: rejected` as the definition of admission.

Keep the shell-versus-work copy discipline, the watermark rule, the closed `Solution_Copy`, and the refusal to repair indentation by hand if the course still wants paste-safe blocks. The blocks that remain are skeletons with `raise NotImplementedError`, not solutions.

## Lessons to spawn

Do not add a "install Kubernetes" lesson. Do not add a GPU lab to Module 2.

1. **This lesson, rebuilt.** Stays Lesson 4. The air gap is the new middle, not a new module.
2. **Lesson 5 stays the Ain change.** The nightly file enters `zones/hospital/incoming/` and uses the same `promote` gate. A live slot API is still a rejection. Spawn nothing unless Lesson 5's current file copy skips the gate.
3. **Later operations lesson, existing planted defect.** Open `int-engine` change `CHG-2025-118` from design note 04. The student traces a platform log that already contains PHI and writes a pipeline allow-list. That is the stdout lesson at a system boundary. It is not a repeat of E2.
4. **Optional seminar, ungraded.** Read the vLLM Docker page and the NIM air-gap page side by side. Deliverable is a one-page note: which flags violate the restricted profile, which health URL means "process up," which means "weights loaded." No container run is required.
5. **Optional appendix on this lesson.** GitOps reconcile and, for a prepared machine, Flux `OCIRepository` pinned to a digest. Ungraded.

## Instructional design

Chapters stay numbered and short. Each coded chapter has three parts: the failure the test will name, the contract (signatures and reason codes), and the command to run that chapter's tests. The contract does not include the branch that returns `accepted`.

The words page gains: startup probe, readiness versus liveness, digest, SBOM, air gap, allow-list, restricted profile. It loses nothing that later chapters need, and it stops revealing `USER 1000` as the answer line. Say "a numeric uid other than 0" and let the test accept `1000`.

Self-check before the graded command: the student can curl `/live` and `/ready`, can show a rejected air-gap bundle, and can show an appointment digest that survived rollback. Then chapter 10 runs `chk-deploy`. The pass line stays `chk-deploy passed.`
