# 08 — The endpoint

[Chapter 07](07-the-probe.md) pointed the probe at the approved row. This chapter replaces the router, the credentials, their tests, and the work pipeline. Then you run the suite.

You replace five files under `work/`, in this order. Paste only the blocks under headings that start with Replace. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back.

1. [router.py](work/app/router.py), under Replace the router
2. [test_router.py](work/tests/test_router.py), under Replace the router test
3. [secrets.py](work/app/secrets.py), under Replace the credentials
4. [test_secrets.py](work/tests/test_secrets.py), under Replace the credential test
5. [ci.yml](work/.github/workflows/ci.yml), under Replace the work pipeline

Each work path must contain `Student_Copy\work`. If the path contains `packet`, close it and open the work copy. There are two workflow files. The one you replace is `Student_Copy\work\.github\workflows\ci.yml`. Leave [packet/.github/workflows/ci.yml](packet/.github/workflows/ci.yml) unchanged.

The suite command on this page is `unittest`. It is not a check. A check prints `chk-w2-deploy`. That command is only in [chapter 10](10-finish.md).

## Read these files

Open these in the packet. Read the comment at the top of each one. Do not edit them.

1. [router.py](packet/app/router.py). Search for `ext-large`. Search for `zone-public`. The shell sends every environment to the external model. The next block is a picture of that file. Do not paste it.

```text
"""Send the assistant to the external model.

This is the shell. Chapter 08 replaces the copy under work/app.
Leave this file in the packet unchanged.

route ignores the environment and returns the external model on
the public zone. While this shell is the file that runs, the
deploy check says the router leaves the private endpoint.
"""

from __future__ import annotations


def route(env: str) -> dict:
    """Return the external model for every environment.

    env is dev or prod. Neither one is used. The endpoint, the
    model, and the zone are the external model on the public zone.
    """
    del env
    return {"endpoint": "ext-large", "model": "ext-large", "zone": "zone-public"}
```

2. [secrets.py](packet/app/secrets.py). Search for `dev.json`. The shell opens that file for every environment. The prod file is not opened. The next block is a picture of that file. Do not paste it.

```text
"""Use the dev credential for every environment.

This is the shell. Chapter 08 replaces the copy under work/app.
Leave this file in the packet unchanged.

credential ignores the environment name and always opens the dev
file. While this shell is the file that runs, the deploy check
says prod uses the dev credential.
"""

from __future__ import annotations

import json
from pathlib import Path


def credential(env: str, pack: Path) -> str:
    """Return the endpoint field from the dev credential file.

    env is the environment name. It is not used. pack is the
    release folder. The file read is credentials/dev.json. The
    prod file is not opened.
    """
    del env
    payload = json.loads((pack / "credentials" / "dev.json").read_text(encoding="utf-8"))
    return payload["endpoint"]
```

3. [ci.yml](packet/.github/workflows/ci.yml). Search for `setup-python`. You should see checkout and the Python setup. You should not see `unittest`. The next block is a picture of that file. Do not paste it over the work file. The block that replaces the work workflow is under the heading Replace the work pipeline, later on this page.

```text
# Shell workflow. Chapter 08 replaces the work copy.
# Leave this file in the packet unchanged.
# Python is installed. The suite step is not here.
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
```

4. [dev.json](packet/release/credentials/dev.json) and [prod.json](packet/release/credentials/prod.json). Search for `"env"`. One file says `dev`. The other says `prod`. The `endpoint` values differ. You do not type them into `secrets.py`.
5. [guide.md](packet/release/endpoint/guide.md). Search for `ep-local-small`. Search for `zone-private`.

The deploy check says `the router leaves the private endpoint` when the route is still the external model. It says `prod uses the dev credential` when prod still reads the dev file. It says `the pipeline is not in CI` when the work workflow does not run the suite. None of those messages names a token.

## Replace the router

This block replaces [work/app/router.py](work/app/router.py). The full path is `Week 02/Day 04/Student_Copy/work/app/router.py`. It does not replace [packet/app/router.py](packet/app/router.py).

Open the work file. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste as plain text. The line `def route` starts at the left edge. Save.

If the terminal later shows `SyntaxError` or `IndentationError`, do not repair the spaces by hand. Run `prepare_work.py` again from the course folder, then paste the blocks from chapters 05, 06, 07, 08, and 09 again from the chapter files.

```text
"""Point the assistant at the private endpoint.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

route returns the private endpoint, the local-small model, and
zone-private. Dev and prod both stay there. The environment
argument stays on the function line and is not used. While the
shell is the file that runs, the deploy check says the router
leaves the private endpoint.
"""

from __future__ import annotations


def route(env: str) -> dict:
    """Return the private endpoint for every environment.

    env is dev or prod. Neither one changes the route. The
    endpoint is ep-local-small. The model is local-small. The
    zone is zone-private.
    """
    del env
    return {"endpoint": "ep-local-small", "model": "local-small", "zone": "zone-private"}
```

Read the file back. You should see `ep-local-small`, `local-small`, and `zone-private`. You should still see `env` on the `def route` line. That is expected. Dev and prod both use this return. You should not see `zone-public`.

## Replace the router test

This block replaces [work/tests/test_router.py](work/tests/test_router.py). It does not replace [packet/tests/test_router.py](packet/tests/test_router.py). Use the same steps. `parents[1]` finds `app`. Do not change that number.

```text
"""The router stays on the private endpoint.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

prod and dev both receive the same route. The environment does
not change the endpoint.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from router import route


class RouterTests(unittest.TestCase):
    """The router stays on the private endpoint."""
    def test_router_uses_the_private_endpoint(self) -> None:
        """Prod and dev both name the private endpoint.

        The endpoint is ep-local-small. The model is local-small.
        The zone is zone-private. The dev call returns that same
        endpoint.
        """
        body = route("prod")
        self.assertEqual(body["endpoint"], "ep-local-small")
        self.assertEqual(body["model"], "local-small")
        self.assertEqual(body["zone"], "zone-private")
        self.assertEqual(route("dev")["endpoint"], "ep-local-small")


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see `ep-local-small` on the prod body and again on the dev call. You should see `zone-private`. You should not see `ext-large`.

## Replace the credentials

This block replaces [work/app/secrets.py](work/app/secrets.py). It does not replace [packet/app/secrets.py](packet/app/secrets.py). Use the same steps. Copy from this chapter file, not from a preview.

```text
"""Select the credential file for the environment.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

credential opens prod.json when the environment is prod, and
dev.json otherwise. The endpoint field is the credential. The
value is read from the file. It is not written in this module.
While the shell is the file that runs, the deploy check says
prod uses the dev credential.
"""

from __future__ import annotations

import json
from pathlib import Path


def credential(env: str, pack: Path) -> str:
    """Return the endpoint field from the file for this environment.

    env selects the file. prod reads credentials/prod.json. Any
    other name reads credentials/dev.json. pack is the release
    folder. The endpoint field is the credential the caller gets.
    """
    name = "prod.json" if env == "prod" else "dev.json"
    payload = json.loads((pack / "credentials" / name).read_text(encoding="utf-8"))
    return payload["endpoint"]
```

Read the file back. You should see `prod.json` when `env` is `prod`. You should still see `dev.json` on the other branch. That is expected. Prod does not read the dev file. You should not see a token written in this file. The value comes from `payload["endpoint"]`.

## Replace the credential test

This block replaces [work/tests/test_secrets.py](work/tests/test_secrets.py). It does not replace [packet/tests/test_secrets.py](packet/tests/test_secrets.py). Use the same steps. `dev-token` and `prod-token` are stand-ins this test writes into a temporary folder. They are not the credentials in the release. `parents[1]` finds `app`. Do not change that number.

```text
"""Prod and dev read different credential files.

Chapter 08 replaces the work copy with this file.
Leave the packet shell unchanged.

dev-token and prod-token are stand-ins written into a temporary
pack. They are not the credentials in today's release.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from secrets import credential


class SecretTests(unittest.TestCase):
    """Prod and dev read different credential files."""
    def setUp(self) -> None:
        """Write two stand-in credential files under a temporary pack."""
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name) / "credentials"
        root.mkdir()
        (root / "dev.json").write_text(json.dumps({"endpoint": "dev-token"}), encoding="utf-8")
        (root / "prod.json").write_text(json.dumps({"endpoint": "prod-token"}), encoding="utf-8")
        self.pack = Path(self.tmp.name)

    def tearDown(self) -> None:
        """Remove the temporary pack."""
        self.tmp.cleanup()

    def test_prod_differs_from_dev(self) -> None:
        """Each environment returns the stand-in from its own file.

        dev reads the dev file. prod reads the prod file. The two
        values are not equal.
        """
        self.assertEqual(credential("dev", self.pack), "dev-token")
        self.assertEqual(credential("prod", self.pack), "prod-token")
        self.assertNotEqual(credential("dev", self.pack), credential("prod", self.pack))


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see `dev-token` for dev and `prod-token` for prod. You should see `assertNotEqual`. The shell expected both calls to return `dev-token`. That expectation is gone.

## Replace the work pipeline

This block replaces [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml). It does not replace [packet/.github/workflows/ci.yml](packet/.github/workflows/ci.yml). Use the same steps. Keep the spaces before each step. The step lines start with six spaces, then a dash.

```text
# Work workflow. Chapter 08 replaces the work copy with this file.
# Leave the packet shell unchanged.
# Checkout and Python setup stay. The tests step runs the suite.
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: tests
        run: python -m unittest discover -s tests -q
```

Read the file back. You should see `unittest` and `tests` on the last step. You should still see `actions/checkout@v4` and `setup-python`. That is expected. The packet copy still has no `unittest`. Leave that packet file as it is.

## Run the suite

Do this only after the five Replace blocks on this page are pasted, and after chapters 06 and 07 are pasted. Before the command, open each work file and search. Every row has to match. A row that fails means the picture was pasted, or that chapter was skipped. Paste that chapter's Replace block again. Do not repair the file by hand.

| Work file | Search for this | You should find it |
| --- | --- | --- |
| `work/app/admit.py` | `return "rejected"` | Yes. The packet copy still says `return "accepted"` |
| `work/deploy/Dockerfile` | `USER 1000` | Yes. The packet copy still says `USER root` |
| `work/app/health.py` | `approved["hash"]` | Yes. The packet copy still says `candidate["hash"]` |
| `work/deploy/deployment.yaml` | `ns-team` | Yes. The packet copy has no namespace line |
| `work/app/router.py` | `ep-local-small` | Yes. The packet copy still says `ext-large` |
| `work/app/secrets.py` | `prod.json` | Yes. The packet copy opens only `dev.json` |
| `work/.github/workflows/ci.yml` | `unittest` | Yes. The packet copy has no `unittest` |

The suite checks the four app files and the four tests. It does not read the Dockerfile, the manifest, or the pages. A suite that prints `OK` can still leave the manifest or the pages unfinished. Those are graded by the check in chapter 10.

Open a new terminal in the course folder. Do not reuse the window that is inside `problem_simulation`. If the window is already inside `Week 02/Day 04/Student_Copy/work`, skip the `cd` line and run the python line. If chapter 01 told you to use `py`, use `py` here.

```text
cd "Week 02/Day 04/Student_Copy/work"
python -m unittest discover -s tests -q
```

You should see a line that starts with `Ran 6 tests`, then a blank line, then `OK`. The time on the `Ran` line can differ. There is no `FAIL` and no `ERROR`. That is the suite you want. This command is not the check. The work workflow runs this same command. You already saw `unittest` and `tests` in the work `ci.yml`.

If you see `The system cannot find the path specified` or `No such file or directory` on the `cd` line, this window is not the course folder. Open a new terminal in the course folder and run both lines. If the count is 5, the admission test is still the shell. Paste `test_admit.py` from chapter 06 again. If you see `FAIL` or `ERROR`, a paste from chapter 06, chapter 07, or this page did not land. Do not repair the file by hand. Paste that chapter's block again from the chapter file. If you see `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05, 06, 07, 08, and 09 again from the chapter files.

Do not run the check until [chapter 10](10-finish.md).

Next: [09 — The pages](09-the-pages.md).
