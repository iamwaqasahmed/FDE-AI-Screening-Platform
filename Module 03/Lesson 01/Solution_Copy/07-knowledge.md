# 07 — Knowledge

This answers the knowledge file from the morning. Open the finished [knowledge.md](work/knowledge.md) and put it beside yours.

The check reads two numbered lines. A second sentence on the next line does not count. The first line has to contain `row` and `patient`, and one of `mother`, `twin`, `mrn`, or `national`. The second line has to contain `fidelity`, and one of `synthetic`, `specialty`, `phrase`, or `real`. When there are fewer than two numbered lines, the message is `knowledge.md needs two answers`. When the first line is wrong, the message is `knowledge.md does not say why a row is not a patient`. When the second line is wrong, the message is `knowledge.md does not say what a fidelity card compares`. The messages do not name a national id or a rate.

The finished sentences are these.

## Why is a row count not a patient count?

A row count is not a patient count because a mother and a newborn can share a national id, twins can share a phone, and an MRN can be reused.

[identifiers.jsonl](sources/release/history/identifiers.jsonl) is where those three cases sit. The mother and the newborn share a national id. The twins share a phone. `reuse-a` and `reuse-b` share an MRN. The first knowledge line says the same thing in one sentence. It does not copy an id from the file.

## What does a fidelity card compare?

A fidelity card compares a synthetic sample with the real specialty mix, the phrase frequencies, and the label margins.

[fidelity.json](sources/release/cards/fidelity.json) is the card. The second knowledge line names the three comparisons. It does not print a rate.

You have the finished day. The trainer's session is [08 — Trainer session](08-trainer.md).

## Carry this forward

You leave Module 3, Lesson 1 with one person-level waitlist, a label sample under ann-v2, and a synthetic sample that passes the fidelity card. A mother and a newborn stayed two people.

Still today, the ruling is signed in the next lesson. You serve a registered adapter inside the quota and the price cap. The cloud fine-tune is closed. The file drop is `rel-m03-l02`.

The trainer chapter, if this page links one, is optional. Tomorrow's lesson is the [Module 3, Lesson 2 student copy](<../../Lesson 02/Student_Copy/README.md>), starting at its background.
