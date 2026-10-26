# 07 — The probe

[Chapter 06](06-the-image.md) rejected a root image. This chapter replaces the health probe, its test, and the manifest.

You replace three files under `work/`, in this order:

1. [health.py](work/app/health.py), under Replace the probe
2. [test_health.py](work/tests/test_health.py), under Replace the probe test
3. [deployment.yaml](work/deploy/deployment.yaml), under Replace the manifest

Paste only those three blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not run the suite on this page. Do not run the check.

## Read these files

Open these in the packet. Read the comment at the top of each one. Do not edit them.

1. [health.py](packet/app/health.py). Search for `candidate["hash"]`. That line is the shell. The register is ignored. The next block is a picture of that file. Do not paste it. Read How the replacement works before the paste. It is not a paste. The block that replaces the work file is under the heading Replace the probe.

```text
"""Report the candidate hash.

This is the shell. Chapter 07 replaces the copy under work/app.
Leave this file in the packet unchanged.

health ignores the register and returns the candidate hash. The
prompt version is empty. The dependency list is empty. While this
shell is the file that runs, the deploy check says the health probe
does not report the registered hash.
"""

from __future__ import annotations


def health(register: dict, candidate: dict) -> dict:
    """Return the candidate hash and ignore the register.

    register is the model list. candidate is the near name that is
    not a registration. The body uses candidate["hash"]. The
    approved row on the register is not read.
    """
    del register
    return {
        "dependencies": [],
        "model_hash": candidate["hash"],
        "prompt_version": "",
        "status": "ok",
    }
```

2. [test_health.py](packet/tests/test_health.py). Search for `sha256:near`. The shell test expects the candidate stand-in. `sha256:good` on that page is a stand-in for a registered row. Neither string is a hash from [models.json](packet/release/registry/models.json). Do not paste the shell test.
3. [deployment.yaml](packet/deploy/deployment.yaml). Search for `containerPort`. You should see the image name `patient-access-assistant`. You should not see a `namespace` line. The next block is a picture of that file. Do not paste it.

```text
# Shell manifest. Chapter 07 replaces the copy under work/deploy.
# Leave this file in the packet unchanged.
# The namespace line is absent. The probe block is absent.
# The account flag that refuses a root account is absent.
apiVersion: apps/v1
kind: Deployment
metadata:
  name: patient-access-assistant
  labels:
    app: patient-access-assistant
spec:
  replicas: 1
  selector:
    matchLabels:
      app: patient-access-assistant
  template:
    metadata:
      labels:
        app: patient-access-assistant
    spec:
      containers:
        - name: assistant
          image: patient-access-assistant:day4
          ports:
            - containerPort: 8080
```

4. [models.json](packet/release/registry/models.json). Search for `"status": "approved"` together with `"id": "local-small"`. That row also has `"prompt": "p1"`. A second `local-small` row has `"status": "previous"` and `"prompt": "p0"`. That previous row stays in the file. That is expected. The probe uses the approved row. You do not type the hash.

The deploy check says `the health probe does not report the registered hash` when the body still uses the candidate, or when the prompt or the endpoint dependency is missing. It does not name the hash. It says `the manifest is not in the team namespace` when `ns-team` is missing. It says `the health probe is missing` when readiness does not call `/v1/health`. It says `the image runs as root` when the manifest does not refuse a root account. None of those messages names a hash.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

`health` reads the model register and reports one row: id `local-small`, status approved. The body carries that row's hash, that row's prompt, and the endpoint dependency. A previous row for the same id is skipped. A near name, the candidate, is not a registration and is not reported.

The shell reported the candidate, or a hash that was not the approved row. The test uses stand-in hashes so you can see which row was selected. Those stand-ins are not the hashes in the register file. Do not copy a register hash onto a page.

Before you paste, say which row the probe is allowed to report, and which near name it must leave out.

This section adds no file and no command.

## Replace the probe

This block replaces [work/app/health.py](work/app/health.py). The full path is `Week 02/Day 04/Student_Copy/work/app/health.py`. It does not replace [packet/app/health.py](packet/app/health.py). It does not replace the test. It does not replace the manifest.

Open [work/app/health.py](work/app/health.py). Do not paste into the packet copy.

1. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
2. Copy from this chapter file, not from a preview. A preview can drop the spaces. If the editor offers a styled paste, use Paste Without Formatting.
3. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it.
4. Paste as plain text. The line `def health` starts at the left edge. The lines inside the function start with four spaces. The lines inside the `return` start with eight spaces. Save.

If the terminal later shows `SyntaxError` or `IndentationError`, do not repair the spaces by hand. Run `prepare_work.py` again from the course folder, then paste the blocks from chapters 05, 06, 07, 08, and 09 again from the chapter files.

```text
"""Report the approved local-small hash from the register.

Chapter 07 replaces the work copy with this file.
Leave the packet shell unchanged.

health reads the register row whose id is local-small and whose
status is approved. The body reports that hash, that prompt, and
the endpoint dependency. The candidate argument stays on the
function line and is not used. While the shell is the file that
runs, the deploy check says the health probe does not report the
registered hash.
"""

from __future__ import annotations


def health(register: dict, candidate: dict) -> dict:
    """Return the approved local-small row from the register.

    register is the model list. The approved local-small row is
    the one the probe reports. A previous row for the same id is
    skipped. candidate is the near name. It is not a registration,
    and this function does not read it.
    """
    del candidate
    approved = next(
        row
        for row in register["models"]
        if row["id"] == "local-small" and row["status"] == "approved"
    )
    return {
        "dependencies": ["endpoint"],
        "model_hash": approved["hash"],
        "prompt_version": approved["prompt"],
        "status": "ok",
    }
```

Read the file back. You should see `local-small` and `approved` on the row the function keeps. You should see `endpoint` in `dependencies`. You should see `approved["hash"]` and `approved["prompt"]`. You should still see `candidate` on the `def health` line. That is expected. The function does not use it. You should not see `candidate["hash"]`.

## Replace the probe test

This block replaces [work/tests/test_health.py](work/tests/test_health.py). It does not replace [packet/tests/test_health.py](packet/tests/test_health.py). Use the same four steps on the work file. Copy from this chapter file, not from a preview.

`parents[1]` finds `app`. Do not change that number. `sha256:old`, `sha256:good`, and `sha256:near` are stand-ins in this test. They are not the hashes in `models.json`.

```text
"""The probe reports the approved row, not the candidate.

Chapter 07 replaces the work copy with this file.
Leave the packet shell unchanged.

sha256:old, sha256:good, and sha256:near are stand-ins. They are
not the hashes in the register file. The test checks which row
the function selects.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from health import health


class HealthTests(unittest.TestCase):
    """The probe reports the approved row, not the candidate."""
    def test_health_reports_the_registered_hash(self) -> None:
        """The approved local-small row wins over the previous row.

        The previous row comes first and is skipped. The approved
        row supplies the hash and the prompt. The candidate hash
        is not the one on the body. endpoint is a dependency.
        """
        register = {
            "models": [
                {"hash": "sha256:old", "id": "local-small", "prompt": "p0", "status": "previous"},
                {"hash": "sha256:good", "id": "local-small", "prompt": "p1", "status": "approved"},
            ]
        }
        body = health(register, {"hash": "sha256:near"})
        self.assertEqual(body["model_hash"], "sha256:good")
        self.assertEqual(body["prompt_version"], "p1")
        self.assertIn("endpoint", body["dependencies"])


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see the previous row first, with `p0`. You should see the approved row second, with `p1`. The assertion expects `sha256:good`, which is the approved stand-in, not `sha256:near`. The candidate argument is still passed in. That is expected.

## Replace the manifest

This block replaces [work/deploy/deployment.yaml](work/deploy/deployment.yaml). It does not replace [packet/deploy/deployment.yaml](packet/deploy/deployment.yaml). Use the same four steps on the work file. Copy from this chapter file, not from a preview. YAML indent is spaces. If a line that should be nested starts at the left edge, delete the file and paste the block again. Do not repair the spaces by hand.

```text
# Team manifest. Chapter 07 replaces the work copy with this file.
# Leave the packet shell unchanged.
# The namespace is ns-team. The account flag refuses a root
# account. Readiness calls /v1/health. Cpu and memory limits are set.
apiVersion: apps/v1
kind: Deployment
metadata:
  name: patient-access-assistant
  namespace: ns-team
  labels:
    app: patient-access-assistant
spec:
  replicas: 1
  selector:
    matchLabels:
      app: patient-access-assistant
  template:
    metadata:
      labels:
        app: patient-access-assistant
    spec:
      securityContext:
        runAsNonRoot: true
      containers:
        - name: assistant
          image: patient-access-assistant:day4
          ports:
            - containerPort: 8080
          readinessProbe:
            httpGet:
              path: /v1/health
              port: 8080
          resources:
            limits:
              cpu: "500m"
              memory: 512Mi
```

Read the file back. You should see `namespace: ns-team`. You should see `runAsNonRoot: true`. You should see `readinessProbe` and `/v1/health`. You should see cpu and memory limits. You should still see the name `patient-access-assistant`. That is expected. The packet manifest still has no `namespace` line. That is expected.

This page is done when `work/app/health.py` contains `approved["hash"]` and `work/deploy/deployment.yaml` contains `ns-team`. Do not run a command on this page. Do not run the check until [chapter 10](10-finish.md).

Next: [08 — The endpoint](08-the-endpoint.md).
