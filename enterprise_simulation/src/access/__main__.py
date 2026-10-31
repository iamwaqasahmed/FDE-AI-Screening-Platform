"""Command line. Run from enterprise_simulation with PYTHONPATH=src."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from access.checks.router import grade_release
from access.http_view import serve
from access.paths import root_from, var_dir
from access.round2.cohort import summarize, workload
from access.world import reset


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="access")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init")
    sub.add_parser("reset")
    scenario = sub.add_parser("scenario")
    scenario.add_argument("--name", required=True)
    work = sub.add_parser("workload")
    work.add_argument("--count", type=int, default=400)
    view = sub.add_parser("serve")
    view.add_argument("--port", type=int, default=8088)
    check = sub.add_parser("check")
    check.add_argument("--release", default="INV-01")
    check.add_argument("--binding")
    check.add_argument("--artifact")
    args = parser.parse_args(argv)
    root = root_from()
    if args.cmd == "init":
        reset(root)
        manifest = json.loads((root / "var" / "manifest.json").read_text(encoding="utf-8"))
        print(json.dumps({"seed": manifest["seed"], "events": len(manifest["events"])}))
        return 0
    if args.cmd == "reset":
        reset(root)
        print("reset")
        return 0
    if args.cmd == "scenario":
        reset(root, args.name)
        manifest = json.loads((root / "var" / "manifest.json").read_text(encoding="utf-8"))
        print(json.dumps({"scenario": manifest["scenario"], "events": len(manifest["events"])}))
        return 0
    if args.cmd == "workload":
        rows = workload(count=args.count)
        folder = var_dir(root)
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / "workload.jsonl"
        with path.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, sort_keys=True) + "\n")
        summary = summarize(rows)
        summary["commands"] = len(rows)
        summary["path"] = "var/workload.jsonl"
        (folder / "workload_summary.json").write_text(
            json.dumps(summary, indent=2) + "\n",
            encoding="utf-8",
        )
        print(json.dumps(summary))
        return 0
    if args.cmd == "serve":
        server = serve(root, args.port)
        print(f"http://127.0.0.1:{args.port}/extracts")
        server.serve_forever()
        return 0
    binding = Path(args.binding) if args.binding else None
    artifact = Path(args.artifact) if args.artifact else None
    problems = grade_release(args.release, root, binding, artifact)
    if problems:
        print("\n".join(problems))
        return 1
    print("satisfactory")
    return 0


if __name__ == "__main__":
    sys.exit(main())
