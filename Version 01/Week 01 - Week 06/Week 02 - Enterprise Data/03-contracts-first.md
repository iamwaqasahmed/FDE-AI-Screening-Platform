# Contracts first

**Days 1 and 2. Be the architect.** A contract is written before the loader. The loader is the test that the contract is true.

`engagement/workstreams/contracts.csv` names the hat that produces each file and the hat that uses it. You do both, in that order. Do not change a shape in one hat without using the new shape in the next. This week's drop already changed one. The eleven feeds below are the ones your pipelines will read. Each gets a file `contracts/<feed>.yaml`, from [the example](templates/contract.example.yaml).

## The eleven feeds

`registry_file`, `registry_api`, `pacs`, `shared_folder`, `grader`, `ophthalmology`, `epr_letters`, `lab`, `booking`, `sms`, `vendor_retrospective`.

For each one, record the system, the trust zone, what one row is, the keys, the columns and what each means, the date formats, the defect you have now seen, the owner, who consumes it, and the conditions that must fail the load. Take the meaning from the file and from the interface note. The data catalogue is a claim about the file. Check the claim before you copy it.

A contract test is code:

- An unknown column fails.
- A missing required column fails.
- A date that does not parse fails.
- A row is never dropped without a line in the log. A silent drop is a failure.

## The catalogue and the lineage

`handover/architecture/data_catalogue.csv` describes columns. `lineage.csv` says which dataset feeds which, and when that was last verified. Several descriptions are no longer true. The booking status, the lab unit, the warehouse eligibility flag, the SMS receipt order, the call-centre reason column, and the finance cost-centre codes are the ones to test against the files.

`unlinked_keys` is the list of person-keys that carry no name and no date of birth in this drop. Lab patient id and booking id are the two. Say so in the contract. Do not invent a join for them.

Cite `data-quality-note`, `district-circular-2022`, and `retention-rule` where a contract depends on them. A rule only applies when its status, dates, and site fit.

## Stop. Contracts before loaders.

Do not write a loader for a feed whose contract file does not yet exist.

## Fill these findings

| Item | What it holds |
|---|---|
| `catalogue_stale` | `entries`, a list of `dataset.column` |
| `unlinked_keys` | `keys`, the person-keys with no demographics |

**A miss that looks like progress.** Copying a catalogue definition into the contract because the catalogue has an owner and a review date.

**Finish.** Eleven contract files exist, each with the fields in the example, and the two findings are filled.

Next: [The APIs](04-the-apis.md).
