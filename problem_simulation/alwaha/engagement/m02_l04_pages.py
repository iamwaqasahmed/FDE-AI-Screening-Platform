"""Participant pages for rel-m02-l04.
Hashes, tokens, the quota, and the national id stay out.

These strings are the deploy notice, the deployment checklist, the endpoint guide, and the starter dashboard. The interface documents cover health, image admission, and inference. The guide fills in the practice address, the namespace, the endpoint, and the model from the shared constants.
"""

from __future__ import annotations

from alwaha.engagement.m02_l04 import ENDPOINT, MODEL, NAMESPACE, URL, ZONE


def deploy_note() -> str:
    return """# Deploy standard

The deployment standard is in force. Prod credentials are in this pack, and they differ from dev. The inference endpoint has a quota. Read the quota from the registry file.

pol-deploy is the checklist the probe can confirm. A container running as root is rejected. A log line that carries a national id is rejected.

The go-live checklist the security office uses is a separate list.
"""


def policy_note() -> str:
    return """# pol-deploy

The probe can confirm this checklist.

| Id | Check |
| --- | --- |
| non-root | The container user is not root. |
| health-probe | Readiness calls /v1/health. |
| resource-limits | The container has cpu and memory limits. |
| no-phi-in-logs | A log line has no national id. |
| image-provenance | The image carries a provenance label. |
| registered-model-hash | The served hash is on the register. |
"""


def endpoint_guide() -> str:
    return f"""# Endpoint

The practice URL is {URL}.
The namespace is {NAMESPACE}.
The endpoint id is {ENDPOINT}.
The model is {MODEL}, in {ZONE}.

GET /v1/health reports the registered hash, the prompt version, and the endpoint dependency. Read the hash from the register. A near name in the candidate fixture is not a registration.

Dev and prod credentials are different files.
"""


def dashboard_note() -> str:
    return """# Starter dashboard

The dashboard shows request rate, error rate, and model latency.
The rest of the operations stack arrives in a later module.
"""


def health_spec() -> str:
    return """openapi: 3.0.3
info:
  title: health
  version: "1"
paths:
  /v1/health:
    get:
      operationId: readHealth
      responses:
        "200":
          description: Status, the registered model hash, the prompt version, and dependency status.
"""


def registry_spec() -> str:
    return """openapi: 3.0.3
info:
  title: registry
  version: "1"
paths:
  /images:
    post:
      operationId: admitImage
      responses:
        "201":
          description: The image is accepted into the team namespace.
        "422":
          description: Rejected. The user is root, or the log line carries a national id.
"""


def endpoint_spec() -> str:
    return f"""openapi: 3.0.3
info:
  title: endpoint
  version: "1"
paths:
  /infer:
    post:
      operationId: infer
      responses:
        "200":
          description: A completion from {ENDPOINT}.
        "429":
          description: Over the quota. Wait. Do not spill onto ext-large.
"""
