# OCT Cursor Environment

This directory configures how Cursor's AI agents work on the OCT OCR platform.

## Structure

```
.cursor/
├── rules/          # Persistent rules (loaded every conversation)
│   ├── solution-building.mdc    # Elicit → Specify → Build (TDD)
│   ├── expert-advisor.mdc       # Correct, teach, push back when wrong
│   ├── tdd-process.mdc          # Red-Green-Refactor, test-first
│   ├── project-vision.mdc       # Mission, stakeholders
│   ├── platform-architecture.mdc   # Infrastructure, evaluation criteria
│   ├── compliance-infrastructure.mdc # Immutable, multi-tenant, audit
│   ├── coding-standards.mdc     # Clean code, naming, error handling
│   ├── testing.mdc              # Test requirements, pytest
│   ├── paperless-ngx-stack.mdc  # Django, ruff, parser conventions
│   └── aws-infrastructure.mdc   # Cloud patterns (when editing infra)
├── skills/         # Dynamic skills (loaded when relevant)
│   ├── solution-building/    # Elicit → Specify → TDD
│   ├── infrastructure-design/ # Architecture evaluation, design decisions
│   ├── ocr-workflow/         # Document processing pipeline
│   ├── testing-delegation/   # Ensure tasks include tests
│   └── aws-deployment/      # Deploy to AWS
└── README.md       # This file
```

## Rules vs Skills

| | Rules | Skills |
|---|-------|--------|
| **When** | Every conversation | When task matches description |
| **Use for** | Standards, guardrails, vision | Workflows, domain knowledge |
| **Edit** | `.cursor/rules/*.mdc` | `.cursor/skills/*/SKILL.md` |

## Adding a Rule

1. Create `.cursor/rules/your-rule.mdc`
2. Add YAML frontmatter: `description`, `globs` (optional), `alwaysApply` (optional)
3. Keep under 50 lines; one concern per rule

## Adding a Skill

1. Create `.cursor/skills/your-skill/SKILL.md`
2. Add YAML frontmatter: `name`, `description` (include trigger terms)
3. Write clear instructions; link to reference files if needed

## Quick Reference

- **Project vision**: `.cursor/rules/project-vision.mdc`
- **Agent instructions**: `AGENTS.md` (project root)
