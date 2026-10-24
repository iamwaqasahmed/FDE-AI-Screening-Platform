"""Address header for a generated document. Status is not fixed to in force."""

from __future__ import annotations

import hashlib


def render_markdown(spec: dict, body: str) -> str:
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
