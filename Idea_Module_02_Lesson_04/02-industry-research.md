# 02 — Industry research

Scope: official specs and project docs a self-paced student can read. Maturity labels are about using the idea in this lesson on a laptop, not about whether the upstream project exists. No adoption percentages are claimed. Al-Waha's `pol-deploy` is not a government control. US HIPAA text is cited as a defensive analogue for log design. It is not the law of the fictional cluster, and finishing the exercise is not a HIPAA, PDPL, or NCA control assessment.

## Image identity — Proven

The OCI image configuration (`application/vnd.oci.image.config.v1+json`) is immutable: changing it produces a new image. `config.User` is the default username or uid (`user`, `uid`, `user:group`, `uid:gid`). If the group is omitted, the image's `/etc/passwd` and `/etc/group` supply groups. If `User` is omitted, conversion to a runtime spec leaves `process.user` implementation-defined. A numeric uid is copied through; a name is resolved in the image rootfs. Source: [OCI image config](https://github.com/opencontainers/image-spec/blob/main/config.md) and the rendered spec at <https://specs.opencontainers.org/image-spec/config/>.

Lesson consequence. `USER 1000` is a real config field and is the right classroom default because it does not depend on a passwd entry named `app`. It is not, by itself, admission control. The cluster can override the image user. Kubernetes documents that the pod `securityContext` takes precedence over the image, which matters when the student does not own the base image. Source: [Linux kernel security constraints](https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/).

A registry tag (`patient-access-assistant:m01_l04` in the solution manifest) is a mutable name. Cosign's own sign command says to sign the digest (`@sha256:…` of the full digest) because a tag can move. Source: [cosign sign](https://github.com/sigstore/cosign/blob/main/doc/cosign_sign.md).

## Probes — Proven

Kubernetes runs three probes. A **startup** probe is the only one that runs until it succeeds; liveness and readiness wait for it. Use it when the process is slow to become able to answer, which is the normal case when weights load. A **liveness** failure restarts the container. A **readiness** failure removes the pod from Service endpoints and does not restart it. The docs warn that readiness and liveness do not wait for each other, and that a slow start should be a startup probe with `failureThreshold * periodSeconds` long enough for the worst start, rather than a long liveness interval that also hides deadlocks. Source: [probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/) and the task page <https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/>.

The course contract in design note 08 is one `GET /v1/health` that reports model hash, prompt version, and dependency status. That is a reasonable identity payload. It is a poor single probe. A liveness hit that also checks a downstream endpoint will restart a pod because the model server blipped. NVIDIA's NIM API splits the question: `GET /v1/health/live` returns 200 when the container is running and does not require the model to be loaded; `GET /v1/health/ready` returns 200 when the model is loaded and inference is available. Source: [NIM API reference](https://docs.nvidia.com/nim/large-language-models/latest/reference/api-reference.html) and [architecture](https://docs.nvidia.com/nim/large-language-models/latest/reference/architecture.html).

vLLM's OpenAI-compatible server exposes `GET /health`. The handler returns 200 when `check_health` succeeds and 503 on `EngineDeadError`. It does not return a weight digest. The server documents that `--api-key` authenticates `/v1`, `/v2`, and `/inference` only, and that other routes on the same port, including `/invocations`, stay open. Source: [vLLM health](https://docs.vllm.ai/en/stable/api/vllm/entrypoints/serve/instrumentator/health/) and [OpenAI-compatible server](https://docs.vllm.ai/en/latest/serving/online_serving/openai_compatible_server/). A hospital assistant that copies a vendor health URL without reading what the status code means will mark a still-loading model as ready, or will treat a 503 as "the hash is wrong."

**Laptop.** A stdlib `http.server` can implement `/live`, `/ready`, and a metadata body. No cluster. The student curls it. That is a probe. Importing a function named `health` is a unit test of a dict.

## Admission — Proven

Pod Security Standards are three cumulative profiles: privileged, baseline, and restricted. Restricted is aimed at security-critical applications. On top of baseline it requires, among other controls: `allowPrivilegeEscalation: false`; `runAsNonRoot: true` at the pod or on every container; `runAsUser` unset or non-zero; `capabilities.drop: ["ALL"]`; a `seccompProfile` of `RuntimeDefault` or `Localhost`; and a volume list limited to configMap, csi, downwardAPI, emptyDir, ephemeral, persistentVolumeClaim, projected, and secret. `hostPath`, host namespaces, and privileged mode fail. Source: [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

Pod Security admission applies a level to a namespace with the label `pod-security.kubernetes.io/enforce: restricted` (warn and audit are separate modes). Source: [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/). The lesson's `admit(user, log_line, national_id)` is not this mechanism. A namespace label is cluster admission. A Python function is a useful simulator of the decision, if the decision includes the restricted fields and not only the username string.

The Kyverno CLI validates policies against resources before they are added to a cluster. Source: [Kyverno CLI](https://kyverno.io/docs/kyverno-cli/). **Emerging** as a required install for this audience, **Proven** as an optional checker for a student who already has it. The required path should be a small Python checker so Windows students without a policy binary can finish.

## Supply-chain levels — Proven as a vocabulary, easy to over-claim

SLSA v1.2's build track: L0 is nothing. L1 means provenance exists that identifies the artifact by cryptographic digest and describes how it was built. The spec says L1 provenance may be incomplete or unsigned, and that it is trivial to bypass. L2 means a hosted build platform generates and signs the provenance, so tampering after the build is detectable. L3 means the platform is hardened so the tenant who ran the build cannot forge the provenance. Source: [build track basics](https://slsa.dev/spec/v1.2/build-track-basics), [requirements](https://slsa.dev/spec/v1.2/build-requirements), [spec home](https://slsa.dev/spec/v1.2/).

A student who writes a JSON file called `provenance.md` with the sentence "the image carries a provenance label" has not produced SLSA provenance. An image `LABEL` is mutable config inside the image. SLSA provenance is an attestation about the digest. A laptop signature made with a key the student also holds is a local integrity check. It is not Build L2, because there is no hosted platform inside a trust boundary the tenant cannot reach. Teach L1's shape (digest, builder identity, source revision) and say in the note which level was not reached. **Experimental** inside this course: claiming L3, or standing up a private transparency log.

## Signatures — Proven for images with a local key; Emerging for models; Experimental when air-gapped and keyless

Cosign signs OCI images. Keyless mode uses an OIDC login, a short-lived Fulcio certificate, and the Rekor transparency log. The project warns that the email in that certificate is stored in a public log and cannot be removed. Key mode is `cosign sign --key cosign.key <digest>`. `--tlog-upload=false` skips the public log. Signatures use the OCI referrers API. Source: [signing containers](https://docs.sigstore.dev/cosign/signing/signing_with_containers/) and the [cosign README](https://github.com/sigstore/cosign/blob/main/README.md).

Sigstore model-transparency (`model_signing`) hashes model files or shards into a manifest, signs an in-toto statement whose predicate type is `https://model_signing/signature/v1.0`, and checks the hashes again on verify. It supports Sigstore OIDC and also a plain key or certificate, including PKCS #11. Source: [model-transparency](https://github.com/sigstore/model-transparency/). Signing a multi-gigabyte weight file is **Emerging** as hospital practice and is the right idea. Doing it keyless from an air-gapped ward is **Experimental**: the OIDC flow and the public log are on the internet. The laptop exercise should sign a few-kilobyte stand-in weight file with a local key, or should verify a signature the pack already contains, and should say that this stands in for `model_signing` rather than inventing a signature format.

## Serving containers — Proven products, wrong as a required lab

vLLM publishes `vllm/vllm-openai` and documents `docker run --runtime nvidia --gpus all` with the Hugging Face cache mounted at `/root/.cache/huggingface` and `HF_TOKEN` in the environment. The ROCm and XPU examples add capabilities, `seccomp=unconfined`, or `--privileged`. Source: [Using Docker](https://docs.vllm.ai/en/latest/deployment/docker/). Those flags are how a GPU server starts. They are the opposite of the restricted profile. Metrics are on `/metrics` (Prometheus text). Source: [production metrics](https://docs.vllm.ai/en/latest/usage/metrics/). A student laptop without an NVIDIA GPU cannot run this, and should not be told to copy the flags into `deployment.yaml`.

NVIDIA NIM documents a two-phase air gap. On a connected machine, download the image and the model assets. Transfer them by archive, `scp`, `rsync`, or physical media. On the isolated machine, mount the local model store, set `NIM_MODEL_PATH`, and do not set `NGC_API_KEY` or `HF_TOKEN`. Readiness stays on `/v1/health/ready` and liveness on `/v1/health/live`. The guide shows `--gpus all` and a specific image tag in its example; the air-gapped phase can add `--network none` and then probe from inside the container, because published ports and `--network none` do not combine. Source: [Air-Gap Deployment](https://docs.nvidia.com/nim/large-language-models/latest/deployment/air-gap-deployment.html).

**Lesson use.** NIM is the best public picture of promotion into a disconnected zone. It is **Emerging** as something this cohort will operate, and **out of scope to execute**. Simulate the two phases with directories and a verifier. Do not require NGC, a GPU, or the NIM container. Quote the "do not set the API keys on the isolated side" rule verbatim in the student note, with the URL.

## Config and secrets — Proven

Twelve-factor config is whatever varies between deploys: resource handles, credentials, the canonical hostname. The litmus test is whether the codebase could be made public without compromising credentials. The factor stores config in environment variables and argues against grouping those variables into named environment blocks inside the repo. Source: [The Twelve-Factor App, III. Config](https://12factor.net/config).

Hospital reality still has a dev trust domain and a prod trust domain. The reconciliation is: the platform separates the domains; the process receives one injected value and does not choose a file called `prod.json` from a directory that also contains `dev.json`. External Secrets Operator is a Kubernetes controller. An `ExternalSecret` says what to fetch; a `SecretStore` says how to authenticate; the controller writes a Kubernetes `Secret`. The project tells operators to give the controller least privilege and to consider admission control (OPA or Kyverno) on who may read which keys. Source: [ESO overview](https://external-secrets.io/latest/introduction/overview/).

SOPS encrypts YAML, JSON, ENV, INI, and binary with AWS KMS, GCP KMS, Azure Key Vault, Huawei Cloud KMS, age, or PGP. It is a CNCF sandbox project. Source: [getsops.io](https://getsops.io/docs/). Flux decrypts SOPS-encrypted Secrets at reconcile time when a `Kustomization` sets `decryption.provider: sops`. Flux's guide says to encrypt `data` and `stringData`, not the object metadata, and not to `kubectl apply` the ciphertext and expect pods to read it. Source: [Flux SOPS guide](https://fluxcd.io/flux/guides/mozilla-sops/).

**Laptop.** age plus SOPS needs no cloud KMS. The student encrypts a prod credential with a key that stays in `zone-hospital`'s verifier directory and is absent from `zone-build`'s git tree. Dev uses a different age key. Checking that `prod-` does not occur in the connected-zone tree replaces `credential("prod", pack)`. ESO itself is **Proven** in clusters and **not required** here, because it needs a cluster and an external store. Teach the object model in one page. Implement the separation with SOPS or, if SOPS is not installed, with a pack rule: the prod secret file is absent from the student work tree and is supplied to the process only when the simulator's zone is `zone-private`.

## Logs — Proven as hygiene, not as a compliance badge

OWASP says not to record, among other things, access tokens, secrets, and sensitive personal data such as health data and government identifiers. Record security events (auth failures, access-control failures, admin changes) through one logging path, and keep the logs protected. Source: [Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) and [Proactive Control C9](https://top10proactive.owasp.org/the-top-10/c9-security-logging-and-monitoring/).

HHS's summary of the HIPAA Security Rule says a regulated entity must implement mechanisms to record and examine activity in systems that contain or use ePHI (audit controls), and must protect confidentiality, integrity, and availability of ePHI. Source: [Summary of the HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html). An audit record of "who accessed which case id" is not the same object as a stdout line that contains a national id. The first is the control. The second is a disclosure into a log pipeline that is often less protected than the record store. Design note 04 already plants this: `int-engine` debug logs include PHI since `CHG-2025-118`. This lesson should teach the stdout half. A later lesson should open that planted defect. Neither lesson should say the student has "done HIPAA."

**Do not** teach a detector for real national-id shapes. The pack's synthetic `NID-` token is enough. The robust pattern is an allow-list of log fields (`request_id`, `status`, `model_digest`, `latency_ms`). Fields not on the list are dropped, so the logger never needs to be told the secret.

## GitOps and network policy — Proven tools, Emerging as the required path

Argo CD is a Kubernetes controller that treats Git as the desired state and reports `OutOfSync` when the live objects differ. It syncs automatically or manually. Source: [Argo CD overview](https://argo-cd.readthedocs.io/en/latest/). Flux is a set of controllers with the same GitOps idea, pull-based, and is a CNCF graduated project. Source: [Flux concepts](https://fluxcd.io/flux/concepts/) and [Flux home](https://fluxcd.io/flux/). Flux `OCIRepository` pulls an OCI artifact on an interval and records the resolved digest in status. The published example tracks a tag (`ref.tag: latest`) and shows the status revision as `latest@sha256:…`. Source: [OCIRepository](https://fluxcd.io/flux/components/source/ocirepositories/).

For an air gap, Git as the source of truth is awkward: the disconnected zone may not reach the Git host. The NIM guide's physical transfer is the honest pattern. An OCI tarball that Flux could later pull from a mirror is the cluster-shaped version of that transfer. Installing Argo CD or Flux is **optional**. A Python reconcile loop that diffs a desired directory against a live directory teaches the same control loop in twenty lines and fails in a way the student can read.

`NetworkPolicy` selects pods and restricts ingress and egress at L3/L4. Pods start non-isolated. A policy object does nothing unless the cluster's network plugin implements it. Source: [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/). The lesson should include a default-deny egress policy that allows the assistant to call the weight service and refuses `ext-large`. The simulator enforces it. The note must say a real cluster still needs a plugin (Calico, Cilium, or another implementation listed by the Kubernetes docs).

## SBOM — Proven format, optional tool

CycloneDX 1.7 (ECMA-424, release date on the spec overview 2025-10-21, published 2025-12-10) is an inventory of components, services, and dependencies. The overview says the component model can represent software and machine learning models, and that services can record endpoint URIs, authentication, and trust-boundary crossings. The predicate type `https://cyclonedx.org/bom` is what in-toto users attach. Source: [CycloneDX specification overview](https://cyclonedx.org/specification/overview/).

Syft writes CycloneDX JSON from an image, a directory, or an archive (`syft <source> -o cyclonedx-json`). Source: [Syft SBOM generation](https://oss.anchore.com/docs/guides/sbom/) and [formats](https://oss.anchore.com/docs/guides/sbom/formats/). **Proven** tool, **optional** binary. The required artifact is a small CycloneDX-shaped `bom.json` the student fills by hand for the stand-in image: component name, version, the image digest, and the model component with its digest. If Syft is installed, generating the file from a locally built image replaces the hand copy. A missing SBOM fails promotion. A BOM that names a different digest than the bundle fails promotion.

## What a laptop can run

| Practice | Required on the laptop | Optional |
| --- | --- | --- |
| Digest with `hashlib.sha256` | Yes | |
| Live vs ready HTTP on localhost | Yes | |
| Allow-list logger | Yes | |
| Manifest checker for restricted fields | Yes | Kyverno CLI |
| Dev/prod secret separation | Yes, as files the prod tree is not allowed to contain in clear text | SOPS + age |
| Image build, non-root `docker run` | No | Docker or Podman |
| `cosign sign --key` with `--tlog-upload=false` | No | cosign + a local registry |
| `model_signing` on a tiny weight file | No | the Python package |
| Syft CycloneDX | No | Syft |
| `kind` + Pod Security admission | No | A student who already has it |
| vLLM or NIM | No | A machine with a supported GPU, outside this lesson |
| Argo CD or Flux | No | Appendix |

The course already requires Python and forbids printing the gold secrets. That is enough for the required path.
