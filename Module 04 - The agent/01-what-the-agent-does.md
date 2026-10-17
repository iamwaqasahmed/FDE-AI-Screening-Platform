# What the agent does

The agent is the only piece that talks to a model. It is not allowed to be the calculator or the librarian.

- A count comes from [screening_tools](../screening_tools).
- A rule comes from [screening_retrieval](../screening_retrieval).
- The reply names the tool, the document, and the result dictionary unchanged.

If the model writes a different eligible count in a sentence, the loop does not keep that sentence. The stored answer is built from the tool result.

A grader still signs any referral, recall, or reassurance. The agent can prepare a letter's fields. It cannot issue the referral.

Next: [The catalog](02-the-catalog.md).
