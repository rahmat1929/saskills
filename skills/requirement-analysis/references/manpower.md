# Manpower Reference — Role Catalog & Rate Card

> **Purpose:** This file defines the standard roles, seniority levels, and hourly
> rates used for team composition recommendations and cost estimation. It serves as
> the DEFAULT reference — users can provide their own rate card following this template.
>
> **When to read:** Phase 2 Block 8 (Team, Budget & Timeline) and Phase 4 Section 9
> (Mandays Estimation Matrix).
>
> **Currency:** All rates in IDR (Indonesian Rupiah) per hour.

---

## Table of Contents

1. [How This File Is Used](#how-this-file-is-used)
2. [Role Catalog](#role-catalog)
3. [Rate Card — Default](#rate-card--default)
4. [Role Descriptions & Scope Triggers](#role-descriptions--scope-triggers)
5. [Seniority Definitions](#seniority-definitions)
6. [Custom Reference Workflow](#custom-reference-workflow)
7. [Template for Custom Rate Card](#template-for-custom-rate-card)

---

## How This File Is Used

1. **During Block 8 interview:** After determining what team the project NEEDS
   (based on Blocks 1–7), use this file to recommend specific roles and seniority
   levels. Cross-reference with the user's actual team to surface gaps.

2. **During mandays estimation:** Use hourly rates to convert mandays into cost
   estimates when the user requests budget projection in IDR.

3. **Custom override:** Before using defaults, ask the user if they have their own
   manpower reference. If yes, they upload it following the template at the bottom
   of this file. Their rates replace the defaults for that session.

---

## Role Catalog

These are the standard roles recognized by this skill. Each role has three seniority
levels: Junior, Middle, and Senior.

| Code | Role | Department |
|------|------|-----------|
| PM | Project Manager | Management |
| SA | System Analyst | Analysis |
| DDA | Data & Digital Analyst | Analysis |
| QA | Quality Assurance Engineer | Quality |
| FE | Frontend Developer | Engineering |
| BE | Backend Developer | Engineering |
| MOB | Mobile Developer | Engineering |
| UIUX | UI/UX Designer | Design |
| GD | Graphic Designer | Design |
| MGD | Motion Graphic Designer | Design |
| DO | DevOps Engineer | Infrastructure |

---

## Rate Card — Default

> **⚠️ These are default rates.** Always ask the user if they have their own rate
> card before applying these. See [Custom Reference Workflow](#custom-reference-workflow).

| Code | Role | Junior (IDR/hr) | Middle (IDR/hr) | Senior (IDR/hr) |
|------|------|---------------:|----------------:|----------------:|
| PM | Project Manager | 100,000 | 175,000 | 300,000 |
| SA | System Analyst | 100,000 | 175,000 | 300,000 |
| DDA | Data & Digital Analyst | 85,000 | 150,000 | 250,000 |
| QA | Quality Assurance Engineer | 75,000 | 125,000 | 225,000 |
| FE | Frontend Developer | 85,000 | 150,000 | 275,000 |
| BE | Backend Developer | 85,000 | 150,000 | 275,000 |
| MOB | Mobile Developer | 85,000 | 160,000 | 300,000 |
| UIUX | UI/UX Designer | 85,000 | 150,000 | 250,000 |
| GD | Graphic Designer | 75,000 | 125,000 | 200,000 |
| MGD | Motion Graphic Designer | 85,000 | 150,000 | 225,000 |
| DO | DevOps Engineer | 100,000 | 175,000 | 300,000 |

**Daily rate conversion:** hourly rate × 8 hours = daily rate.
**Monthly rate conversion:** daily rate × 20 workdays = monthly rate.

### Blended Rate Quick Reference

For rough cost estimation when exact role breakdown is not yet available:

| Team Composition | Blended Rate (IDR/hr) | Typical Use |
|-----------------|---------------------:|-------------|
| Junior-heavy (70% Jr, 30% Mid) | ~100,000 | Small, low-risk projects |
| Balanced (30% Jr, 50% Mid, 20% Sr) | ~150,000 | Standard projects |
| Senior-heavy (20% Mid, 80% Sr) | ~265,000 | Complex, high-risk projects |

---

## Role Descriptions & Scope Triggers

Each role below includes the **scope signals** that trigger a recommendation for
that role during Block 8.

### PM — Project Manager

**What they do:** Coordinates stakeholders, manages timeline, removes blockers,
runs sprint ceremonies, handles client communication.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Internal project, single stakeholder, <30 mandays |
| Middle | 2–3 stakeholders, 30–80 mandays, single vendor |
| Senior | 3+ stakeholders, multi-vendor, 80+ mandays, fixed deadline |

**Scope triggers for requiring PM:**
- 3+ stakeholders or multi-vendor → Dedicated PM (High)
- Fixed contractual deadline → PM at minimum part-time
- Client-facing delivery → PM handles communication

### SA — System Analyst

**What they do:** Translates business requirements to technical specifications,
validates feature completeness, writes functional specs, bridges business and
engineering teams.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Simple CRUD systems, well-defined requirements |
| Middle | Moderate business logic, 5–10 features, integration work |
| Senior | Complex business rules, compliance requirements, legacy migration |

**Scope triggers for requiring SA:**
- Complex business rules or multi-role authorization → SA (High)
- Compliance requirements (PDPA, PCI-DSS) → Senior SA
- Legacy system integration or migration → SA for mapping

### DDA — Data & Digital Analyst

**What they do:** Defines analytics requirements, sets up tracking/tagging plans,
designs dashboards and reports, analyzes user behavior data.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Basic reporting, simple analytics dashboard |
| Middle | Custom dashboards, funnel analysis, A/B test setup |
| Senior | Complex data pipelines, BI strategy, predictive analytics |

**Scope triggers for requiring DDA:**
- Reporting module in scope → DDA at minimum part-time
- Analytics dashboard with custom metrics → Middle DDA
- Data-driven decision features (recommendations, predictions) → Senior DDA

### QA — Quality Assurance Engineer

**What they do:** Writes test cases, performs manual and automated testing,
validates acceptance criteria, manages defect lifecycle.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Simple CRUD, <5 features, no integrations |
| Middle | 5–10 features, 1–3 integrations, standard auth |
| Senior | Payment handling, PII, 3+ integrations, compliance |

**Scope triggers for requiring dedicated QA:**
- Payment integration OR PII handling → Dedicated QA (Critical)
- 3+ third-party integrations → Dedicated QA (High)
- Compliance/regulatory requirements → Senior QA

### FE — Frontend Developer

**What they do:** Implements web UI, handles client-side logic, integrates with
backend APIs, ensures responsive design and cross-browser compatibility.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Simple forms, list pages, basic CRUD UI |
| Middle | Complex interactions, responsive design, state management |
| Senior | Real-time UI, complex data visualization, performance optimization |

**Scope triggers:**
- Web frontend in scope → FE (Critical)
- Complex UI interactions (drag-drop, real-time) → Senior FE
- Admin panel with advanced features → Additional FE resource

### BE — Backend Developer

**What they do:** Implements server-side logic, designs database schema, builds
APIs, handles authentication, integrates third-party services.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Simple CRUD APIs, basic auth, single database |
| Middle | Business logic, 2–3 integrations, caching, background jobs |
| Senior | Microservices, complex auth (RBAC/MFA), real-time, high scale |

**Scope triggers:**
- Backend API in scope → BE (Critical)
- 3+ integrations → Senior BE
- Microservices or event-driven architecture → Senior BE + DevOps

### MOB — Mobile Developer

**What they do:** Implements native or cross-platform mobile applications (iOS,
Android, Flutter, React Native), handles device APIs (GPS, camera, sensors,
push notifications), manages app store submissions and mobile-specific UX patterns.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Simple mobile UI, single platform, wrapper-style app |
| Middle | Cross-platform (Flutter/RN), device APIs, offline support, 2–3 integrations |
| Senior | Native iOS + Android, complex animations, real-time features, background services, performance optimization |

**Scope triggers for requiring MOB:**
- Mobile app in scope → MOB (Critical — cannot build without one)
- Cross-platform (Flutter/RN) → Middle MOB minimum
- Native per platform (iOS + Android separately) → 1 Senior MOB per platform
- GPS tracking, camera, sensors, or background services → Middle–Senior MOB
- Offline-first or sync requirements → Senior MOB

**Platform-specific notes:**
- Flutter/React Native: One MOB can cover both platforms, but test effort doubles
- Native iOS + Native Android: Requires separate developers (Swift vs Kotlin)
- If project has BOTH web frontend AND mobile → FE and MOB are separate roles;
  do not assume a frontend developer can also build mobile

### UIUX — UI/UX Designer

**What they do:** Creates wireframes, mockups, prototypes, design systems, user
flows, and conducts usability testing.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Simple interfaces, existing design system, internal tools |
| Middle | Custom design, 3–5 user journeys, mobile-responsive |
| Senior | Design system creation, complex multi-platform, user research |

**Scope triggers:**
- Custom design required (no client-provided assets) → UIUX (High)
- Mobile + Web design needed → Middle–Senior UIUX
- Public-facing product with UX-critical flows → Senior UIUX

### GD — Graphic Designer

**What they do:** Creates visual assets — icons, illustrations, marketing
materials, brand identity elements, social media assets.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Basic icon sets, simple illustrations |
| Middle | Custom illustration style, brand assets, marketing materials |
| Senior | Brand identity creation, illustration systems, art direction |

**Scope triggers:**
- Custom illustration or icon system → GD
- Marketing landing pages with custom visuals → GD
- Brand identity work alongside product → Senior GD

### MGD — Motion Graphic Designer

**What they do:** Creates animations, micro-interactions, loading animations,
onboarding animations, video content, and animated UI transitions.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Simple loading animations, basic transitions |
| Middle | Onboarding flows, micro-interactions, animated illustrations |
| Senior | Complex animation systems, video content, Lottie animations |

**Scope triggers:**
- Animated onboarding or walkthrough → MGD
- Custom micro-interactions throughout product → Middle MGD
- Video content or complex Lottie animations → Senior MGD

### DO — DevOps Engineer

**What they do:** Sets up CI/CD pipelines, manages cloud infrastructure,
configures monitoring and alerting, handles deployments, manages environments.

| Seniority | When to Recommend |
|-----------|------------------|
| Junior | Basic CI/CD, single environment, managed hosting |
| Middle | Multi-environment (staging/prod), Docker, monitoring setup |
| Senior | Kubernetes, auto-scaling, multi-region, infrastructure-as-code |

**Scope triggers:**
- Microservices or Kubernetes → DevOps (Critical)
- Multi-environment deployment → DevOps (High)
- Auto-scaling or high-availability requirements → Senior DevOps

---

## Seniority Definitions

These definitions apply across all roles:

| Level | Experience | Characteristics | Supervision |
|-------|-----------|----------------|-------------|
| **Junior** | 0–2 years | Executes defined tasks, needs guidance on approach, learning domain patterns | Needs daily direction from mid/senior |
| **Middle** | 2–5 years | Works independently on standard tasks, can mentor juniors, proposes solutions | Needs weekly alignment, self-directed on execution |
| **Senior** | 5+ years | Leads technical decisions, handles ambiguity, mentors team, owns architecture | Self-directed, provides direction to others |

**Billing note:** Seniority affects both rate AND velocity. A senior developer at
2× the rate may deliver 2.5–3× the output of a junior on complex tasks — but only
1.2× on simple tasks. Factor this into estimation.

---

## Custom Reference Workflow

**This workflow runs at the START of Block 8, before any team recommendation.**

### Step 1: Check for Custom Reference

Ask the user:

> "Before I recommend the team composition and estimate costs, I need to know:
> **do you have your own manpower rate card or team catalog?**
>
> If yes, please share it — I'll use your rates instead of the defaults.
> If no, I'll use the standard rate card which I can show you for review.
>
> You can provide it as a file (any format) or paste it in. As long as it has
> roles, seniority levels, and rates, I can work with it."

### Step 2: Process the Response

**If user provides a custom reference:**
1. Read and extract: roles, seniority levels, rates, and any role descriptions
2. Map their roles to the standard codes (PM, SA, DDA, QA, FE, BE, UIUX, GD, MGD, DO)
3. If their catalog has roles not in the standard list, add them as custom roles
4. If their catalog is missing roles from the standard list, note the gaps
5. Present a mapping summary: "I've mapped your rate card as follows: [table]. Correct?"
6. Use their rates for all subsequent estimation in this session

**If user does not have a custom reference:**
1. Briefly present the default rate card summary (not the full table — just the
   roles and rate ranges)
2. Ask: "These are the standard rates I'll use. Do they roughly match your market?
   If any rates are significantly off, tell me and I'll adjust."
3. Proceed with defaults (or adjusted defaults)

### Step 3: Lock the Reference

Once confirmed, the rate card is locked for the session. All cost calculations in
the document will reference the confirmed rates with a note:

```markdown
**Rate Card Source:** [Default / Custom — provided by {user}]
**Confirmed:** [date]
```

---

## Template for Custom Rate Card

> Share this template with the user when they want to provide their own reference
> but don't have a structured format. They fill in the values and send it back.

```markdown
# [Company Name] — Manpower Rate Card

**Currency:** IDR / USD / [other]
**Rate basis:** Per hour / Per day / Per month
**Effective date:** [date]

## Roles & Rates

| Role | Junior | Middle | Senior |
|------|-------:|-------:|-------:|
| Project Manager | | | |
| System Analyst | | | |
| Data & Digital Analyst | | | |
| QA Engineer | | | |
| Frontend Developer | | | |
| Backend Developer | | | |
| Mobile Developer | | | |
| UI/UX Designer | | | |
| Graphic Designer | | | |
| Motion Graphic Designer | | | |
| DevOps Engineer | | | |
| [Custom Role 1] | | | |
| [Custom Role 2] | | | |

## Notes
- [Any special billing rules, e.g., overtime rates, minimum engagement, etc.]
```
