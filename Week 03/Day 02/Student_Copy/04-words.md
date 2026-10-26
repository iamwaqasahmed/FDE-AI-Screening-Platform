# 04 — Words

Read this page once. You do not need to memorize it, and you do not need to open every link. Scan the tables, then go to [chapter 05](05-the-sprint.md). When a later chapter uses a word you want in the file's own sentence, come back to that row and open the link. You do not paste anything on this page, and you do not run a command. If you are lost on this page, scroll to the line that starts with Next. That line is the end of the reading.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself. This page does not type a hash, a watermark, or a held-out item id. Those values stay in the files [chapter 03](03-the-ruling.md) already opened, or in the built pack.

## The ruling and the seats

| Word | Meaning |
| --- | --- |
| Ruling | The signed note in [ruling.md](packet/release/notices/ruling.md). Patient data stays off `ext-large`. Training stays on the private cloud |
| Case date | `2027-01-25`, on the ruling |
| Phi | A field that identifies a person. The ruling names four: national id, date of birth, name, and phone |
| National id | A phi field. It stays off `ext-large` and in `zone-private` |
| Date of birth | A phi field. The router name is `date_of_birth` |
| Name | A phi field. A person's name, not the name of a clinic |
| Phone | A phi field. A phone photo of a letter is a different word: that one is source type `photo` |
| `ext-large` | The external model. The ruling says patient data stays off it. Its register row is `zone-public` |
| Private cloud | Where training stays. The local models live here |
| Cloud fine-tune | A training job on the external side. The ruling closes it. The sprint says the same sentence |
| Clinic hours | A public fact. Hours questions stay on retrieval. They are in [hours.jsonl](packet/release/slices/hours.jsonl) |
| Public | The residency zone for clinic hours. The cell is the word `public` |
| Retrieval | Look up an answer in a document. Hours questions for `p-info` stay here |
| GPU quota | A count of GPUs. The field is `gpus` in [quota.json](packet/release/budget/quota.json). You read the count from that file |
| Price cap | The spend and latency limits in [price-cap.json](packet/release/budget/price-cap.json) |
| F1 floor | The `f1_floor` field in the price cap. A score under it is outside the budget. You read the number from the file. On this day the score called F1 is the share of fields that match. It is not a precision-and-recall F1 |
| Token count | The `tokens` field in the price cap. The quote prices that count |
| Data Protection Officer | The person who signed the ruling. The checks do not ask you to interview them |
| Finance | The seat that holds the quota and the cap. The checks do not ask you to interview them |
| Lead | Sequences the sprint and tells steering the cloud fine-tune is closed |
| AI or data engineer | Serves the registered adapter, and replaces the three advanced files |
| Application engineer | Keeps the prompt local, relabels letters, classifies messages, refuses a bad call, and prices local tokens |
| Product manager | Revises the approach memo |
| Architect | Records residency |

## The register, the slices, and the router

| Word | Meaning |
| --- | --- |
| `reg-models` | [reg-models.json](packet/release/registry/reg-models.json). The approved hashes live here. You open the file. You do not paste it |
| Approved | A row whose `status` is `approved`. Only those hashes may be served |
| `local-small` | The small local model. The prompt baseline targets it. `lora-local` uses it as `base` |
| `local-embed` | The local embedding model. It is on the register. Today's adapter does not serve it |
| `lora-local` | The adapter row. Status `approved`, base `local-small`, zone `zone-private`. The legal hash is this row on `reg-models` |
| `zone-private` | The register zone for the local models and for `lora-local`. Residency uses the same words for the four phi fields |
| `zone-public` | The register zone for `ext-large` |
| `cloud-tune` | The id in [cloud.json](packet/release/fixtures/cloud.json). It is not on `reg-models` |
| Unregistered | The status on the cloud fixture. An unregistered hash is refused |
| Letter | One row in [letters.jsonl](packet/release/slices/letters.jsonl). Fields: `item_id`, `source_type`, `sub_specialty`, `text` |
| Source type | How the letter arrived: `photo`, `scan`, or `typed` |
| Photo | Source type when the text says phone or photo |
| Scan | Source type when the text says scan and does not say phone or photo |
| Typed | Source type when the text says neither phone, photo, nor scan. The weak prompt always returns this |
| Sub-specialty | `retina`, `pediatric`, or blank when the text names neither |
| Retina | The sub-specialty when the text contains retina |
| Pediatric | The sub-specialty when the text contains pediatric and does not contain retina |
| Message | One row in [messages.jsonl](packet/release/slices/messages.jsonl). Fields: `intent`, `message_id`, `text` |
| `status` | A message asking where a referral is. The weak prompt always returns this |
| `emergency` | A message whose text has an emergency phrase. That phrase wins over status |
| `book` | A request for a slot |
| `cancel` | A request to cancel a visit |
| `info` | A question about documents to bring |
| `reschedule` | A request to move a visit |
| Hours question | A row in [hours.jsonl](packet/release/slices/hours.jsonl). Not a model call |
| Domain line | A row in [ds-domain.jsonl](packet/release/domain/ds-domain.jsonl). It has `text` and no item id |
| Preference pair | The `draft` and `edited` fields in [ds-prefs.jsonl](packet/release/prefs/ds-prefs.jsonl) |
| Clause id | The short code in the preference draft, such as the endocrinology clause. The edit keeps it |
| `sugar clinic` | Shorthand in the domain lines and in the preference draft. The edit expands it to endocrinology |
| Router | [router.yaml](packet/release/openapi/router.yaml). `POST /route`, operation `routeCall` |
| Shell | The starter app in `packet/app`. Chapter 01 copies it into `work/app`. You replace the work copy |
| Suite | `python -m unittest discover -s tests -q`, run from `work/` in chapter 08. It is not a check |
| CI | [.github/workflows/ci.yml](packet/.github/workflows/ci.yml). Copied and not replaced. On Windows the `.github` folder is hidden |
| Watermark | A mark the gateway refuses. The demo does not print it. A file that carries it must not sit in `work/` |
| `practice` | The shared classroom world. The build and the checks use it |
| `rel-w3d2` | Today's release name. Week 3, day 2 |
| Held-out slice | Letters and messages the checks score that are not in the packet. You do not type their ids |

## The modules and the pages

| Word | Meaning |
| --- | --- |
| Prompt baseline | [prompt.py](packet/app/prompt.py). A weak local prompt. It is scored and not served |
| Served | `served` in the prompt file. False means the prompt is not the model on the endpoint |
| Adapter | [adapter.py](packet/app/adapter.py). The served model is the approved `lora-local` row |
| Rank | How wide the adapter is. The fit in [qlora.py](packet/app/qlora.py) has to stay inside the GPU count |
| Hash | The `hash` field on a register row. The approach page records the `lora-local` hash. A Python file copies it from the row. It does not type it |
| Quote | [cost.py](packet/app/cost.py). It prices the published token count |
| `price.ext_large_per_1k` | The external rate. The shell uses it. That cost is over the cap |
| `price.local_per_1k` | The local rate. The filled quote uses it |
| QLoRA | The method in `qlora.py`. A higher rank fits in the same GPU count. The two checks do not require the file |
| Router allow | `allow` in [route.py](packet/app/route.py). It refuses phi on `ext-large` and a hash that is not approved |
| Task route | `task` in `route.py`. Hours return `retrieve`. DNA returns `classical-ml` |
| `classical-ml` | The family for DNA. A table with a label. Gradient boosting, not a language model |
| Sprint | [sprint.md](packet/templates/sprint.md). Baseline, then adapter, then register, then memo |
| Approach | [approach.md](packet/templates/approach.md). The Week 1 families, plus the customization table |
| Family | The `family` column. Words you already used in Week 1: `extract+retrieve`, `no-model`, `classical-ml`, `agent`, `retrieve`, `forecast`, `blocked` |
| Measured | The `measured` column. A baseline line, or a leader figure marked claim |
| Customization | The second table. Tasks `extraction`, `intent`, and `hours`. Methods `lora` and `retrieve` |
| Residency | [residency.md](packet/templates/residency.md). Columns `field` and `zone` |
| `p-bounce` | Referral letters. Family `extract+retrieve` |
| `p-waitlist` | Rows the coordinators do not trust. Family `no-model` |
| `p-dna` | The appointment table. Family `classical-ml` |
| `p-status` | Referral status. Family `agent` |
| `p-slots` | Empty chairs. Family `no-model` |
| `p-clock` | The wait-time clock. Family `no-model` |
| `p-info` | Hours, preparation, and documents. Family `retrieve` |
| `p-forecast` | Monthly session volumes. Family `forecast` |
| `p-triage` | Clinical urgency. Family `blocked`. You do not build it |

## What the check will see

| Word | Meaning |
| --- | --- |
| `prompt.py` | The prompt stays on `local-small`, phi is false, and it is not served. `extract` stays typed with a blank sub-specialty. `intent` stays `status` |
| `extract.py` | Photo, scan, retina, pediatric, or blank come from the text |
| `intent.py` | An emergency phrase wins. A status question with no emergency phrase stays status |
| `adapter.py` | `lora-local` on `local-small`, using that row's hash, inside the quota |
| `route.py` | Phi on `ext-large` is refused. An unapproved hash is refused. Hours stay `retrieve`. DNA stays `classical-ml` |
| `cost.py` | The published token count is priced with `price.local_per_1k`. The model is `local-small` |
| `qlora.py` | Present for the suite. The two checks do not require it. Do not delete it |
| `domain.py` | Present for the suite. A row with an item id is left out. The two checks do not require it |
| `prefs.py` | Present for the suite. Shorthand expands, the clause id stays, and a date the calendar cannot keep is dropped. The two checks do not require it |
| `sprint.md` | The words baseline, adapter, register, and memo, in that order, and the sentence that the cloud fine-tune is closed |
| `approach.md` | The nine Week 1 families, and the customization table. Hours stay `retrieve` |
| `residency.md` | National id, date of birth, name, and phone in `zone-private`. Clinic hours `public` |
| `knowledge.md` | Two numbered answers. Hours questions for `p-info` stay on retrieval. The legal hash is `lora-local` on `reg-models` |
| `chk-w3-model` | The model check. It reads the six graded modules and the four pages |
| `slice-lora` | The LoRA check. The adapter has to clear the slice. The prompt baseline must not. It does not read the four pages |

This page is done when you can find a word in the table and open its file. You do not need to memorize the rows.

## A plain reading

Week 1 Day 2 separated fine-tuning from retrieval. Fine-tuning changes weights. Retrieval looks up a document. The ruling closed a fine-tune on the external model. Patient data stays off `ext-large`.

An adapter, on this day, is the small set of extra weights registered as `lora-local` on `local-small`. That style of small added weights is called LoRA. Parameter-efficient fine-tuning is the family name: you do not change every weight. You do not run a training loop in this folder. `adapter.py` selects the approved row and copies its hash. Rank is how wide that adapter is. A wider rank can ask for more GPUs.

QLoRA is the fit in `qlora.py`. It has to stay inside the GPU count you read from the quota file. The two checks do not require that file. The suite does.

The prompt baseline stays weak, and it is not the model you serve. Hours questions for `p-info` stay on retrieval. DNA stays a table, `classical-ml`, not a language model.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
