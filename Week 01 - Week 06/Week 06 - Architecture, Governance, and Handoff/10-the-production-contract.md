# The production contract

**Day 4. Be the software engineer, then the data engineer.** Write two files. The checker reads them. It does not build an image, so you do not need Docker.

## The contract

Use [the contract template](templates/production.contract.yaml) and save it as `contracts/production.yaml`. Every field in the template is required.

- `service` is `screening-agent`. `zone` is `authority`. The workbench stays tier 1; set `dr_tier` to match the grader.
- `writes` is empty. The scopes are reads. The text says `read-only`.
- `account` is a name you are introducing. It is not `discovery-team`.
- `owner` is a person named in the staff or the component list. The security officer is the natural owner of the account. Do not leave it blank.
- `models` lists only models approved for official-sensitive data. The one note 09 named is enough.
- `logs` says the log holds no name and no phone. `audit` names the access audit log. `sign_in` names sign-in through the identity provider.
- `image` says the image does not contain the handover. `data` says the files are mounted, not copied.
- `fails_when` says the run fails when a question is stored.

## The Dockerfile

Save it as `deploy/Dockerfile`.

- Do not `COPY` anything under `data/`, and do not copy `.env`.
- Do not set an `ENV` or `ARG` whose name contains `key`, `token`, `secret`, or `password`.
- Do not mention `api.openai.com` or a `gpt-` model name. If you name a model id, it is `M01`, `M02`, or `M04`.

A non-root user and a pinned base image are worth doing. The checker does not grade them.

**A miss that looks like progress.** Moving the data to a volume and leaving the key in `ENV`. The volume fixes one gap. The key opens another.

**Finish.** The contract names an account that is not the discovery token, and the Dockerfile copies no authority data.

Next: [Decisions on the record](11-decisions-on-the-record.md).
