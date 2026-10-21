"""Build the world to collect every spec, then report on, fill, or prune the prose cache."""

from __future__ import annotations

from collections import Counter

from simulation.build import build_world
from simulation.prose import cache
from simulation.prose.compose import DRAFTS, SPECS


def run(command: str, family: str, limit: int) -> None:
    build_world()
    specs = [spec for spec in SPECS.values() if not family or spec.family == family]
    missing = [spec for spec in specs if cache.read(spec) is None]
    if command == "status":
        _status(specs, missing)
    elif command == "author":
        _author(missing[: limit or None])
    elif command == "prune":
        stale = cache.stale_entries({spec.key() for spec in SPECS.values()})
        for path in stale:
            path.unlink()
        print(f"Removed {len(stale)} stale cache files.")


def _status(specs, missing) -> None:
    totals = Counter(spec.family for spec in specs)
    gaps = Counter(spec.family for spec in missing)
    for name in sorted(totals):
        print(f"{name:28} {totals[name] - gaps[name]:5} cached / {totals[name]:5}")
    print(f"{'all':28} {len(specs) - len(missing):5} cached / {len(specs):5}")


def _author(missing, workers: int = 8) -> None:
    from concurrent.futures import ThreadPoolExecutor

    from simulation.prose.author import author

    done = failed = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = pool.map(lambda spec: (spec, *author(spec, DRAFTS[spec.doc_id])), missing)
        for index, (spec, ok, issues) in enumerate(results, start=1):
            if ok:
                done += 1
            else:
                failed += 1
                print(f"  {spec.doc_id}: kept the template draft ({'; '.join(issues[:3])})")
            if index % 50 == 0:
                print(f"  {index}/{len(missing)} done", flush=True)
    print(f"Authored {done}, failed {failed}. Commit simulation/prose/cache.")
