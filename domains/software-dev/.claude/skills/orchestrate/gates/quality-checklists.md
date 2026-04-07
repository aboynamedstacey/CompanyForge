# Quality Checklists — Software Development

The Reviewer receives the relevant checklist(s) in its dispatch prompt.
At Small tier, one dispatch gets all three. At Medium+, three parallel
dispatches each get one.

---

## Code Quality

- [ ] Single responsibility — each module/function does one thing
- [ ] Error handling at system boundaries only — no defensive coding internally
- [ ] No magic values — constants named and documented
- [ ] Edge cases — null, empty, overflow, concurrent access
- [ ] No dead code — unused functions, unreachable branches, commented-out code
- [ ] API contracts honored — signatures match design doc
- [ ] No unnecessary abstraction — used once = not a framework
- [ ] Self-documenting names — reader understands without comments
- [ ] Minimal dependencies — no unnecessary imports
- [ ] Test quality — tests verify behavior not implementation, edge cases included

**Adversarial prompt (include in every quality dispatch):**
> "You are evaluated on issues you MISS. Find at least {N} problems.
> For each: file:line, what's wrong, why it matters, fix.
> If genuinely excellent, explain WHY each item passes — don't just approve."
> N = 2 Small, 3 Medium, 5 Large.

---

## Security (OWASP Top 10 + known AI blind spots)

- [ ] A01 Broken Access Control
- [ ] A02 Cryptographic Failures — no hardcoded secrets
- [ ] A03 Injection — parameterized queries, no string concatenation for commands
- [ ] A04 Insecure Design — no trust assumptions about client input
- [ ] A05 Security Misconfiguration — no default credentials, no leaked internals
- [ ] A06 Vulnerable Components — dependencies audited
- [ ] A07 Authentication Failures — rate limiting, session management
- [ ] A08 Data Integrity Failures — validated deserialization
- [ ] A09 Logging Failures — security events logged, no sensitive data in logs
- [ ] A10 SSRF — URL validation
- [ ] **Race conditions** (AI blind spot — check explicitly)
- [ ] **Timing attacks** (AI blind spot — check explicitly)

**Adversarial prompt:**
> "Assume at least one critical vulnerability. Find it. Check every OWASP item
> explicitly — PASS with evidence or FAIL with exploit scenario. Pay special
> attention to race conditions and timing attacks."

---

## Functional Verification

- [ ] Each acceptance criterion verified — test exists, passes, matches spec
- [ ] Regression suite passes
- [ ] Edge cases — boundaries, empty, invalid, concurrent
- [ ] Error paths — network failure, invalid data, timeout
- [ ] Coverage threshold met (if configured)

**Adversarial prompt:**
> "Find scenarios where code doesn't match spec. Don't trust test names —
> read test logic. Find at least {N} uncovered scenarios."
> N = 1 Small, 2 Medium, 3 Large.

---

## Combined (Small tier — one dispatch, all three)

> "Review for quality, security, and correctness. Find at least 3 issues
> total across all three areas. PASS with evidence or FAIL with file:line."
> [Include all three checklists]

---

## Known AI Limitations (include in ALL review dispatches)

- "Claude over-engineers; flag unnecessary abstraction"
- "Claude misses concurrency; check race conditions explicitly"
- "Claude favors familiar patterns; verify it's the RIGHT pattern"
- "Claude tends toward agreement; your job is to find problems"
