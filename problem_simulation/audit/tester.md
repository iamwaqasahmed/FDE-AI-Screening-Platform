# Blinded tester

This pass is for a person who has not read `alwaha/` or `build/`. The author of the generator cannot sign it.

## Setup

From `problem_simulation`:

```text
python -m alwaha.worldbuild --profile small
docker compose -f host/compose.yaml up
```

The mocks listen on port 8080. The reference assistant listens on port 8081. Do not open `build/` or `design/`.

## One day

1. Open the day folder under `Module 0N/Lesson 0N` and follow its four notes in order.
2. Use the pack named in that README under `data/`. Build it only with the command the note prints.
3. Edit the `work/` copy, not the shell.
4. Run the check command in the day's last note.
5. Write down the check id and whether it passed. Do not read the truth files if a check fails. Ask a facilitator.

## Done

A day is done when its foundation check passes from the pack and the running services, and the tester can name the trap the day warned about without opening the generator.
