# 06 — The pages

Open the finished [approach.md](work/approach.md) and [residency.md](work/residency.md) and put them beside yours.

## Approach

The first table keeps the Week 1 families. `p-dna` stays `classical-ml`. `p-info` stays `retrieve`. A family that does not fit says `family does not fit`, except DNA, which says `dna is not a tabular model`, and `p-info`, which says `hours questions are not left on retrieval`. A missing id, a missing file, or a missing table says `approach.md is missing`.

The second table is the customization block. Extraction and intent use method `lora`. Hours use method `retrieve`. Once the live score clears the floor, the F1 cell, the cost cell, and the hash cell have to match the adapter that was just served. The cells are already in [approach.md](work/approach.md). This chapter does not type them again. A mismatch says `the measured value does not match the adapter`, or `the hash is not on reg-models` when the hash cell is the wrong row. The message does not print an F1, a cost, or a hash. Do not put the cloud hash on this page.

The pipe characters stay. The check reads the cells between them.

## Residency

The columns are `field` and `zone`. National id, date of birth, name, and phone are `zone-private`. Clinic hours are `public`. A missing row, or a phi field in another zone, says `the residency note lets a phi field leave`. The message does not name the field. The pipe characters stay.

`slice-lora` does not read these two files. A page miss fails only the model check.

Next: [07 — Knowledge](07-knowledge.md).
