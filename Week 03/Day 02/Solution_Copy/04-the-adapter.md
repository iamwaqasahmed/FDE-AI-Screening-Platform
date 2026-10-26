# 04 — The adapter

Open the finished [adapter.py](work/app/adapter.py), [route.py](work/app/route.py), and [cost.py](work/app/cost.py) and put them beside yours.

## Adapter

[reg-models.json](sources/release/registry/reg-models.json) has the approved rows. The row you serve has id `lora-local`, status `approved`, and base `local-small`. The hash is the field on that row. This chapter does not type it. [cloud.json](sources/release/fixtures/cloud.json) is `cloud-tune`, and its status is `unregistered`.

The shell loads that cloud hash and asks for one more GPU than [quota.json](sources/release/budget/quota.json). While that shell is the file that runs, the check says the hash is not on reg-models, and the gpu count is over the quota. The message does not print a hash or a GPU count.

The filled file selects the approved `lora-local` row and returns that row's hash. The GPU count it returns fits the quota. The rank on that return is 8.

## Router

[router.yaml](sources/release/openapi/router.yaml) allows a call when the hash is on `reg-models` and a phi field was not sent to `ext-large`. The four phi names are national id, date of birth, name, and phone.

The shell allows every call and sends every task to `ext-large`. While that shell is the file that runs, the check says the call sends phi to ext-large, and the hash is not on reg-models. The filled file refuses a present hash that is not approved, and it refuses phi on `ext-large`. `ext-large` remains on the refuse line. That is expected. `task` returns `retrieve` for hours and `classical-ml` for DNA.

## Cost

[price-cap.json](sources/release/budget/price-cap.json) holds the floor, the spend cap, the latency cap, and the token count. You read the numbers from that file.

The shell prices the token count with `price.ext_large_per_1k` and names the model `ext-large`. While that shell is the file that runs, the check says the cost is over the price cap. The message does not print a price. The filled quote uses `price.local_per_1k`, names `local-small`, and keeps `seconds` inside the cap. If the model is still `ext-large` while the spend is inside the cap, `slice-lora` says ext-large at the price cap does not clear the slice.

## The path through the files

The morning chapter [07-the-adapter.md](../Student_Copy/07-the-adapter.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [05 — The advanced path](05-the-advanced.md).
