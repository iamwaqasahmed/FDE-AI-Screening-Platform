# 04 — The outage

Four more modules. The shell of each one is what the morning packet still holds. The filled copy is in this folder. The work tests are not the shell tests.

## Breaker

The shell waits on insure and names insure as the target. That shell makes the slo check say `the booking path waits on insure`, then `insurance is treated as a site`. Those are two lines. Do not collapse them.

[breaker.py](work/app/breaker.py) opens the breaker when insure is down, leaves it uncalled, and sends the booking path to the rules worker. [outage.json](sources/release/insure/outage.json) names the partner. Do not copy a timeout. insure is a partner. It is not a site.

## Degradation

The shell fails the reply when the model is down. That shell makes the slo check say `the patient reply fails closed when the model is down`.

[degrade.py](work/app/degrade.py) keeps a status row's text and sends a booking to the rules worker. [model-down.json](sources/release/serving/model-down.json) has one status row and one booking row.

## Purchase

The shell buys every note. That shell makes the slo check say `the purchase route misses Ramadan`. The message does not print a date or a week count.

[procure.py](work/app/procure.py) returns rent when the purchase misses the deadline and the rent arrival is on or before it. It returns buy when the purchase meets the deadline. That buy path is expected. The shell sentence `Buy the GPUs.` is gone. [lead-time.json](sources/release/finance/lead-time.json) names `purchase_weeks`. Do not copy the count or a date off the file. The architecture draft says a purchase takes 16 weeks.

## Hospitals

The shell bills every hospital the full backlog. That shell makes the slo check say `the hospital split uses one figure for every hospital`. The message does not print a figure.

[hospitals.py](work/app/hospitals.py) bills each hospital its own share. [shares.json](sources/release/hospitals/shares.json) names h-nakhl, h-safra, h-wadi, and h-ain. Do not copy a figure.

The shell suite prints `Ran 8 tests` and `OK`. That pass is the shell. This folder's suite prints `Ran 9 tests` and `OK`. The extra test is the purchase that fits.

A breaker miss, a degradation miss, a purchase miss, and a hospital miss all fail the same check, `chk-w4-slo`.

## The path through the files

The morning chapter [07-the-outage.md](../Student_Copy/07-the-outage.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [05 — The pages](05-the-pages.md).
