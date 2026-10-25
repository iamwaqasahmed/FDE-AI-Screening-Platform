# 10 — Finish

Two actions. Replace `knowledge.md`. Run two commands. You are done when each command prints `passed`.

The checks grade the prompt, the letter relabel, the message intent, the adapter, the router, the cost, the sprint, the approach memo, the residency note, and the shape of `knowledge.md`. The sentences in `knowledge.md` are still part of done. The checks do not read an interview note. They do not import `qlora.py`, `domain.py`, or `prefs.py`. Leave those three files in place.

`slice-lora` does not read the four pages. A page miss fails only the model check. Both checks can still say the adapter did not run, or one of the lines that come from the six graded modules.

Use the failure table at the bottom only when a check fails. It is not more work. Do not run `prepare_work.py` on this page unless a row in that table tells you to. A second run erases the files you pasted.

## Do this

1. Open [work/knowledge.md](work/knowledge.md). The full path is `Week 03/Day 02/Student_Copy/work/knowledge.md`. It sits beside `sprint.md`. It does not go inside `work/app`, and it does not go inside `packet/`. If the file is missing, create it in that `work` folder. On Windows the name sometimes becomes `knowledge.md.txt`. Click the name and remove `.txt`. If you cannot see `.txt`, in File Explorer open View and tick File name extensions, then rename the file so the name ends in `.md` only.

   Select the whole file and delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save. These are the finished sentences. This block replaces `knowledge.md`.

```text
# Knowledge

1. Hours questions for p-info stay on retrieval.
2. The legal hash is lora-local on reg-models.
```

Open [work/knowledge.md](work/knowledge.md). Search inside that file, not inside this chapter. You should see two numbered lines. Line 1 contains `retrieval`. Line 2 contains `lora-local` and `reg-models`. Line 2 names the register row. It does not print the hash. If the search fails, you pasted into the wrong file. The path has to contain `Student_Copy\work`. On macOS it shows as `Student_Copy/work`.

2. Open a terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Week 03`. If chapter 01 told you to use `py`, use `py` here. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines.

```text
cd problem_simulation
python -m alwaha.check model --release rel-w3d2 --work "../Week 03/Day 02/Student_Copy/work" --profile practice
python -m alwaha.check lora --release rel-w3d2 --work "../Week 03/Day 02/Student_Copy/work" --profile practice
```

## You should now see

```text
chk-w3-model passed.
slice-lora passed.
```

Each command prints its own line. Wait for one line before you start the next command. You need both. `work/knowledge.md` has both answers. The first says hours questions for p-info stay on retrieval. The second says the legal hash is lora-local on reg-models.

If you see those two `passed` lines, skip the table below and go to Done.

## If a check fails

A failed check prints `failed`, then one or more lines that start with a dash. The words after the dash are what you look up in the left column below. Do what the right column says. Then run the command again. A line can say the prompt baseline is still the served model, extraction F1 is outside the budget, intent F1 is outside the budget, the cost is over the price cap, the call sends phi to ext-large, the hash is not on reg-models, the gpu count is over the quota, the latency is over the budget, or the adapter did not run. It can also say hours questions are not left on retrieval, dna is not a tabular model, family does not fit, the measured value does not match the adapter, the residency note lets a phi field leave, a page is missing, or a knowledge line is missing a fact. `slice-lora` can also say the prompt baseline clears the slice, or ext-large at the price cap does not clear the slice. It does not print a hash, a GPU count, a price, an F1, or a gold label. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

| What it prints | Where to go |
| --- | --- |
| `Build rel-w3d2 first.` | The pack or the grader's gold file is missing. From the course folder, run `cd problem_simulation` and then `python -m alwaha.build --profile practice --release rel-w3d2`. If you are already inside `problem_simulation`, skip the `cd` line. Then run the two checks again |
| `the prompt baseline is still the served model` | The message does not name the model. Open [prompt.py](work/app/prompt.py). `served` has to return false. `target` has to name `local-small` and leave phi false. [Chapter 06](06-the-baseline.md). Paste `prompt.py` again. You should see `Do not serve it.` You should still see `typed` and `status` in that file. That is expected. If the customization table says a method other than `lora` for extraction or intent, paste [approach.md](work/approach.md) again from [chapter 09](09-the-pages.md). Label the call: the prompt is scored, and it is not the served model |
| `extraction F1 is outside the budget` | The message does not print an F1 or a gold label. Open [letters.jsonl](packet/release/slices/letters.jsonl). A row's `text` is the input. Phone or photo in the text is source type photo. The word scan, with neither phone nor photo, is scan. Retina in the text fills retina. Pediatric, when retina is absent, fills pediatric. Otherwise the sub-specialty stays blank and the source type stays typed. [Chapter 06](06-the-baseline.md). Paste `extract.py` again. You should see `elif "pediatric" in text:`. Label the row you opened: which words set the source type, and which words set the sub-specialty |
| `intent F1 is outside the budget` | The message does not print an F1 or a gold label. Open [messages.jsonl](packet/release/slices/messages.jsonl). A row's `text` is the input. An emergency phrase wins before a status word. A status question with no emergency phrase stays status. [Chapter 06](06-the-baseline.md). Paste `intent.py` again. You should see `cannot wait`. `return "status"` is still in the file. That is expected. Label the message you opened: which phrase won |
| `the cost is over the price cap` | The message does not print a price. Open [price-cap.json](packet/release/budget/price-cap.json) and [cost.py](work/app/cost.py). The quote uses `price.local_per_1k` and the `tokens` field. The returned model is `local-small`. `seconds` stays a number the cap file allows. [Chapter 07](07-the-adapter.md). Paste `cost.py` again. You should see `Price the token count on local-small.` You should not see `price.ext_large_per_1k`. Label the quote: which rate it used, and whether that model is the local one |
| `the call sends phi to ext-large` | The message does not name the field. Two files can cause it. If [prompt.py](work/app/prompt.py) still returns `ext-large` with phi true, paste `prompt.py` again from chapter 06. You should see `"phi": False`. If [route.py](work/app/route.py) still allows every call, paste `route.py` again from chapter 07. The inputs are a call whose `model` is `ext-large` and whose `fields` include `national_id`, `date_of_birth`, `name`, or `phone`. That call is refused. You should see `date_of_birth`. `ext-large` on the refuse line is expected. Label the call: phi stayed off the external model |
| `the hash is not on reg-models` | The message does not print a hash. Open [reg-models.json](packet/release/registry/reg-models.json). Find the row whose `id` is `lora-local` and whose `status` is `approved`. [adapter.py](work/app/adapter.py) returns that row's hash. It does not type a hash. [Chapter 07](07-the-adapter.md). Paste `adapter.py` again. You should see `chosen["hash"]`. You should not see `cloud["hash"]`. The same line can come from [route.py](work/app/route.py) when a call's hash is not on an approved row. Paste `route.py` again if `allow` still returns true for every call. The customization hash cell, if it is not the `lora-local` row, is fixed by pasting `approach.md` again from chapter 09. Do not copy [cloud.json](packet/release/fixtures/cloud.json) onto the page. Label the row you opened: its id is `lora-local`, and its status is approved |
| `the gpu count is over the quota` | The message does not print a GPU count. Open [quota.json](packet/release/budget/quota.json). The field is `gpus`. [adapter.py](work/app/adapter.py) has to return a count that does not sit above that field. [Chapter 07](07-the-adapter.md). Paste `adapter.py` again. You should see `"rank": 8`. You should not see `quota["gpus"] + 1`. Label the count: it fits the field you opened |
| `the latency is over the budget` | The message does not print a latency. Open [price-cap.json](packet/release/budget/price-cap.json) and read `max_seconds`. [cost.py](work/app/cost.py) returns `seconds`. Paste `cost.py` again from chapter 07. You should see `seconds`. Label the number you return against the field you opened |
| `the adapter did not run` | The message does not name the line. A work module is missing, or the paste broke the indentation, or a name the check calls is missing. Run `prepare_work.py` from the course folder, then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand. Do not delete `qlora.py`, `domain.py`, or `prefs.py` |
| `the prompt baseline clears the slice` | This line is from `slice-lora`. The message does not print an F1. [prompt.py](work/app/prompt.py) copied the letter relabel and the message classifier. Paste the prompt block again from chapter 06. You should see `return False`. You should still see `typed` and `status` in that file. That is expected. The weak baseline stays under the floor. Label the prompt: it is scored, and it does not clear the slice |
| `ext-large at the price cap does not clear the slice` | This line is from `slice-lora`. The message does not print a price. Open [cost.py](work/app/cost.py). The returned model has to be `local-small`. If the model is `ext-large`, paste `cost.py` again from chapter 07. You should see `Price the token count on local-small.` Label the model on the quote |
| `hours questions are not left on retrieval` | The message does not name the row. Open [approach.md](work/approach.md). `p-info` needs family `retrieve`. The hours row in the customization table needs method `retrieve`. [Chapter 09](09-the-pages.md). Paste `approach.md` again. You should see `Hours stay on retrieval.` |
| `dna is not a tabular model` | The message does not name the family word it wanted. Open `approach.md`. The `p-dna` row needs `classical-ml`. Paste `approach.md` again from chapter 09. You should see `classical-ml` on that row. `gradient boosting` is still in the opening paragraph. That is expected |
| `family does not fit` | The message does not name the problem. Open `approach.md`. Each Week 1 id keeps the family already in the block from chapter 09. Paste `approach.md` again. Keep the pipe characters |
| `the measured value does not match the adapter` | The message does not print an F1, a cost, or a hash. Open the customization table in the block from chapter 09. Paste `approach.md` again. The cells are already in that block. Do not type a second hash, and do not copy a hash from `cloud.json` |
| `the residency note lets a phi field leave` | The message does not name the field. [Chapter 09](09-the-pages.md). `residency.md` needs a table whose header has `field` and `zone`. National id, date of birth, name, and phone are `zone-private`. Clinic hours are `public`. Keep the pipe characters. Paste `residency.md` again |
| `approach.md is missing` | The file is missing, empty, or a table is missing a Week 1 id or a customization task. Paste `approach.md` again from chapter 09. You should see `p-bounce` and `extraction` |
| `sprint.md does not sequence the adapter` | The message does not print the four words. [Chapter 05](05-the-sprint.md). The page needs baseline, then adapter, then register, then memo, and the sentence `The cloud fine-tune is closed.` Paste `sprint.md` again |
| `knowledge.md needs two answers` | Paste the block above again. Two numbered lines, each with words after the number. A second sentence on the next line does not count |
| `knowledge.md does not say which problem stays on retrieval` | The message does not name the missing fact. Line 1 of the block above says hours questions for p-info stay on retrieval |
| `knowledge.md does not say which hash is legal to serve` | Line 2 of the block above says the legal hash is lora-local on reg-models. That sentence names the register row. It does not print the hash |
| `a watermarked sample is in the work directory` | A file that carries the mark is under `work/`. Delete that copy. The message does not print the watermark. Do not delete `qlora.py`, `domain.py`, or `prefs.py` |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python lines |
| `SyntaxError` or `IndentationError` | Run `python "Week 03/Day 02/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand |

## Done

The two checks print `passed`, and `knowledge.md` answers both questions. The first says hours questions for p-info stay on retrieval. The second says the legal hash is lora-local on reg-models.

Keep `work/`. Leave `problem_simulation/build` closed.
