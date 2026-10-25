# 06 — The pages

Open the finished pages and put them beside yours. `slice-hybrid` and `slice-acl` do not read these pages. A page miss fails only the rag check.

## Refusal

[refusal.md](work/refusal.md). The blank template is only a heading. The check looks for `no document` and `cannot see`. If either is missing, the line is `the refusal copy is missing`.

The finished sentences are the ones in the file:

When no document is in force, say that no document binds the answer.

When the asker cannot see the document, say it is not for them.

## Audience

[audience.md](work/audience.md). The check reads a table whose lines start with `|`. The header is `asker` and `audiences`. The separator row of dashes is skipped.

The patient row contains `public` and must not contain `staff` or `restricted`. The staff row contains `public` and `staff` and must not contain `restricted`. The records row contains `restricted`. Keep the pipe characters. A patient row that also contains staff or restricted fails. A staff row that contains restricted fails. The line is `the audience note lets a patient see a staff document`. The message does not name the document.

| asker | audiences |
| --- | --- |
| patient | public |
| staff | public, staff |
| records | public, staff, restricted |

Next: [07 — Knowledge](07-knowledge.md).
