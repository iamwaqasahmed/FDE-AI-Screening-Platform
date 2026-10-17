"""Schema version negotiation through the Accept-Version header, with versions that publish on an engagement week."""

from __future__ import annotations

from dataclasses import dataclass, field

from fastapi import HTTPException

from serve.settings import Settings


@dataclass(frozen=True)
class VersionPolicy:
    default: str
    versions: tuple[str, ...]
    published_week: dict[str, int] = field(default_factory=dict)

    def available(self, week: int) -> tuple[str, ...]:
        return tuple(version for version in self.versions if self.published_week.get(version, 1) <= week)


def negotiate(policy: VersionPolicy, header: str | None, settings: Settings) -> str:
    wanted = (header or policy.default).strip().lower().removeprefix("v")
    if wanted not in policy.versions:
        raise HTTPException(406, detail=f"unknown version {wanted}; available: {', '.join(policy.available(settings.week))}")
    if wanted not in policy.available(settings.week):
        week = policy.published_week[wanted]
        raise HTTPException(406, detail=f"version {wanted} is published from engagement week {week}")
    return wanted
