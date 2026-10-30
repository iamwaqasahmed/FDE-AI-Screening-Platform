# 02 — The sprint

Open the finished [sprint.md](work/sprint.md) and put it beside yours.

[data-request.md](sources/release/notices/data-request.md) says the request is approved and the pack is the full history. The cluster job comes first, because one patient is not one row. The relabel comes next, then the synthetic sample, then the scan. Adjudication is booked with the coordinators before the labels are used. [annotate.yaml](sources/release/openapi/annotate.yaml) names that call `adjudicate`.

The Order section is two sentences. The first says the cluster job, then the relabel, then the synthetic sample, then the scan. The word `sample` sits on that sentence. The check looks for cluster, relabel, sample, and scan, in that order. It uses the first time each word appears. It also looks for adjudication. It does not print those words.

The blank sprint has the heading and an empty section. While that blank is the file that runs, the check says `sprint.md does not sequence the cluster job`.

Next: [03 — The clusters](03-the-clusters.md).
