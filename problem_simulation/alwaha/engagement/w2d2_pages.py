"""Participant pages for rel-w2d2. Hidden field names stay out of these strings."""

from __future__ import annotations


def notice() -> str:
    return """# Feeds

eref pushes referral.submitted. The webhook fixture is in this pack.

WhatsApp is open beside SMS.

HL7 v2 from h-nakhl and h-safra arrives through int-engine. The sample is in this pack.

The schema registry lists the fields a consumer may trust. A field that is not listed is ignored.
"""


def registry() -> str:
    return """# Schema registry

| Topic | Version | Owner | Required fields |
| --- | --- | --- | --- |
| referral.submitted | 1 | eref | event_id, topic, occurred_at, sequence, referral_id, patient_key, letter |
| session.cancelled | 1 | hospital | event_id, topic, occurred_at, sequence, booking_id, session_id, facility_id, slot |

A consumer ignores a field it does not know. session.cancelled is owned by the hospital that holds the session.
"""


def eref_spec() -> str:
    return """openapi: 3.0.3
info:
  title: eref
  version: "2"
paths:
  /referrals/{referral_id}:
    get:
      operationId: readReferral
      responses:
        "200":
          description: Polling is the previous intake.
  /subscriptions/referral.submitted:
    post:
      operationId: subscribeReferralSubmitted
      responses:
        "202":
          description: Webhook subscription.
"""


def sms_spec() -> str:
    return """openapi: 3.0.3
info:
  title: sms
  version: "1"
paths:
  /messages:
    post:
      operationId: sendMessage
      responses:
        "202":
          description: Accepted. A receipt follows.
  /receipts/{id}:
    get:
      operationId: readReceipt
      responses:
        "200":
          description: Receipt.
"""


def wa_spec() -> str:
    return """openapi: 3.0.3
info:
  title: wa
  version: "1"
paths:
  /messages:
    post:
      operationId: sendTemplate
      parameters:
        - name: template
          in: query
          required: true
          schema:
            type: string
      responses:
        "202":
          description: Accepted inside the session window.
        "409":
          description: The session window has closed.
"""


def wa_note() -> str:
    return """# WhatsApp

A template message needs a registered template. A reply after the session window is rejected.

SMS remains the channel this day's check scores.
"""


def dms_note() -> str:
    return """# dms

The change feed is not part of today's check.
"""
