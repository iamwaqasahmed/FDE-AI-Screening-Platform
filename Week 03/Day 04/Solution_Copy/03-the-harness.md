# 03 — The harness

Open the three finished files and put them beside yours. The shell is the file that makes the eval check name the miss. The filled file is the one in this folder.

## Score

The shell reports a perfect score for every slice. That shell makes the eval check say the extraction score misses the held-out slice, the citation score misses the held-out slice, and the journey score misses the held-out slice. The judge check still passes.

[score.py](work/app/score.py) counts field matches for extraction, and it counts a citation only when the document id and the span both match, and a journey only when the state and the approval both match. The function names `extraction_f1`, `citation_accuracy`, and `journey_pass` stay. That is expected.

[metrics.json](sources/release/budget/metrics.json) holds the three floors. [score.jsonl](sources/release/slices/score.jsonl) has outputs and no label field. The check does not score that file. It scores the held-out rows. A miss does not print an F1, a doc id, or a span.

## Forecast

The shell copies last year's months into the later window. That shell makes the eval check say the forecast ignores the campaign. A forecast that returns the earlier year makes the eval check say the forecast scores the fit window. A forecast that is neither the later window nor a copy of the fit window makes the eval check say the forecast misses the later window.

[forecast.py](work/app/forecast.py) returns year 2027, months 2 and 3, and the visits written on those rows. `_LATER` and `_MONTHS` stay. `_PRIOR` does not. [campaign.md](sources/release/notices/campaign.md) says to read the counts from [ophth.csv](sources/release/demand/ophth.csv). Read them there. A miss does not print a visit count.

## Failures

The shell names every log row a pass. That shell makes the eval check say a planted failure is misnamed.

[failures.py](work/app/failures.py) reads the reply text. `return "pass"` stays on the last line. That is expected. It is the row that is not one of the four. [failures.jsonl](sources/release/slices/failures.jsonl) has `log_id` and `output` only. The file does not contain hallucination, retrieval, reasoning, or workflow. Those names are on the benchmark page. A miss does not print a log id.

Next: [04 — The gate](04-the-gate.md).
