# The estate as it runs

**Day 2. Be the architect.** Draw the current state before you draw a target. `corpus` document `ea-current-state` is the prose. `handover/architecture/components.csv` is the table. They are the same estate.

## What to read off the table

Eight zones. The component list is the membership. FHIR is whatever the protocol cell mentions: read it, do not assume only booking speaks it. A component at recovery tier 4 has no backup. The tiers that matter for this pilot are the shared folder, the grader workbench, and the vendor.

The callback path is vendor, vendor callback, integration engine, grader, in that order. Record each component's zone in that same order. The path is how a score gets back. It is also the first threat, in note 07.

## Three facts the target has to live with

The vendor's hosting is on `handover/interfaces/vendor.md`. It is not a UK region. `cloud-policy` says official-sensitive personal data stays in a UK region unless the data protection officer approves another region in writing. That approval is not in the drop. The flow that would send a photograph is pending, not allowed. Note 06 records it.

The primary-care photographs sit on the shared folder. That component is tier 4. The grader workbench is tier 1. A design that treats the folder as a backed-up store is describing a different estate.

The integration engine carries HL7 v2, and FHIR only for Patient and Appointment. Do not draw a FHIR result, a FHIR grade, or a FHIR letter. Those are file drops or HL7.

## Fill these findings

| Item | What it holds |
|---|---|
| `current_state` | `zones`, `callback_path`, `callback_zones`, `fhir`, `no_backup`, `tiers`, `vendor_hosting` |

`callback_path` and `callback_zones` keep the path order. `tiers` holds `shared-folder`, `grader`, and `vendor`. `vendor_hosting` is the hosting line, copied from the interface note.

**A miss that looks like progress.** A target diagram with no current-state page under it. The target is note 06. This note is the estate you were given.

**Finish.** You can name the zone of each step on the callback path, the components with no backup, and the region the vendor uses.

Next: [Flows across zones](06-flows-across-zones.md).
