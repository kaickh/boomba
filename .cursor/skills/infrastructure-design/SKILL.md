---
name: infrastructure-design
description: Evaluate and propose architecture for platform infrastructure. Use when designing systems, proposing architecture, making design decisions, or when the user asks about scalability, multi-tenancy, compliance, audit, or infrastructure patterns.
---

# Infrastructure Design

## Before Proposing

Run every proposal through these five criteria:

1. **Scalability** — Does it work at 10x and 100x growth?
2. **Compliance defensibility** — Can we defend it in a regulatory review?
3. **Tenant isolation** — Are isolation guarantees preserved?
4. **Ecosystem integration** — Does it support future SSO, SCIM, retention, analytics?
5. **Regional advantage** — Does it strengthen our position in West African markets?

## Anti-Patterns

- **Tight coupling to Paperless** — Prefer adapters, facades, event-driven integration
- **Blocking workflows** — Use queues; async by default
- **Silent overwrites** — Immutable; version explicitly; audit every mutation
- **Monolithic changes** — Prefer service separation, extensibility

## Discovery Questions (Architecture)

When designing infrastructure:

- "How does this behave at 10x document volume?"
- "Where is the tenant boundary? How is it enforced?"
- "What audit events does this produce?"
- "Can we add retention/legal hold without redesign?"
- "What happens in low-bandwidth or offline?"

## Output

Proposals should include: scalability impact, tenant isolation approach, audit implications, and extensibility for future requirements.
