# 04 — Words

Read this page once. You will look back at it while you read the pack and run the shell. You do not need to memorize it.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself.

## The service

| Word | Meaning |
| --- | --- |
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population. This client is the Al-Waha Health Cluster |
| Patient access | Referrals, appointments, reminders, and the phone line. The assistant you are building sits on that service |
| Referral | A request from a local clinic for a hospital appointment. Booking that appointment from chat waits |
| Patient | The person the referral is about |
| Caregiver | A person who asks or finishes a task for the patient. The `caregiver` script is that person asking about her mother's referral |
| Phone line | The way most families still reach the cluster. [Abdullah Al-Harthy](packet/kickoff/personas/patient-rep.md) says it never answers |
| Patient representative | Abdullah Al-Harthy. His id is `patient-rep`. Today's drop is from him |
| SMS | A text message to the patient. The partner that sends it sits outside the private cloud |
| Receipt | The partner's answer that a message was accepted, and later that it is due |
| Case clock | The clock you pin. A receipt follows this clock |
| Wall clock | The clock on the computer. Waiting on it no longer makes a receipt due |
| Interval | The field `minutes` in [receipt.json](packet/release/clock/receipt.json). Chapter 08 reads it from that file. This page does not type the number |
| Switch | The fault name in that same file. The field is `switch`. The value is `receipt-late` |
| `receipt-late` | While this switch is on, the receipt stays pending after the case clock has moved. [Chapter 09](09-the-pages.md) puts that name on the definition of done |
| Pending | The receipt is not due yet. The SMS spec uses this for the response that is still waiting |
| Due | The receipt is due. The shell treats every receipt as due. The filled receipt does that only after the case clock has moved, and only while the switch is off |
| Pin | `PUT /clock` sets the case clock to the timestamp in `at`. [guide.md](packet/release/clock/guide.md) is that call |

## The clauses and the scripts

| Word | Meaning |
| --- | --- |
| Access clause | A rule for a task a person can finish. The four ids are in [access.md](packet/release/standards/access.md) |
| `plain-language` | The task uses short words |
| `caregiver-complete` | A caregiver can finish the task |
| `named-control` | A control has a name, not a color alone |
| `one-action` | The task has one next step |
| Usability script | One task, one actor, one layer. The lines are in [scripts.jsonl](packet/release/usability/scripts.jsonl) |
| Foundation | The layer today's table finishes. `status-short` and `caregiver` are foundation |
| Advanced | A later layer. `phone-only` is advanced. It stays out of today's table |
| `status-short` | The patient asks where the referral is, in a short message |
| `caregiver` | The script id for the caregiver asking about her mother's referral. The same word is also the person |
| `phone-only` | Ask the same question by phone, with no app. Actor `pop-literacy`. Do not add this row |
| `pop-literacy` | The actor on the phone-only script. Not a row in today's table |
| `finished` | The column that says the script is done. Today's two scripts use `yes` |

## The calendar

| Word | Meaning |
| --- | --- |
| Business calendar | Working days, the weekend, and the holiday list. The copy is [business-calendar.json](packet/carried/calendar/business-calendar.json). The tests read the same document from `data/rel-w1d3` |
| Working day | Sunday, Monday, Tuesday, Wednesday, or Thursday. The start counts when it is one of these and not a holiday |
| Weekend | Friday and Saturday. Those days do not count |
| Friday | A weekend day. The shell still counts it. The filled calendar keeps the name in the weekday list and counts it only when `working_days` lists it |
| Saturday | The other weekend day |
| Holiday | A date on the holiday list. The shell ignores that list. The filled calendar skips those dates |
| SLA | The service clock from Week 1. Today's count is the days that clock uses |
| `thursday` | The case that starts on 21 January 2027 and counts two working days. [cases.json](packet/release/calendar/cases.json) has the start and the count. Chapter 06 has the date that count lands on |
| `eid` | The case that starts on 9 March 2027 and counts three working days. The holiday list sits on the days after that start |
| Hijri | The other calendar in [hijri.json](packet/release/calendar/hijri.json). The checks do not grade a note about it |

## The zones and the reply

| Word | Meaning |
| --- | --- |
| Zone | Where a piece sits. [zones.md](packet/kickoff/world/zones.md) names three |
| `zone-private` | The private cloud. `h-wadi` sits here. The calendar stays here. The receipt leaves from here |
| Partner | The SMS sender outside the cluster. The receipt row names `partner` in the `to` column |
| Schema | The fields a reply must have. Today's required field is `intent` |
| Intent | The field `schema_ok` reads. `status` is a value. An empty sentence can still have an intent |
| Journey | The check that a reply and a state agree. Today's journey trusts the state |
| Mock state | The recorded outcome, including `booked`. The sentence is not that outcome |
| Fixture | The recorded reply in the pack. [model.json](packet/release/fixtures/model.json) is that file. The journey reads it. It does not copy it |
| Watermark | The mark on the fixture text. The check message does not print it. A copy of the file in `work/` fails the check |

## The suite

| Word | Meaning |
| --- | --- |
| Suite | The tests under `work/tests`, together with the three app files they call |
| Shell | The starter copy in `packet/`. It still counts Friday, still judges the sentence, and still treats every receipt as due. The receipt test in the shell still waits |
| CI | The workflow in [ci.yml](packet/.github/workflows/ci.yml). It runs the suite. You copy it. You do not edit it |
| Definition of done | [dod.md](work/dod.md). The switch is on this list. The suite goes red when that switch is on |
| Sprint | The order of the work. The suite comes before usability sign-off |
| Sign-off | The usability pass. It sits under Later |
| `practice` | The shared classroom world. The build in chapter 01 uses it |
| `rel-w2d3` | Today's file drop |

## What the check will see

| Piece | What you should see |
| --- | --- |
| Calendar | The cluster week. Friday stays in the name list. The holiday list is used |
| Reply | An empty sentence with `intent` passes. A sentence with no `intent` fails |
| Journey | `booked` on the state is the result. The sentence in the fixture is still loaded |
| Receipt | Pending at the sent time, due after the clock moves, pending again when the switch is on |
| Demo | `switch off: passed`, then `switch on: failed` |
| Pages | `status-short` and `caregiver` finished. Four clause ids. Two zone rows. The switch named on the definition of done |

The date a calendar case lands on is in [chapter 06](06-the-calendar.md). This page does not store it.

## A plain reading

The receipt becomes due when the case clock moves. The shell test sleeps on the wall clock and then expects the receipt to be due. A fixed sleep follows the wall clock. The receipt follows the case clock, and the switch can hold it. The clock guide says to advance the pinned time. It says not to sleep.

The journey trusts the mock's final state. The model's sentence is a fixture you load. The journey does not treat that sentence as the result.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
