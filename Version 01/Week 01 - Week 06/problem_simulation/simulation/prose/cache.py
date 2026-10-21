"""The committed prose cache. One Markdown body per spec hash, grouped by family."""

from __future__ import annotations

from pathlib import Path

from simulation.prose.spec import FactSpec

CACHE = Path(__file__).resolve().parent / "cache"


def path_for(spec: FactSpec) -> Path:
    return CACHE / spec.family / f"{spec.doc_id}--{spec.key()}.md"


def read(spec: FactSpec) -> str | None:
    path = path_for(spec)
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def write(spec: FactSpec, text: str) -> Path:
    path = path_for(spec)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")
    return path


def stale_entries(live_keys: set[str]) -> list[Path]:
    """Cache files whose spec no longer exists. Safe to delete after a fact change."""
    if not CACHE.exists():
        return []
    return [path for path in CACHE.rglob("*.md") if path.stem.split("--")[-1] not in live_keys]
