# Forward Deployed Engineer

A forward deployed engineer embeds with a customer, turns a messy business problem into a working AI system, and leaves it running in production.

Unlike a traditional software developer who builds features in a controlled internal environment, an FDE works inside the customer's systems, data, and constraints. The role needs four things: production engineering, applied AI, customer consulting, and ownership in that environment.

## 1. Production engineering

Enough to read a messy client system and ship a production integration.

### Fluent programming

- Write production code in Python, the default for AI deployment
- Work in a second language when the client stack requires it, typically TypeScript, Go, or Java
- Read an unfamiliar legacy codebase and ship a patch or integration in a day

### API integration

- Consume and build REST, GraphQL, and gRPC endpoints
- Hook company software into the client's existing architecture
- Handle auth, permissions, rate limits, webhooks, and retries

### Data

- Query databases with solid SQL
- Profile messy enterprise data: missing, stale, duplicated, and sensitive records
- Build batch, sync, and event-driven pipelines
- Decide what data the system may use, store, and show

### Infrastructure

- Deploy on the client's cloud: AWS, Azure, or Google Cloud
- Package and run services with Docker and Kubernetes
- Ship through CI/CD
- Add logging, tracing, alerts, retries, and fallbacks
- Manage latency, throughput, and model cost under real load

## 2. Applied AI

Enough to turn a prototype into a system you can measure, trace, and trust.

### LLM systems

- Choose the right pattern: prompt, retrieval, tool use, workflow, agent, or fine-tune
- Implement retrieval-augmented generation and work with vector databases
- Design context, tools, and control flow so the model does a bounded job
- Produce structured model outputs
- Know the limits: hallucination, latency, cost, context window, and nondeterminism

### Orchestration

- Build multi-step workflows and agentic orchestration
- Design the human workflow around the model, including review and override
- Add guardrails for unsafe, private, or out-of-policy outputs

### Evaluation and observability

- Define what "good" means for the customer's task
- Build a small golden set and an error taxonomy
- Track, log, and evaluate the system under real load
- Use evals to decide what to change, and watch quality after launch

## 3. Customer consulting

Enough to turn a vague business pain into a phased build, and explain it to both engineers and executives.

### Problem discovery

- Run structured discovery with operators and executives
- Separate the real job to be done from the requested feature
- Map a vague pain ("logistics tracking is too slow") into a concrete technical roadmap
- Scope an outcome, a success metric, and a first shippable slice

### Communication

- Explain architectural tradeoffs to client engineers
- Translate the same work into business value for executives: time saved, cost cut, risk reduced
- Write a clear problem brief, design, and decision log
- Demo working software and turn feedback into the next change

### Product judgment

- Decide what to configure, what to build, and what to refuse
- Push back on unrealistic requirements and offer a phased alternative
- Sequence an MVP that proves value before a platform

### Domain learning

- Learn the customer's vocabulary, constraints, and incentives in days
- Map how work actually happens, including exceptions
- Reuse the pattern on the next deployment without copying the last solution

## 4. Ownership in the client environment

Enough to get the system approved, deployed, and handed off.

### Delivery

- Own timeline, risks, and unblocking across the customer and your own company
- Take the implementation end to end, from first demo to production
- Run a tight build-demo-fix loop with the people who use the system
- Hand off something operable: docs, runbooks, and a named owner

### Security and governance

- Apply least privilege, secrets handling, and auditability
- Keep customer data inside agreed boundaries
- Navigate the client's security, compliance, and approval process
- Meet the controls the deployment requires, such as access review and data-handling rules

### Operating in ambiguity

- Work with unclear requirements, messy data, and internal politics
- Make progress before the problem is fully specified
- Stay responsible for the outcome when the environment is not yours

## Checklist

| Category | What to assess |
|---|---|
| Production engineering | Python, SQL, REST/GraphQL/gRPC, pipelines, Docker, Kubernetes, AWS/Azure/GCP, CI/CD |
| Applied AI | RAG, vector databases, agents, structured outputs, evals, observability, guardrails |
| Customer consulting | Discovery, tradeoff communication, executive translation, scope negotiation, domain learning |
| Ownership | End-to-end delivery, security and governance, operating in ambiguity |
