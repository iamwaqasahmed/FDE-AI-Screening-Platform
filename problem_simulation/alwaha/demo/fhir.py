"""Show a v1 his-wadi client fail, then the generated client succeed.

The starter client is loaded from W2D1_APP. A second client is rendered from the current spec into a temporary file and loaded from that path. Both clients read the same body. The page prints a fixed line for each result.
"""

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
    """Load a module from a file path and return it.

    name is the module name importlib records. A spec with no loader cannot be executed, so that case raises before exec_module.
    """
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    # A spec with no loader has nothing to execute.
    if spec.loader is None:
        raise RuntimeError(name)
    spec.loader.exec_module(module)
    return module


def main(argv: list[str] | None = None) -> None:
    """Print the v1 result and the generated-client result. Returns nothing.

    argv replaces the process arguments. The profile is loaded, the spec is rendered into a temporary client, and both clients read the same reference body. The printed lines name success or failure and do not print the body.
    """
    # Read the profile argument. Omitting it uses the environment default.
    parser = argparse.ArgumentParser(description="Read his-wadi with a v1 client, then a generated client.")
    parser.add_argument("--profile", default=None)
    args = parser.parse_args(argv)
    load(args.profile)
    spec = his_wadi_spec()
    # Load the starter client and the generator from the week 2 day 1 app.
    starter = _load(W2D1_APP / "client.py", "w2d1_v1_client")
    generate = _load(W2D1_APP / "generate.py", "w2d1_generate")
    # Render a second client into a temporary file and load that file.
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "client.py"
        path.write_text(generate.render(generate.fields(spec)), encoding="utf-8", newline="\n")
        generated = _load(path, "w2d1_v2_client")
    # Both clients read the same reference. The printed lines say ok or failed.
    v1 = read(starter.read_body("ref-status"), FIELD, REMOVED)
    v2 = read(generated.read_body("ref-status"), FIELD, REMOVED)
    print("v1 client: his-wadi read failed" if not v1["ok"] else "v1 client: his-wadi read ok")
    print("v2 client: his-wadi read ok" if v2["ok"] else "v2 client: his-wadi read failed")


if __name__ == "__main__":
    # A direct run prints the page. Importing this module does not.
    main(sys.argv[1:])
