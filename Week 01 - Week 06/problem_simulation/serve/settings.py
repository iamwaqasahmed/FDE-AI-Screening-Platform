"""Runtime settings for the mock APIs, read from the environment each time an app is built."""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from datetime import datetime, time
from pathlib import Path

SERVE_DIR = Path(__file__).resolve().parent
VERSION_ROOT = SERVE_DIR.parent
SYSTEMS = ("registry", "booking", "letters", "ophthalmology", "vendor")
DEFAULT_CLOCK = "2026-10-01"


@dataclass(frozen=True)
class Settings:
    data_root: Path
    clock: datetime
    week: int
    booking_debug: bool
    tokens_path: Path
    log_dir: Path

    @property
    def handover(self) -> Path:
        return self.data_root / "handover"


def parse_clock(value: str) -> datetime:
    text = value.strip()
    if len(text) == 10:
        return datetime.combine(datetime.fromisoformat(text).date(), time(23, 59, 59))
    return datetime.fromisoformat(text).replace(tzinfo=None)


def _env_path(name: str, default: Path) -> Path:
    value = os.environ.get(name, "")
    return Path(value).resolve() if value else default.resolve()


def load_settings() -> Settings:
    return Settings(
        data_root=_env_path("HARTLAND_DATA", SERVE_DIR / ".." / ".." / "data"),
        clock=parse_clock(os.environ.get("HARTLAND_CLOCK", DEFAULT_CLOCK)),
        week=int(os.environ.get("HARTLAND_WEEK", "1")),
        booking_debug=os.environ.get("HARTLAND_BOOKING_DEBUG", "1") != "0",
        tokens_path=_env_path("HARTLAND_TOKENS", SERVE_DIR / "tokens.yaml"),
        log_dir=_env_path("HARTLAND_LOG_DIR", SERVE_DIR / "runtime" / "logs"),
    )


def ensure_simulation_path() -> None:
    root = str(VERSION_ROOT)
    if root not in sys.path:
        sys.path.insert(0, root)
