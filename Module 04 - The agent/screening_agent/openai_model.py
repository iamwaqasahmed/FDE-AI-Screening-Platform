"""OpenAI-compatible tool-calling client. A missing key raises only when complete() is called."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_MODEL = "gpt-5.6-luna"
_ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
_ENV_LOADED = False


def load_env() -> None:
    global _ENV_LOADED
    if _ENV_LOADED or not _ENV_PATH.is_file():
        _ENV_LOADED = True
        return
    for line in _ENV_PATH.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if not text or text.startswith("#") or "=" not in text:
            continue
        name, value = text.split("=", 1)
        name = name.strip()
        value = value.strip().strip('"').strip("'")
        if name and name not in os.environ:
            os.environ[name] = value
    _ENV_LOADED = True


class OpenAIModel:
    def complete(self, messages: list[dict], tools: list[dict]) -> dict:
        load_env()
        key = os.environ.get("OPENAI_API_KEY", "").strip()
        if not key:
            raise RuntimeError("OPENAI_API_KEY is not set. Add it to .env in the repository root.")
        base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        model = os.environ.get("OPENAI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
        body = json.dumps(
            {
                "model": model,
                "messages": messages,
                "tools": tools,
                "temperature": 0,
                "reasoning_effort": "none",
            }
        ).encode("utf-8")
        request = urllib.request.Request(
            f"{base}/chat/completions",
            data=body,
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Model request failed: {exc.code} {detail}") from exc
        message = payload["choices"][0]["message"]
        calls = message.get("tool_calls") or []
        if calls:
            function = calls[0]["function"]
            raw = function.get("arguments") or "{}"
            return {"type": "tool", "name": function["name"], "arguments": json.loads(raw)}
        return {"type": "final", "answer": message.get("content") or ""}
