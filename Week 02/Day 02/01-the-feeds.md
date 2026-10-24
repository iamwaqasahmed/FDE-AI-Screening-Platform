# The feeds

The morning is a stand-up. You have the Week 1 packs, the Day 1 shell, and nothing from later this week.

Open the release readme, [data/rel-w2d2/README.md](../../data/rel-w2d2/README.md). Then read:

1. [notices/feeds.md](../../data/rel-w2d2/notices/feeds.md)
2. [registry/topics.md](../../data/rel-w2d2/registry/topics.md)
3. [openapi/eref.yaml](../../data/rel-w2d2/openapi/eref.yaml)
4. [webhooks/referral.submitted.json](../../data/rel-w2d2/webhooks/referral.submitted.json)
5. [feeds/int-engine.jsonl](../../data/rel-w2d2/feeds/int-engine.jsonl)

`eref` pushes `referral.submitted`. The registry names the owner and the fields a consumer may trust. A field that is not listed is ignored.

The Day 1 notes still stand. A new conversation uses the same shape and can live in `Week 02/Day 02/work/interviews`.

From `problem_simulation`:

```text
python -m alwaha.interview --persona ea --script "..\Week 02\Day 02\work\interviews\ea.questions.txt"
python -m alwaha.interview --persona access-mgr --script "..\Week 02\Day 02\work\interviews\access-mgr.questions.txt"
```

Ask `ea` about HL7 first, then the webhook, then who owns `referral.submitted`, then where the integration engine sits. Ask `access-mgr` about the cost ledger first, then the contact-center calls, then how a cancellation is told, then WhatsApp, then the mart figure at the desk. Write what you hear in each persona's notes.

The lead copies [templates/sprint.md](templates/sprint.md) to `work/sprint.md` and sequences the subscription before any use of the mart figure.
