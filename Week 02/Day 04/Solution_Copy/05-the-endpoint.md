# 05 — The endpoint

Open the finished [router.py](work/app/router.py), [secrets.py](work/app/secrets.py), [test_router.py](work/tests/test_router.py), [test_secrets.py](work/tests/test_secrets.py), and [ci.yml](work/.github/workflows/ci.yml) and put them beside yours.

[guide.md](sources/release/endpoint/guide.md) names the endpoint `ep-local-small`, the model `local-small`, and the zone `zone-private`. `route` returns those three for prod and for dev. `env` stays on the function line and is not used. The shell returned `ext-large` on `zone-public`. While that shell is the file that runs, the check says `the router leaves the private endpoint`.

[dev.json](sources/release/credentials/dev.json) and [prod.json](sources/release/credentials/prod.json) each have `endpoint`, `env`, and `registry`. The `env` values differ. The `endpoint` values differ. `credential` opens `prod.json` when the environment is prod, and `dev.json` otherwise. The value is read from the file. It is not written in the module. The test stand-ins `dev-token` and `prod-token` are not those release values. The shell opened the dev file for every environment. While that shell is the file that runs, the check says `prod uses the dev credential`. The message does not name a token.

The work workflow keeps checkout and the Python setup, and it adds a step that runs `python -m unittest discover -s tests -q`. The packet workflow stops after Python is installed. The two files are not the same. While the packet workflow is the file that runs, the check says `the pipeline is not in CI`.

`parents[1]` on each test finds `app`. The tests do not walk up to the course folder.

The suite has six tests once the filled admission test is in place. The suite does not read the manifest or the pages. The check does.

Next: [06 — The pages](06-the-pages.md).
