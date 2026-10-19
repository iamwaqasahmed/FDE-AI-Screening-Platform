# The threat model

**Day 3. Architect and software engineer.** Four threats are already in the estate. Write `threats.csv` with one row each. Use [the threats template](templates/threats.example.csv). The columns are `threat_id,title,components,evidence,standard,live,mitigation,owner`.

`live` is `true` or `false`. `standard` is a document id. `owner` is a person named in the files. `evidence` or `components` has to carry the key below, so a reader can find the same row you found.

## The four

T1. The callback path from note 05. Zones: external, dmz, authority, screening-service. The path still exists, so it is live. Cite `ea-principles`, `security-supplier-assurance`, or `ea-current-state`. Put the four component ids in `components`.

T2. A service account holds `directory-admin`. Read `handover/identity/accounts.csv` and `role_mappings.csv`. Service accounts have account type `service`. The excess role is `directory-admin`. Put the account id in `evidence`. Cite `security-authentication-standard`. It is live: the role is still granted.

T3. `INC-0270`. Names and phone numbers were written to `handover/booking/api.log` inside the window on the service-desk ticket. R-08 was closed with a mitigation, and the debug lines stop at the end of that window. The threat is not live. Cite `security-logging-standard`. Put `INC-0270` in `evidence`.

T4. Accounts that should have lost access and have not. Two ways to see them, and either key is accepted in `evidence`:

- `INC-0262`, or
- the account ids themselves.

A workforce row with status `left` whose identity account is still `enabled` is one. An account whose open roles were granted on more than one date is the other: the later grant was a role that should have ended. Cite `security-authentication-standard`. This one is live, and it is why R-11 reopens. R-11's mitigation says monthly. The standard says one working day.

`reopen` in the finding is `R-11`. `stays_closed` is `R-08`.

## Fill these findings

| Item | What it holds |
|---|---|
| `threat_summary` | `threat_ids`, `live`, `service_account`, `excess_role`, `stale_accounts`, `reopen`, `stays_closed` |

`threat_ids` is `T1` to `T4`. `live` is the ones that are still true. `excess_role` is `directory-admin`. `stale_accounts` is the account ids, sorted.

**A miss that looks like progress.** Treating a closed risk as a closed threat, or a past incident as a live one. R-08 is closed and T3 is not live. R-11 is closed and T4 is live. Those are different sentences.

**Finish.** `threats.csv` has four rows. You can say which two risks you would touch, and which one you would leave closed.

Next: [Service levels](08-service-levels.md).
