# 04 — The sample

Open the finished [labels.py](work/app/labels.py), [synthetic.py](work/app/synthetic.py), and [scan.py](work/app/scan.py) and put them beside yours.

## Relabel

[ann-v1.md](sources/release/guidelines/ann-v1.md) records a phone photo as a scan and may leave the sub-specialty blank. [ann-v2.md](sources/release/guidelines/ann-v2.md) reads the text. Phone or photo is source type photo. Scan, when the text does not say phone or photo, is source type scan. Anything else is typed. Retina and pediatric come from the text. Any other sub-specialty stays blank. The guideline on the result is `ann-v2`.

[adjudicated.jsonl](sources/release/letters/adjudicated.jsonl) holds the four development labels. They already follow ann-v2. The check scores the held-out letters. Those letters live in the clerk file. That file is not in this folder.

The shell copies the clerk fields and sets the guideline to ann-v1. While that shell is the file that runs, the check says a phone photo is still a scan, a sub-specialty is still blank, and the sample still follows ann-v1. The word `scan` remains in the filled file as a source type for a real scan. That is expected. `ann-v1` does not.

## Sample

[fidelity.json](sources/release/cards/fidelity.json) is the card. It names a sample size, a rare sub-specialty, a specialty mix, a phrase band for Kindly, and a label margin. The check does not print a rate. `sample` ignores the clerk letters and returns four invented rows. Two are endocrinology and two are ophthalmology. Two name the rare sub-specialty. Two say Kindly. None carry an id.

The shell returns the first real letter. While that shell is the file that runs, the check says the synthetic sample misses the fidelity card, contains a watermark, and contains a national id. The message does not print the watermark, a rate, or a national id.

## Scan

`accept` returns false when the text contains the mark prefix, and false when a non-empty history id is in the text. A clean invented sentence returns true. The shell returns true for every file. While that shell is the file that runs, and the filled sample is left in place, the check says the synthetic sample contains a watermark and contains a national id. Copying the shell sample instead says those two lines and also says the sample misses the fidelity card.

The clerk file stays in the built pack. A copy under `work/` makes every check say `a watermarked sample is in the work directory`. The message does not print the watermark.

Next: [05 — The advanced path](05-the-advanced.md).
