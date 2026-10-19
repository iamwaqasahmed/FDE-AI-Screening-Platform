"""Run the mock APIs without Docker: python -m serve --system all --port 8800."""

from __future__ import annotations

import argparse

import uvicorn

from serve.app import create_app
from serve.settings import SYSTEMS


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="python -m serve", description=__doc__)
    parser.add_argument("--system", default="all", choices=("all", *SYSTEMS))
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8800)
    args = parser.parse_args(argv)
    uvicorn.run(create_app(args.system), host=args.host, port=args.port)


if __name__ == "__main__":
    main()
