"""INV-08. boundary() classifies each fixture, including a mixed object."""

from __future__ import annotations

from pathlib import Path

from access.checks.runtime import load_module
from access.checks.template_policy import scan_template
from access.sealed_holdouts import BYTES
from access.sealed_release import RESTRICTED_NAMES


def grade_boundary(path: Path) -> list[str]:
    module, problems = load_module(path)
    if module is None:
        return problems
    fn = getattr(module, "boundary", None)
    if not callable(fn):
        return ["the artifact does not define boundary"]
    template = getattr(module, "TEMPLATE", None)
    if not isinstance(template, str) or not template.strip():
        problems.append("the account template is missing")
    else:
        problems.extend(scan_template(template))
    for item in BYTES:
        try:
            got = fn(item)
        except Exception:
            problems.append(f"the boundary function raised on {item['name']}")
            continue
        if not isinstance(got, dict):
            problems.append(f"the boundary function returned no record for {item['name']}")
            continue
        problems.extend(_judge(item, got))
    return problems


def _judge(item: dict, got: dict) -> list[str]:
    upload = got.get("upload")
    restricted = any(name in RESTRICTED_NAMES for name in item["contains"])
    if restricted and upload is not False:
        if item["name"] == "letter-match":
            return ["a matching processor region was treated as permission"]
        return ["a restricted fixture is on the asset list"]
    if not restricted and upload is not True:
        return ["a public leaflet was kept off the asset list"]
    return []
