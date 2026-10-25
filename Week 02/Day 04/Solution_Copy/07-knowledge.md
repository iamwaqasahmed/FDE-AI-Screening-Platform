# 07 — Knowledge

This answers the knowledge file from the morning. Open the finished [knowledge.md](work/knowledge.md) and put it beside yours.

The check reads two numbered lines. The first line has to contain `zone-private`. The second line has to contain `hash`. When the first line is wrong, the message is `knowledge.md does not name the zone`. When the second line is wrong, the message is `knowledge.md does not say what a rollback changes`. When there are fewer than two numbered lines, the message is `knowledge.md needs two answers`.

The finished sentences are these.

## Which zone is this URL in?

The URL is in zone-private.

[guide.md](sources/release/endpoint/guide.md) states the address and the zone. [zones.md](sources/kickoff/world/zones.md) says `zone-private` is the private cloud. The zone table in [zones.md](work/zones.md) records the same fact with surface `url`.

## What does a rollback change?

A rollback changes the model hash.

[models.json](sources/release/registry/models.json) has a previous `local-small` row beside the approved row. [rollback.md](work/rollback.md) says a rollback changes the served hash to that previous registered hash, and that it does not rewrite patient records. The check does not read `rollback.md`. The knowledge line is what the check reads. The second sentence says a rollback changes the model hash.

You have the finished day. The trainer's session is [08 — Trainer session](08-trainer.md).
