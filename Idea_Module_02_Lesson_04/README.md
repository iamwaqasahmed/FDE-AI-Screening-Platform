# Module 02 Lesson 04 — Deploy: curriculum research

Research only. Nothing in this folder changes `Module 02/Lesson 04`, the checks, or the design notes. The lesson id stays `rel-m02-l04`. The check name stays `chk-deploy`.

**Thesis.** A Dockerfile and a probe are the start of deployment. A hospital private cloud also needs admission control, a non-root workload, an SBOM, a signed image, a signed model artifact, secret separation, a network policy, and a promotion path across zones. This lesson can teach that on one laptop. It cannot teach it by pasting finished files that a string search then accepts.

## Recommendation

Rebuild the day as a **local promotion bundle** the student can verify with Python already required by the course. Keep Docker, Kyverno, cosign, Syft, and Kubernetes optional. Do not require a GPU, a registry account, or a cluster.

The student still holds every role. The work stops being a paste of `admit.py`, `health.py`, `router.py`, `secrets.py`, the Dockerfile, the manifest, and the workflow. Those files become small behaviors with failing tests: an HTTP live/ready split, an allow-list logger that never receives the national-id fixture as an argument, a manifest checker for the Pod Security Standards **restricted** fields the current solution omits, and a promotion script that will not copy a bundle from the connected build zone into the air-gapped hospital zone until the digest, the signature stand-in, the SBOM, and the secret scan agree.

Three architectures are compared in [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md).

| Path | Maturity for this lesson | Cluster |
| --- | --- | --- |
| A. Local promotion bundle | **Proven** parts, assembled as a simulation | None |
| B. GitOps pull (Argo CD or Flux), optional `kind` | **Emerging** as the student's daily driver | Optional |
| C. Keyless sigstore plus one in-toto statement for image, weights, and prompt | **Experimental** inside an air gap | No, and it still needs the public transparency log or a private one |

Path A is the required lesson. Path B is an appendix for a student who already runs a local cluster. Path C is a reading and a fixture that fails closed, because keyless signing wants Fulcio and Rekor, and NVIDIA's own air-gap guide tells the operator to drop registry API keys before the disconnected phase.

Delete the graded theater: substring checks for `runasnonroot`, `unittest`, the word `hash`, and the words `health` and `prod`; the `admit` signature that is handed the national id; `str.replace` as log hygiene; unread provenance and limits notes; truncated `sha256:` prefixes treated as image digests; credential JSON sitting in the student pack; a workflow that only discovers unit tests while the sprint sentence says the image is built in CI. Details are in [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) and [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md).

Keep the case: `pol-deploy`, `zone-private` versus `zone-public` versus `zone-hospital`, the register (`local-small` approved and previous, `local-embed`, `ext-large`, lookalike `local-smallx`), the quota that must not spill onto `ext-large`, the clinician who assigns urgency, and the rule that booking from chat still waits. Lesson 5's nightly file into Ain should pass the same promotion gate. That is a sequel, not a second copy of this day.

Do not claim the exercise meets HIPAA, PDPL, or the National Cybersecurity Authority Essential Cybersecurity Controls. Al-Waha is fictional. `pol-deploy` is a course checklist. US HHS audit-control language and the OWASP logging cheat sheet are defensive analogues only.

## Files

| File | Job |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | What `rel-m02-l04` teaches, what `chk-deploy` scores, what it skips |
| [02-industry-research.md](02-industry-research.md) | OCI, probes, Pod Security, SLSA, cosign, model signing, vLLM, NIM, twelve-factor, External Secrets, SOPS, OWASP, HHS, Argo CD, Flux, NetworkPolicy, CycloneDX |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | Three architectures and the air-gapped promotion simulation |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | Laptop constraints, exercises, the rebuilt check, deletions, lessons to spawn |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | Tradeoffs, maturity labels, source list |

## Five sources to read first

1. Pod Security Standards, restricted profile — <https://kubernetes.io/docs/concepts/security/pod-security-standards/>
2. Liveness, readiness, and startup probes — <https://kubernetes.io/docs/concepts/workloads/pods/probes/>
3. NVIDIA NIM air-gap deployment (two phases; no API keys on the isolated side) — <https://docs.nvidia.com/nim/large-language-models/latest/deployment/air-gap-deployment.html>
4. SLSA build track (L1 provenance exists; L2 and L3 are stronger and are not a laptop self-signature) — <https://slsa.dev/spec/v1.2/build-track-basics>
5. OWASP Logging Cheat Sheet (do not record government identifiers or health data) — <https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html>
