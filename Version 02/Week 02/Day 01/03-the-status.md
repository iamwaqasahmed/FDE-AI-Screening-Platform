# The status

Copy [app](app) to `Week 02/Day 01/work/app`. Leave the copy in this folder unchanged. Copy [compose.yaml](compose.yaml), [Dockerfile](Dockerfile), and [deploy/namespace.yaml](deploy/namespace.yaml) with it.

The hand-written client still speaks the previous spec. From `work`:

```text
python app\generate.py --spec ..\..\..\data\rel-w2d1\openapi\his-wadi.yaml
```

That writes `work/app/client.py` from the spec. The generator is [app/generate.py](app/generate.py).

Keep the Week 1 status tool. A status question reads `his-wadi`, then answers with that tool. Do not call book.

From `work`, with the pack built:

```text
python app\run.py --pack ..\..\..\data\rel-w2d1 --db sessions.db --out trace.json
python app\server.py --pack ..\..\..\data\rel-w2d1 --db sessions.db
```

Open `/` and sign in. The patient reaches `/chat`. The coordinator reaches `/console`. [compose.yaml](compose.yaml) is the laptop stand-in for the dev namespace. [deploy/namespace.yaml](deploy/namespace.yaml) lists both routes. A live cluster deploy is a later day.

The assistant rule from Day 1 still applies. A coding assistant may see your script. It may not see the scenario file. That file is watermarked. Do not copy it into `work/`.
