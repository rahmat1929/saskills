# Detection Matrices

> You are reading this because you're about to generate edge cases and error
> scenarios. Use the categories as a checklist — walk through each one per
> feature. Skip only with reason.

---

## Table of Contents

1. [How to Use This](#how-to-use-this)
2. [Edge Case Detection (8 Categories)](#edge-case-detection-categories)
3. [Error Scenario Patterns (8 Types)](#error-scenario-patterns)
4. [Domain-Specific Checklists](#domain-specific-checklists)

---

## How to Use This

For each feature, walk through the 8 edge case categories below. Not every
category applies — but you must **consider** each one. If you skip a category,
you should be able to say why (e.g., "Category 5: Integration Failures — N/A,
no external dependencies").

**Depth scales with complexity:**
- **Small features:** Check the 3-4 most relevant categories. Target 2-3 edge cases, 1-2 errors.
- **Medium features:** Check 5-6 categories. Target 4-6 edge cases, 2-3 errors.
- **Large features:** Check all 8 categories. Target 6-10 edge cases, 3-5 errors.

**Format for edge cases:**
```
EC-[NNN]: [Description]
  Scenario: [Specific situation]
  Expected: [What should happen — be concrete, not "handle gracefully"]
  Category: [Which category]
```

**Format for error scenarios:**
```
ERR-[NNN]: [Title]
  Trigger: [What causes this]
  User sees: [Exact message or behavior]
  System does: [Log, retry, fallback, alert]
  Recovery: [How user gets back to working state]
```

---

## Edge Case Detection Categories

### Category 1: Boundary Values

Check the limits of every input, output, and data field.

| Check | Questions |
|-------|----------|
| Empty / null | Required field empty? Optional field null? |
| Min / max length | At 0? At minimum? At maximum? At max + 1? |
| Numeric limits | Zero? Negative? Decimal where integer expected? Very large? |
| List boundaries | Empty list? Single item? Maximum items? |
| Date boundaries | Past dates? Far future? Leap year? Timezone midnight? |
| Special characters | Emoji? Unicode? HTML tags? SQL injection? |
| Whitespace | Only spaces? Leading/trailing spaces? Tabs? Line breaks? |

### Category 2: State Conflicts

What happens when actions collide or state is unexpected.

| Check | Questions |
|-------|----------|
| Concurrent actions | Two users editing same record? Double-click submit? |
| Mid-flow interruption | App backgrounded during submit? Network drops mid-upload? |
| Stale state | Data changed on server since page loaded? |
| Double submission | User taps button twice? Form resubmit while pending? |
| Out-of-order events | Webhook arrives before request completes? |
| Undo after effects | User undoes action but downstream effects already fired? |

### Category 3: Permission Boundaries

Edges of authorization and access control.

| Check | Questions |
|-------|----------|
| Role transitions | Guest converts to logged-in mid-session? |
| Session expiry | Action submitted after session expired? |
| Role escalation | Regular user tries admin action via URL? |
| Data visibility | Can user A see user B's data? |
| Permission revocation | Role downgraded while user is mid-action? |
| Guest vs authenticated | Which features work for guests? What wall do they hit? |

### Category 4: Data Integrity

Data stays consistent and correct.

| Check | Questions |
|-------|----------|
| Duplicates | Same item saved twice? Duplicate registration? |
| Orphaned records | Parent deleted, children remain? |
| Data sync | Local and server out of sync? Offline edits conflict? |
| Character encoding | Emoji in names? RTL text? Mixed scripts? |
| Cascading effects | Delete user — what happens to their content? |
| Migration | Old data meets new validation rules? |

### Category 5: Integration Failures

Every external dependency — APIs, services, third-party.

| Check | Questions |
|-------|----------|
| API timeout | External API too slow — what does user see? |
| Partial response | API returns some data but errors on rest? |
| Rate limiting | Too many API calls — throttled? |
| API format change | Response schema changes? New/removed fields? |
| Auth expiry | OAuth token expired during request? Refresh token revoked? |
| Service downtime | Provider completely unavailable — graceful degradation? |
| Quota exhaustion | Monthly quota reached — what happens? |

### Category 6: Temporal

Time-related assumptions.

| Check | Questions |
|-------|----------|
| Timezone differences | User in UTC+8, server in UTC — dates shift? |
| Daylight saving | Clock springs forward during scheduled action? |
| Session duration | Very long session? Very short? |
| Expiry timing | OTP expires the second user submits? Token mid-request? |
| Historical data | Viewing data from before a schema change? |

### Category 7: Multi-Device / Context

Behavior across devices, screens, environments.

| Check | Questions |
|-------|----------|
| Cross-device | Started on phone, continued on tablet? |
| Cross-platform | iOS vs Android identical? Web vs mobile? |
| Screen sizes | 320px? Foldable? Very large? |
| Orientation | Portrait to landscape mid-action? |
| Accessibility | Screen reader? High contrast? Large text? Reduced motion? |
| Connectivity | 2G? Intermittent? Airplane mode? |
| Low-resource | Low battery? Low storage? Slow CPU? |

### Category 8: Scale / Volume

Behavior at high volume — works for 10 users, breaks for 10,000.

| Check | Questions |
|-------|----------|
| Large datasets | 10,000 history entries? 5,000 content items? |
| Bulk operations | Admin updates 500 records? CSV import 10K rows? |
| Search results | 0 results? 10,000 results? Very slow query? |
| Pagination | Last page? Empty page? Beyond total? |
| Concurrent users | 1,000 users on same endpoint? |

---

## Error Scenario Patterns

Use these templates. Every error MUST have: Trigger, User sees, System does,
Recovery.

### Pattern 1: Validation Errors (User Input)

| Field | Template |
|-------|----------|
| Trigger | User submits invalid data in field [X] |
| User sees | Inline error below field. Other fields preserved. |
| System does | Block submission. Client-side validation. No API call. |
| Recovery | User corrects field and resubmits. |

**Rule:** Never clear the entire form on validation error.

### Pattern 2: Authentication Errors

| Field | Template |
|-------|----------|
| Trigger | API returns 401 Unauthorized |
| User sees | Redirect to login. "Your session has expired." |
| System does | Clear tokens. Preserve intended destination (deep link back). |
| Recovery | User re-authenticates and returns to where they were. |

**Rule:** Never leak which part of credential is wrong. "Invalid email or
password" — not "Password is incorrect."

### Pattern 3: Authorization Errors

| Field | Template |
|-------|----------|
| Trigger | API returns 403 Forbidden |
| User sees | "You don't have permission." No detail about required role. |
| System does | Log attempt (audit trail). Don't expose admin routes. |
| Recovery | User navigates to features they can access. |

**Rule:** 403 on `/admin/users` should look identical to 404.

### Pattern 4: Integration / External API Errors

| Field | Template |
|-------|----------|
| Trigger | External API returns 5xx, times out, or malformed data |
| User sees | Feature-specific message, NOT generic "Something went wrong." |
| System does | Log details. Retry with backoff (max 3). Serve cache. Fall back. |
| Recovery | Auto-retry. Cached content. Manual retry button. |

**Rule:** Integration failure must NEVER take down the whole app. Graceful
degradation.

### Pattern 5: Network Errors

| Field | Template |
|-------|----------|
| Trigger | Device offline or request timeout |
| User sees | Offline indicator. Pending actions show "waiting to sync." |
| System does | Queue locally. Retry on reconnect. Preserve work. |
| Recovery | Connection restores → sync queued actions → notify user. |

**Rule:** NEVER lose user's work due to network error.

### Pattern 6: Rate Limit Errors

| Field | Template |
|-------|----------|
| Trigger | API returns 429 |
| User sees | Nothing (silent) OR "Please wait" if user-initiated |
| System does | Queue. Wait for reset. Retry. |
| Recovery | Automatic after cooldown. |

### Pattern 7: Data Conflict Errors

| Field | Template |
|-------|----------|
| Trigger | Data modified by someone else since user loaded it |
| User sees | "Updated by someone else. [Keep mine / Keep theirs]" |
| System does | Detect via version/timestamp. Do NOT silently overwrite. |
| Recovery | User resolves conflict manually. |

### Pattern 8: System / Server Errors

| Field | Template |
|-------|----------|
| Trigger | API 500 or unhandled exception |
| User sees | "Something unexpected happened. Our team has been notified." |
| System does | Log with stack trace. Alert engineering. Capture context. |
| Recovery | User retries. Persistent → contact support with reference ID. |

**Rule:** Never expose technical details to user.

---

## Domain-Specific Checklists

Check the relevant domain checklist AFTER the 8 categories.

### Mobile Apps

- App backgrounding / foregrounding during critical flows
- Push notification arriving during active session
- Low storage space on device
- Battery saver mode affecting background processes
- App update available mid-session
- Deep link opening when app is in unexpected state
- Force close and reopen — what state is preserved?
- First launch vs subsequent launches

### Wellbeing / Health-Adjacent

- Content safety: features touching emotional data need safety AC
- Non-diagnostic language — never imply medical assessment
- Data sensitivity: mood/emotional data has special retention rules
- Consent: explicit stories for data collection and withdrawal
- Supportive messaging: gentle tone in error states
- Helpline links: must be current, working, and regional

### Multi-Provider Integration

- Provider preference when multiple connected
- Per-provider graceful degradation
- Data normalization across providers (different formats)
- Aggregate rate limit management
- OAuth consent revoked on provider side
- Provider API versioning changes

### Admin / CMS

- Content published without review — approval flow?
- Bulk operations — "select all" and delete?
- Content referenced by users — deactivate vs delete?
- Audit trail — who changed what, when?
- Admin session security — timeout, MFA, concurrent limits
