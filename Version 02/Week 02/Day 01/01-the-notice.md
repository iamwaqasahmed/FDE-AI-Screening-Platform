# The notice

The morning is a stand-up. You have the Week 1 packs and nothing from later this week.

Open the release readme, [data/rel-w2d1/README.md](../../data/rel-w2d1/README.md). Then read:

1. [notices/fhir-v2.md](../../data/rel-w2d1/notices/fhir-v2.md)
2. [openapi/his-wadi.yaml](../../data/rel-w2d1/openapi/his-wadi.yaml)

`his-wadi` has a new spec. Generate the client from that file. Booking is a later day.

The Day 1 notes still stand. A new conversation uses the same shape and can live in `Week 02/Day 01/work/interviews`.

From `problem_simulation`:

```text
python -m alwaha.interview --persona ea --script "..\Week 02\Day 01\work\interviews\ea.questions.txt"
```

Ask about the API strategy, then which hospitals still send HL7 and where `h-wadi` sits, then where the FHIR notice is. Write what you hear in that persona's notes.

The lead copies [templates/sprint.md](templates/sprint.md) to `work/sprint.md` and sequences the generated client before any booking.
