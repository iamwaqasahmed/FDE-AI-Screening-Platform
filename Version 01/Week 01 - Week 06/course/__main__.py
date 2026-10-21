"""Run a Week 01 - Week 06 module tool.

    python -m course discovery_check --work <folder> [--data data] [--rerun]
    python -m course reference_discovery --data <build> --out <dir> --profile <name>
    python -m course discovery_check.key --data <build>
    python -m course enterprise_check --work <folder> [--data data] [--rerun]
    python -m course reference_enterprise --data <build> --out <dir> --profile <name>
    python -m course enterprise_check.key --data <build>
    python -m course evidence_check --work <folder> [--data data] [--rerun]
    python -m course evidence_check.questions --data <build> --out questions.jsonl
    python -m course evidence_check.baseline --name keyword|tfidf --data <build> --out <file>
    python -m course evidence_check.score --answers <file> [--data <build>] [--baseline]
    python -m course reference_evidence --data <build> --out <dir> --profile <name>
    python -m course evidence_check.key --data <build>
    python -m course graph_check --work <folder> [--data data] [--rerun]
    python -m course graph_check.questions --data <build> --out questions.jsonl
    python -m course graph_check.baseline --name keyword|tfidf --data <build> --out <file>
    python -m course graph_check.score --answers <file> [--data <build>] [--baseline]
    python -m course reference_graph --data <build> --out <dir> --profile <name>
    python -m course graph_check.key --data <build>
    python -m course agent_check --work <folder> [--data data] [--rerun]
    python -m course agent_check.questions --data <build> --out questions.jsonl
    python -m course agent_check.baseline --name single_loop|keyword_veto --data <build> --out <file>
    python -m course agent_check.score --answers <file> [--data <build>] [--baseline]
    python -m course reference_agent --data <build> --out <dir> --profile <name>
    python -m course agent_check.key --data <build>
    python -m course handoff_check --work <folder> [--data data] [--rerun]
    python -m course reference_handoff --data <build> --out <dir> --profile <name>
    python -m course handoff_check.key --data <build>
"""

from __future__ import annotations

import os
import runpy
import sys

USAGE = "Usage: python -m course <discovery_check|enterprise_check|evidence_check|graph_check|agent_check|handoff_check|reference_discovery|reference_enterprise|reference_evidence|reference_graph|reference_agent|reference_handoff> ..."


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(USAGE)
    profile = _profile(sys.argv[2:])
    if profile:
        os.environ["HARTLAND_PROFILE"] = profile
    from course import install

    install()
    module = sys.argv[1]
    sys.argv = [module, *sys.argv[2:]]
    runpy.run_module(module, run_name="__main__")


def _profile(argv: list[str]) -> str:
    if "--profile" in argv:
        return argv[argv.index("--profile") + 1]
    return ""


if __name__ == "__main__":
    main()
