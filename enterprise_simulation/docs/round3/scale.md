# Round-3 stress scale

`stress_commands` is opt-in. `history()` does not import it, and `python -m access init` leaves these rows out of the default log. This set is not the student pack.

## What it emits

`stress_commands(count=2000, seed=20270110)` returns one dict per index `n` from 0 through `count - 1`. The field formulas are closed, so a given `count` always returns the same list. `seed` is the project seed and does not change a field.

- `command_id` is `cmd-r3i-{n}`.
- `authority` cycles `hospital`, `channel`, then `payer`.
- `stream_id` is `r3i-{authority}-{n // 50}`, so each stream carries many revisions and the authority is part of the id.
- `stream_rev` is `(n % 50) + 1`.
- `type` is `StressTick`.
- `occurred_at` starts at `2026-04-01T00:00:00Z` and steps one minute per index.
- `payload` is `ref` `R3I-{n}`, `n`, `queue_depth` `(n * 3) % 500`, and `retry` `1` when `n % 17 == 0`, else `0`.

## Materialize

From `enterprise_simulation`, set `PYTHONPATH` to `src`, then:

```text
python -c "from access.round3.scale import time_build; print(time_build(2000))"
```

`time_build` builds the command list, opens a temporary SQLite file, calls `access.logs.init_db` and `append_all`, and returns `commands`, `seconds`, and `events`. The temporary directory is removed before the function returns. The function leaves `enterprise_simulation/var` untouched.

To keep a log, choose a directory outside this repo and outside the student pack, call `stress_commands`, then `init_db` and `append_all` on that path.
