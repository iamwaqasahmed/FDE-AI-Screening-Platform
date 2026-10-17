"""Rebuild one profile's data folder from its seed, validate it, and score the baselines against it."""

from __future__ import annotations

from simulation.build import build_world
from simulation.check.invariants import check_world
from simulation.config import active
from simulation.eval.baselines.run import run_all
from simulation.export import write_world
from simulation.paths import DATA
from simulation.prose.compose import summary


def main(repeat: bool = True) -> None:
    profile = active()
    print(f"Profile {profile.name}, seed {profile.seed}, scale {profile.scale}, output {profile.output}")
    world = build_world()
    write_world(world)
    print(f"Prose: {summary()}")
    check_world(world, repeat=repeat)
    print("Scoring baselines...")
    for name, slices in run_all(DATA).items():
        print(f"  {name}: overall pass {slices['overall']['all']['pass_rate']:.2f}")


if __name__ == "__main__":
    main()
