# Mandays Reference — Complexity & Effort Estimation Guide

> **Purpose:** This file defines the standard complexity tiers, mandays ranges, and
> role allocation patterns used for effort estimation. It works alongside
> `manpower.md` (role catalog & rates) to produce team composition and cost estimates.
>
> **When to read:** Phase 2 Block 3 (initial estimate), Block 5–7 (refinement),
> Block 8 (final estimate), and Phase 4 Section 9 (Mandays Estimation Matrix).
>
> **Relationship to manpower.md:** This file defines HOW MUCH effort. Manpower.md
> defines WHO does the work and at WHAT COST. Together they produce the full
> estimation matrix.

---

## Table of Contents

1. [How This File Is Used](#how-this-file-is-used)
2. [Complexity Tiers](#complexity-tiers)
3. [Feature Complexity Matrix](#feature-complexity-matrix)
4. [Role Allocation by Complexity](#role-allocation-by-complexity)
5. [Integration Effort Reference](#integration-effort-reference)
6. [Cross-Cutting Effort (Non-Feature)](#cross-cutting-effort)
7. [Platform Multipliers](#platform-multipliers)
8. [Project-Level Complexity Classification](#project-level-complexity-classification)
9. [Progressive Estimation Workflow](#progressive-estimation-workflow)
10. [Cost Projection Formula](#cost-projection-formula)
11. [Custom Reference Workflow](#custom-reference-workflow)
12. [Template for Custom Mandays Reference](#template-for-custom-mandays-reference)

---

## How This File Is Used

1. **After Block 3 (Scope):** Classify each feature by complexity tier → produce a
   rough mandays estimate (±40%) using the Feature Complexity Matrix.

2. **After Blocks 5–7:** Refine by adding integration effort, platform multipliers,
   and cross-cutting costs → estimate improves to ±20%.

3. **At Block 8:** Add QA, PM, SA, Design, DevOps, and buffer → final estimate (±15%).
   Cross-reference with `manpower.md` to determine which roles at which seniority.

4. **Phase 4 output:** Use these tables to populate Section 9 (Mandays Estimation
   Matrix) in the output document.

---

## Complexity Tiers

Four tiers classify individual features by effort. Each tier implies a mandays
range, minimum role set, and expected depth of testing.

| Tier | Label | Mandays Range | Description | Example |
|------|-------|:------------:|-------------|---------|
| T1 | **Low** | 0–3 | Single-purpose feature, no integrations, minimal business rules. One role can complete it. | Static page, simple toggle, basic list view, single form submission |
| T2 | **Medium** | 4–7 | Multi-step feature with moderate business rules or one integration. Requires 1–2 roles. | CRUD module with validation, filtered search, profile management with image upload |
| T3 | **High** | 8–14 | Complex feature with multiple business rules, 1–2 integrations, or multi-role access. Requires 2–3 roles. | Multi-step checkout, approval workflow, role-based dashboard, data import/export |
| T4 | **Complex** | 15+ | Feature with significant technical complexity — real-time, AI/ML, complex algorithms, 3+ integrations, or cross-platform sync. Requires 3+ roles including senior. | Real-time collaboration, recommendation engine, payment + reconciliation, complex reporting with drill-down |

### Tier Assignment Rules

When classifying a feature, check these signals:

| Signal | Complexity Impact |
|--------|------------------|
| Single CRUD operation | T1 (Low) |
| CRUD + business rules / validation | T2 (Medium) |
| Multi-step flow / state machine | T3 (High) |
| Real-time / AI / complex algorithm | T4 (Complex) |
| Each additional integration | +1 tier (e.g., T1→T2, T2→T3) |
| Multi-role access with different views | +1 tier |
| Data migration component | +1 tier |
| Compliance/audit requirements on feature | +1 tier |

**Cap:** Maximum T4. If signals push beyond T4, the feature should be split.

---

## Feature Complexity Matrix

Detailed breakdown of common feature types and their typical effort. Use this as a
lookup when estimating individual features.

### T1 — Low Complexity (0–3 mandays)

| Feature Type | Mandays | Roles Involved | Notes |
|-------------|:-------:|---------------|-------|
| Static/informational page | 0.5–1 | FE | Content only, no backend |
| Simple toggle/setting | 0.5–1 | FE, BE | One API endpoint, one UI control |
| Basic list view (no filter) | 1–2 | FE, BE | Paginated list, single data source |
| Single form submission | 1–2 | FE, BE | Validation, submit, success/error |
| Like/favorite button | 0.5–1 | FE, BE | Optimistic UI, simple backend toggle |
| Basic notification display | 1–2 | FE, BE | Read list from API, mark as read |
| Simple file download | 0.5–1 | FE, BE | Generate link, serve file |

### T2 — Medium Complexity (4–7 mandays)

| Feature Type | Mandays | Roles Involved | Notes |
|-------------|:-------:|---------------|-------|
| CRUD module with business rules | 4–6 | FE, BE, QA | List + create + edit + delete + validation |
| Filtered search with sorting | 3–5 | FE, BE | Multiple filter types, debounce, pagination |
| Profile management (with image) | 4–5 | FE, BE | Upload, crop, validation, storage |
| Basic reporting page | 4–6 | FE, BE, DDA | Charts, date range filter, export to CSV |
| Email notification system | 3–5 | BE, DO | Templates, queue, delivery tracking |
| Content management (basic) | 4–7 | FE, BE | Rich text editor, image upload, publish/draft |
| User invitation flow | 3–5 | FE, BE | Email invite, role assignment, expiry |

### T3 — High Complexity (8–14 mandays)

| Feature Type | Mandays | Roles Involved | Notes |
|-------------|:-------:|---------------|-------|
| Multi-step checkout flow | 10–14 | FE, BE, QA, UIUX | Cart → address → payment → confirmation |
| Approval workflow (multi-level) | 8–12 | FE, BE, SA, QA | State machine, notifications, escalation |
| Role-based dashboard | 8–12 | FE, BE, DDA, UIUX | Different data per role, widgets, filters |
| Data import with validation | 8–10 | FE, BE, QA | File parsing, row-level errors, preview, commit |
| Advanced search (full-text) | 8–10 | FE, BE, DO | Elasticsearch/Algolia, relevance, facets |
| Scheduling/calendar system | 8–12 | FE, BE, UIUX | Time slots, conflicts, timezone, recurring |
| Multi-step onboarding | 8–10 | FE, BE, UIUX | Progress tracking, conditional steps, resume |

### T4 — Complex (15+ mandays)

| Feature Type | Mandays | Roles Involved | Notes |
|-------------|:-------:|---------------|-------|
| Real-time dashboard | 15–20 | FE, BE, DO, DDA | WebSocket, live data, alerts, drill-down |
| Payment + reconciliation | 15–25 | BE, FE, QA, SA | Gateway, webhook, retry, refund, reporting |
| Recommendation engine | 15–30 | BE, DDA, QA | Algorithm, training data, A/B testing |
| Complex reporting with drill-down | 15–20 | FE, BE, DDA, UIUX | Multi-level, export, scheduling, permissions |
| AI/ML feature (pre-built API) | 15–20 | BE, FE, DDA | Prompt engineering, cost management, fallbacks |
| AI/ML feature (custom model) | 25–40 | BE, DDA, DO, QA | Data prep, training, evaluation, serving |
| Multi-provider integration hub | 15–25 | BE, SA, QA, DO | Multiple external APIs, failover, monitoring |
| Real-time collaboration | 20–30 | FE, BE, DO | CRDT/OT, conflict resolution, presence |

---

## Role Allocation by Complexity

This table shows which roles from `manpower.md` are typically needed at each
complexity tier. Use it when recommending team composition at Block 8.

### Minimum Role Set per Tier

| Role | T1 (Low) | T2 (Medium) | T3 (High) | T4 (Complex) |
|------|:--------:|:-----------:|:---------:|:------------:|
| PM | — | Part-time | Part-time | Dedicated |
| SA | — | — | Part-time | Dedicated |
| DDA | — | If reporting | If dashboard | Dedicated |
| QA | — | Part-time | Dedicated | Dedicated |
| FE | Part-time | Dedicated | Dedicated | Dedicated |
| BE | Part-time | Dedicated | Dedicated | Dedicated (Senior) |
| MOB | — | If mobile in scope | If mobile in scope | Dedicated |
| UIUX | — | If custom design | Part-time | Dedicated |
| GD | — | — | If visual assets | If brand/illustration |
| MGD | — | — | — | If animation required |
| DO | — | — | Part-time | Dedicated |

### Recommended Seniority per Tier

| Tier | Minimum Seniority | Recommended Seniority |
|------|-------------------|----------------------|
| T1 (Low) | Junior | Junior–Middle |
| T2 (Medium) | Junior–Middle | Middle |
| T3 (High) | Middle | Middle–Senior |
| T4 (Complex) | Middle–Senior | Senior |

**Rule:** If the project has ANY T4 feature, the team should include at least one
Senior in the primary development roles (BE, FE, and/or MOB). If the project has 3+ T3
features, treat team composition as if it were T4-level.

---

## Integration Effort Reference

Each third-party integration adds effort independently of feature complexity.
Cross-reference with `validation-rules.md` → Integration Effort Floors.

| Integration Type | Mandays | Roles | Notes |
|-----------------|:-------:|-------|-------|
| Payment gateway (basic: one-time) | 5–7 | BE, QA | Webhook, error states |
| Payment gateway (advanced: recurring, refund) | 8–12 | BE, QA, SA | Reconciliation, split payment |
| SMS gateway (OTP) | 2–4 | BE, QA | Delivery status, retry |
| Maps API (display, geocode) | 3–5 | FE, BE | Place search, markers |
| Maps API (tracking, routing) | 6–10 | FE, MOB, BE, DO | Real-time, geofencing |
| Email service (transactional) | 2–3 | BE | Templates, API send |
| Email service (marketing, bulk) | 4–6 | BE, DDA | Tracking, scheduling |
| Push notifications (Firebase/APNs) | 2–4 | BE, MOB | Topic/token management |
| OAuth/SSO (per provider) | 3–5 | BE, FE | Google, Facebook, Apple |
| File storage (S3/CDN, basic) | 2–4 | BE, DO | Upload, serve |
| File storage (advanced: processing) | 5–8 | BE, DO | Image resize, video transcode, virus scan |
| External REST API (per service) | 3–7 | BE, QA | Error handling, rate limiting |
| AI/ML service (pre-built API) | 5–10 | BE, DDA | Prompt engineering, cost mgmt |
| AI/ML (custom model) | 15–40 | BE, DDA, DO | Data prep, training, serving |
| Real-time (WebSocket/SSE) | 5–8 | BE, FE, DO | Connection mgmt, reconnection |
| Search engine (Elasticsearch/Algolia) | 5–10 | BE, FE, DO | Index setup, relevance tuning |

---

## Cross-Cutting Effort

These costs apply at the PROJECT level, not per feature. Add them on top of
feature + integration totals.

| Activity | Formula | Roles | Notes |
|----------|---------|-------|-------|
| Auth system (basic: username/password) | 3–5 mandays | BE, FE | Login, register, forgot password |
| Auth system (multi-role RBAC) | 5–8 mandays | BE, FE, SA | Increases with role count |
| Auth system (with SSO/MFA) | 8–12 mandays | BE, FE, SA, QA | Token management, recovery flows |
| DevOps setup (basic CI/CD) | 3–5 mandays | DO | Pipeline, staging, production |
| DevOps setup (advanced) | 6–10 mandays | DO | K8s, multi-env, auto-scaling, monitoring |
| QA / Testing | 20–25% of dev total | QA | Higher for payment/compliance |
| Design (UI/UX) | 15–20% of dev total | UIUX | If design is in scope (not client-provided) |
| PM / Coordination | 10–15% of total | PM | Higher for multi-stakeholder/vendor |
| SA / BA support | 5–10% of total | SA | Higher for complex business rules |
| Data migration | 5–15 mandays | BE, DDA, QA | Varies by volume and data quality |
| Documentation | 3–5 mandays | SA, BE | API docs, user manual, runbook |
| Buffer / contingency | 15–20% of total | — | **Never skip this** |

---

## Platform Multipliers

Additional platform layers multiply the base effort:

| Platform Layer | Multiplier | Roles Added |
|---------------|:----------:|-------------|
| Mobile — cross-platform (Flutter/RN) | +40–50% of web effort | MOB, QA |
| Mobile — native iOS | +60–80% of web effort | MOB (iOS), QA |
| Mobile — native Android | +60–80% of web effort | MOB (Android), QA |
| Admin panel (basic CRUD) | 8–15 mandays flat | FE, BE |
| Admin panel (advanced with analytics) | 15–25 mandays flat | FE, BE, DDA, UIUX |
| Background workers / job queue | 3–8 mandays | BE, DO |

---

## Project-Level Complexity Classification

Classify the OVERALL project to set expectations for team size and duration:

| Project Complexity | Total Mandays | Typical Team Size | Typical Duration | Characteristics |
|-------------------|:------------:|:-----------------:|:----------------:|----------------|
| **Simple** | 0–30 | 1–2 developers | 2–4 weeks | Few features (T1–T2), no integrations, single platform |
| **Standard** | 31–80 | 2–4 developers + QA | 1–3 months | Mix of T1–T3 features, 1–3 integrations, 1–2 platforms |
| **Complex** | 81–150 | 4–6 developers + QA + DO | 3–6 months | T3–T4 features, 3+ integrations, multi-platform |
| **Enterprise** | 150+ | 6+ developers + full support | 6+ months | Multiple T4 features, complex integrations, compliance |

### Minimum Team Composition by Project Complexity

| Role | Simple | Standard | Complex | Enterprise |
|------|:------:|:--------:|:-------:|:----------:|
| PM | — | Part-time | Dedicated | Dedicated (Senior) |
| SA | — | — | Part-time | Dedicated |
| DDA | — | — | If reporting | Part-time–Dedicated |
| QA | Dev handles | Part-time | Dedicated | Dedicated (+ automation) |
| FE | 1 Jr–Mid | 1 Mid | 1–2 Mid–Sr | 2+ Sr |
| BE | 1 Jr–Mid | 1 Mid | 1–2 Mid–Sr | 2+ Sr |
| MOB | — | If mobile in scope | 1 Mid–Sr | 1–2 Sr (per platform) |
| UIUX | — | If custom design | Part-time | Dedicated |
| GD | — | — | If visual assets | Part-time |
| MGD | — | — | — | If required |
| DO | Dev handles | Part-time | Dedicated | Dedicated (Senior) |

---

## Progressive Estimation Workflow

Estimates are built progressively — never all at once. This is the exact sequence:

### After Block 3 (Scope) — Rough Estimate (±40%)

```
step_1 = sum of (each feature's mandays floor based on complexity tier)
```

Present to the user:
> "Based on the features you've described, a rough floor estimate is **[N] mandays**
> for development alone. This doesn't yet include integrations, auth, mobile, QA,
> or PM effort — those come as we discuss them. But if your budget is [M], we should
> check alignment now."

If `step_1 > budget × 0.7` → trigger early scope negotiation.

### After Block 5 (Integrations) — Add Integration Effort (±30%)

```
step_2 = step_1 + sum of (each integration's mandays)
```

### After Block 6 (Security) — Add Auth Effort (±25%)

```
step_3 = step_2 + auth_system_effort
```

### After Block 7 (Technology) — Add Platform & DevOps (±20%)

```
step_4 = step_3
        + mobile_multiplier (if applicable)
        + admin_panel (if applicable)
        + background_workers (if applicable)
        + devops_setup
```

### At Block 8 (Team/Budget) — Final Estimate (±15%)

```
dev_subtotal = step_4
qa_effort    = dev_subtotal × 0.22
design_effort = dev_subtotal × 0.17 (if design in scope, else 0)
pm_effort    = (dev_subtotal + qa_effort + design_effort) × 0.12
sa_effort    = (dev_subtotal) × 0.07 (if complex business rules)
documentation = 4 mandays (default)
buffer       = (all above) × 0.17

GRAND_TOTAL  = dev_subtotal + qa_effort + design_effort + pm_effort
             + sa_effort + documentation + buffer
```

### Reality Check at Block 8

```
If GRAND_TOTAL > stated_budget × 1.3 → trigger CONF-04
If GRAND_TOTAL ÷ team_capacity_per_month > stated_timeline → trigger CONF-11
```

---

## Cost Projection Formula

To convert mandays to IDR cost, cross-reference with `manpower.md`:

```
cost_per_role = mandays_for_role × 8 hours × hourly_rate_for_role

total_cost = sum of (cost_per_role for each role on the project)
```

### Example

For a Standard project (60 mandays total):

| Role | Mandays | Seniority | Rate (IDR/hr) | Cost (IDR) |
|------|:-------:|-----------|:-------------:|:----------:|
| BE | 20 | Middle | 150,000 | 24,000,000 |
| FE | 15 | Middle | 150,000 | 18,000,000 |
| QA | 8 | Junior | 75,000 | 4,800,000 |
| UIUX | 5 | Middle | 150,000 | 6,000,000 |
| PM | 5 | Middle | 175,000 | 7,000,000 |
| DO | 3 | Middle | 175,000 | 4,200,000 |
| Buffer | 4 | — (blended) | 150,000 | 4,800,000 |
| **Total** | **60** | | | **68,800,000** |

---

## Custom Reference Workflow

**This workflow runs at the START of Block 8, alongside the manpower check.**

### Step 1: Check for Custom Mandays Reference

Ask the user:

> "I also want to check — **does your team use a standard estimation reference
> or effort matrix?** For example, your own complexity-to-mandays mapping, or a
> historical reference from past projects.
>
> If yes, share it and I'll calibrate my estimates to match your benchmarks.
> If no, I'll use the standard estimation guide."

### Step 2: Process the Response

**If user provides a custom reference:**
1. Read and extract: complexity tiers, mandays ranges, role allocations
2. Map to the standard tiers (T1–T4) where possible
3. Present a comparison: "Your reference vs standard. Key differences: [list]"
4. Use their reference for all subsequent estimation
5. Note in the document: `**Estimation Source:** Custom — provided by {user}`

**If user does not have a custom reference:**
1. Briefly explain the tier system: "I use 4 complexity tiers: Low (0–3 days),
   Medium (4–7), High (8–14), and Complex (15+). Does this framework make sense
   for your context?"
2. Proceed with defaults

---

## Template for Custom Mandays Reference

> Share this template when the user wants to provide their own estimation
> benchmarks but doesn't have a structured format.

```markdown
# [Company Name] — Estimation Reference

**Effective date:** [date]
**Based on:** [historical projects / industry benchmark / internal standard]

## Complexity Tiers

| Tier | Label | Mandays Range | Description |
|------|-------|:------------:|-------------|
| 1 | [name] | [range] | [description] |
| 2 | [name] | [range] | [description] |
| 3 | [name] | [range] | [description] |
| 4 | [name] | [range] | [description] |

## Feature Benchmarks (from past projects)

| Feature Type | Typical Mandays | Notes |
|-------------|:--------------:|-------|
| [feature type] | [mandays] | [context] |
| [feature type] | [mandays] | [context] |

## Integration Benchmarks

| Integration | Typical Mandays | Notes |
|------------|:--------------:|-------|
| [integration] | [mandays] | [context] |

## Overhead Percentages

| Activity | Percentage of Dev | Notes |
|----------|:-----------------:|-------|
| QA / Testing | [%] | |
| PM / Coordination | [%] | |
| Buffer | [%] | |

## Notes
- [Any calibration notes, e.g., "our teams tend to run 1.3× the standard"]
```
