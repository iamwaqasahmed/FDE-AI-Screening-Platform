# The standard

The morning is a stand-up. You have the Week 1 packs, the Day 1, Day 2, and Day 3 shells, and nothing from later this week.

Open the release readme, [data/rel-w2d4/README.md](../../data/rel-w2d4/README.md). Then read:

1. [notices/deploy.md](../../data/rel-w2d4/notices/deploy.md)
2. [standards/pol-deploy.md](../../data/rel-w2d4/standards/pol-deploy.md)
3. [registry/models.json](../../data/rel-w2d4/registry/models.json)
4. [registry/quota.json](../../data/rel-w2d4/registry/quota.json)
5. [credentials/dev.json](../../data/rel-w2d4/credentials/dev.json)
6. [credentials/prod.json](../../data/rel-w2d4/credentials/prod.json)
7. [endpoint/guide.md](../../data/rel-w2d4/endpoint/guide.md)
8. [dashboard/starter.md](../../data/rel-w2d4/dashboard/starter.md)

The standard is a checklist the probe can confirm. Prod credentials differ from dev. Read both files. Read the quota from the registry file. Health must report the hash on the register.

The Day 1, Day 2, and Day 3 notes still stand. A new conversation uses the same shape and can live in `Week 02/Day 04/work/interviews`.

From `problem_simulation`:

```text
python -m alwaha.interview --persona ciso --script "..\Week 02\Day 04\work\interviews\ciso.questions.txt"
```

Ask about the security review first, then the go-live checklist, then the integration-engine log. Write what you hear.

The lead copies [templates/sprint.md](templates/sprint.md) to `work/sprint.md` and sequences the deploy before the readout.
