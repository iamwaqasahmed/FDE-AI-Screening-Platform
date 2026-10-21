# Datasets

Facilitators only. Development sets ship in the participant pack. Hidden test sets, adjudicated labels, and canary keys stay in `truth/` and `eval/` until a release explicitly moves a copy. Releases are listed in [10 Release schedule](10-release-schedule.md).

Text is generated from fact specs, per-author style cards, a PHC shorthand glossary, OCR noise, and a cached paraphrase bank. A regular expression written against the template, or a model that memorizes a template, fails the held-out authors. The hardness audit includes that check.

## Referral letters (`ds-letters`)

Sources are typed notes, scans, and phone photos. Phone photos are synthetic page images with a gold transcription.

The extraction schema is: patient name, date of birth, id type and value, PHC, specialty, sub-specialty, clinical question, medications, requested clinician gender, and source quality. Gold spans mark PHI.

Clerk labels follow annotation guideline `ann-v1` and are noisy: sub-specialty is often blank, and a phone photo is often typed as a scan. `ann-v2`, released on `rel-w3d1`, splits sub-specialty and adds the source type. Adjudicated labels for a held-out slice arrive with that release. The rest can be bought through the annotation service in [08 Live services](08-live-services.md).

Rare sub-specialties are too thin to fine-tune until synthetic letters, checked against the real-label distribution, are added. A slice trains on real data only and shows the gap (`slice-synth`).

## Patient messages (`ds-messages`)

Intents: `status`, `book`, `reschedule`, `cancel`, `info`, `complaint`, `emergency`, `other`. Some messages mix a status question with an emergency phrase. The gold intent is `emergency`, and the gold action is the redirect.

A share of messages use a Hijri date, a working-day expression ("next Sunday"), or a Ramadan-hours assumption. Gold is the resolved Gregorian instant on the business calendar.

## Did-not-attend table (`ds-dna`)

One row per invitation. Features as of invite time: district, age band, sex, insurance class, travel minutes, lead time, reminder channel, prior DNA, month, clinic, slot hour. The label is `did_not_attend`.

`appointment_status_final` is present and is filled after the visit. It is the leaky column (`slice-pit`, `slice-gbm`). A random row split reuses people. The honest split holds out people and scores invitations from 1 July 2026 onward.

Point-in-time feature code must join the identity and insurance tables as of the invite timestamp. A join to the latest row leaks later eligibility and later addresses.

## Retrieval and agent sets

| Set | What a row is | Gold |
|---|---|---|
| `ds-retrieve` | A question, an audience, a case date | Document id, version, status, span. Includes unanswerable and conflicting pairs |
| `ds-agent` | A scenario with a scripted patient | Final mock state, tools that were allowed, whether a human had to approve |
| `ds-sessions` | The same patient across two or more days | Memory that may be reused, and memory that consent or retention blocks |
| `ds-reason` | A request with date, gender preference, travel, and hours constraints | The offer that satisfies every constraint, or a refusal that names the constraint |
| `ds-prefs` | Coordinator draft and the edited sent text | Style rules: clause id present, shorthand expanded, no date the calendar cannot keep |
| `ds-usability` | Task scripts by literacy group | Task completion, and the accessibility checks in the digital-service standard |
| `ds-domain` | Unlabeled in-domain text plus the shorthand glossary | Used for continued pretraining, not for the extraction test |
| `ds-redteam` | Attacks, specified in [09](09-traffic-and-threats.md) | The attack fails and the workflow stays intact |

`ds-prefs` is the seed for preference tuning (`slice-pref`). Prompt-only drafting misses the coordinators' style on a held-out editor.

## Summary statistics for synthetic data

The pack includes distribution cards: specialty mix, phrase frequencies, PHI rates, and label margins. A synthetic set is scored against those cards, against a train-on-synthetic test-on-real slice, and against canary strings. A generated letter that contains a canary, or a real national id, fails `chk-w3-synthetic`.

Judge calibration items, with scored answers, ship as `eval/judge_calibration.jsonl` for facilitators and as a student subset on `rel-w3d4`.
