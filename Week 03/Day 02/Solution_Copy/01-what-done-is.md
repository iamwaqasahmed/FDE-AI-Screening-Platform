# 01 — What done is

This page is the map. The day is finished by the sprint, the prompt, the letter relabel, the message intent, the adapter, the router, the cost, the rank fit, the domain filter, the preference edit, the approach memo, the residency note, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Baseline, then adapter, then register, then memo. The cloud fine-tune is closed. Explained in [chapter 02](02-the-sprint.md) |
| [app/prompt.py](work/app/prompt.py) | A weak local prompt. It is scored and not served. Explained in [chapter 03](03-the-baseline.md) |
| [app/extract.py](work/app/extract.py) | Source type and sub-specialty come from the letter text. Explained in chapter 03 |
| [app/intent.py](work/app/intent.py) | An emergency phrase wins over a status question. Explained in chapter 03 |
| [tests/test_prompt.py](work/tests/test_prompt.py) | The prompt stays local and is not served. The same bytes as the packet |
| [tests/test_extract.py](work/tests/test_extract.py) | A phone photo is retina. A scan with no named specialty stays blank |
| [tests/test_intent.py](work/tests/test_intent.py) | Chest pain wins. A status question stays status |
| [app/adapter.py](work/app/adapter.py) | The approved `lora-local` row, inside the quota. Explained in [chapter 04](04-the-adapter.md) |
| [app/route.py](work/app/route.py) | Phi on `ext-large` is refused. An unapproved hash is refused. Explained in chapter 04 |
| [app/cost.py](work/app/cost.py) | The published token count is priced on `local-small`. Explained in chapter 04 |
| [tests/test_adapter.py](work/tests/test_adapter.py) | The served id is `lora-local` and the base is `local-small` |
| [tests/test_route.py](work/tests/test_route.py) | Phi and an unregistered hash are refused. Hours stay on retrieval |
| [tests/test_cost.py](work/tests/test_cost.py) | The local quote stays inside the cap |
| [app/qlora.py](work/app/qlora.py) | A higher rank fits the same GPU count. Explained in [chapter 05](05-the-advanced.md). The two checks do not require it |
| [app/domain.py](work/app/domain.py) | Unlabeled lines stay. Letters are left out. Explained in chapter 05. The two checks do not require it |
| [app/prefs.py](work/app/prefs.py) | Shorthand expands. A date the calendar cannot keep is dropped. Explained in chapter 05. The two checks do not require it |
| [tests/test_qlora.py](work/tests/test_qlora.py) | Rank 32 still fits |
| [tests/test_domain.py](work/tests/test_domain.py) | A row with an item id is left out |
| [tests/test_prefs.py](work/tests/test_prefs.py) | The clause id stays. The shorthand expands |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | Runs the suite. Same bytes as the packet |
| [approach.md](work/approach.md) | The Week 1 families and the customization table. Explained in [chapter 06](06-the-pages.md) |
| [residency.md](work/residency.md) | Four phi fields in `zone-private`. Clinic hours public. Explained in chapter 06 |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 07](07-knowledge.md) |
| [dpo.notes.md](work/interviews/dpo.notes.md) | What the Data Protection Officer says. The checks do not read it |
| [dpo.questions.txt](work/interviews/dpo.questions.txt) | The questions that produced those notes. The checks do not read them |
| [finance.notes.md](work/interviews/finance.notes.md) | What finance says. The checks do not read it |
| [finance.questions.txt](work/interviews/finance.questions.txt) | The questions that produced those notes. The checks do not read them |

The checks print `passed` when the prompt is not served, extraction and intent clear the floor, the served hash is the approved `lora-local` row, the GPU count fits the quota, phi stays off `ext-large`, the local price and the latency fit the cap, the sprint sequences baseline then adapter then register then memo and closes the cloud fine-tune, the approach families fit, hours stay on retrieval, DNA stays tabular, the customization cells match the adapter, residency keeps the four phi fields private, and both knowledge answers are present.

`slice-lora` also requires that the prompt baseline does not clear the slice. It does not read the four pages.

The checks do not read the interview notes.

Next: [02 — The sprint](02-the-sprint.md).
