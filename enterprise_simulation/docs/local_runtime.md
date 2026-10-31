# Local runtime

Northline runs on this laptop. These commands create no AWS resources.

The account shape for a later cohort is described in `docs/aws_compatibility.md`.

## Requirements

Python 3.12 or newer, with the standard library and SQLite. From `enterprise_simulation`:

```text
$env:PYTHONPATH = "src"
```

## Init

```text
python -m access init
```

`init` clears generated `var/` and `student_pack/`, then writes them from seed `20270110`. The log file is `var/log.sqlite`. The extracts are `student_pack/extracts`. The command prints the seed and the event count.

## Reset

```text
python -m access reset
```

`reset` rebuilds the same generated state and prints `reset`.

## Serve

```text
python -m access serve --port 8088
```

`serve` publishes the JSON files in `student_pack/extracts` at `http://127.0.0.1:8088/extracts`. The process stays in the foreground until Ctrl+C.

## Test

```text
python -m unittest tests.test_simulation tests.test_releases
```

The tests pass a case clock into the functions that care about time.

## Runtime report

```text
python -m access.runtime_check
```

`report` reads the tree and returns a dict. `main` prints that dict as JSON for this `enterprise_simulation` root. The check records the Python version and keeps running when the interpreter is older than 3.12. It looks for `src/access`, `tests`, and `docs`, and for `var/log.sqlite` and `student_pack/extracts` after a build. Absent paths are listed in `missing`. The check does not rebuild them. When `student_pack` is absent, its status is `missing`. When the pack is present, the check reads the pack text and lists any file containing `dec-accept` or `refused` in `leaks`.

`notes` states that AWS apply and cdk synth are not part of this check. The check makes no network calls.
