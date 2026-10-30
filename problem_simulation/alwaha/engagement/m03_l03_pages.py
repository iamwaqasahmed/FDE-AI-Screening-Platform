"""Participant pages for rel-m03-l03.
Held-out questions stay out.

These strings are the criteria notice, a rendered document page, and the document-store interface. The notice says a referral keeps the criteria version it started with, and that a draft or an unauthorized document is not citable. The interface covers fetch, search, and the change feed.
"""

from __future__ import annotations

from alwaha.engagement.m03_l03_docs import CASE_DATE, V4


def criteria_note() -> str:
    """Return the criteria notice.

    It names the specialties on v4, says an in-flight referral keeps the version it started with, and says a draft or an unauthorized document is not citable.
    """
    names = f"{', '.join(V4[:-1])}, and {V4[-1]}"
    return f"""# Criteria v4

Criteria v4 is in force for {names}. It is not in force for every specialty. A referral that already started keeps the criteria version it started with.

An unauthorized circular was filed in the document store. A draft can be searched. A draft is not citable. An unauthorized document is not citable.

The change feed is the update. The snapshot is the store before that feed.

Case date: {CASE_DATE}.
"""


def render_doc(doc: dict) -> str:
    return f"""# {doc["title"]}

- doc_id: {doc["doc_id"]}
- family: {doc["family"]}
- status: {doc["status"]}
- effective: {doc["effective"]}
- sunset: {doc["sunset"]}
- site: {doc["site"]}
- audience: {doc["audience"]}
- supersedes: {doc["supersedes"]}
- content_hash: {doc["content_hash"]}
- version: {doc["version"]}
- clause_id: {doc["clause_id"]}

{doc["body"]}
"""


def dms_spec() -> str:
    return """openapi: 3.0.3
info:
  title: dms
  version: "1"
paths:
  /documents/{doc_id}:
    get:
      operationId: fetchDocument
      responses:
        "200":
          description: One document, including status, audience, and the effective window.
  /documents:search:
    post:
      operationId: searchDocuments
      responses:
        "200":
          description: Search hits. A hit is not a citation. Drafts are searchable.
  /feeds/changes:
    get:
      operationId: readChangeFeed
      responses:
        "200":
          description: document.changed events since the snapshot.
"""
