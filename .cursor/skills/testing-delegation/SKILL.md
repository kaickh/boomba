---
name: testing-delegation
description: Ensure delegated tasks include tests and verification. Use when the user delegates a task, asks an agent to implement something, or when completing any coding task that adds or changes behavior.
---

# Testing Delegation

## TDD Order

**Tests before implementation.** Write the failing test first, then the code to pass it.

## When Completing a Task

**Never mark a task done without:**

1. **Tests written first** - Red, then Green, then Refactor
2. **Tests run** - Execute the test suite; all must pass
3. **Verification** - Confirm the solution works (manual or automated)

## Checklist Before "Done"

```
- [ ] New code has corresponding tests
- [ ] Existing tests still pass
- [ ] Edge cases covered (empty, invalid, boundary)
- [ ] Run: npm test / pytest / cargo test (as applicable)
```

## If Tests Don't Exist

Create them. Prefer:
- Same directory as source (`*.test.ts` next to `*.ts`)
- Or dedicated `tests/` / `__tests__/` directory

## Report Back

When finishing: "Implemented X. Added tests in Y. All tests pass."
