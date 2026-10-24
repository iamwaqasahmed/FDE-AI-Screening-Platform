"""Show a v1 his-wadi client fail, then the generated client succeed."""

from __future__ import annotations

import argparse
import importlib.util
import sys
import tempfile
from pathlib import Path

from alwaha.config.profile import load
from alwaha.engagement.w2d1 import FIELD, REMOVED, his_wadi_spec
from alwaha.paths import W2D1_APP
from alwaha.serve.fhir import read


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError(name)
    spec.loader.exec_module(module)
    return module


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Read his-wadi with a v1 client, then a generated client.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    spec = his_wadi_spec()
    starter = _load(W2D1_APP / "client.py", "w2d1_v1_client")
    generate = _load(W2D1_APP / "generate.py", "w2d1_generate")
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "client.py"
        path.write_text(generate.render(generate.fields(spec)), encoding="utf-8", newline="\n")
        generated = _load(path, "w2d1_v2_client")
    v1 = read(starter.read_body("ref-status"), FIELD, REMOVED)
    v2 = read(generated.read_body("ref-status"), FIELD, REMOVED)
    print("v1 client: his-wadi read failed" if not v1["ok"] else "v1 client: his-wadi read ok")
    print("v2 client: his-wadi read ok" if v2["ok"] else "v2 client: his-wadi read failed")


if __name__ == "__main__":
    main(sys.argv[1:])
