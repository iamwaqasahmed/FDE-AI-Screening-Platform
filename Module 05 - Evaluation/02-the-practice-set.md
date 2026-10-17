# The practice set

[practice_cases.jsonl](practice_cases.jsonl) is one JSON object per line. You may add a line. You may not copy `data/eval/cases.jsonl` into it.

A count case names the catalog tool and the figures that tool returns:

- `tool` is `coverage`, `unfinished_photos`, `grader_queue`, `vendor_pilot`, `letter_fields`, or `retrieve`.
- `document_id` is the rule that tool must cite.
- `expect` holds the numbers or the status.

A refusal case sets `expect_refused` to true and `reason` to `diagnosis` or `unsigned_referral`. It has no tool.

The eight lines cover North City coverage, unfinished photos for the whole region, the sight-threatening queue count, the 14-day draft, one result letter, empty vendor labels, a retina grade, and an unsigned referral.

`data/eval` uses older tool names such as `coverage_query` and `session_list`. The scorer maps the ones the catalog can answer. A due-count for a single clinic, or one person's wait, is `unsupported`. That is a gap in the tools, not a wrong answer.

Next: [What is recorded](03-what-is-recorded.md).
