# pol-deploy

The probe can confirm this checklist.

| Id | Check |
| --- | --- |
| non-root | The container user is not root. |
| health-probe | Readiness calls /v1/health. |
| resource-limits | The container has cpu and memory limits. |
| no-phi-in-logs | A log line has no national id. |
| image-provenance | The image carries a provenance label. |
| registered-model-hash | The served hash is on the register. |
