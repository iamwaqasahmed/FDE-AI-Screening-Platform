"""Scan a template fragment. This does not call AWS and does not synth a stack."""

from __future__ import annotations


def scan_template(text: str) -> list[str]:
    problems: list[str] = []
    lowered = text.lower()
    if '"*"' in text or "principal: *" in lowered:
        problems.append("the template uses a wildcard principal")
    if "public-read" in lowered or "publicread" in lowered:
        problems.append("the template grants a public read")
    if "blockpublicacls: false" in lowered or "block_public_acls=false" in lowered:
        problems.append("the template turns public-access blocking off")
    if "akia" in lowered:
        problems.append("the template contains a plaintext secret")
    if "aws::bedrock" in lowered or "aws_bedrock" in lowered:
        problems.append("the template contains a model resource")
    if "0.0.0.0/0" in text:
        problems.append("the template opens a network to the world")
    return problems
