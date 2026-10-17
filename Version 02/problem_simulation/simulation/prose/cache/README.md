# Prose cache

LLM-written document bodies, one file per fact spec, named `<doc_id>--<spec hash>.md`. Commit this folder.

- `python -m simulation.prose status` shows how many specs have cached prose.
- `python -m simulation.prose author --family <family> --limit <n>` writes missing entries. The key, URL, and model come from `HARTLAND_LLM_*` or `OPENAI_*` variables, or from a `.env` file in problem_simulation, Version 02, or Version 01 (see `simulation/prose/settings.py`).
- `python -m simulation.prose prune` removes entries whose facts changed.

A build never calls a model. A spec with no cached body uses its seeded template draft, and both pass the same fact check.
