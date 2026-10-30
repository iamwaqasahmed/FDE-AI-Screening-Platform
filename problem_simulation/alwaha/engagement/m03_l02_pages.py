"""Participant pages for rel-m03-l02.
Hashes, the quota, and the canary stay out.

These strings are the ruling and the router interface. The ruling says where training stays, which fields stay off the external model, and which questions stay on retrieval. The router describes a call that is allowed and a call that is refused.
"""

from __future__ import annotations

from alwaha.engagement.m03_l02 import CASE_DATE


def ruling_note() -> str:
    return f"""# Ruling

The ruling is signed. Patient data stays off the external model ext-large. Training stays on the private cloud. A cloud fine-tune is closed.

These fields are phi, and they stay off ext-large: national id, date of birth, name, and phone.

Clinic hours and public leaflets may leave the private cloud. Hours questions stay on retrieval.

The approved hashes are in the model register. The GPU quota is a count of GPUs. The price cap is beside it.

Case date: {CASE_DATE}.
"""


def router_spec() -> str:
    return """openapi: 3.0.3
info:
  title: router
  version: "1"
paths:
  /route:
    post:
      operationId: routeCall
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [model, hash]
              properties:
                model:
                  type: string
                hash:
                  type: string
                fields:
                  type: array
                  items:
                    type: string
      responses:
        "200":
          description: The call is allowed. The hash is on reg-models, and a phi field was not sent to ext-large.
        "403":
          description: Refused. A phi field was sent to ext-large, or the hash is not on reg-models.
"""
