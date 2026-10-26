# 06 — The image

[Chapter 05](05-the-sprint.md) put the deploy before the readout. This chapter replaces the admission code, its test, and the image account.

You replace three files under `work/`, in this order:

1. [admit.py](work/app/admit.py), under Replace the admission
2. [test_admit.py](work/tests/test_admit.py), under Replace the admission test
3. [Dockerfile](work/deploy/Dockerfile), under Replace the image

Paste only those three blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

Do not run the suite on this page. The suite command is in [chapter 08](08-the-endpoint.md). It is not a check. The check prints `chk-w2-deploy`. That command is only in [chapter 10](10-finish.md).

## Read these files

Open these in the packet. Read the comment at the top of each one. Do not edit them.

1. [admit.py](packet/app/admit.py). Search for `return "accepted"`. That line is the shell. Every image is accepted. The user, the log line, and the national id are ignored. The next block is a picture of that file. Do not paste it. Pasting it puts the shell back into `work/`. The block that replaces the work file is under the heading Replace the admission, later on this page.

```text
"""Accept every image and keep the log line.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

admit ignores the user, the log line, and the national id. It
returns accepted for every call. emitted_log returns the log line
unchanged. While this shell is the file that runs, the deploy check
says the image runs as root, and a national id is in the deploy log.
"""

from __future__ import annotations


def admit(user: str, log_line: str, national_id: str) -> str:
    """Return accepted and ignore every argument.

    user is the account the image would run as. log_line is the
    deploy log. national_id is the id the log must not keep. None
    of them is used. A root image is still accepted.
    """
    del user, log_line, national_id
    return "accepted"


def emitted_log(log_line: str, national_id: str) -> str:
    """Return the log line unchanged.

    national_id is the id that should leave the line. This shell
    keeps it. The fixture log stays in the pack.
    """
    del national_id
    return log_line
```

2. [test_admit.py](packet/tests/test_admit.py). Search for `accepted`. The shell test expects a root account to be accepted, and it expects the stand-in id to stay on the log line. Do not paste that file into `work/`. The stand-in is `NID-sample`. It is not the id in the pack log.
3. [Dockerfile](packet/deploy/Dockerfile). Search for `USER root`. That line is the shell. The next block is a picture of that file. Do not paste it.

```text
# Shell image. Chapter 06 replaces the copy under work/deploy.
# Leave this file in the packet unchanged.
# The last USER line is root. While this file is the image that
# runs, the deploy check says the image runs as root.
FROM python:3.12-slim
WORKDIR /app
COPY app/ /app/
EXPOSE 8080
USER root
CMD ["python", "app.py"]
```

4. [log.json](packet/release/fixtures/log.json). Open it. Do not copy it into `work/`. Do not paste it into a prompt. The filled admission removes an id from a line it is given. It does not read this file itself. The check reads the file from the built pack.

The deploy check says `the image runs as root` when a root account is still accepted, or when the image account is still root. It says `a national id is in the deploy log` when the id stays on the emitted line. It says `the deploy rejected a registered image` when a clean account with a clean line is rejected. None of those messages names the id.

The demo in [chapter 03](03-the-standard.md) already printed `root image: rejected` and `registered image: accepted`. Those lines do not print a hash or a national id. The test under Replace the admission test uses the stand-in `NID-sample`. That is expected. The demo and the test are different.

## Replace the admission

This block replaces [work/app/admit.py](work/app/admit.py). The full path is `Week 02/Day 04/Student_Copy/work/app/admit.py`. It does not replace [packet/app/admit.py](packet/app/admit.py). It does not replace the test. It does not replace the Dockerfile.

Open [work/app/admit.py](work/app/admit.py). That is the work copy. Do not paste into the packet copy.

1. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
2. Copy from this chapter file, not from a preview. A preview can drop the spaces. If the editor offers a styled paste, use Paste Without Formatting.
3. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it.
4. Paste as plain text. The line `def admit` starts at the left edge. The lines inside the function start with four spaces. Save.

If the terminal later shows `SyntaxError` or `IndentationError`, do not repair the spaces by hand. Run `prepare_work.py` again from the course folder, then paste the blocks from chapters 05, 06, 07, 08, and 09 again from the chapter files. Do not repair a Python file by hand.

```text
"""Reject root, and keep a national id out of the log.

Chapter 06 replaces the work copy with this file.
Leave the packet shell unchanged.

admit rejects a root account and an account named 0. It rejects a
log line that still carries the national id. A clean account with
a clean line is accepted. emitted_log removes the id from the
line. While the shell is the file that runs, the deploy check says
the image runs as root, and a national id is in the deploy log.
"""

from __future__ import annotations


def admit(user: str, log_line: str, national_id: str) -> str:
    """Reject root, reject a logged id, and accept a clean image.

    user is the account the image would run as. root and 0 are
    rejected. log_line is the deploy log. national_id is the id
    that must not remain on that line. A line that still contains
    it is rejected. Any other account with a clean line is accepted.
    """
    if str(user).lower() in {"root", "0"}:
        return "rejected"
    if national_id and national_id in log_line:
        return "rejected"
    return "accepted"


def emitted_log(log_line: str, national_id: str) -> str:
    """Return the log line with the national id removed.

    national_id is the id the pack fixture carries. The returned
    line no longer contains it. The fixture file itself stays in
    the pack.
    """
    if national_id:
        return log_line.replace(national_id, "")
    return log_line
```

Read the file back. You should see `rejected` when the user is root, and `rejected` when the user is `0`. You should see `rejected` when the national id is still on the log line. You should see `accepted` on the last return, for a clean account. You should still see the word `root` on the line that rejects it. That is expected. The deployment page in chapter 09 does not say the container runs as root.

## Replace the admission test

This block replaces [work/tests/test_admit.py](work/tests/test_admit.py). It does not replace [packet/tests/test_admit.py](packet/tests/test_admit.py). Use the same four steps on the work file. Copy from this chapter file, not from a preview. Do not paste the picture from the top of this page.

`parents[1]` is the folder that contains `app`. That line stays as it is. Do not change the number.

```text
"""Root is rejected, and the stand-in id leaves the log.

Chapter 06 replaces the work copy with this file.
Leave the packet shell unchanged.

NID-sample is a stand-in. It is not read from a pack file. The
fixture log stays in the pack.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from admit import admit, emitted_log


class AdmitTests(unittest.TestCase):
    """Root is rejected, and the stand-in id leaves the log."""
    def test_root_is_rejected(self) -> None:
        """root and 0 are rejected.

        started is a clean log line. The stand-in id is not on
        that line. The account is what fails.
        """
        self.assertEqual(admit("root", "started", "NID-sample"), "rejected")
        self.assertEqual(admit("0", "started", "NID-sample"), "rejected")

    def test_clean_user_is_accepted(self) -> None:
        """A clean account with a clean line is accepted.

        1000 is not root. started does not carry the stand-in id.
        """
        self.assertEqual(admit("1000", "started", "NID-sample"), "accepted")

    def test_national_id_is_rejected_and_dropped(self) -> None:
        """A line that still carries the id is rejected, then stripped.

        The admit call sees the id on the line. emitted_log returns
        the line without that id.
        """
        line = "nid=NID-sample"
        self.assertEqual(admit("1000", line, "NID-sample"), "rejected")
        self.assertNotIn("NID-sample", emitted_log(line, "NID-sample"))


if __name__ == "__main__":
    unittest.main()
```

Read the file back. You should see `rejected` for `root` and for `0`. You should see `accepted` for `1000` with the line `started`. You should see `NID-sample` removed from the emitted line. The shell's `accepted` result for root is gone. The word `root` is still on the rejection line. That is expected.

## Replace the image

This block replaces [work/deploy/Dockerfile](work/deploy/Dockerfile). It does not replace [packet/deploy/Dockerfile](packet/deploy/Dockerfile). Use the same four steps on the work file. Copy from this chapter file, not from a preview.

```text
# Non-root image. Chapter 06 replaces the work copy with this file.
# Leave the packet shell unchanged.
# The last USER line is the unprivileged account. The shell still
# ends on root.
FROM python:3.12-slim
WORKDIR /app
COPY app/ /app/
EXPOSE 8080
USER 1000
CMD ["python", "app.py"]
```

Read the file back. You should see `USER 1000`. You should not see `USER root`. The comment still says the shell ends on root. That comment describes the packet file. The last `USER` line in this work file is `1000`.

This page is done when `work/app/admit.py` contains `return "rejected"`, `work/tests/test_admit.py` contains `test_clean_user_is_accepted`, and `work/deploy/Dockerfile` contains `USER 1000`. The packet copies still contain `return "accepted"` and `USER root`. That is expected. Do not run a command on this page. Do not run the check until [chapter 10](10-finish.md).

Next: [07 — The probe](07-the-probe.md).
