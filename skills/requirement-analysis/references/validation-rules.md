# Validation Rules — Cross-Block Conflict Matrix

> Read this file at the start of Phase 3 before generating output. These rules catch
> inconsistencies that would cause project failure or significant rework if not
> addressed.

---

## Table of Contents

1. [Critical Conflicts (Must Resolve)](#critical-conflicts)
2. [Warning Flags (Document, Don't Block)](#warning-flags)
3. [Mandays Estimation Guide](#mandays-estimation-guide)
4. [Confidence Threshold Reference](#confidence-threshold-reference)

---

## Critical Conflicts

These combinations indicate fundamental inconsistencies. Surface them explicitly
and require the user to choose a resolution before generating the final document.
Each conflict includes the exact message to present and the resolution options.

---

### CONF-01: Scale vs Infrastructure Mismatch

**Trigger:** Block 2 concurrent users > 1,000 AND Block 7 specifies shared hosting,
single VPS, or basic plan with no load balancing.

**Message to user:**
> "You've indicated [X] concurrent users, but the infrastructure preference
> ([hosting type]) typically supports 50–200 concurrent users under normal load. This
> creates a serious capacity risk at launch."

**Resolution options:**
A. Scale up infrastructure (load balancer, auto-scaling, managed service)
B. Revise user estimates (are the numbers aspirational or realistic?)
C. Add caching and CDN strategy to reduce server load

---

### CONF-02: Sensitive Data Without Compliance Framework

**Trigger:** Block 6 confirms PII or financial data AND Block 6 has no regulatory
framework mentioned.

**Message to user:**
> "The system handles [PII/financial data], which triggers data protection
> obligations. Proceeding without a compliance framework creates legal exposure for
> both the client and the development vendor. This cannot be left undefined."

**Resolution options:**
A. Define the applicable compliance framework (UU PDP, GDPR, PCI-DSS, HIPAA, OJK)
B. Confirm with client's legal team and add as a GAP with deadline
C. Scope compliance work as a separate workstream with its own budget

---

### CONF-03: Feature Implies Integration Not Declared

**Trigger:** Block 3 includes features that typically require a third-party service,
AND Block 5 does not declare that service.

**Common implied integrations:**

| Feature keyword | Implied integration |
|----------------|-------------------|
| Shopping cart, checkout, billing | Payment gateway |
| Location tracking, maps, delivery | Maps API |
| OTP verification, phone confirmation | SMS gateway |
| Login with Google/Facebook/Apple | OAuth / SSO provider |
| Email notification, password reset | Email service (SMTP/API) |
| Push notification | Push service (Firebase/APNs) |
| File upload, media storage | Cloud storage (S3/GCS) |
| Full-text search | Search engine (Elasticsearch/Algolia) |
| Chat, messaging | Real-time messaging service |

**Message to user:**
> "The feature '[feature]' typically requires [integration type], which wasn't
> mentioned in the integrations block. Is it in scope? If yes, it affects mandays,
> vendor selection, and potentially compliance."

**Resolution options:**
A. Add the integration to Block 5 with vendor selection and effort estimate
B. Confirm the feature will be built without the integration (explain how)
C. Move the feature to post-launch until the integration is scoped

---

### CONF-04: Mandays Floor Exceeded by >30%

**Trigger:** Estimated minimum mandays for declared scope exceeds stated budget by
more than 30%.

**Calculation:** Use the mandays estimation guide at the bottom of this file.

**Message to user:**
> "Based on the features declared, the minimum realistic effort is approximately
> [X] mandays. Your stated budget is [Y] mandays — a gap of [Z]%. Before we
> continue, we need to align on one of three paths."

**Resolution options:**
A. **Cut scope** — which MVP features move to post-launch?
B. **Increase budget** — what is the ceiling you can extend to?
C. **Extend timeline** — what is the latest acceptable go-live date?

The user must choose one. Do not proceed to output without a resolution.

---

### CONF-05: Team Composition vs Architecture Mismatch

**Trigger:** Block 7 specifies microservices, Kubernetes, or event-driven architecture
AND Block 8 has no senior DevOps resource or fewer than 2 senior backend engineers.

**Message to user:**
> "The proposed architecture ([type]) requires strong DevOps and backend seniority to
> implement and maintain safely. With the current team composition, this introduces
> significant delivery risk."

**Resolution options:**
A. Simplify to a well-structured monolith (faster, lower risk for this team)
B. Add a senior DevOps / architect resource
C. Use managed services to reduce ops complexity (managed K8s, serverless)

---

### CONF-06: Real-Time Feature with Incompatible Stack

**Trigger:** Block 3 includes real-time features (live chat, live dashboard, real-time
notifications, live tracking) AND Block 7 specifies REST-only API with no WebSocket
or SSE support.

**Message to user:**
> "Real-time features like [feature] require persistent connection protocols (WebSocket
> or SSE). A REST-only API cannot support true real-time — only polling, which increases
> server load and introduces latency."

**Resolution options:**
A. Add WebSocket or SSE support to the tech stack
B. Accept polling-based "near-real-time" with defined refresh interval
C. Move real-time features to post-launch and build with polling for MVP

---

### CONF-07: Client-Provided Design With No Delivery SLA

**Trigger:** Block 4 states design is client-provided AND no delivery timeline is
defined.

**Message to user:**
> "When design is client-provided, late delivery is the single most common cause of
> development delays. The project plan must include a design delivery deadline with
> a clear escalation path."

**Resolution options:**
A. Define a contractual design delivery date with consequences for late delivery
B. Add a buffer in the timeline for design delays
C. Switch to dev-team-managed design to remove the dependency

---

### CONF-08: Mobile + Web + Admin Panel with Small Team

**Trigger:** Block 7 declares 3+ platform layers (web frontend, mobile iOS, mobile
Android, admin panel) AND Block 8 team size is fewer than 4 developers.

**Message to user:**
> "You've scoped [N] platform layers but have [M] developers. Each platform layer
> requires dedicated effort — this creates a significant capacity risk for the
> timeline."

**Resolution options:**
A. Prioritize platforms — which launches first? (e.g., web MVP, then mobile)
B. Use a cross-platform approach to reduce mobile effort
C. Increase team size or extend timeline

---

### CONF-09: No Authentication on System with Multiple Roles

**Trigger:** Block 2 declares 2+ user roles AND Block 6 does not specify any
authentication or authorization method.

**Message to user:**
> "The system has [N] user roles but no authentication or authorization model is
> defined. Without this, there is no way to control who can access what."

**Resolution options:**
A. Define auth method (username/password, SSO, OAuth2) and authorization model (RBAC)
B. Mark as GAP with Critical priority — blocks development of all role-dependent features

---

## Warning Flags

These don't block document generation but MUST appear in the Risk Register (Section 6)
with severity and recommended action.

| Flag ID | Condition | Risk | Severity |
|---------|-----------|------|----------|
| WARN-01 | No post-launch owner defined | Orphaned system post-go-live | High |
| WARN-02 | No dedicated QA on project with 3+ integrations | High defect rate at launch | High |
| WARN-03 | "Simple" label on feature with 3+ integrations | Scope underestimation | Medium |
| WARN-04 | No contingency buffer in mandays | No room for discovered complexity | High |
| WARN-05 | Fixed deadline + undefined scope | Classic scope creep setup | Critical |
| WARN-06 | No user training for non-technical users | Low adoption, support burden | Medium |
| WARN-07 | No staging environment mentioned | Risky direct-to-production deploys | High |
| WARN-08 | Mobile app with no app store submission plan | Launch delay risk | Medium |
| WARN-09 | Reporting requirements vague or mentioned late | Often 20–30% extra effort | Medium |
| WARN-10 | Multiple vendors with no integration owner | Accountability gap | High |
| WARN-11 | PM shared across projects >50% | Coordination bottleneck | Medium |
| WARN-12 | No rollback plan for data migration | Data loss risk | High |
| WARN-13 | No monitoring/alerting strategy defined | Silent failures post-launch | Medium |
| WARN-14 | Junior-only team on 6+ month project | Knowledge risk, burnout risk | High |
| WARN-15 | No API versioning strategy on public-facing API | Breaking changes for consumers | Medium |
| WARN-16 | No dedicated PM on project with 3+ stakeholders | Coordination failure | High |
| WARN-17 | No BA/SA on project with complex business rules | Missed requirements, scope creep | High |
| WARN-18 | Shared QA across projects on integration-heavy project | Defect leakage | High |

---

## Team Composition Validation

### CONF-10: Missing Critical Role for Declared Scope

**Trigger:** Scope requires a role that doesn't exist on the team.

Use this matrix to determine which roles are critical vs recommended:

| Scope Signal | Required Role | Severity if Missing |
|-------------|--------------|-------------------|
| Mobile app in scope | Mobile Developer | Critical — cannot build without one |
| Web frontend in scope | Frontend Developer | Critical |
| Backend API in scope | Backend Developer | Critical |
| Payment integration OR PII handling | QA Engineer (dedicated) | Critical — too risky without testing |
| 3+ integrations | QA Engineer (dedicated) | High |
| Microservices / K8s / multi-env | DevOps Engineer | Critical |
| Custom design required, no client-provided assets | UI/UX Designer | High |
| 3+ stakeholders or multi-vendor | Project Manager (dedicated) | High |
| Complex business rules, compliance, multi-role auth | System/Business Analyst | High |
| 100+ total mandays | Tech Lead / Architect | High |
| Data migration from legacy | Data Engineer / DBA | High |
| AI/ML features | ML Engineer | Critical — specialized skill |

**Message to user (Critical):**
> "Your scope includes [feature/layer] which requires a [role], but your team
> doesn't have one. This is a hard blocker — you cannot deliver [feature/layer]
> without this role. Options:
> (A) Hire or outsource for this role
> (B) Remove [feature/layer] from MVP scope
> (C) Reassign from existing team (state who and confirm they have the skill)"

**Message to user (High):**
> "Your scope would benefit significantly from a [role], which isn't on your team.
> Without this role, you're accepting risk in [area]. This won't block the project
> but will likely cause [consequence]."

### CONF-11: Team Capacity vs Timeline Mismatch

**Trigger:** Total mandays ÷ available team capacity per sprint > stated timeline.

**Example:** 120 mandays with 3 developers (60 mandays/month capacity) = 2 months
minimum. If the deadline is 1 month, it's impossible.

**Message to user:**
> "With your current team ([N] developers at [X]% availability), the maximum
> throughput is approximately [Y] mandays per month. Your scope requires [Z]
> mandays, which means a minimum of [Z/Y] months. Your deadline is [date].
> This doesn't fit. Options:
> (A) Add developers to increase throughput
> (B) Cut scope to fit the timeline
> (C) Extend the deadline"

---

## Mandays Estimation Guide

Use these as floor estimates (minimum realistic effort), not ceilings. Actual effort
is typically 1.2–1.5× the floor.

### Progressive Estimation Method

Mandays should be estimated **progressively** as information is gathered — not all
at once at Block 8. Use this sequence:

| After Block | What You Can Estimate | Accuracy |
|-------------|---------------------|----------|
| Block 3 (Scope) | Feature development effort only | ±40% (rough) |
| Block 5 (Integrations) | + integration effort | ±30% |
| Block 6 (Security) | + auth system effort | ±25% |
| Block 7 (Technology) | + mobile multiplier, admin panel, DevOps | ±20% |
| Block 8 (Team/Budget) | + QA, PM, design, buffer = **final estimate** | ±15% |

Present estimates at Block 3 (rough) and Block 8 (refined). The user should never
be surprised by the final number.

### Feature Complexity Floors

| Feature Type | Mandays Floor | Example |
|-------------|--------------|---------|
| Simple CRUD module | 3–5 | List, create, edit, delete, detail |
| Medium module with logic | 6–10 | CRUD + business rules, validations, states |
| Complex multi-step flow | 10–15 | Checkout, onboarding, multi-approval |
| XL feature | 15–25 | Real-time dashboard, complex search, AI integration |

### Integration Effort Floors

| Integration Type | Mandays Floor | Includes |
|-----------------|--------------|----------|
| Payment gateway (basic) | 5–7 | One-time payment, webhook handling, basic error states |
| Payment gateway (advanced) | 8–12 | + recurring billing, refunds, split payment, reconciliation |
| SMS gateway | 2–4 | OTP, delivery status |
| Maps API (basic) | 3–5 | Display, geocoding, place search |
| Maps API (tracking/routing) | 6–10 | + real-time tracking, route optimization, geofencing |
| Email service (transactional) | 2–3 | Templates, send via API |
| Email service (advanced) | 4–6 | + tracking, scheduling, bulk, marketing |
| Push notifications | 2–4 | Firebase/APNs setup, topic/token management |
| OAuth/SSO | 3–5 | Google, Facebook, Apple — per provider |
| File storage (S3/CDN) | 2–4 | Upload, serve, basic processing |
| File storage (advanced) | 5–8 | + image processing, video transcoding, virus scan |
| External REST API (per integration) | 3–7 | Depends on API complexity and error handling |
| AI/ML service (pre-built API) | 5–10 | Prompt engineering, error handling, cost management |
| AI/ML (custom model) | 15–40 | Data prep, training, evaluation, serving |
| Real-time (WebSocket) | 5–8 | Connection management, presence, reconnection |
| Search engine (Elasticsearch/Algolia) | 5–10 | Index setup, query building, relevance tuning |

### Platform Multipliers

| Additional Layer | Multiplier |
|-----------------|-----------|
| Mobile — cross-platform (Flutter/RN) | +40–50% of web effort |
| Mobile — native per platform | +60–80% of web effort per platform |
| Admin panel (basic CRUD) | 8–15 mandays |
| Admin panel (advanced with analytics) | 15–25 mandays |
| Background workers / job queue | 3–8 mandays |

### Cross-Cutting Effort (Non-Development)

| Activity | Estimate | Notes |
|----------|----------|-------|
| Auth system (multi-role RBAC) | 5–8 mandays | Increases with role count |
| Auth system (with SSO/MFA) | 8–12 mandays | |
| DevOps / deployment setup | 3–5 mandays | CI/CD, staging, production |
| DevOps (advanced) | 6–10 mandays | K8s, multi-env, auto-scaling, monitoring |
| QA / Testing | 20–25% of dev | Higher for payment/compliance projects |
| Design (UI/UX) | 15–20% of dev | If design is in scope (not client-provided) |
| PM / Coordination | 10–15% of total | Higher for multi-stakeholder, multi-vendor |
| SA / BA support | 5–10% of total | Higher for complex business rules |
| Data migration | 5–15 mandays | Varies wildly by volume and quality |
| Documentation | 3–5 mandays | API docs, user manual, runbook |
| Buffer / contingency | 15–20% of total | **Never skip this** |

### Team Throughput Calculator

```
team_capacity_per_month = sum(developer_count × availability × 20 workdays)

Example:
  2 full-time devs: 2 × 1.0 × 20 = 40 mandays/month
  1 part-time dev:  1 × 0.5 × 20 = 10 mandays/month
  Total: 50 mandays/month

minimum_months = total_mandays ÷ team_capacity_per_month
```

### Quick Formula

```
total_floor = sum(feature_floors) + sum(integration_floors)
            + auth_system (if multi-role)
            + devops_setup
            + mobile_multiplier (if applicable)
            + admin_panel (if applicable)
            + background_workers (if applicable)

total_with_qa = total_floor × 1.22
total_with_design = total_with_qa + (design_mandays if in scope)
total_with_pm = total_with_design × 1.12
total_with_buffer = total_with_pm × 1.15

If total_with_buffer > stated_budget × 1.3 → trigger CONF-04
```

---

## Confidence Threshold Reference

| Block | Minimum Confidence | Priority |
|-------|-------------------|----------|
| Vision & Business Goal | 80% | Critical |
| Users & Usage Patterns | 75% | High |
| Features & Scope | 90% | Critical |
| Design & UX | 70% | High |
| Integrations & Data | 85% | Critical |
| Security & Compliance | 80% | High |
| Technology & Architecture | 75% | High |
| Team, Budget & Timeline | 85% | Critical |
| Launch & Post-Launch | 65% | Medium |

**Confidence formula:**
```
confidence = (answered_questions / applicable_questions) × quality_weight
```

**Quality weights:**
- 1.0 = Specific, measurable, confirmed by user
- 0.7 = General but reasonable
- 0.4 = Vague or assumed
- 0.0 = Unanswered or skipped
