"""Run a check against a participant work directory.

Command line for every check. The command name is not unique across the course, so the release argument picks the grader. Later releases are tested before earlier ones that share a name. A shared name that arrives with the wrong release exits before any grader runs. When the miss list is empty, the check id is printed as passed. Any miss prints the id, each sentence, and exits with a failure status. The repository and the interview are the fall-through, after every later release has been rejected.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from alwaha.check.agent import agent_problems
from alwaha.check.approach import approach_problems
from alwaha.check.auth import auth_problems
from alwaha.check.brief import brief_problems
from alwaha.check.deploy_m02 import deploy_problems
from alwaha.check.design import design_problems
from alwaha.check.dispatch_m02_l05 import deploy as m02_l05_deploy
from alwaha.check.dispatch_m02_l05 import individual as m02_l05_individual
from alwaha.check.dispatch_m02_l05 import journey as m02_l05_journey
from alwaha.check.dispatch_m02_l05 import readout as m02_l05_readout
from alwaha.check.dispatch_m03_l01 import identity as m03_l01_identity
from alwaha.check.dispatch_m03_l01 import labels as m03_l01_labels
from alwaha.check.dispatch_m03_l01 import synthetic as m03_l01_synthetic
from alwaha.check.dispatch_m03_l02 import lora as m03_l02_lora
from alwaha.check.dispatch_m03_l02 import model as m03_l02_model
from alwaha.check.dispatch_m03_l03 import acl as m03_l03_acl
from alwaha.check.dispatch_m03_l03 import hybrid as m03_l03_hybrid
from alwaha.check.dispatch_m03_l03 import rag as m03_l03_rag
from alwaha.check.dispatch_m03_l04 import evaluation as m03_l04_eval
from alwaha.check.dispatch_m03_l04 import judge as m03_l04_judge
from alwaha.check.dispatch_m03_l05 import evaluation as m03_l05_eval
from alwaha.check.dispatch_m03_l05 import individual as m03_l05_individual
from alwaha.check.dispatch_m03_l05 import rcp as m03_l05_rcp
from alwaha.check.dispatch_m03_l05 import readout as m03_l05_readout
from alwaha.check.dispatch_m04_l01 import access as m04_l01_access
from alwaha.check.dispatch_m04_l01 import fair as m04_l01_fair
from alwaha.check.dispatch_m04_l01 import privacy as m04_l01_privacy
from alwaha.check.dispatch_m04_l01 import redteam as m04_l01_redteam
from alwaha.check.dispatch_m04_l02 import cache as m04_l02_cache
from alwaha.check.dispatch_m04_l02 import incident as m04_l02_incident
from alwaha.check.dispatch_m04_l03 import slo as m04_l03_slo
from alwaha.check.dispatch_m04_l03 import surge as m04_l03_surge
from alwaha.check.dispatch_m04_l04 import slo as m04_l04_slo
from alwaha.check.dispatch_m04_l05 import individual as m04_l05_individual
from alwaha.check.dispatch_m04_l05 import integrate as m04_l05_integrate
from alwaha.check.dispatch_m04_l05 import ops as m04_l05_ops
from alwaha.check.dispatch_m04_l05 import rcp as m04_l05_rcp
from alwaha.check.dispatch_m04_l05 import readout as m04_l05_readout
from alwaha.check.events import events_problems
from alwaha.check.individual import individual_problems
from alwaha.check.interviews import interview_problems, load_truth
from alwaha.check.journey import journey_problems
from alwaha.check.journey_m02 import journey_problems as journey_m02_problems
from alwaha.check.readout import readout_problems
from alwaha.check.tests_m02 import test_problems
from alwaha.check.ux_m02 import ux_problems
from alwaha.check.repo import repo_problems
from alwaha.check.trajectory import trajectory_problems
from alwaha.config.profile import load
from alwaha.paths import pack_dir, truth_dir
from alwaha.samples.measure import measure_pack


def _m01_l04(which: str, work: Path, profile) -> tuple[str, list[str]]:
    """Return the agent or trajectory result for the first agent release.

    The pack and the agent gold must both exist. The agent command grades state. Anything else asked here is the trajectory. The written note is included.
    """
    pack = pack_dir(profile.name, "rel-m01-l04")
    gold_path = truth_dir(profile.name) / "agent_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m01-l04 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    if which == "agent":
        return "chk-agent", agent_problems(work, pack, gold, profile.canary())
    return "chk-trajectory", trajectory_problems(work, pack, gold, profile.canary())


def _m01_l05_gold(profile) -> tuple[Path, Path, dict]:
    """Return the agent pack, the failure pack, and the merged scenario list.

    The merged list is the first agent day's scenarios followed by the later day's scenarios. Any missing directory or gold file exits with the build sentence.
    """
    pack = pack_dir(profile.name, "rel-m01-l04")
    failures = pack_dir(profile.name, "rel-m01-l05")
    root = truth_dir(profile.name)
    agent_path = root / "agent_gold.json"
    m01_l05_path = root / "m01_l05_gold.json"
    if not pack.is_dir() or not failures.is_dir() or not agent_path.is_file() or not m01_l05_path.is_file():
        raise SystemExit("Build rel-m01-l04 and rel-m01-l05 first.")
    agent_gold = json.loads(agent_path.read_text(encoding="utf-8"))
    m01_l05_gold = json.loads(m01_l05_path.read_text(encoding="utf-8"))
    merged = {"scenarios": agent_gold["scenarios"] + m01_l05_gold["scenarios"]}
    return pack, failures, merged


def _m01_l05_score(which: str, work: Path, profile) -> tuple[str, list[str]]:
    """Return the agent or trajectory result for the later agent release.

    The failure pack is passed in. The written note is turned off because the written commands grade it separately.
    """
    pack, failures, merged = _m01_l05_gold(profile)
    if which == "agent":
        # The note is left off because the written commands grade it separately.
        problems = agent_problems(work, pack, merged, profile.canary(), failures, written=False)
        return "chk-agent", problems
    # The note is left off because the written commands grade it separately.
    problems = trajectory_problems(work, pack, merged, profile.canary(), failures, written=False)
    return "chk-trajectory", problems


def _m01_l05_written(which: str, work: Path, profile) -> tuple[str, list[str]]:
    """Return the design, readout, or personal-trace result for the later written release.

    The failure pack and the day gold must exist. Design is shown every release directory so a citation can name a file from any of them. Readout and the personal trace read the day gold only.
    """
    failures = pack_dir(profile.name, "rel-m01-l05")
    gold_path = truth_dir(profile.name) / "m01_l05_gold.json"
    if not failures.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m01-l05 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    packs = [pack_dir(profile.name, release) for release in ("rel-m01-l01", "rel-m01-l02", "rel-m01-l03", "rel-m01-l04", "rel-m01-l05")]
    if which == "design":
        return "chk-design", design_problems(work, gold, profile.canary(), packs)
    if which == "readout":
        return "chk-readout", readout_problems(work, gold, profile.canary())
    return "chk-individual-m01", individual_problems(work, gold, profile.canary())


def _m01_l03(work: Path, profile) -> tuple[str, list[str]]:
    """Return the worker-check result.

    The worker pack and the events gold must both exist.
    """
    pack = pack_dir(profile.name, "rel-m01-l03")
    gold_path = truth_dir(profile.name) / "events_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m01-l03 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    return "chk-events", events_problems(work, pack, gold, profile.canary())


def _m02_l04(work: Path, profile) -> tuple[str, list[str]]:
    """Return the deploy result for the smoke release.

    The note grader is the default one inside the deploy check.
    """
    pack = pack_dir(profile.name, "rel-m02-l04")
    gold_path = truth_dir(profile.name) / "m02_l04_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m02-l04 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    return "chk-deploy", deploy_problems(work, pack, gold, profile.canary())


def _m02_l03(which: str, work: Path, profile) -> tuple[str, list[str]]:
    """Return the test result or the usability result for the test release.

    The test command grades the suite. Anything else asked here is the usability note.
    """
    pack = pack_dir(profile.name, "rel-m02-l03")
    gold_path = truth_dir(profile.name) / "m02_l03_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m02-l03 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    if which == "tests":
        return "chk-tests", test_problems(work, pack, gold, profile.canary())
    return "chk-ux", ux_problems(work, gold, profile.canary())


def _m02_l02(work: Path, profile) -> tuple[str, list[str]]:
    """Return the webhook-journey result.

    The pack and the gold must both exist.
    """
    pack = pack_dir(profile.name, "rel-m02-l02")
    gold_path = truth_dir(profile.name) / "m02_l02_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m02-l02 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    return "chk-journey", journey_m02_problems(work, pack, gold, profile.canary())


def _m02_l01(which: str, work: Path, profile) -> tuple[str, list[str]]:
    """Return the sign-in result or the status-question result.

    The auth command grades sign-in. Anything else asked here is the status question. Both use the same pack and gold.
    """
    pack = pack_dir(profile.name, "rel-m02-l01")
    gold_path = truth_dir(profile.name) / "m02_l01_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m02-l01 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    if which == "auth":
        return "chk-auth", auth_problems(work, pack, gold, profile.canary())
    return "chk-journey", journey_problems(work, pack, gold, profile.canary())


def _m01_l02(which: str, work: Path, profile) -> tuple[str, list[str]]:
    """Return the approach result or the brief result.

    The measured values come from the pack. The approach command grades the family table. Anything else asked here is the brief.
    """
    pack = pack_dir(profile.name, "rel-m01-l02")
    gold_path = truth_dir(profile.name) / "approach_gold.json"
    if not pack.is_dir() or not gold_path.is_file():
        raise SystemExit("Build rel-m01-l02 first.")
    gold = json.loads(gold_path.read_text(encoding="utf-8"))
    measured = measure_pack(pack)
    if which == "approach":
        return "chk-approach", approach_problems(work, pack, gold, measured, profile.canary())
    return "chk-brief", brief_problems(work, pack, gold, measured, profile.canary())


def main(argv: list[str] | None = None) -> None:
    """Parse the command and print a pass line or the misses.

    The release argument selects which week a shared command name belongs to. Later releases are matched first. A name that arrives with the wrong release exits. The repository and the interview do not take a release. They need the persona truth file. A non-empty miss list prints each sentence and exits with a failure status.
    """
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
            "integrate",
            "ops",
        ),
    )
    parser.add_argument("--work", required=True)
    parser.add_argument("--profile", default=None)
    parser.add_argument("--release", default="")
    args = parser.parse_args(argv)
    profile = load(args.profile)
    work = Path(args.work)
    # Sign-in exists only on the first shell release. Any other release is a usage error.
    if args.which == "auth":
        if args.release != "rel-m02-l01":
            raise SystemExit("auth needs --release rel-m02-l01.")
        name, problems = _m02_l01(args.which, work, profile)
    # The later deploy release is matched first so the earlier deploy arm does not claim the same command.
    elif args.which == "deploy" and args.release == "rel-m02-l05":
        name, problems = m02_l05_deploy(work, profile)
    # What remains must be the smoke-day release. Any other release is a usage error.
    elif args.which == "deploy":
        if args.release != "rel-m02-l04":
            raise SystemExit("deploy needs --release rel-m02-l04 or rel-m02-l05.")
        name, problems = _m02_l04(work, profile)
    elif args.which in {"tests", "ux"}:
        if args.release != "rel-m02-l03":
            raise SystemExit("tests and ux need --release rel-m02-l03.")
        name, problems = _m02_l03(args.which, work, profile)
    # The later journey is matched before the webhook journey and the status question, which share the command name.
    elif args.which == "journey" and args.release == "rel-m02-l05":
        name, problems = m02_l05_journey(work, profile)
    # This release is the webhook journey, matched before the status-question fallback.
    elif args.which == "journey" and args.release == "rel-m02-l02":
        name, problems = _m02_l02(work, profile)
    elif args.which == "journey":
        if args.release != "rel-m02-l01":
            raise SystemExit("journey needs --release rel-m02-l01, rel-m02-l02, or rel-m02-l05.")
        name, problems = _m02_l01(args.which, work, profile)
    elif args.which in {"approach", "brief"}:
        name, problems = _m01_l02(args.which, work, profile)
    elif args.which == "events":
        name, problems = _m01_l03(work, profile)
    # The later agent release rescores with the failure pack and leaves the written note to the written commands.
    elif args.which in {"agent", "trajectory"} and args.release == "rel-m01-l05":
        name, problems = _m01_l05_score(args.which, work, profile)
    # What remains is the first agent release, which grades the trace and the note together.
    elif args.which in {"agent", "trajectory"}:
        name, problems = _m01_l04(args.which, work, profile)
    # Later readouts are matched before the week-one readout, which shares the command name.
    elif args.which == "readout" and args.release == "rel-m04-l05":
        name, problems = m04_l05_readout(work, profile)
    elif args.which == "individual" and args.release == "rel-m04-l05":
        name, problems = m04_l05_individual(work, profile)
    elif args.which == "readout" and args.release == "rel-m03-l05":
        name, problems = m03_l05_readout(work, profile)
    elif args.which == "individual" and args.release == "rel-m03-l05":
        name, problems = m03_l05_individual(work, profile)
    elif args.which == "readout" and args.release == "rel-m02-l05":
        name, problems = m02_l05_readout(work, profile)
    elif args.which == "individual" and args.release == "rel-m02-l05":
        name, problems = m02_l05_individual(work, profile)
    elif args.which in {"identity", "labels", "synthetic"}:
        if args.release != "rel-m03-l01":
            raise SystemExit("identity, labels, and synthetic need --release rel-m03-l01.")
        if args.which == "identity":
            name, problems = m03_l01_identity(work, profile)
        elif args.which == "labels":
            name, problems = m03_l01_labels(work, profile)
        else:
            name, problems = m03_l01_synthetic(work, profile)
    elif args.which in {"model", "lora"}:
        if args.release != "rel-m03-l02":
            raise SystemExit("model and lora need --release rel-m03-l02.")
        if args.which == "model":
            name, problems = m03_l02_model(work, profile)
        else:
            name, problems = m03_l02_lora(work, profile)
    elif args.which in {"rag", "hybrid", "acl"}:
        if args.release != "rel-m03-l03":
            raise SystemExit("rag, hybrid, and acl need --release rel-m03-l03.")
        if args.which == "rag":
            name, problems = m03_l03_rag(work, profile)
        elif args.which == "hybrid":
            name, problems = m03_l03_hybrid(work, profile)
        else:
            name, problems = m03_l03_acl(work, profile)
    # The second-run evaluation is matched before the draft evaluation arm.
    elif args.which == "eval" and args.release == "rel-m03-l05":
        name, problems = m03_l05_eval(work, profile)
    # The proposal is matched before the requirements arm, which shares the command name.
    elif args.which == "rcp" and args.release == "rel-m04-l05":
        name, problems = m04_l05_rcp(work, profile)
    elif args.which == "rcp":
        if args.release != "rel-m03-l05":
            raise SystemExit("rcp needs --release rel-m03-l05 or rel-m04-l05.")
        name, problems = m03_l05_rcp(work, profile)
    elif args.which == "integrate":
        if args.release != "rel-m04-l05":
            raise SystemExit("integrate needs --release rel-m04-l05.")
        name, problems = m04_l05_integrate(work, profile)
    elif args.which == "ops":
        if args.release != "rel-m04-l05":
            raise SystemExit("ops needs --release rel-m04-l05.")
        name, problems = m04_l05_ops(work, profile)
    elif args.which in {"redteam", "privacy", "access", "fair"}:
        if args.release != "rel-m04-l01":
            raise SystemExit("redteam, privacy, access, and fair need --release rel-m04-l01.")
        if args.which == "redteam":
            name, problems = m04_l01_redteam(work, profile)
        elif args.which == "privacy":
            name, problems = m04_l01_privacy(work, profile)
        elif args.which == "access":
            name, problems = m04_l01_access(work, profile)
        else:
            name, problems = m04_l01_fair(work, profile)
    elif args.which in {"incident", "cache"}:
        if args.release != "rel-m04-l02":
            raise SystemExit("incident and cache need --release rel-m04-l02.")
        if args.which == "incident":
            name, problems = m04_l02_incident(work, profile)
        else:
            name, problems = m04_l02_cache(work, profile)
    elif args.which == "surge":
        if args.release != "rel-m04-l03":
            raise SystemExit("surge needs --release rel-m04-l03.")
        name, problems = m04_l03_surge(work, profile)
    # One command name covers the load release and the failover release. Anything else is a usage error.
    elif args.which == "slo":
        if args.release == "rel-m04-l03":
            name, problems = m04_l03_slo(work, profile)
        elif args.release == "rel-m04-l04":
            name, problems = m04_l04_slo(work, profile)
        else:
            raise SystemExit("slo needs --release rel-m04-l03 or rel-m04-l04.")
    # The second-run evaluation was matched above. This arm is the draft day, and the judge exists only here.
    elif args.which in {"eval", "judge"}:
        if args.release != "rel-m03-l04":
            raise SystemExit("eval needs --release rel-m03-l04 or rel-m03-l05. judge needs --release rel-m03-l04.")
        if args.which == "eval":
            name, problems = m03_l04_eval(work, profile)
        else:
            name, problems = m03_l04_judge(work, profile)
    # Every later release that shares these names was rejected above. What remains is the week-one written set.
    elif args.which in {"design", "readout", "individual"}:
        name, problems = _m01_l05_written(args.which, work, profile)
    # The remaining commands are the repository and the interview. They need the persona truth file.
    else:
        truth = truth_dir(profile.name) / "personas.json"
        if not truth.is_file():
            raise SystemExit(f"No truth for {profile.name}. Build rel-m01-l01 first.")
        personas, canary = load_truth(truth)
        if args.which == "repo":
            problems = repo_problems(work, canary)
            name = "chk-repo"
        else:
            problems = interview_problems(work, personas)
            name = "chk-interview"
    if problems:
        print(f"{name} failed.")
        for item in problems:
            print(f"- {item}")
        raise SystemExit(1)
    print(f"{name} passed.")


if __name__ == "__main__":
    main(sys.argv[1:])
