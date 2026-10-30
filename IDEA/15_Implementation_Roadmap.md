# 15 — Implementation roadmap

Nothing in this folder is built yet. The existing lessons stay until a gate’s checker exists. Build in this order. Do not start with the cloud template.

1. **SQLite logs and projectors.** Three logs, three projectors, five extracts, one public reference id. `check` compares a hand-written binding to gold for INV-01 only. Confirm a missing binding fails and a `pass` field is ignored.
2. **INV-01 and INV-02 content.** Prediction file required. Chapter names the mechanism on a different object. A reviewer who does not know gold reads the chapter and lists any graded column that leaked.
3. **INV-03 and INV-04.** Capability and business key. Template fragment for the queue. Policy pack fails a public bucket. Still no live account.
4. **INV-05 and INV-06.** Citation and scorer. Confirm the calibration row’s label is not in the scorer input.
5. **INV-07 and INV-08.** Signal, class function, full template, promotion directory. Re-read the Regions table and the Bedrock model table the week the lab text is frozen. If a Saudi geography exists, update [the AWS document](08_AWS_Implementation.md) and the INV-08 chapter together. Do not update only one.
6. **INV-09 pack.** New nouns. A dry run that pastes INV-01 field names must fail.
7. **Cumulative suite.** Run INV-01 through INV-09 on one seed. Seed `20270110` rebuilds to the same manifest.
8. **Distinctions,** only after the nine checks exist: Postgres, container image, live apply and destroy.

Each investigation is one small change set: a projector or fixture, a student module, a checker, a solution that appears after the check, and a chapter that obeys the prediction rule. One person can review that change set.

## Staffing

Someone who can keep gold out of the student tree. Someone who will re-read cloud tables before INV-08 is published. They can be the same person. They should not be the only reader of the chapter text.

## Pilot

Before writing INV-04 through INV-09 in full prose, pilot INV-01, INV-03, and INV-08 with one reader who has not seen gold. Those three are the easiest to spoil and the easiest to measure. If the reader can name the graded column from the chapter, the chapter is wrong.
