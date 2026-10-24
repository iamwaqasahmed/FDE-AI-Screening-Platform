"""Run a check against a participant work directory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from alwaha.check.agent import agent_problems
from alwaha.check.approach import approach_problems
from alwaha.check.auth import auth_problems
from alwaha.check.brief import brief_problems
from alwaha.check.deploy_w2 import deploy_problems
from alwaha.check.design import design_problems
from alwaha.check.dispatch_w2d5 import deploy as w2d5_deploy
from alwaha.check.dispatch_w2d5 import individual as w2d5_individual
from alwaha.check.dispatch_w2d5 import journey as w2d5_journey
from alwaha.check.dispatch_w2d5 import readout as w2d5_readout
from alwaha.check.dispatch_w3d1 import identity as w3d1_identity
from alwaha.check.dispatch_w3d1 import labels as w3d1_labels
from alwaha.check.dispatch_w3d1 import synthetic as w3d1_synthetic
from alwaha.check.dispatch_w3d2 import lora as w3d2_lora
from alwaha.check.dispatch_w3d2 import model as w3d2_model
from alwaha.check.dispatch_w3d3 import acl as w3d3_acl
from alwaha.check.dispatch_w3d3 import hybrid as w3d3_hybrid
from alwaha.check.dispatch_w3d3 import rag as w3d3_rag
from alwaha.check.dispatch_w3d4 import evaluation as w3d4_eval
from alwaha.check.dispatch_w3d4 import judge as w3d4_judge
from alwaha.check.dispatch_w3d5 import evaluation as w3d5_eval
from alwaha.check.dispatch_w3d5 import individual as w3d5_individual
from alwaha.check.dispatch_w3d5 import rcp as w3d5_rcp
from alwaha.check.dispatch_w3d5 import readout as w3d5_readout
from alwaha.check.dispatch_w4d1 import access as w4d1_access
from alwaha.check.dispatch_w4d1 import fair as w4d1_fair
from alwaha.check.dispatch_w4d1 import privacy as w4d1_privacy
from alwaha.check.dispatch_w4d1 import redteam as w4d1_redteam
from alwaha.check.dispatch_w4d2 import cache as w4d2_cache
from alwaha.check.dispatch_w4d2 import incident as w4d2_incident
from alwaha.check.dispatch_w4d3 import slo as w4d3_slo
from alwaha.check.dispatch_w4d3 import surge as w4d3_surge
from alwaha.check.dispatch_w4d4 import slo as w4d4_slo
from alwaha.check.events import events_problems
from alwaha.check.individual import individual_problems
from alwaha.check.interviews import interview_problems, load_truth
from alwaha.check.journey import journey_problems
from alwaha.check.journey_w2 import journey_problems as journey_w2_problems
from alwaha.check.readout import readout_problems
from alwaha.check.tests_w2 import test_problems
from alwaha.check.ux_w2 import ux_problems
from alwaha.check.repo import repo_problems
from alwaha.check.trajectory import trajectory_problems
from alwaha.config.profile import load
from alwaha.paths import pack_dir, truth_dir
from alwaha.samples.measure import measure_pack


def _day4(which: str, work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w1d4")
    gold_path = truth_dir(profile.name) / "agent_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w1d4 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    if which == "agent":
        return "chk-w1-agent", agent_problems(work, pack, gold, profile.canary())
    return "chk-w1-trajectory", trajectory_problems(work, pack, gold, profile.canary())


def _day5_gold(profile) -> tuple[Path, Path, dict]:
    pack = pack_dir(profile.name, "rel-w1d4")
    failures = pack_dir(profile.name, "rel-w1d5")
    root = truth_dir(profile.name)
    agent_path = root / "agent_gold.json"
    day5_path = root / "day5_gold.json"
    if not pack.is_dir() or not failures.is_dir() or not agent_path.is_file() or not day5_path.is_file():
        raise SystemExit("Build rel-w1d4 and rel-w1d5 first.")
    agent_gold = json.loads(agent_path.read_text(encoding="utf-8"))
    day5_gold = json.loads(day5_path.read_text(encoding="utf-8"))
    merged = {"scenarios": agent_gold["scenarios"] + day5_gold["scenarios"]}
    return pack, failures, merged


def _day5_score(which: str, work: Path, profile) -> tuple[str, list[str]]:
    pack, failures, merged = _day5_gold(profile)
    if which == "agent":
        problems = agent_problems(work, pack, merged, profile.canary(), failures, written=False)
        return "chk-w1-agent", problems
    problems = trajectory_problems(work, pack, merged, profile.canary(), failures, written=False)
    return "chk-w1-trajectory", problems


def _day5_written(which: str, work: Path, profile) -> tuple[str, list[str]]:
    failures = pack_dir(profile.name, "rel-w1d5")
    gold_path = truth_dir(profile.name) / "day5_gold.json"
    if not failures.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w1d5 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    packs = [pack_dir(profile.name, release) for release in ("rel-w1d1", "rel-w1d2", "rel-w1d3", "rel-w1d4", "rel-w1d5")]
    if which == "design":
        return "chk-w1-design", design_problems(work, gold, profile.canary(), packs)
    if which == "readout":
        return "chk-readout", readout_problems(work, gold, profile.canary())
    return "chk-individual-w1", individual_problems(work, gold, profile.canary())


def _day3(work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w1d3")
    gold_path = truth_dir(profile.name) / "events_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w1d3 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    return "chk-w1-events", events_problems(work, pack, gold, profile.canary())


def _w2d4(work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w2d4")
    gold_path = truth_dir(profile.name) / "w2d4_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w2d4 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    return "chk-w2-deploy", deploy_problems(work, pack, gold, profile.canary())


def _w2d3(which: str, work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w2d3")
    gold_path = truth_dir(profile.name) / "w2d3_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w2d3 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    if which == "tests":
        return "chk-w2-tests", test_problems(work, pack, gold, profile.canary())
    return "chk-w2-ux", ux_problems(work, gold, profile.canary())


def _w2d2(work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w2d2")
    gold_path = truth_dir(profile.name) / "w2d2_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w2d2 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    return "chk-w2-journey", journey_w2_problems(work, pack, gold, profile.canary())


def _w2d1(which: str, work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w2d1")
    gold_path = truth_dir(profile.name) / "w2d1_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w2d1 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    if which == "auth":
        return "chk-w2-auth", auth_problems(work, pack, gold, profile.canary())
    return "chk-w2-journey", journey_problems(work, pack, gold, profile.canary())


def _day2(which: str, work: Path, profile) -> tuple[str, list[str]]:
    pack = pack_dir(profile.name, "rel-w1d2")
    gold_path = truth_dir(profile.name) / "approach_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-w1d2 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    measured = measure_pack(pack)
    if which == "approach":
        return "chk-w1-approach", approach_problems(work, pack, gold, measured, profile.canary())
    return "chk-w1-brief", brief_problems(work, pack, gold, measured, profile.canary())


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Check a work directory.")
    parser.add_argument(
        "which",
        choices=(
            "repo",
            "interview",
            "approach",
            "brief",
            "events",
            "agent",
            "trajectory",
            "design",
            "readout",
            "individual",
            "auth",
            "journey",
            "tests",
            "ux",
            "deploy",
            "identity",
            "labels",
            "synthetic",
            "model",
            "lora",
            "rag",
            "hybrid",
            "acl",
            "eval",
            "judge",
            "rcp",
            "redteam",
            "privacy",
            "access",
            "fair",
            "incident",
            "cache",
            "slo",
            "surge",
        ),
    )
    parser.add_argument("--work", required=True)
    parser.add_argument("--profile", default=None)
    parser.add_argument("--release", default="")
    args = parser.parse_args(argv)
    profile = load(args.profile)
    work = Path(args.work)
    if args.which == "auth":
        if args.release != "rel-w2d1":
            raise SystemExit("auth needs --release rel-w2d1.")
        name, problems = _w2d1(args.which, work, profile)
    elif args.which == "deploy" and args.release == "rel-w2d5":
        name, problems = w2d5_deploy(work, profile)
    elif args.which == "deploy":
        if args.release != "rel-w2d4":
            raise SystemExit("deploy needs --release rel-w2d4 or rel-w2d5.")
        name, problems = _w2d4(work, profile)
    elif args.which in {"tests", "ux"}:
        if args.release != "rel-w2d3":
            raise SystemExit("tests and ux need --release rel-w2d3.")
        name, problems = _w2d3(args.which, work, profile)
    elif args.which == "journey" and args.release == "rel-w2d5":
        name, problems = w2d5_journey(work, profile)
    elif args.which == "journey" and args.release == "rel-w2d2":
        name, problems = _w2d2(work, profile)
    elif args.which == "journey":
        if args.release != "rel-w2d1":
            raise SystemExit("journey needs --release rel-w2d1, rel-w2d2, or rel-w2d5.")
        name, problems = _w2d1(args.which, work, profile)
    elif args.which in {"approach", "brief"}:
        name, problems = _day2(args.which, work, profile)
    elif args.which == "events":
        name, problems = _day3(work, profile)
    elif args.which in {"agent", "trajectory"} and args.release == "rel-w1d5":
        name, problems = _day5_score(args.which, work, profile)
    elif args.which in {"agent", "trajectory"}:
        name, problems = _day4(args.which, work, profile)
    elif args.which == "readout" and args.release == "rel-w3d5":
        name, problems = w3d5_readout(work, profile)
    elif args.which == "individual" and args.release == "rel-w3d5":
        name, problems = w3d5_individual(work, profile)
    elif args.which == "readout" and args.release == "rel-w2d5":
        name, problems = w2d5_readout(work, profile)
    elif args.which == "individual" and args.release == "rel-w2d5":
        name, problems = w2d5_individual(work, profile)
    elif args.which in {"identity", "labels", "synthetic"}:
        if args.release != "rel-w3d1":
            raise SystemExit("identity, labels, and synthetic need --release rel-w3d1.")
        if args.which == "identity":
            name, problems = w3d1_identity(work, profile)
        elif args.which == "labels":
            name, problems = w3d1_labels(work, profile)
        else:
            name, problems = w3d1_synthetic(work, profile)
    elif args.which in {"model", "lora"}:
        if args.release != "rel-w3d2":
            raise SystemExit("model and lora need --release rel-w3d2.")
        if args.which == "model":
            name, problems = w3d2_model(work, profile)
        else:
            name, problems = w3d2_lora(work, profile)
    elif args.which in {"rag", "hybrid", "acl"}:
        if args.release != "rel-w3d3":
            raise SystemExit("rag, hybrid, and acl need --release rel-w3d3.")
        if args.which == "rag":
            name, problems = w3d3_rag(work, profile)
        elif args.which == "hybrid":
            name, problems = w3d3_hybrid(work, profile)
        else:
            name, problems = w3d3_acl(work, profile)
    elif args.which == "eval" and args.release == "rel-w3d5":
        name, problems = w3d5_eval(work, profile)
    elif args.which == "rcp":
        if args.release != "rel-w3d5":
            raise SystemExit("rcp needs --release rel-w3d5.")
        name, problems = w3d5_rcp(work, profile)
    elif args.which in {"redteam", "privacy", "access", "fair"}:
        if args.release != "rel-w4d1":
            raise SystemExit("redteam, privacy, access, and fair need --release rel-w4d1.")
        if args.which == "redteam":
            name, problems = w4d1_redteam(work, profile)
        elif args.which == "privacy":
            name, problems = w4d1_privacy(work, profile)
        elif args.which == "access":
            name, problems = w4d1_access(work, profile)
        else:
            name, problems = w4d1_fair(work, profile)
    elif args.which in {"incident", "cache"}:
        if args.release != "rel-w4d2":
            raise SystemExit("incident and cache need --release rel-w4d2.")
        if args.which == "incident":
            name, problems = w4d2_incident(work, profile)
        else:
            name, problems = w4d2_cache(work, profile)
    elif args.which == "surge":
        if args.release != "rel-w4d3":
            raise SystemExit("surge needs --release rel-w4d3.")
        name, problems = w4d3_surge(work, profile)
    elif args.which == "slo":
        if args.release == "rel-w4d3":
            name, problems = w4d3_slo(work, profile)
        elif args.release == "rel-w4d4":
            name, problems = w4d4_slo(work, profile)
        else:
            raise SystemExit("slo needs --release rel-w4d3 or rel-w4d4.")
    elif args.which in {"eval", "judge"}:
        if args.release != "rel-w3d4":
            raise SystemExit("eval needs --release rel-w3d4 or rel-w3d5. judge needs --release rel-w3d4.")
        if args.which == "eval":
            name, problems = w3d4_eval(work, profile)
        else:
            name, problems = w3d4_judge(work, profile)
    elif args.which in {"design", "readout", "individual"}:
        name, problems = _day5_written(args.which, work, profile)
    else:
        truth = truth_dir(profile.name) / "personas.json"
        if not truth.is_file():
            raise SystemExit(f"No truth for {profile.name}. Build rel-w1d1 first.")
        personas, canary = load_truth(truth)
        if args.which == "repo":
            problems = repo_problems(work, canary)
            name = "chk-w1-repo"
        else:
            problems = interview_problems(work, personas)
            name = "chk-w1-interview"
    if problems:
        print(f"{name} failed.")
        for item in problems:
            print(f"- {item}")
        raise SystemExit(1)
    print(f"{name} passed.")


if __name__ == "__main__":
    main(sys.argv[1:])
