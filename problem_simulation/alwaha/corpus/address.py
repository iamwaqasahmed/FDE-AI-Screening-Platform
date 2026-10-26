"""Address header for a generated document. Status is not fixed to in force.

The header copies status, effective, audience, and the optional sunset, site, and supersedes fields from the spec. A missing optional field is written empty. The content hash is a short hash of the body, so the header changes when the body changes. The return is the header, a blank line, the stripped body, and a trailing newline.
"""

from __future__ import annotations

import hashlib


def render_markdown(spec: dict, body: str) -> str:
    """Return the markdown document: front matter from the spec, then the body."""
    digest = hashlib.sha256(body.encode()).hexdigest()[:16]
    header = "\n".join(
        [
            "---",
            f"doc_id: {spec['doc_id']}",
            f"family: {spec['family']}",
            f"title: {spec['title']}",
            f"status: {spec['status']}",
            f"effective: {spec['effective']}",
            f"sunset: {spec.get('sunset', '')}",
            f"site: {spec.get('site', '')}",
            f"audience: {spec['audience']}",
            f"supersedes: {spec.get('supersedes', '')}",
            f"content_hash: {digest}",
            "---",
            "",
        ]
    )
    return header + body.strip() + "\n"
