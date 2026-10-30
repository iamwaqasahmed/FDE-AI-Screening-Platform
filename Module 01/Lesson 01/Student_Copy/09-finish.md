# 09 — Finish

Two checks grade the pipeline, the access request, and the two interviews. The knowledge file is still part of done. The trainer reads it against the solution. The checker does not print a score for it.

Use the failure table at the bottom only when a check fails. It is not more work.

## Do this

1. Open a terminal in the course folder, the same way as chapter 01. Then run:

```text
cd problem_simulation
python -m alwaha.check repo --work "../Module 01/Lesson 01/Student_Copy/work" --profile practice
python -m alwaha.check interview --work "../Module 01/Lesson 01/Student_Copy/work" --profile practice
```

2. Create `work/knowledge.md` and answer both questions in your own sentences. You already have the answers in files you read today:

- Question 1 is the G0 line in [pol-stage-gate.md](packet/kickoff/corpus/pol-stage-gate.md), which you wrote about in [chapter 05](05-the-kickoff.md). To pass G0, the problem, the users, and the sponsor are named. Naming them is not the same as accepting the sponsor's sentence.
- Question 2 needs both pages. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) is what stays out: patient data, secrets, unpublished cluster documents, the sample referral letter, and the watermark. [Chapter 07](07-the-pipeline.md) is what may be shown: code you wrote, the tests, and that published rule. The policy file does not name those three. Your answer includes the allow-list and the prohibitions.
- The zone rows are the ones you already put in [notes/zones.md](notes/zones.md), from [zones.md](packet/kickoff/world/zones.md).

Copy the zone sketch from [notes/zones.md](notes/zones.md) into the bottom of `knowledge.md`.

```text
# Knowledge

1. What must be true to pass gate G0?

Your answer.

2. What may a coding assistant be shown on this engagement?

Your answer.

## Zones

| Zone | What sits there |
| --- | --- |
| zone-hospital | |
| zone-private | |
| zone-public | |
```

The zone rows come from [packet/kickoff/world/zones.md](packet/kickoff/world/zones.md) only. `zone-hospital` holds `h-nakhl`, `h-safra`, and `h-ain`. Ain is the diabetes and eye center, not a fourth hospital. `zone-private` holds `h-wadi`, and the zone line also names `site-a` and `site-b`. `zone-public` is the external model. That row has no hospital. Do not invent one.

## You should now see

```text
chk-repo passed.
chk-interview passed.
```

`work/knowledge.md` has both answers and three zone rows.

## If a check fails

A failed check names the problem. An incomplete interview does not name the missing fact. Go back to the questions.

| What it prints | Where to go |
| --- | --- |
| `access request is missing` a field | [Chapter 06](06-the-access-request.md). The value sits on the same line as the label |
| `credentials/dev.json is missing` or `credentials do not match this profile` | [Chapter 01](01-setup.md). From `Module 01/Lesson 01/Student_Copy`, run `python prepare_work.py` again. Then run the chapter 01 build with `--profile practice` |
| `health test failed` or `secret scan failed` | [Chapter 07](07-the-pipeline.md). Run the two commands inside `work/` and remove the file the scan names |
| `assistant-use rule is not the cluster document` | Restore `work/policy/pol-assistant-use.md` from `packet/starter/policy/pol-assistant-use.md` |
| `ci workflow is missing the scan or the evaluation-gate placeholder` | Restore `work/.github/workflows/ci.yml` from the starter. Leave the `evaluation-gate` comment in the file |
| `submit exactly two interview scripts` | [Chapter 08](08-the-interviews.md). Keep exactly two `*.questions.txt` files |
| `unknown persona` | The file name before `.questions.txt` is the card id |
| `missing notes` | Add `work/interviews/<id>.notes.md` for that same id |
| `<id> interview is incomplete` | The questions have not yet reached what that person will say. Ask a narrower question. Ask the topic before its follow-up. The check will not name the missing fact |
| `notes need a table with a Kind column` | Use the header in chapter 08, with `Kind` as a column |
| `each note needs at least two rows marked claim, request, or fact` | Add rows until there are two, and use only those three words in the Kind column |
| `notes contain a banned sentence` | The check reads the whole note, including a row marked `claim`. It does not print the sentence. On the medical director's note the sentence is `The assistant may set clinical urgency.` On the data protection officer's note the sentence is `The external model may receive identified patient data.` Delete that row. A claim row does not make it safe |

## Done

This release is done when all four of these are true. The two checks are only the first.

- Both checks print `passed`. The interview check can print `passed` when a notes file has only two rows. [Chapter 08](08-the-interviews.md) says which rows still have to be there. Search `med-dir.notes.md` for `pol-clinical-safety` and `pol-stage-gate`. Search `dpo.notes.md` for `unsigned` and `pol-assistant-use`.
- `work/knowledge.md` answers question 1 with the problem, the users, and the sponsor.
- The same file answers question 2 with what a coding assistant may be shown and what stays out.
- The three zone rows are filled from `zones.md`. `zone-public` has no hospital.

Keep `work/` and the worksheets. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

The next lesson is the approach. The leaders' numbers arrive there. You run four baselines and write an approach memo. You are still not building the assistant. The file drop is `rel-m01-l02`.

Open [the next lesson](<../../Lesson 02/Student_Copy/README.md>) and read `00-background.md` before any command.
