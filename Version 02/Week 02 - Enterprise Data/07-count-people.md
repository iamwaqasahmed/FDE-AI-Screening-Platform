# Count people

**Day 3. Data engineer.** Week 1 counted living rows and said aliases were later. Later is this week.

Use version 3. An eligible person has an empty `FLAG` and a local id that does not start with `LX`. Aliases are not extra people. Deceased and moved rows are not eligible. The register rule is `sop-national-v3`. The warehouse SQL is a different rule, and it still counts a deceased flag as eligible.

## By district

Break the same count by `DISTRICT`. Version 3 uses the canonical district names. If your Week 1 code still maps `N. City`, it is mapping a spelling this file no longer uses.

## Coverage

The warehouse marks a person covered when `last_screen_date` is inside twelve months of the snapshot. The SQL comment says the register rule in force uses two years. Version 2 of the national procedure says two years. Version 3 supersedes version 2 and does not shorten the window. Cite `sop-national-v3`, and use 730 days.

Join the warehouse snapshot to version 3 through the reissue batch, keep the eligible people, and count those whose last screen is on or after the snapshot minus 730 days. The warehouse's own covered count is the twelve-month figure. Yours should not equal it.

Death and move flags are written 45 days after the event. A person who died last month can still look eligible. Say so. Do not invent the true flag date. It is not in this drop.

## Fill these findings

| Item | What it holds |
|---|---|
| `eligible_people` | `count` |
| `eligible_by_district` | `counts`, a map of district name to count |
| `coverage` | `people`, `days` (730), `warehouse_months` (12) |

The row count and the warehouse eligible count are both the wrong answer. A count that equals either one fails.

**Finish.** You can recompute the three numbers from version 3 and the warehouse file, and the code does not contain a site name or a month.

Next: [Pathway by site and date](08-pathway-by-site-and-date.md).
