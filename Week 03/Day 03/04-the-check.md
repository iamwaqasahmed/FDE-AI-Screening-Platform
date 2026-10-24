# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check rag --release rel-w3d3 --work "..\Week 03\Day 03\work"
python -m alwaha.check hybrid --release rel-w3d3 --work "..\Week 03\Day 03\work"
python -m alwaha.check acl --release rel-w3d3 --work "..\Week 03\Day 03\work"
```

`chk-w3-rag` scores the citation on the held-out questions: the document, the version, the status, the audience, and the span. It also reads the sprint, the refusal, the audience note, and the knowledge file. A miss says the citation is not the in-force span, a draft is cited, the unauthorized circular is cited, an in-flight referral is restarted on v4, v4 is applied outside its specialties, the answer does not refuse, a staff document is shown to a patient, or the index ignores the change feed. It does not print a doc id, a span, or a clause.

`slice-hybrid` passes when vector search returns the unauthorized neighbor and hybrid search, with the version filter, returns the in-force circular. If vector search is pointed at the hybrid result, the miss says vector search alone clears the slice.

`slice-acl` passes when a patient is not shown the staff leaflet. A filter that keeps every audience fails it.

A watermarked file copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can show the near-duplicate leaflets:

```text
python -m alwaha.demo.duplicate --profile practice
```

The lines are the two titles and that one is superseded. They do not include the clause that tells them apart.

Then write `work/knowledge.md` from [templates/knowledge.md](templates/knowledge.md), with two short answers:

1. What makes a document in force?
2. Who may see a staff document?

The day is done when all three checks print `passed` and the knowledge file has both answers.
