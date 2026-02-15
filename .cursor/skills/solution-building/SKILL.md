---
name: solution-building
description: Elicit requirements through clarifying questions, then build with TDD. Use when the user says "build", "implement", "create", "add a feature", "I want to", "make me", or describes something they want the system to do.
---

# Solution-Building Workflow

## Trigger

User describes what they want to build. **Do not start coding.**

## Phase 0: Sanity Check

If the request would violate compliance, security, tenant isolation, or harm users—**push back now**. Explain why, propose a better approach. Do not proceed. See expert-advisor.mdc.

## Phase 1: Discovery

Ask clarifying questions. Cover:

1. **Scope** — What exactly is in/out? API? UI? Batch vs single?
2. **Inputs** — Format, source, validation rules
3. **Outputs** — Response shape, side effects, errors
4. **Edge cases** — Empty, invalid, timeout, partial failure
5. **Acceptance** — "How will you know it works?"

### For Infrastructure Work

Also ask (see `infrastructure-design` skill):
- Scalability at 10x/100x?
- Tenant isolation—where is the boundary?
- Audit events—what gets logged?
- Compliance—retention, legal hold implications?

### Example Exchange

User: "I want to add document verification for banking."

Agent: "To scope this correctly:
1. **Input**: Is it a single document upload, or batch? What formats (PDF, image)?
2. **Verification**: What are we verifying—signature, content match, format validity?
3. **Output**: Pass/fail only, or detailed report? Stored where?
4. **Integration**: New endpoint, or extend the existing document API?
5. **Infrastructure**: Multi-tenant? What audit events? Immutable storage?"

## Phase 2: Specification

Summarize in 2–4 acceptance criteria. Get user confirmation.

```
Acceptance criteria:
- [ ] Given X, when Y, then Z
- [ ] ...
```

User confirms → Proceed to Phase 3.

## Phase 3: TDD Implementation

1. **Red**: Write failing test(s) for first acceptance criterion
2. **Green**: Minimal code to pass
3. **Refactor**: Clean up
4. Repeat for each criterion
5. Run full suite: `cd src && pytest`

## Completion

- All acceptance criteria met
- All tests pass
- Report: "Built X. Tests in Y. Acceptance: [list]. All pass."
