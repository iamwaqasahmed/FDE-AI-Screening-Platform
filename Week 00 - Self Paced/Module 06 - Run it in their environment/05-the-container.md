# The container

[Dockerfile](../Dockerfile) is the handover image. It copies:

- `screening_tools`
- `screening_retrieval`
- `screening_agent`
- `screening_service`
- `data/handover`
- `data/corpus`

It does not copy `.env`, `data/truth`, or `data/eval`. The command inside the image is the same `screening_service.run` entry, with the scripted model.

The checker does not need Docker installed. It reads the Dockerfile and fails if a forbidden path is copied. Building the image is optional and uses whatever network the authority already allows. You can finish this module without a Docker install.

**Finish.** You can say what the image copies: the four packages, the handover, and the corpus.

Next: [Check](06-check.md).
