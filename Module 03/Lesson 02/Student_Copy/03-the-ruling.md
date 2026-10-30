# 03 — The ruling

[Chapter 02](02-the-role.md) named the five parts. This chapter is the signed ruling and the files that sit beside it. You read. You run one demo. You do not paste a file.

To open a link, Ctrl+click on Windows or Command+click on macOS. To search, Ctrl+F or Command+F inside the file named below, not inside this chapter.

## Read these files

Open [release/README.md](packet/release/README.md), then read these in order. They are the copies in the packet. You do not open `data/` or `case/`.

Stay on this list until item 11. Then run the demo. You do not paste any of these files.

1. [ruling.md](packet/release/notices/ruling.md). Search for `signed`. You should see patient data staying off `ext-large`, training staying on the private cloud, and a cloud fine-tune closed. Search for `national id`. You should see date of birth, name, and phone on that same sentence. The case date is on the last line. You are done with this file when you have seen those three sentences.
2. [reg-models.json](packet/release/registry/reg-models.json). Search for `lora-local`. You should see `"status": "approved"` and `"base": "local-small"` on that row. Read the `hash` on that same row. Chapter 09's pasted memo already contains that hash. You compare the two. You do not copy the hash into a prompt, and you do not type a second one. Then search for `local-small`, `local-embed`, and `ext-large`. Each of those is its own row. `local-embed` is approved and is not the adapter you serve today. Do not copy this file into `work/`. Stay on this page until Next. You are done with this file when you have seen those four ids and the `lora-local` hash.
3. [quota.json](packet/release/budget/quota.json). Search for `gpus`. That field is a count of GPUs. Read the number in the file. You are done when you have seen that field.
4. [price-cap.json](packet/release/budget/price-cap.json). Search for `tokens`. You should also see `f1_floor`, `max_sar`, and `max_seconds`. Read the numbers in the file. `tokens` is the published token count. You are done when you have seen those four fields.
5. [letters.jsonl](packet/release/slices/letters.jsonl). Each row is one long line. A search can land in the middle of that line. Read the whole line. There are four lines. Each line has `item_id`, `source_type`, `sub_specialty`, and `text`. The next block is a picture of the first row. Do not paste it. It is not a file you replace. You are done when the first line in the file matches that picture and you have seen four lines.

```text
{"item_id": "dev-letter-1", "source_type": "photo", "sub_specialty": "retina", "text": "Phone photo from the retina service."}
```

6. [messages.jsonl](packet/release/slices/messages.jsonl). Each row is one long line. There are six lines. Each line has `intent`, `message_id`, and `text`. The next block is a picture of the first row. Do not paste it. You are done with this file when the first line matches that picture and you have seen six lines.

```text
{"intent": "status", "message_id": "dev-message-1", "text": "What is the status of my referral?"}
```

7. [hours.jsonl](packet/release/slices/hours.jsonl). Search for `clinic`. Three questions. Each line has `question_id` and `text`. They are not a model call. You are done with this file when you have seen three questions.
8. [ds-domain.jsonl](packet/release/domain/ds-domain.jsonl). Search for `sugar`. Three lines. Each line has `text` and no item id. Chapter 08 uses them. You are done with this file when you have seen three lines.
9. [ds-prefs.jsonl](packet/release/prefs/ds-prefs.jsonl). Search for `draft`. The other field is `edited`. The clause id is in the draft. Chapter 08 uses this pair. You are done with this file when you have seen both fields.
10. [cloud.json](packet/release/fixtures/cloud.json). Search for `unregistered`. The id on that row is `cloud-tune`. Do not copy this file into `work/`. Do not copy the hash onto a page. You are done with this file when you have seen that id and that status.
11. [router.yaml](packet/release/openapi/router.yaml). Search for `403`. You should also see `routeCall`. `POST /route` needs `model` and `hash`. `fields` is optional. `200` means the hash is on `reg-models` and a phi field was not sent to `ext-large`. `403` is the refusal. You are done with this file when you have seen both response lines.

The dev slices are what you read today. The checks also score a held-out slice that is not in this folder. You do not need those rows to write the files. A check does not print a gold label.

## Run the demo

The demo shows the gateway refusing a prompt that carries the mark. It does not print the mark.

The terminal from chapter 01 that ran `prepare_work.py` is in the course folder. Use that window, or open a new one the same way. Do not reuse the build window unless you are sure it is still inside `problem_simulation`. If the window is already inside `problem_simulation`, skip the `cd` line and run the python line. If chapter 01 told you to use `py`, use `py` here.

```text
cd problem_simulation
python -m alwaha.demo.gateway --profile practice
```

That block is a command, not a picture.

## You should now see

```text
the gateway refused the prompt
```

That is the only line. The prompt returns after it. There is no error. The line does not print the watermark. If you see more than that one line, you ran a different command. Run this one again.

If the `cd` line says the path cannot be found, this window is already inside `problem_simulation`. Skip the `cd` line and run the python line.

## What you are deciding

The prompt baseline stays on `local-small` and is not served. The adapter that is served is the approved `lora-local` row. Hours stay on retrieval. DNA stays a tabular model. The cloud fine-tune stays closed.

This page is done when each of the 11 files has shown you the words named above, and the demo has printed `the gateway refused the prompt` and nothing else.

Next: [04 — Words](04-words.md).
