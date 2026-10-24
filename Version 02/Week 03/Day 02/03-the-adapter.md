# The adapter

Read [registry/reg-models.json](../../data/rel-w3d2/registry/reg-models.json) and [fixtures/cloud.json](../../data/rel-w3d2/fixtures/cloud.json). The shell loads the cloud-tune hash. That hash is not on `reg-models`. Serve `lora-local` on `local-small`, and return that row's hash.

The shell asks for more GPUs than [budget/quota.json](../../data/rel-w3d2/budget/quota.json). The rank has to fit that count. The quota is a number of GPUs.

Price the published token count on `local-small`. The local line stays inside the cap. The external line does not.

The router refuses a phi field sent to `ext-large`. It also refuses a hash that is not approved. DNA stays on gradient boosting. Hours stay on retrieval.

The product manager copies [templates/approach.md](templates/approach.md) to `work/approach.md` and keeps the Week 1 families. The second table records the adapter's F1, the local cost, and the registered hash for extraction and for intent. Hours are `retrieve`.

The architect copies [templates/residency.md](templates/residency.md) to `work/residency.md`. National id, date of birth, name, and phone stay in `zone-private`. Clinic hours may be public.

`qlora.py` fits a higher rank in the same GPU count. `domain.py` keeps the unlabeled lines in [domain/ds-domain.jsonl](../../data/rel-w3d2/domain/ds-domain.jsonl) and leaves the extraction letters out. `prefs.py` expands shorthand, keeps the clause id, and drops a date the calendar cannot keep. The pairs are in [prefs/ds-prefs.jsonl](../../data/rel-w3d2/prefs/ds-prefs.jsonl). Those three are the advanced path. The two checks do not require them.
