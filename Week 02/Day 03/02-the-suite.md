# The suite

Copy [app](app) to `Week 02/Day 03/work/app`. Copy [tests](tests) to `Week 02/Day 03/work/tests`. Leave the copies in this folder unchanged. Copy [.github/workflows/ci.yml](.github/workflows/ci.yml) into `work/.github/workflows/ci.yml`.

The shell calendar still counts Friday and ignores the holiday list. The shell receipt test sleeps. The shell journey treats the model's sentence as the result.

Use the business calendar from Week 1. Pin the clock. Read the minutes from [clock/receipt.json](../../data/rel-w2d3/clock/receipt.json). Assert the mock state.

The recorded completion stays in the pack. Do not copy [fixtures/model.json](../../data/rel-w2d3/fixtures/model.json) into `work/`. That file is watermarked.

From `work`, with the pack built:

```text
python -m unittest discover -s tests -q
```

The workflow runs that same command. A live cluster deploy is a later day.
