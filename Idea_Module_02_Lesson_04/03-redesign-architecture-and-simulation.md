# 03 — Redesign, architecture, and simulation

The rebuilt lesson still ends at `chk-deploy` and still leaves booking unstarted. The assistant is a small process the student can run. The model is a stand-in file, `weights.bin`, of a few kilobytes of non-patient bytes. The private cloud is three directories plus a verifier. A URL string remains in the deployment note, and it is also something `curl` can hit on `127.0.0.1`.

## Zones in the simulation

Use the names the course already has.

| Directory | Course zone | Network flag in the simulator | What may live there |
| --- | --- | --- | --- |
| `zones/build/` | Connected build, outside the hospitals | `connected` | Source, Dockerfile, dev age key, unsigned drafts |
| `zones/site-a/` | `zone-private` | `internal` | Promoted bundle after verification, prod secret injected at start, assistant process |
| `zones/hospital/` | `zone-hospital` | `airgap` | A copy of the bundle that arrived on "media." No dev key, no registry token, no Git remote |

`ext-large` stays a hostname in `zone-public`. The simulator's network policy denies it. `local-embed` stays on the register and is the wrong row for chat, as it is today. `local-smallx` stays the lookalike.

Site-b is the same pattern as site-a with a different digest pointer, used only in the rollback exercise. Ain is not given a slot API. Lesson 5's nightly file is a later payload through `zones/hospital/`. This lesson's hospital zone only accepts or rejects a bundle.

## The bundle

A promotion bundle is one directory the student assembles:

```text
bundle/
  image-ref.txt          # name@sha256:<64 hex> of the stand-in image config
  weights.bin            # stand-in weights, no text, no id
  weights.digest         # sha256 of weights.bin
  model.sig              # detached signature, or "VERIFY WITH PACK VERIFIER"
  bom.json               # CycloneDX-shaped inventory
  deploy/deployment.yaml # assistant workload, restricted fields
  deploy/networkpolicy.yaml
  register-snapshot.json # approved row only, copied from the pack register
  provenance.json        # SLSA-shaped L1 fields: subject digest, source revision, builder id
```

`provenance.json` is allowed to be unsigned. The deployment note must say "Build L1 shape, self-described, not L2." That sentence is graded. The old sentence "the image carries a provenance label" is deleted.

The pack ships a public key `pack/keys/promote.pub` and a helper `pack/tools/verify_sig.py` that the student calls and does not rewrite. The helper is documented as a stand-in for `cosign verify --key` and for `model_signing verify` with a key. Students who have cosign may replace the call and must pass the same tests. Students do not invent a signature algorithm.

## Air-gapped promotion path

This is the core new activity. It follows NIM's two phases without NIM.

**Phase 1, connected (`zones/build`).** The student computes the full SHA-256 of `weights.bin` and of a canonical image-config JSON (the fields that matter: `User`, `Entrypoint`, `Env`). They reject the build if `User` is missing, `root`, or `0`. They write `bom.json` with two components: the image digest and the model digest. They run the allow-list logger against a fixture request and keep the stdout transcript in the bundle only if the synthetic id is absent. They encrypt nothing for prod here. A scan fails the phase if the tree contains `prod-`, the gold national id, the watermark, or `NGC_API_KEY` / `HF_TOKEN` as environment names. The NIM guide's rule ("do not set `NGC_API_KEY` or `HF_TOKEN` in the air-gapped phase") is applied one step earlier: those names are banned in the bundle, so they cannot ride across on media.

**Transfer.** The student copies the bundle directory to `zones/hospital/incoming/`. The simulator sets the hospital network flag to `airgap` before the copy is eligible. Under that flag the verifier refuses any step that would open a socket, read `zones/build`, or load `credentials/dev.json`. The implementation of "refuses" is a parameter the student's `promote.py` must honor: if `network == "airgap"` and the code path requests `dev` or a public hostname, the function returns `rejected`.

**Phase 2, hospital.** `promote.py` admits the bundle into `zones/hospital/running/` only when all of the following hold:

1. `weights.digest` matches a fresh hash of `weights.bin` and matches the approved `local-small` row. The row's `zone` is `zone-private` or `zone-hospital`. `ext-large` is rejected even if someone pastes its digest into the local row.
2. The lookalike id `local-smallx` is rejected even when its digest field has been edited to equal the approved digest. Name, status, and digest bind together.
3. `verify_sig(weights.bin, model.sig, promote.pub)` returns true. A tampered byte in `weights.bin` fails.
4. `bom.json` lists both digests. A missing file fails. A BOM for a different digest fails.
5. The manifest contains the restricted fields the current solution omits: `runAsNonRoot: true`, `runAsUser` greater than 0, `allowPrivilegeEscalation: false`, `capabilities.drop` including `ALL`, `seccompProfile.type: RuntimeDefault`, no `hostPath`, no `privileged: true`. Resource limits exist and are the assistant class (`cpu` and `memory` present). A second workload, if present, named `weights`, must not reuse the assistant's `512Mi` without an explicit class label. The checker fails a weights container whose memory limit is `512Mi`, because that limit fits the course's current API container and will OOM a real serving process. The stand-in weights process is tiny; the class label is the lesson.
6. `networkpolicy.yaml` selects the assistant, sets `policyTypes` to include `Egress`, and does not allow the `ext-large` hostname or a default `0.0.0.0/0` egress. The simulator, not a CNI plugin, enforces this. The note says enforcement on a real cluster needs a plugin.
7. No file in the bundle contains the national-id fixture or the watermark. Prod material appears only as ciphertext or is absent. The running process receives the prod endpoint from the hospital injector, which is outside the bundle.
8. `provenance.json` names the same image digest. The note records that this is L1-shaped.

Failure at any step leaves `running/` unchanged. The student records the rejection reason in `promotion-log.txt` using the allow-list (`bundle_id`, `reason_code`, `digest_prefix` of 12 hex characters). Reason codes are fixed strings: `digest-mismatch`, `lookalike`, `bad-signature`, `sbom-mismatch`, `pss-restricted`, `egress-open`, `secret-in-bundle`, `phi-in-log`. The log line does not contain the id.

**Rollback.** A second approved-looking row with `status: previous` is already on the register. Rollback copies that digest into the running pointer. `/ready` then returns 503 until the process's reported digest equals the previous row. A fixture file `cases/appointments.json` is hashed before and after. The hashes match. The knowledge line stops being "a sentence that contains the word hash" and becomes this observation: the served digest changed and the appointment file digest did not.

**Quota.** The stand-in counts requests. At the gold quota, the next call returns a wait status and the same private endpoint. A test that expects the router to switch to `ext-large` fails the student. The quota integer stays out of `deployment.md`, as it does today.

## Alternative A — Local promotion bundle

**Maturity: Proven pieces, simulated composition. This is the required path.**

The student runs Python, `curl`, and the pack verifier. Optional tools slot in behind the same tests. Admission is the Phase 2 function, which is the course's `admit`, expanded from a username check into the bundle gate. The probe is HTTP. Secrets never sit in the connected tree in clear text. The air gap is a directory flag.

What the student can get wrong, and the test catches: signing the tag text instead of the digest; a `/ready` that returns 200 while `weights.bin` is absent; a logger that accepts `national_id` as a parameter (the new signature does not have that parameter, and a test greps the source for the gold id only on the hidden side); a NetworkPolicy that is present and allows all egress; a provenance file that is a single sentence.

Cluster: none. GPU: none. Time: one self-paced sitting if the skeletons and tests are already in the pack. The current paste sitting is shorter and teaches less. The new sitting is longer. Cut the reading that repeats the answer.

## Alternative B — GitOps reconcile, cluster optional

**Maturity: Emerging for this audience. Appendix, not the gate.**

Desired state lives in `git/site-a/` as YAML. A `reconcile.py` diffs that tree against `live/site-a/` and prints `OutOfSync` or applies the copy. That is the Argo CD control loop without Argo CD. Promotion from site-a to the hospital zone is not a Git pull. It is still the bundle copy, because the hospital flag is `airgap` and Flux's `GitRepository` needs a Git URL the zone can reach. The optional extension for a student who already has a cluster: install nothing new unless they want to; if Flux is present, an `OCIRepository` can point at a local registry they loaded with the bundle tarball. The published Flux example tracks a tag and records the resolved digest in status. The lesson tells them to pin the digest they just verified, and to treat `ref.tag: latest` as the bug the example is allowed to show and the hospital is not allowed to run.

SOPS fits this alternative cleanly: the Git tree contains ciphertext, and only the internal zone's reconcile step holds the age key. External Secrets is explained and not installed. A student who skips the appendix still passes `chk-deploy` via Alternative A.

Risk: a student spends the day on `kind` and never reaches the air gap. The appendix is after the check, or it is a separate ungraded stretch. It is not on the critical path.

## Alternative C — Keyless transparency and one statement for image, model, and prompt

**Maturity: Experimental for an air gap. Reading plus one failing fixture.**

The public sigstore path (Fulcio, Rekor, OIDC email in a public log) is the wrong default on a hospital network and on a student laptop that should not publish an email into Rekor. Cosign documents that the identity is stored and cannot be removed. Keyless mode also fails closed when the air-gapped phase has no route to the log, unless the inclusion proof was bundled during the connected phase and a private or mirrored log is trusted. Running a private Rekor is a platform project.

The useful experimental object is one in-toto statement whose subjects are the image digest, the weight digest, and the prompt id `p1`. model-transparency already puts an in-toto statement inside a sigstore bundle and uses predicate type `https://model_signing/signature/v1.0`. CycloneDX names `https://cyclonedx.org/bom` as its predicate type. The lesson does not ask the student to produce either envelope from scratch.

The graded fixture for this alternative is negative. `bundle/experimental/` contains a keyless bundle with no offline inclusion proof. `promote.py` in air-gap mode returns `rejected` with reason `needs-online-log`. The student writes that rejection and a paragraph that says a private transparency log would be a different project. They do not stand up Fulcio.

## Alternative D — Run NIM or vLLM as the lesson

**Rejected as the required path. Emerging as a later optional seminar.**

vLLM and NIM are real serving systems. Their official quick starts assume a GPU, a registry credential, and, in the vLLM Docker example, a root cache path. NIM's air-gap page is assigned reading inside Alternative A. Executing it is a different course, on a different machine, with a license the student may not have. A seminar can compare `/health` (vLLM, 200 or 503, no digest) with `/v1/health/live` and `/v1/health/ready` (NIM) and with the course's single `/v1/health`. No install steps in the required chapter.

## Synthetic data

Keep the generator's discipline. Hashes, tokens, the quota, and the national id stay in gold. Prose and the bundle must not contain them. Change the digest shape the student sees: the register snapshot used in the exercise stores full 64-hex digests of the stand-in files, still derived from the profile seed so `practice` and `small` differ. The old 16-hex prefix can remain as a legacy field the probe must not report. That preserves the lookalike lesson and stops teaching a short prefix as an image id.

`weights.bin` is `hashlib.sha256(seed).digest()` repeated, or any non-textual bytes. It is not a model file downloaded from the internet. The prompt text is the existing `p1` / `p0` ids, not a clinical prompt. The log corpus is twenty lines built from the synthetic id and from benign lines. Cases the allow-list must survive:

- the id in a JSON field named `national_id`
- the id split across two fields so `str.replace` of the concatenated form does nothing useful
- a line that is only `request_id` and `status`
- a line that includes `HF_TOKEN=…` and must drop that field
- the watermark alone, which still fails the copy rule

No real identifier grammar. No patient rows. Appointment rollback uses a three-line JSON fixture with fictional case ids already in the style of earlier modules.

## Production failures to plant

| Failure | What the student should see | Maturity of the underlying issue |
| --- | --- | --- |
| Readiness returns 200 before weights are loaded | `/live` is 200, `/ready` is 503, promotion of traffic is refused | Proven (NIM's split; Kubernetes readiness) |
| Liveness calls the model and restarts during load | Startup probe is the fix; the stand-in counts restarts | Proven |
| Tag moves, digest stays in the note | Verifier compares bytes to the digest, ignores the tag | Proven (cosign's own warning) |
| `USER app` where the name is uid 0 | Checker resolves a tiny passwd fixture | Proven (OCI name resolution) |
| Restricted fields missing while `runAsNonRoot` is set | Current solution manifest fails the new checker | Proven |
| All-egress NetworkPolicy, or a policy and no enforcer | Simulator denies `ext-large`; the note says a CNI is still required on a real cluster | Proven |
| Prod token in the bundle | Phase 2 `secret-in-bundle` | Proven (twelve-factor litmus; NIM's ban on API keys in the air-gapped phase) |
| Keyless bundle in the air gap | `needs-online-log` | Experimental path, Proven failure |
| Quota spill to `ext-large` | Router stays on `ep-local-small` | Course rule, keep it |
| Logger handed the national id | Signature has no such parameter; stdout scanned | Proven hygiene, poorly matched by `str.replace` |
| Rollback rewrites appointments | Appointment digest unchanged | Course claim, now tested |
| SBOM digest is the tag string | `sbom-mismatch` | Proven |
| `512Mi` on the weights container | Class label required | Proven resource control; the number 512Mi is the course's current assistant limit, not a NIM sizing guide. Do not invent a GPU memory number. |

## What the deployment note is allowed to claim

The note cites `pol-deploy`, `ciso`, and `endpoint/guide.md`, as it does now. It states the URL, `zone-private`, live versus ready, the digest algorithm, non-root, the air-gap flag, and the sentence that provenance is L1-shaped and unsigned. It states that monitoring at this stage is request rate, error rate, and model latency, and that the rest arrives in a later module. It does not say "until Module 2." It does not say the cluster is compliant with any named law. A clinician still assigns urgency. Patient data still stays off `ext-large`, and the network policy is the mechanism named in the Boundary section.
