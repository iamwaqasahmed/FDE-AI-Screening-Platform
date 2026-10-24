# The scripts

Read [usability/scripts.jsonl](../../data/rel-w2d3/usability/scripts.jsonl), [standards/access.md](../../data/rel-w2d3/standards/access.md), and [calendar/cases.json](../../data/rel-w2d3/calendar/cases.json).

The product manager copies [templates/usability.md](templates/usability.md) to `work/usability.md`. Finish `status-short` and `caregiver`. Cite the clause ids. One script uses a caregiver.

The AI or data engineer copies [templates/fixtures.md](templates/fixtures.md) to `work/fixtures.md`. The journey reads the recorded fixture and asserts the mock state.

The architect copies [templates/crossings.md](templates/crossings.md) to `work/crossings.md`. The receipt row is case `receipt`, from `zone-private`, to `partner`. The calendar row is case `calendar`, and both zones are `zone-private`.

The lead copies [templates/dod.md](templates/dod.md) to `work/dod.md` and adds `receipt-late`. The suite goes red when that switch is on.

Two readings are advanced. They are not in today's check.

- [calendar/hijri.json](../../data/rel-w2d3/calendar/hijri.json). A property check that a due date is never Friday or Saturday. Write it in `work/hijri.md`.
- The phone-only script is `pop-literacy`. Do not add it to today's table.
