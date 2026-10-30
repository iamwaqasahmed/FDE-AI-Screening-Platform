# 03 — The standard

[Chapter 00](00-background.md) named Al-Waha and the front-desk wish. This chapter is the fourth morning of Module 2. The deployment standard and the prod credentials arrive.

The case date on today's drop is 20 January 2027. The note is from the Chief Information Security Officer, [Omar Al-Zahrani](packet/kickoff/personas/ciso.md). His id is `ciso`. You read his drop. You do not interview him today.

## What you do on this page

Three steps. You do not edit a file. You do not paste a block from this page into `work/`.

1. Open each linked file and search it. In the editor, press Ctrl+F on Windows or Command+F on macOS, then type the word this page names. Every fenced block below is a picture of a file you just opened. Leave the picture on this page.
2. Run the deploy demo under [Run the deploy demo](#run-the-deploy-demo). You should see two lines.
3. Open [chapter 04](04-words.md).

If chapter 01 told you to use `py` instead of `python`, use `py` in the command on this page too.

## What arrived today

[deploy.md](packet/release/notices/deploy.md) says the deployment standard is in force. Search for `Read the quota`. The number stays in the quota file. Search for `pol-deploy`. That checklist is what the probe can confirm. Search for `national id`. A log line that carries one is rejected. This block is a picture of that file. Do not paste it into `deployment.md`. The block that replaces `deployment.md` is in [chapter 09](09-the-pages.md).

```text
# Deploy standard

The deployment standard is in force. Prod credentials are in this pack, and they differ from dev. The inference endpoint has a quota. Read the quota from the registry file.

pol-deploy is the checklist the probe can confirm. A container running as root is rejected. A log line that carries a national id is rejected.

The go-live checklist the security office uses is a separate list.
```

The sentence in that notice is about a container that is running as root being rejected. The deployment page you write later says the container user is non-root. It does not say "The container runs as root."

[pol-deploy.md](packet/release/standards/pol-deploy.md) is the checklist. The columns are Id and Check. Search for `non-root`. Search for `/v1/health`. This block is a picture of that table. Do not paste it into `deployment.md`. Chapter 09 cites `pol-deploy` and uses the word `non-root`.

```text
| Id | Check |
| --- | --- |
| non-root | The container user is not root. |
| health-probe | Readiness calls /v1/health. |
| resource-limits | The container has cpu and memory limits. |
| no-phi-in-logs | A log line has no national id. |
| image-provenance | The image carries a provenance label. |
| registered-model-hash | The served hash is on the register. |
```

Provenance and the resource limits are on this list. The check does not read a provenance page or a limits page. You do not write those pages today.

[models.json](packet/release/registry/models.json) is the register. The fields are `hash`, `id`, `status`, and `zone`. Two of the rows also have `prompt`. This block is a picture of that file. Do not paste it into `health.py`. [Chapter 07](07-the-probe.md) reads the approved row from the file. You do not type the hash.

```text
{
  "models": [
    {
      "hash": "sha256:f23bd66c0c3d29ba",
      "id": "ext-large",
      "status": "approved",
      "zone": "zone-public"
    },
    {
      "hash": "sha256:f44c007923644956",
      "id": "local-small",
      "prompt": "p1",
      "status": "approved",
      "zone": "zone-private"
    },
    {
      "hash": "sha256:8867d023c85ca94d",
      "id": "local-small",
      "prompt": "p0",
      "status": "previous",
      "zone": "zone-private"
    },
    {
      "hash": "sha256:c79a865ded71c33f",
      "id": "local-embed",
      "status": "approved",
      "zone": "zone-private"
    }
  ]
}
```

You should see two `local-small` rows. The approved row has `prompt` `p1` and `status` `approved`. The previous row has `prompt` `p0` and `status` `previous`. That is expected. The probe uses the approved row. `ext-large` stays on the public zone. `local-embed` stays approved beside it. That is expected. The hash values are in this file. Chapter 07 does not copy them into the function.

[quota.json](packet/release/registry/quota.json) is the quota. The fields are `endpoint` and `requests`. This block is a picture of that file. Do not paste it into a page. Read the number under `requests` in the file. [Chapter 04](04-words.md) does not type that number.

```text
{
  "endpoint": "ep-local-small",
  "requests": 47
}
```

[dev.json](packet/release/credentials/dev.json) and [prod.json](packet/release/credentials/prod.json) are the two credential files. Each one has `endpoint`, `env`, and `registry`. These blocks are pictures of those files. Do not paste them into `secrets.py`. [Chapter 08](08-the-endpoint.md) reads the file for the environment. You do not type the endpoint value.

```text
{
  "endpoint": "dev-87f9cded",
  "env": "dev",
  "registry": "dev-87f9cded"
}
```

```text
{
  "endpoint": "prod-2f020c0e",
  "env": "prod",
  "registry": "prod-2f020c0e"
}
```

The `env` field on the first file is `dev`. The `env` field on the second file is `prod`. The `endpoint` values differ. That is expected. Prod does not reuse the dev file.

[guide.md](packet/release/endpoint/guide.md) is the endpoint guide. Search for `https://assistant.site-a.alwaha.internal`. Search for `ns-team`. Search for `ep-local-small`. Search for `zone-private`. Search for `/v1/health`. This block is a picture of that file. Do not paste it into `deployment.md`. Chapter 09 cites `endpoint/guide.md`.

```text
# Endpoint

The practice URL is https://assistant.site-a.alwaha.internal.
The namespace is ns-team.
The endpoint id is ep-local-small.
The model is local-small, in zone-private.

GET /v1/health reports the registered hash, the prompt version, and the endpoint dependency. Read the hash from the register. A near name in the candidate fixture is not a registration.

Dev and prod credentials are different files.
```

[starter.md](packet/release/dashboard/starter.md) is the monitoring list for this stage. Search for `request rate`. Search f. This block is a picture of that file. Do not paste it into `deployment.md`. The Monitoring section in chapter 09 uses these words.

```text
# Starter dashboard

The dashboard shows request rate, error rate, and model latency.
The rest of the operations stack arrives in a later module.
```

[health.yaml](packet/release/openapi/health.yaml) is the health spec. Search for `readHealth`. Search for `/v1/health`. [registry.yaml](packet/release/openapi/registry.yaml) is the admission spec. Search for `admitImage`. Search for `national id`. [endpoint.yaml](packet/release/openapi/endpoint.yaml) is the inference spec. Search for `Over the quota`. A request over the quota waits. It does not spill onto `ext-large`. The check does not read a quota page. You do not write one today.

[candidate.json](packet/release/fixtures/candidate.json) is the near name. The fields are `hash`, `id`, and `status`. This block is a picture of that file. Do not paste it into `health.py`.

```text
{
  "hash": "sha256:21a5beff519caf63",
  "id": "local-smallx",
  "status": "unregistered"
}
```

The id is `local-smallx`. The status is `unregistered`. That is not a registration. The approved `local-small` row is the registration. The extra letter on this id is expected. The probe does not report this hash.

[root.json](packet/release/fixtures/root.json) names the account the shell image still uses. The field is `user`. This block is a picture of that file. Do not paste it into the Dockerfile.

```text
{
  "user": "root"
}
```

[log.json](packet/release/fixtures/log.json) is the deploy log. Open it. The file has one field, `line`. The line carries a national id and then a watermark. Leave the file in the packet. Do not copy it into `work/`. Do not paste it into a prompt. This page does not show a picture of that file.

[zones.md](packet/kickoff/world/zones.md) names the three zones. Search for `zone-private`. The private cloud is site-a and site-b. Search for `zone-public`. `ext-large` sits there. Chapter 09 maps the URL onto `zone-private`.

## Run the deploy demo

Open a terminal in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line.

```text
cd problem_simulation
python -m alwaha.demo.deploy --profile practice
```

You should see exactly these two lines, and nothing else:

```text
root image: rejected
registered image: accepted
```

The first line is a root image. The second line is a registered image on a clean account. The lines do not print a hash, a token, the quota, a national id, or a watermark. You do not write those values down. [Chapter 06](06-the-image.md) is where you label the root rejection in the admission code. [Chapter 09](09-the-pages.md) is where the deployment note says the container user is non-root. [Chapter 10](10-finish.md) is where you name the zone and what a rollback changes.

This page is done when those two lines are on the screen and you have not copied a picture into `work/`.

Next: [04 — Words](04-words.md).
