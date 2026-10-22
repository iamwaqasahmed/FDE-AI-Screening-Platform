# Two interviews

The product seat picks two personas. The cards are `data/rel-w1d1/personas/`. The ids are `cdo`, `med-dir`, `access-mgr`, `phc-lead`, `coord-lead`, `dpo`, `ciso`, `ea`, `bi-lead`, `finance`, `patient-rep`, and `vendor`.

Each person will say one thing first. That sentence is a claim. A later answer appears only if you ask for it, and a follow-up is heard only after the topic it hangs from. Twelve questions is the budget for one persona. You are submitting two.

Write one question per line in:

```text
work/interviews/<id>.questions.txt
```

Run it from `problem_simulation`. Point `--script` at that file. Send the answers to a transcript you can read:

```text
python -m alwaha.interview --persona phc-lead --script "..\Week 01\Day 01\work\interviews\phc-lead.questions.txt"
```

If the answer repeats the opening line, the question missed. Ask a narrower one. A question about a returned referral can be followed by a question about the form that produced it. Use that shape on the other persona too: one topic, then the thing that topic is made of.

Write `work/interviews/<id>.notes.md` as a table. Kind is `claim`, `request`, or `fact`.

```text
| Who | Their words | Kind |
| --- | --- | --- |
| phc-lead | Hospitals return referrals arbitrarily | claim |
| phc-lead | Ask what the return looks like on the page | request |
```

A claim is their sentence. A request is what you will do next. A fact is something you could point at in a file. Two rows is the minimum. Label the opening line as a claim. Do not promote it because it was said with confidence.

Submit exactly two personas. A third script is not a stronger interview.
