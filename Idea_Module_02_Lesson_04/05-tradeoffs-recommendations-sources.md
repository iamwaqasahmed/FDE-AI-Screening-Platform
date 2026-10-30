# 05 — Tradeoffs, recommendations, and sources

## Recommendation

Rebuild `rel-m02-l04` around Alternative A, the local promotion bundle, including the air-gapped hospital directory. Keep `chk-deploy`, the five roles, the register, the zones, the quota rule, and the secret-free failure messages. Stop pasting finished deploy files. Leave Kubernetes, cosign, Syft, SOPS, Kyverno, NIM, and vLLM as reading or as optional tools behind the same tests.

Alternative B (GitOps) is the right production shape for site-a and the wrong critical path for a laptop lesson, because the air gap cannot pull Git. Alternative C (keyless sigstore, one statement covering image and weights and prompt) is the right story about what a mature registry does, and it is the wrong thing to require offline. Alternative D (run the vendor serving container) teaches the product and breaks the restricted profile and the no-GPU constraint.

## Comparison

|  | A. Local bundle | B. GitOps | C. Keyless in-toto | D. NIM or vLLM |
| --- | --- | --- | --- | --- |
| Maturity for this lesson | **Proven** parts, simulated | **Emerging** | **Experimental** offline | **Emerging** product, rejected as the lab |
| Cluster | None | Optional `kind` or a file reconcile | None | GPU host |
| What is admitted | Bundle gate in `promote.py` | Desired-state diff, then the same gate for the hospital | A fixture that must fail in the air gap | Vendor container start |
| Image identity | Full SHA-256, numeric non-root user | Digest pinned in the desired state | Digest inside a statement the student does not mint | Vendor image tag from upstream docs |
| Model identity | Stand-in file, signed with the pack key helper | Same | Predicate type documented, not produced | Real weights, out of scope |
| Secrets | Prod absent from the connected tree | SOPS ciphertext if the tool is installed | OIDC email would hit a public log; do not | `HF_TOKEN` / `NGC_API_KEY` banned in the air-gapped phase by NVIDIA's guide |
| Air gap | Required simulation | Git pull does not cross it; the bundle still does | Fails closed without an offline proof | Documented by NVIDIA; not executed |
| SBOM | Hand-written CycloneDX-shaped JSON, optional Syft | Same artifact, stored in Git or OCI | CycloneDX predicate cited only | Not the lesson |
| Main way to fail the student honestly | Secret in the bundle, ready too early, lookalike digest | They install `kind` and never promote | They are sent to sign up for OIDC | They copy `--privileged` or `/root/.cache` into the manifest |
| Passes without optional binaries | Yes | The file reconcile yes; Flux no | The negative fixture yes; real keyless no | No |

## Tradeoffs worth keeping visible

**Simulation versus a cluster.** A directory flag named `airgap` is not a disconnected network. It is a test double of the decision NVIDIA documents: prepare while connected, run from local storage, do not carry registry API keys. The gain is that every student hits the decision. The loss is that they do not feel a registry timeout. The note should say that in one sentence so the readout does not over-claim. An optional `kind` lab does not fix the air gap; a cluster on a laptop is still on the laptop's network.

**Self-signed versus SLSA L2.** A key in the student pack proves the bytes were not edited after the pack was signed. SLSA L2 wants the signature from a hosted build platform the tenant cannot forge. Calling the exercise L2 would be a false claim. L1's value, which the spec itself describes as catching mistakes rather than stopping a determined tamperer, matches a classroom. Say so in `provenance.json`'s companion sentence.

**Allow-list versus redaction.** Redaction needs a detector and needs the secret in the process that deletes it. An allow-list drops unknown fields and can still miss a secret placed in an allowed field such as `request_id`. The tests should include that case: a `request_id` whose value is the synthetic id must be rejected or replaced with a generated id. That is the residual hole, and it belongs in the trainer chapter. Do not add a regex for real-world national ids.

**One health URL versus two.** Design note 08's `GET /v1/health` is the contract the traffic simulator uses. Splitting live and ready breaks that contract unless `/v1/health` remains as an alias that is ready-shaped (503 until weights load) and the new paths are additive. Recommendation: keep `/v1/health` as the ready alias so later modules do not break, and add `/v1/health/live` and `/v1/health/ready`. Document the alias in the note.

**Resource numbers.** The current solution's `512Mi` is a fine limit for the small API process and a bad limit for a weight server. The checker treats `512Mi` on a container named `weights` as a fail. Do not publish a fake GPU sizing table. The lesson's point is that the two processes are different classes.

**Twelve-factor environments.** The factor warns against baking a named environment block into the repo. The hospital still has two trust domains. The app reads one injected variable. The platform decides which domain injects it. Teaching `if env == "prod": open("prod.json")` with both files in the repo fails the factor's litmus test and also fails the air gap, because the prod file would be on the media. ESO is the cluster version of the injector. SOPS is the Git version. The Python injector is the classroom version. All three are the same split of duties.

**NetworkPolicy without a plugin.** Shipping a YAML file that a string search accepts repeats today's manifest bug. The simulator must deny an egress the policy forbids, and the note must say a real cluster ignores the object until a policy engine is installed. That sentence is a feature, not a hedge.

**Paste pedagogy.** Whole-file answers make the day finishable by a non-specialist and make the traps unobservable, because the student never sees a root container accepted. Skeletons with `NotImplementedError` keep the finishable surface and return the traps. The cost is a longer day. Pay for it by deleting the unread notes and the repeated pictures of shell files in the chapters.

## Deletions

Delete as student work and as grader behavior:

1. Finished pastes of the six code and manifest files and of the graded markdown.
2. `admit(user, log_line, national_id)` and substring redaction.
3. Substring checks for `runasnonroot`, `unittest`, `health`, `prod`, and `hash`.
4. Truncated digests in the probe body, and the tag `patient-access-assistant:m01_l04`.
5. Clear-text prod and dev credentials in the student-visible pack.
6. Provenance and limits files that announce they are unscored. Enforce the control or mark the checklist row deferred.
7. The monitoring line that says the rest of the stack waits until Module 2.
8. Any chapter sentence that says the exercise is HIPAA-compliant, PDPL-compliant, or an NCA assessment. Those regimes are outside the fiction. HHS and OWASP stay as reading for log design.
9. A required `docker run` of vLLM or NIM, including the upstream flags `--privileged`, `seccomp=unconfined`, and a cache mounted under `/root`.

Keep: `pol-deploy`, `ciso`, zones, the lookalike model name, the quota spill ban, clinician-assigned urgency, the watermark, secret-free check messages, one person for every role, and Lesson 5's refusal to promise live slots at Ain.

## New work, in order

1. Replace the lesson's code contracts and `deploy_m02.py` as in [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md). This research folder does not do that replacement.
2. Point Lesson 5's nightly file at the same promote gate.
3. Schedule the `int-engine` PHI log (`CHG-2025-118`) in a later operations lesson.
4. Add an ungraded one-page reading: vLLM `/health` versus NIM live/ready versus the course alias.

## Claims this research does not make

- No count of hospitals using cosign, Flux, or NIM.
- No statement that Pod Security restricted is sufficient for a GPU device plugin. Device access can force exceptions the restricted profile will not allow. That is a platform issue for the optional seminar, and it is not solved here.
- No statement that a self-signed bundle meets SLSA L2 or L3.
- No statement that an allow-list logger satisfies the HIPAA Security Rule. The HHS page describes duties of regulated entities. The fictional cluster is not one of them. Audit controls (record and examine activity) and "do not write the identifier to stdout" are different requirements. The lesson teaches the second, and names the first as later work.
- No measurement of how long `kind` takes on Windows. The risk stated is qualitative: cluster install crowds out the air-gap exercise.
- CycloneDX 1.7 dates are taken from the specification overview fetched for this note (release 2025-10-21, ECMA-424 published 2025-12-10). If that page moves, re-check before printing the version in a student chapter.

## Sources

Image and workload

- OCI image config, `User`: <https://github.com/opencontainers/image-spec/blob/main/config.md> and <https://specs.opencontainers.org/image-spec/config/>
- Probes: <https://kubernetes.io/docs/concepts/workloads/pods/probes/>
- Probe task page: <https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/>
- Pod Security Standards: <https://kubernetes.io/docs/concepts/security/pod-security-standards/>
- Pod Security admission: <https://kubernetes.io/docs/concepts/security/pod-security-admission/>
- Run as non-root, pod context overrides the image: <https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/>
- NetworkPolicy, including the default of non-isolation and the need for a plugin: <https://kubernetes.io/docs/concepts/services-networking/network-policies/>
- Kyverno CLI, validate before a cluster: <https://kyverno.io/docs/kyverno-cli/>

Supply chain

- SLSA v1.2 spec: <https://slsa.dev/spec/v1.2/>
- SLSA build track: <https://slsa.dev/spec/v1.2/build-track-basics>
- SLSA build requirements: <https://slsa.dev/spec/v1.2/build-requirements>
- Cosign container signing: <https://docs.sigstore.dev/cosign/signing/signing_with_containers/>
- Cosign sign, digest warning and `--tlog-upload=false`: <https://github.com/sigstore/cosign/blob/main/doc/cosign_sign.md>
- Cosign README, keyless flow and the public-log warning: <https://github.com/sigstore/cosign/blob/main/README.md>
- model-transparency: <https://github.com/sigstore/model-transparency/>
- CycloneDX overview (components include machine learning models; predicate `https://cyclonedx.org/bom`): <https://cyclonedx.org/specification/overview/>
- Syft: <https://oss.anchore.com/docs/guides/sbom/> and formats <https://oss.anchore.com/docs/guides/sbom/formats/>

Serving

- vLLM Docker: <https://docs.vllm.ai/en/latest/deployment/docker/>
- vLLM OpenAI-compatible server and `--api-key` scope: <https://docs.vllm.ai/en/latest/serving/online_serving/openai_compatible_server/>
- vLLM `/health`: <https://docs.vllm.ai/en/stable/api/vllm/entrypoints/serve/instrumentator/health/>
- vLLM metrics: <https://docs.vllm.ai/en/latest/usage/metrics/>
- NIM air gap: <https://docs.nvidia.com/nim/large-language-models/latest/deployment/air-gap-deployment.html>
- NIM API, live and ready: <https://docs.nvidia.com/nim/large-language-models/latest/reference/api-reference.html>
- NIM architecture: <https://docs.nvidia.com/nim/large-language-models/latest/reference/architecture.html>

Config, logs, GitOps

- Twelve-factor config: <https://12factor.net/config>
- External Secrets overview: <https://external-secrets.io/latest/introduction/overview/>
- SOPS: <https://getsops.io/docs/>
- Flux with SOPS: <https://fluxcd.io/flux/guides/mozilla-sops/>
- OWASP Logging Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html>
- OWASP Proactive Control C9: <https://top10proactive.owasp.org/the-top-10/c9-security-logging-and-monitoring/>
- HHS HIPAA Security Rule summary (audit controls, ePHI): <https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html>
- Argo CD: <https://argo-cd.readthedocs.io/en/latest/>
- Flux concepts: <https://fluxcd.io/flux/concepts/>
- Flux OCIRepository: <https://fluxcd.io/flux/components/source/ocirepositories/>

Course materials used for the evaluation are the lesson, check, and design files named in [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md). They are not external evidence.
