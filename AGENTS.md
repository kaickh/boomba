# OCT - Agent Instructions

This file provides context for AI agents working on the OCT OCR platform.

## Project

**OCT** is the foundational digital document infrastructure layer for West Africa's financial and institutional systems. The goal: build something so powerful that non-users are left behind.

**Foundation**: [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) is ingestion and OCR baseline only. We transform it into a multi-tenant, compliance-grade, API-first, bank-ready infrastructure platform.

**Mindset**: Build infrastructure, not a feature tool. Platform evolution, not feature additions.

## Architecture Evaluation

When proposing design or features, evaluate against:
1. Scalability at 10x and 100x growth
2. Compliance defensibility
3. Tenant isolation guarantees
4. Long-term ecosystem integration (SSO, SCIM, retention, fraud, analytics)
5. Regional competitive advantage

See `.cursor/rules/platform-architecture.mdc` and `.cursor/rules/compliance-infrastructure.mdc`.

## Primary Workflow: Solution Building

When the user describes what they want to build:

1. **Elicit** — Ask clarifying questions until you know exactly what to build. Do not code until the user confirms.
2. **Specify** — Summarize acceptance criteria. Get explicit "yes, build that."
3. **Build (TDD)** — Red (failing test) → Green (minimal code) → Refactor. No implementation before tests.

See `.cursor/rules/solution-building.mdc` and `.cursor/skills/solution-building/`.

## How to Work

1. **Correct before executing** - If the request is wrong, harmful, or suboptimal, push back. Explain why, propose the right approach, teach. Do not blindly implement. See `.cursor/rules/expert-advisor.mdc`.
2. **Execute when sound** - When the request aligns with standards and helps real people, do it. Implement, don't just suggest.
3. **Test first (TDD)** - Write failing test, then code. Run `pytest` in `src/` before marking done.
4. **Clean code** - Write code that would impress a senior engineer. No shortcuts.
5. **Production mindset** - AWS best practices, security, scalability, observability.

## Stack (Paperless-ngx + OCT extensions)

| Layer | Technology |
|-------|------------|
| Backend | Django 5.x, Python 3.10+ |
| Frontend | Angular (src-ui/) |
| OCR | Tesseract (paperless_tesseract), OCRmyPDF, Tika, Azure Document Intelligence |
| Tasks | Celery + Redis |
| Deployment | Docker, docker-compose |
| Tests | pytest (src/) |

## Key Directories

- `src/` - Django backend, document parsers, OCR logic
- `src/oct/` - OCT platform extensions (multi-tenant, compliance, infrastructure)
- `src-ui/` - Angular frontend
- `src/paperless_tesseract/` - Tesseract OCR parser (ingestion baseline)
- `src/documents/` - Document models, views, API
- `docker/` - Docker compose configs
- `.cursor/rules/` - Project rules (always read these)
- `.cursor/skills/` - Specialized skills (OCR, AWS, infrastructure-design, testing)

## Commands

```bash
# Run tests
cd src && pytest

# Format Python (ruff)
ruff format . && ruff check .
```

## When Stuck

- Check `.cursor/rules/` for standards
- Use skills in `.cursor/skills/` for domain-specific workflows
- See [Paperless-ngx docs](https://docs.paperless-ngx.com) for architecture
