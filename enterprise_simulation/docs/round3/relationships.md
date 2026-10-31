# Relationships

`edges(commands)` in `src/access/round3/identity_graph.py` walks every command and appends a dict. Keys are `from`, `rel`, `to`, and `source`. `source` is that command's `command_id`. A later command does not remove an earlier dict from the list.

`rel` is `phone`, `member`, `mrn`, or `same_person`.

## How a command becomes edges

If the payload has `bindings`, each binding is a subject. Otherwise the payload itself is the subject. A subject with `person_id` and `phone` adds a `phone` edge. `member_id` adds a `member` edge. `mrn` adds an `mrn` edge. `from` is the person id. `to` is the phone, member id, or medical-record number.

A payload `same_person` pair adds one `same_person` edge. `from` is the first id. `to` is the second id. That pair is an extra edge. It does not replace a `member` or `mrn` edge from the same command.

## Rows on R3C-1

`commands()` returns eight commands. Ids start with `cmd-r3c-`. Stream ids start with `r3c-`. Times are in 2026. Authority is `hospital`, `channel`, or `payer`.

`cmd-r3c-request` is channel `RequestAccepted` for `p-r3c-1`. It stores member id `MBR-R3C-1`, phone `604-555-2770`, and ref `R3C-1`. Its `same_person` pair is `p-r3c-1` and `MBR-R3C-1`. `cmd-r3c-member` records that member id again.

`cmd-r3c-mrn` stores medical-record number `MRN-R3C-1` on `p-r3c-1`. `cmd-r3c-chart` opens a chart for `p-r3c-2` and stores no phone. On stream `r3c-chart`, `cmd-r3c-phone-copy` is `stream_rev` 3 and stores phone `604-555-2770` on `p-r3c-2`.

`cmd-r3c-split` is hospital `IdentitySplit` at `stream_rev` 4. Its bindings store phone `604-555-2770` on `p-r3c-1` and phone `604-555-2771` on `p-r3c-2`. `cmd-r3c-phone-copy` is still in `commands()`, and the phone edge from that command is still in `edges()`.

`cmd-r3c-coverage` is payer `CoverageDecided` for ref `R3C-1`. The member id on that row is `MBR-R3C-9`. Currency is CAD. `member_region` is BC. `answer` is yes. `effective_from` and `effective_to` are the window, and `window` repeats those two instants.

`cmd-r3c-note` names the two hospital phone rows and the two member ids. It adds no edge.

Read the list in order. The same phone can appear on more than one edge, each with its own source.
