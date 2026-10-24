# The pipeline

Copy [app](app) to `Week 02/Day 04/work/app`. Copy [deploy](deploy) to `Week 02/Day 04/work/deploy`. Copy [tests](tests) to `Week 02/Day 04/work/tests`. Leave the copies in this folder unchanged. Copy [.github/workflows/ci.yml](.github/workflows/ci.yml) into `work/.github/workflows/ci.yml`.

The shell image is root. The shell admission keeps the fixture log line. The shell health returns the candidate hash. The shell workflow does not run the tests.

Read the approved `local-small` hash from [registry/models.json](../../data/rel-w2d4/registry/models.json). A near name in [fixtures/candidate.json](../../data/rel-w2d4/fixtures/candidate.json) is not a registration. Do not copy [fixtures/log.json](../../data/rel-w2d4/fixtures/log.json) into `work/`. That file is watermarked.

The manifest belongs in the team namespace from the endpoint guide. Readiness calls `/v1/health`. The workflow runs the suite.

From `work`, with the pack built:

```text
python -m unittest discover -s tests -q
```
