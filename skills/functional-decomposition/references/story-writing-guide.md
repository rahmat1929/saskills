# Story Writing Guide

> You are reading this because you're about to decompose features. Use this as a
> lookup during Phase 2. Don't read end-to-end — jump to the section you need.

---

## Table of Contents

1. [Story Format](#story-format)
2. [Strong vs Weak Examples](#strong-vs-weak-examples)
3. [INVEST Criteria](#invest-criteria)
4. [Story Pointing (Fibonacci)](#story-pointing)
5. [Story Splitting Strategies](#story-splitting-strategies)
6. [System Stories](#system-stories)
7. [Anti-Patterns](#anti-patterns)
8. [Acceptance Criteria Format](#acceptance-criteria-format)

---

## Story Format

```
**[FEATURE-ID]-US-[NNN]: [Short descriptive title]**
As a [specific role — never generic "user"],
I want [action — what the user does, not system implementation],
So that [user value — why the user cares, not why the system needs it].

Priority: Must / Should / Could / Won't
Points: [1 / 2 / 3 / 5 / 8 / 13]
Dependencies: [story IDs] or "none"
```

### Writing Strong Clauses

**"As a"** — use specific roles:
- Bad: "As a user" (who? guest? admin? premium?)
- Good: "As a guest user" / "As a logged-in customer" / "As an admin"

**"I want"** — express the action, not implementation:
- Bad: "I want the system to store my data in a database"
- Good: "I want to save my preferences so they're there next time"

**"So that"** — express user value, not system purpose:
- Bad: "So that the system has the data" / "So that the database is updated"
- Good: "So that I can check out faster next time" / "So that I don't lose my progress"

The best "So that" answers: *"What is the user trying to accomplish in their
life, not just in your app?"* (Lenny `problem-definition` framework)

---

## Strong vs Weak Examples

**Weak story:**
```
FT-002-US-001: Login
As a user,
I want to log in,
So that I am logged in.
```

**Strong story:**
```
FT-002-US-001: Login with email and password
As a registered user,
I want to log in with my email and password,
So that I can access my saved history and bookmarks.

Priority: Must | Points: 3 | Dependencies: none
```

**Weak acceptance criteria:**
```
AC-001: User can log in
  Given a user exists,
  When they log in,
  Then they are logged in.
```

**Strong acceptance criteria:**
```
AC-001: Successful login
  Given a registered user with valid credentials,
  When they enter email and password and tap "Log in",
  Then they are redirected to the home screen,
  their session is active, and their name appears in the nav bar.

AC-002: Invalid credentials rejected
  Given a registered user,
  When they enter an incorrect password and tap "Log in",
  Then "Invalid email or password" is shown (not specifying which),
  the password field is cleared, and submit remains enabled.
```

---

## INVEST Criteria

Flag violations only when actionable. Don't flag every story for everything.

| Letter | Meaning | Common Violation | Fix |
|--------|---------|-----------------|-----|
| **I** Independent | Can ship alone | Story B needs Story A in same sprint | Merge or reorder |
| **N** Negotiable | Describes WHAT not HOW | "Use React" / "Store in PostgreSQL" | Remove implementation details |
| **V** Valuable | "So that" has user value | "So that data is normalized" | Reframe from user perspective |
| **E** Estimable | Team can point it | "Integrate with payment provider" (which?) | Add context or create spike first |
| **S** Small | Fits in one sprint | 13 points | Split using strategies below |
| **T** Testable | AC can be verified | "Should feel fast" | Add threshold: "responds in <2s" |

---

## Story Pointing

Fibonacci scale: 1, 2, 3, 5, 8, 13.

| Points | What It Means | Time Signal | Examples |
|--------|--------------|-------------|---------|
| **1** | Trivial. Config change. | < 2 hours | Update label. Toggle flag. Add CSS class. |
| **2** | Very small. One thing changes. | 2-4 hours | Add form field. Update error message. |
| **3** | Small. One component/endpoint. | 4-8 hours | Single page. Basic API endpoint. CRUD op. |
| **5** | Medium. Multiple interactions. | 1-2 days | Form + validation + API + states. |
| **8** | Large. Multi-component. Integration. | 2-3 days | Multi-page feature. Complex 3rd-party integration. |
| **13** | **TOO BIG. MUST SPLIT.** | > 3 days | This is an epic. Apply splitting strategies. |

**Tips:** Compare to known stories (relative sizing). Include non-coding time
(testing, review, docs). Add a point for unknowns.

---

## Story Splitting Strategies

When a story is 8+ points or 13, split using one of these:

### By User Role
Before: "As a user, I want to manage my account"
After: Create account (guest) / Update profile (logged-in) / Change password / Deactivate (admin)

### By Happy Path vs Edge Cases
Before: "As a user, I want to upload a file"
After: Upload valid file (happy) / See error on size limit (edge) / Resume interrupted upload (edge)

### By Read vs Write
Before: "As a user, I want to manage bookmarks"
After: View bookmarks / Add bookmark / Remove bookmark

### By CRUD Operations
Before: "As an admin, I want to manage content"
After: Create / Edit / Deactivate / Search+filter

### By Data Source / Integration
Before: "As a user, I want music recommendations"
After: From curated content (no integration) / From Spotify (integration) / Fallback when Spotify down

### By Platform
Before: "As a user, I want notifications"
After: Push (mobile) / In-app badge (web) / Configure preferences

---

## System Stories

For behaviors initiated by the system, not the user:

```
As the system,
When [trigger condition],
I [action],
So that [purpose].
```

**Use for:** Background jobs (token refresh, data sync), scheduled events
(expiry checks, digests), reactive behaviors (auto-retry, circuit breaker),
security automation (session timeout, brute-force lockout).

**Example:**
```
As the system,
When a user fails login 5 times within 10 minutes,
I lock the account temporarily and send an alert email,
So that brute-force attacks are mitigated.
```

---

## Anti-Patterns

| Anti-Pattern | Example | Fix |
|-------------|---------|-----|
| Epic as story | "I want authentication" | Split into login, register, logout, reset, session |
| Technical task | "As a developer, I want CI/CD" | Move to engineering backlog — no user value |
| No value | "I want a database" | What does the DB enable? "I want my data saved" |
| Implementation | "I want React components" | Describe behavior: "I want to filter by date" |
| Compound | "I want to search AND sort AND filter" | Three separate stories |
| Missing So-that | "I want to upload files" | Add: "So that I can share documents" |

---

## Acceptance Criteria Format

Always **Given/When/Then** (Gherkin):

```
AC-[NNN]: [Short title]
  Given [precondition — starting state],
  When [action — what happens],
  Then [outcome — observable, verifiable].
```

**Rules:**
1. Minimum 2 AC per story (happy path + boundary/negative)
2. Every AC must be binary — pass or fail
3. At least one negative AC per feature ("should NOT allow X")
4. Cover state transitions: loading → success → error
5. Be specific: not "show error" → "show inline error below email field in red"
6. If a business rule exists, there MUST be an AC testing it
