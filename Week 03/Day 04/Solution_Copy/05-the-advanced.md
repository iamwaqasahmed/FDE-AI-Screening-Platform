# 05 — The advanced path

Open the two finished files and put them beside yours. The two checks do not require these files. You still do not delete them. The suite imports them. When the files are present, they keep the behavior the advanced tests already compare.

## Intervals

The shell treats every district as a point at one. [intervals.py](work/app/intervals.py) is a Wilson interval. An empty slice covers the whole range. `z` stays `1.96`. `by_district` groups on district and counts the correct rows.

## Experiment

The shell reports the contained count. [experiment.py](work/app/experiment.py) reads `protocol["metric"]` and does not substitute another field. The higher rate on that metric is the arm the report returns. The notice says the effect is not stated. This file does not name a winning arm in a comment. [ab-status.md](sources/release/notices/ab-status.md) is that notice. [ab-status.json](sources/release/experiment/ab-status.json) holds the counts and the metric name.

The suite in this folder prints `Ran 11 tests` and then `OK`. The seven test files match the packet byte for byte. Do not add a comment to a test. The same tests fail beside the shells.

Next: [06 — The pages](06-the-pages.md).
