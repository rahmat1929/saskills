# PRD Full Template Reference

> Read this file before generating any PRD. Contains the complete 19-section structure with detailed guidance, RICE scoring framework, user story format, and domain-specific considerations.

---

## Table of Contents

1. [Conditional Section Matrix](#conditional-section-matrix)
2. [Section 1: Document Control](#section-1-document-control)
3. [Section 2: Executive Summary](#section-2-executive-summary)
4. [Section 3: Product Vision & Strategic Context](#section-3-product-vision--strategic-context)
5. [Section 4: Problem Statement & Opportunity](#section-4-problem-statement--opportunity)
6. [Section 5: Target Users & Personas](#section-5-target-users--personas)
7. [Section 6: User Stories & Use Cases](#section-6-user-stories--use-cases)
8. [Section 7: Functional Overview](#section-7-functional-overview)
9. [Section 8: User Flows & Interaction Model](#section-8-user-flows--interaction-model)
10. [Section 9: Requirements Prioritization (RICE)](#section-9-requirements-prioritization-rice)
11. [Section 10: Non-Functional Requirements](#section-10-non-functional-requirements)
12. [Section 11: Scope & Boundaries](#section-11-scope--boundaries)
13. [Section 12: Success Metrics & KPIs](#section-12-success-metrics--kpis)
14. [Section 13: Competitive Feature Comparison](#section-13-competitive-feature-comparison)
15. [Section 14: Assumptions & Constraints](#section-14-assumptions--constraints)
16. [Section 15: Dependencies & Integrations](#section-15-dependencies--integrations)
17. [Section 16: Release Strategy](#section-16-release-strategy)
18. [Section 17: Risks & Mitigations](#section-17-risks--mitigations)
19. [Section 18: Open Questions & Decisions Log](#section-18-open-questions--decisions-log)
20. [Section 19: Glossary & Appendices](#section-19-glossary--appendices)
21. [RICE Scoring Guide](#rice-scoring-guide)
22. [Prompt Template](#prompt-template)

---

## Conditional Section Matrix

| Section | New Product | Enhancement | Migration | Compliance | Integration |
|---------|:-----------:|:-----------:|:---------:|:----------:|:-----------:|
| 1. Document Control | Core | Core | Core | Core | Core |
| 2. Executive Summary | Core | Core | Core | Core | Core |
| 3. Product Vision & Strategy | ✅ Yes | Optional | Skip | Skip | Optional |
| 4. Problem Statement | Core | Core | Core | Core | Core |
| 5. Target Users & Personas | ✅ Yes | ✅ Yes | Optional | Optional | Optional |
| 6. User Stories & Use Cases | Core | Core | Core | Core | Core |
| 7. Functional Overview | Core | Core | Core | Core | Core |
| 8. User Flows & Interaction | ✅ Yes | ✅ Yes | Optional | Optional | ✅ Yes |
| 9. Requirements Prioritization | Core | Core | Core | Core | Core |
| 10. Non-Functional Requirements | Core | Core | Core | Core | Core |
| 11. Scope & Boundaries | Core | Core | Core | Core | Core |
| 12. Success Metrics & KPIs | Core | Core | Core | Core | Core |
| 13. Competitive Feature Comparison | ✅ Yes | Optional | Skip | Skip | Skip |
| 14. Assumptions & Constraints | Core | Core | Core | Core | Core |
| 15. Dependencies & Integrations | Core | Core | Core | Core | Core |
| 16. Release Strategy | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | Optional |
| 17. Risks & Mitigations | Core | Core | Core | Core | Core |
| 18. Open Questions & Decisions | Core | Core | Core | Core | Core |
| 19. Glossary & Appendices | Core | Core | Core | Core | Core |

---

## Section 1: Document Control

**Purpose:** Same as BRD — traceability, ownership, audit trail.

| Field | Value |
|-------|-------|
| Document ID | PRD-YYYY-XXX |
| Version | Start at 0.1 for drafts, 1.0 for approved |
| Status | Draft / In Review / Approved / Superseded |
| Author | Name, Role |
| Product Owner | Name (single point of product authority) |
| Created Date | Date |
| Last Updated | Date |
| Approved By | Name, Role, Date |
| Verified Against | [branch name, verification date — matches FSD Codebase Verification Record] |

**Change Log:**

| Version | Date | Author | Change Description |
|---------|------|--------|-------------------|
| 0.1 | [Date] | [Name] | Initial draft |
| 1.0 | [Date] | [Name] | Approved |

**Reviewers:**

| Name | Role | Review Status |
|------|------|--------------|
| [Name] | [Role] | Pending / Reviewed / Signed Off |

---

## Section 2: Executive Summary

**Purpose:** Max 1 page. Any stakeholder can read this and understand what the product does, who it's for, and why it matters.

**Structure:**

- **Product:** One sentence — what is being built.
- **Problem:** The user problem this solves (user-centric, not business-centric).
- **Users:** Who this is for (primary persona in one line).
- **Key Features:** Top 3-5 capabilities in bullet form.
- **Success Metric:** One headline product metric.
- **Timeline:** Expected delivery window.

**Rules:**
- Write LAST after all other sections
- Frame from the user's perspective, not the company's
- No technical jargon — readable by any stakeholder
- Lead with the user pain, not the feature list

---

## Section 3: Product Vision & Strategic Context

> **Conditional:** Core for New Product. Optional for Enhancement, Integration. Skip for Migration, Compliance.

**Purpose:** Where does this product/feature fit in the company's broader product strategy? This is the "north star" that guides trade-off decisions during development.

**Structure:**

**Product Vision Statement:**
> A single paragraph describing the long-term aspiration for this product. What does the world look like when this product is fully realized?

**Strategic Alignment:**

| Strategic Theme | How This Product Contributes |
|----------------|------------------------------|
| [Company OKR or strategy pillar] | [How this product moves the needle] |

**Product Positioning:**
- Where does this sit in the product portfolio?
- What adjacent products/features does it complement or replace?
- What is the product's unique value proposition in one sentence?

**Long-Term Roadmap Context:**
- What comes AFTER this version? (High-level, not detailed)
- How does this lay the foundation for future capabilities?

**Writing Tips:**
- Vision should be aspirational but grounded — "We want to eliminate manual expense reporting for mid-market companies" not "We want to revolutionize finance"
- Strategic alignment prevents the product from becoming a feature factory — every feature should trace back to strategy

---

## Section 4: Problem Statement & Opportunity

**Purpose:** What user or market problem are we solving? Unlike the BRD which frames problems from the business perspective, the PRD frames them from the **user's perspective**.

**Structure:**

**User Problem:**
- What specific frustration, inefficiency, or unmet need do target users face?
- How are they solving this problem today? (workarounds, competitor tools, manual processes)
- What makes the current alternatives inadequate?

**Evidence:**

| Evidence Type | Source | Key Finding |
|--------------|--------|-------------|
| User interviews | [# interviews, dates] | [What users said] |
| Analytics data | [Tool, metric] | [What data shows] |
| Support tickets | [Volume, category] | [Pattern observed] |
| Survey results | [Sample size, date] | [Key insight] |
| Market research | [Source] | [Trend or gap] |

**Opportunity Sizing (if applicable):**
- How many users are affected?
- What's the frequency of the problem? (daily, weekly, per transaction)
- What's the cost of the problem to users? (time, money, frustration)

**Jobs to Be Done (optional but recommended):**
> When [situation], I want to [motivation], so I can [expected outcome].

**Writing Tips:**
- Be specific: "Users spend 45 minutes/week manually reconciling invoices" not "Invoice management is painful"
- Include direct user quotes from research where available
- Quantify wherever possible — numbers make the problem real

---

## Section 5: Target Users & Personas

> **Conditional:** Core for New Product, Enhancement. Optional for Migration, Compliance, Integration.

**Purpose:** Who exactly are we building for? Behavioral context, not just demographics.

**Primary Persona:**

| Field | Detail |
|-------|--------|
| Persona Name | [Descriptive name, e.g., "Sarah the Store Manager"] |
| Role / Title | [Job title or role description] |
| Goals | [What they're trying to accomplish] |
| Frustrations | [What blocks them today] |
| Behavior Patterns | [How they work: tools, frequency, context] |
| Technical Comfort | [Low / Medium / High — how tech-savvy?] |
| Decision Authority | [Can they buy/adopt, or do they need approval?] |
| Success Looks Like | [What would make them say "this product is great"?] |

**Secondary Persona(s):** (Same structure, briefer — these users benefit but aren't the primary design target)

**Anti-Persona(s):**

| Who We're NOT Building For | Why |
|---------------------------|-----|
| [Description] | [Why they're excluded — different needs, different product] |

**Domain-Specific Persona Considerations:**
- **Healthcare:** Clinicians vs. administrators vs. patients have fundamentally different needs, workflows, and technical comfort levels
- **Fintech:** Retail users vs. institutional users vs. compliance officers
- **B2B SaaS:** End users vs. administrators vs. decision-makers (buyer ≠ user)
- **E-commerce:** Shoppers vs. merchants vs. fulfillment operators
- **Government:** Citizens vs. case workers vs. policy administrators

**Writing Tips:**
- Personas should feel like real people, not demographic checkboxes
- Include behavioral context: WHEN do they use this? WHERE? On what device?
- Anti-personas prevent scope creep — "We're NOT building this for power users who want CLI access" saves months of feature debate

---

## Section 6: User Stories & Use Cases

**Purpose:** The core of the PRD. Structured user stories grouped by **Feature Module**.

**Structure — Organize by Feature Module:**

```
═══════════════════════════════════════════
FEATURE MODULE: [Module Name, e.g., "Authentication"]
Module Description: [One-line description of this module's purpose]
═══════════════════════════════════════════
```

**Per User Story within a Module:**

| Field | Value |
|-------|-------|
| Story ID | US-[Module]-001 (e.g., US-AUTH-001) |
| Title | Short descriptive name |
| User Story | As a [persona], I want [goal], so that [reason] |
| Feature Module | [Module name this belongs to] |
| RICE Score | [Calculated — see RICE Scoring Guide below] |
| Priority Tier | MVP / Post-MVP / Future |
| Implementation Status | ✅ Implemented / ⚠️ Partial / [GAP] Not Implemented |
| Gap Reference | [Gap ID(s) from Appendix A, or "None"] |
| Acceptance Criteria | Given [context], When [action], Then [outcome] |
| Edge Cases | [Known edge cases or exception scenarios] |
| UI/UX Notes | [Any interaction expectations — NOT wireframes, just behavior] |
| Dependencies | [Other stories this depends on, if any] |

**Example:**

```
═══════════════════════════════════════════
FEATURE MODULE: Search & Filtering
Module Description: Enables users to find and narrow down results across the platform.
═══════════════════════════════════════════

Story ID: US-SRCH-001
Title: Keyword Search
User Story: As a store manager, I want to search products by name or SKU,
            so that I can quickly find items without scrolling through catalogs.
Feature Module: Search & Filtering
RICE Score: 675 (R:9000 × I:3 × C:0.5 ÷ E:20)
Priority Tier: MVP
Implementation Status: ✅ Implemented
Gap Reference: None
Acceptance Criteria:
  - Given I am on the product list page
    When I type 3+ characters in the search bar
    Then results filter in real-time showing matching products
  - Given I search for a term with no matches
    When results return empty
    Then I see a "No results found" message with suggested actions
Edge Cases: Special characters in search, very long queries (>200 chars), SQL injection attempts
UI/UX Notes: Search should be persistent across navigation. Debounce input (300ms).
Dependencies: None
```

**Module Organization Tips:**
- Typical modules: Authentication, Dashboard, Search, Notifications, Settings, Reporting, Payments, User Management, Admin, etc.
- Each module should have 3-15 stories. If more, consider splitting the module.
- Cross-module stories (e.g., "audit logging across all modules") go in a "Platform / Cross-Cutting" module.

---

## Section 7: Functional Overview

**Purpose:** High-level description of what the product does. Not FSD-level detail, but enough to understand feature scope.

**Structure:**

**Feature Map:**

| Feature Module | Key Capabilities | User Impact | Priority Tier |
|---------------|-----------------|-------------|---------------|
| [Module name] | [Top 3 capabilities in this module] | [What it enables for the user] | MVP / Post-MVP |

**Core Workflows:**
- List the 3-5 most important end-to-end workflows the product supports
- Describe each in 2-3 sentences focusing on user outcome, not technical steps

**Feature Interaction Matrix (for complex products):**

| Feature | Depends On | Feeds Into | Shared Data |
|---------|-----------|------------|-------------|
| [Feature A] | [What it needs] | [What uses its output] | [Shared entities/data] |

**Writing Tips:**
- This section is a map, not a manual — keep it high-level
- Engineers should read this and understand the product's shape without drowning in detail
- If you catch yourself writing API schemas or database fields, you've gone too far — that's FSD/SDD

---

## Section 8: User Flows & Interaction Model

> **Conditional:** Core for New Product, Enhancement, Integration. Optional for Migration, Compliance.

**Purpose:** Key user journeys mapped logically. Not wireframes — the logical sequence of steps, decisions, and outcomes.

**Structure per Flow:**

```
Flow Name: [e.g., "New User Onboarding"]
Trigger: [What initiates this flow — e.g., "User clicks Sign Up"]
Actor: [Which persona]
Preconditions: [What must be true before this flow starts]

Steps:
1. [Action / Screen] → [What user does] → [System response]
2. [Action / Screen] → [What user does] → [System response]
   ├── IF [condition A] → [Path A outcome]
   └── IF [condition B] → [Path B outcome]
3. [Action / Screen] → [What user does] → [System response]

Success Outcome: [What "done" looks like for the user]
Error Paths:
  - [Error scenario 1] → [How the system responds] → [User recovery path]
  - [Error scenario 2] → [How the system responds] → [User recovery path]

Post-Conditions: [State of the system after flow completes]
```

**Key Flows to Document:**
- Primary happy path (the "golden path" most users take)
- First-time user experience (onboarding)
- Core value action (the thing users come back to do repeatedly)
- Error recovery (what happens when things go wrong)
- Edge case flows (admin overrides, bulk operations, etc.)

**Writing Tips:**
- Keep flows focused — one flow per user goal
- Always include error paths, not just happy paths
- Decision points (IF/THEN branches) are critical — they reveal complexity that engineers need to plan for
- Reference personas: "As Sarah the Store Manager, she starts at the Dashboard..."

---

## Section 9: Requirements Prioritization (RICE)

**Purpose:** Data-informed prioritization using the RICE framework. Every feature or story gets scored to make trade-offs objective.

**RICE Formula:**

```
RICE Score = (Reach × Impact × Confidence) ÷ Effort
```

**Scoring Guide:**

| Factor | What It Measures | Scale |
|--------|-----------------|-------|
| **Reach** | How many users will this affect per quarter? | Estimated number of users (e.g., 500, 5000, 50000) |
| **Impact** | How much will this improve the user experience? | 3 = Massive, 2 = High, 1 = Medium, 0.5 = Low, 0.25 = Minimal |
| **Confidence** | How sure are we about reach and impact estimates? | 1.0 = High (data-backed), 0.8 = Medium (informed guess), 0.5 = Low (gut feeling) |
| **Effort** | How many person-weeks to build? | Estimated person-weeks (e.g., 1, 4, 12, 20) |

**RICE Scoring Table:**

| Story ID | Title | Reach | Impact | Confidence | Effort (pw) | RICE Score | Priority Tier |
|----------|-------|-------|--------|------------|-------------|------------|---------------|
| US-SRCH-001 | Keyword Search | 9000 | 3 | 0.5 | 20 | 675 | MVP |
| US-AUTH-002 | Social Login | 6000 | 1 | 0.8 | 8 | 600 | MVP |
| US-RPT-001 | Export to CSV | 2000 | 2 | 1.0 | 4 | 1000 | MVP |

**Priority Tier Thresholds (calibrate per project):**
- **MVP:** Top-scored items that deliver core value. Ship or fail.
- **Post-MVP:** High-value items that enhance but aren't essential for launch.
- **Future:** Lower-scored or low-confidence items. Revisit after launch data.

**Rules:**
- Score ALL stories, even ones you think are obvious
- Be honest with Confidence — a 0.5 score isn't shameful, it's informative
- Effort should include design, development, QA, AND documentation
- Revisit scores when new data arrives (post-research, post-beta)

---

## Section 10: Non-Functional Requirements

**Purpose:** Constraints the product must meet that aren't features. This is where the 40% technical lives most heavily.

**Structure by Category:**

### Performance
| Requirement | Target | Measurement |
|-------------|--------|-------------|
| Page load time | [e.g., <2 seconds for 95th percentile] | [Tool: Lighthouse, New Relic, etc.] |
| API response time | [e.g., <500ms for core endpoints] | [Monitoring tool] |
| Concurrent users | [e.g., Support 10,000 simultaneous users] | [Load testing] |
| Throughput | [e.g., Process 500 transactions/second] | [Benchmark] |

### Scalability
| Dimension | Current | Target | Growth Assumption |
|-----------|---------|--------|-------------------|
| Users | [Current count] | [Target count] | [Growth rate] |
| Data volume | [Current] | [Projected] | [Growth rate] |
| Geographic reach | [Current regions] | [Target regions] | [Expansion plan] |

### Security
| Requirement | Standard | Implementation Notes |
|-------------|----------|---------------------|
| Authentication | [e.g., OAuth 2.0 / SAML / MFA] | [Which users, when enforced] |
| Encryption | [e.g., TLS 1.2+ in transit, AES-256 at rest] | [Scope] |
| Audit logging | [What's logged, retention period] | [Compliance driver] |
| Data privacy | [GDPR, CCPA, HIPAA requirements] | [Applicable to which data] |

### Accessibility
| Standard | Level | Notes |
|----------|-------|-------|
| WCAG | [2.1 AA / 2.1 AAA] | [Required by regulation or policy?] |
| Screen reader support | [Required / Best effort] | [Priority screens] |
| Keyboard navigation | [Full / Partial] | [Scope] |

### Reliability & Availability
| Requirement | Target |
|-------------|--------|
| Uptime SLA | [e.g., 99.9%] |
| RTO (Recovery Time Objective) | [e.g., <1 hour] |
| RPO (Recovery Point Objective) | [e.g., <15 minutes] |
| Disaster recovery | [Active-passive / Active-active / None] |

### Localization & Internationalization
| Requirement | Scope |
|-------------|-------|
| Languages supported | [List] |
| Currency support | [List] |
| Timezone handling | [User-local / UTC / Configurable] |
| RTL support | [Required / Not required] |

**Domain-Specific NFR Considerations:**
- **Healthcare:** HIPAA compliance, HL7/FHIR data standards, clinical system uptime
- **Fintech:** PCI-DSS, SOC 2, transaction processing guarantees, audit trails
- **Government:** FedRAMP, Section 508 accessibility, data sovereignty
- **E-commerce:** Peak traffic handling (Black Friday), payment gateway SLAs, cart abandonment recovery
- **SaaS:** Multi-tenancy isolation, per-tenant rate limiting, white-labeling support

---

## Section 11: Scope & Boundaries

**Purpose:** What ships vs. what doesn't. Product-focused scope.

**MVP Scope (Must Ship):**

| Feature Module | Included Capabilities | Stories Included |
|---------------|----------------------|-----------------|
| [Module] | [What's in MVP] | [US-XXX-001, US-XXX-002] |

**Post-MVP Scope (Fast Follow):**

| Feature Module | Capabilities | Target Release | Reason for Deferral |
|---------------|-------------|----------------|---------------------|
| [Module] | [What's deferred] | [v1.1 / Q3 / etc.] | [Why not MVP] |

**Explicitly Out of Scope:**

| Item | Reason | Alternative (if any) |
|------|--------|---------------------|
| [What's excluded] | [Why] | [Workaround or future plan] |

**Scope Decision Principles:**
- If it doesn't serve the primary persona's core workflow → out of scope
- If RICE score is below the MVP threshold → post-MVP
- If confidence is 0.5 or below AND effort is L or XL → defer until validated
- When in doubt, cut scope. Launching lean and iterating > launching late and bloated

---

## Section 12: Success Metrics & KPIs

**Purpose:** How we measure if the product works. Product-level metrics, not business-level.

**Structure:**

### Adoption Metrics
| Metric | Definition | Baseline | Target | Timeline |
|--------|-----------|----------|--------|----------|
| Activation rate | [% of signups who complete onboarding] | [Current or N/A] | [Target] | [When] |
| DAU / WAU / MAU | [Active user counts] | [Current or N/A] | [Target] | [When] |
| Feature adoption | [% of users using key feature X] | [N/A for new] | [Target] | [When] |

### Engagement Metrics
| Metric | Definition | Baseline | Target | Timeline |
|--------|-----------|----------|--------|----------|
| Session duration | [Average time in product] | [Current] | [Target] | [When] |
| Task completion rate | [% of users completing core workflow] | [Current] | [Target] | [When] |
| Return frequency | [How often users come back] | [Current] | [Target] | [When] |

### Satisfaction Metrics
| Metric | Definition | Baseline | Target | Timeline |
|--------|-----------|----------|--------|----------|
| NPS / CSAT | [Score] | [Current] | [Target] | [When] |
| Support ticket volume | [Tickets related to this feature] | [Current] | [Target reduction] | [When] |
| User feedback sentiment | [Positive/negative ratio] | [N/A] | [Target] | [When] |

### Performance Metrics
| Metric | Definition | Target |
|--------|-----------|--------|
| Error rate | [% of failed operations] | [<X%] |
| Latency (P95) | [95th percentile response time] | [<Xms] |
| Uptime | [Availability percentage] | [99.X%] |

**Leading vs. Lagging:**
- **Leading (early signals):** Activation rate, first-week engagement, support tickets
- **Lagging (final outcomes):** Retention at 30/60/90 days, NPS, churn impact

---

## Section 13: Competitive Feature Comparison

> **Conditional:** Core for New Product. Optional for Enhancement. Skip for Migration, Compliance, Integration.

**Purpose:** Feature-level comparison against competitors. Shows where you lead, match, or trail.

**Feature Comparison Matrix:**

| Feature | Our Product | Competitor A | Competitor B | Competitor C | Our Advantage |
|---------|:-----------:|:------------:|:------------:|:------------:|---------------|
| [Feature 1] | ✅ / 🔶 / ❌ | ✅ / 🔶 / ❌ | ✅ / 🔶 / ❌ | ✅ / 🔶 / ❌ | [Why we're better or different] |
| [Feature 2] | ✅ / 🔶 / ❌ | ✅ / 🔶 / ❌ | ✅ / 🔶 / ❌ | ✅ / 🔶 / ❌ | [Why we're better or different] |

Legend: ✅ = Full support | 🔶 = Partial | ❌ = Not available

**Competitive Positioning Summary:**
- Where do we lead? (features with clear differentiation)
- Where do we match? (table stakes features)
- Where do we trail? (gaps to acknowledge and plan for)
- What's our unique angle? (what competitors CAN'T easily replicate)

---

## Section 14: Assumptions & Constraints

**Purpose:** What we're assuming about users, market, and technology. What limits design choices.

**Product Assumptions:**

| ID | Assumption | Risk if Wrong | How to Validate |
|----|-----------|--------------|-----------------|
| PA-001 | [e.g., Users prefer self-service over calling support] | [Impact] | [A/B test, survey, beta feedback] |

**Technical Constraints:**

| ID | Constraint | Impact on Product | Flexibility |
|----|-----------|-------------------|-------------|
| TC-001 | [e.g., Must run on existing AWS infrastructure] | [Limits tech choices] | Hard / Negotiable |

**Resource Constraints:**

| Constraint | Detail | Impact on Scope |
|-----------|--------|-----------------|
| Team size | [# engineers, designers, PMs available] | [What can realistically ship in timeline] |
| Timeline | [Hard deadline or flexible?] | [MVP vs. full scope trade-off] |
| Budget | [Fixed or flexible?] | [Build vs. buy decisions] |

---

## Section 15: Dependencies & Integrations

**Purpose:** What external systems, teams, and services the product depends on.

**External Dependencies:**

| ID | Dependency | Type | Owner | Status | Impact if Delayed |
|----|-----------|------|-------|--------|-------------------|
| ED-001 | [System / API / Service] | External Vendor / Internal Team / Platform | [Who controls it] | Confirmed / Pending / At Risk | [Consequence] |

**Integration Points:**

| System | Integration Type | Data Exchanged | Direction | Criticality |
|--------|-----------------|---------------|-----------|-------------|
| [System name] | API / Webhook / File / Manual | [What data flows] | Inbound / Outbound / Bidirectional | Critical / Important / Nice-to-have |

**Internal Team Dependencies:**

| Team | What We Need | When | Status |
|------|-------------|------|--------|
| [Team name] | [Deliverable or support needed] | [Date/phase] | Aligned / Pending / Blocked |

---

## Section 16: Release Strategy

> **Conditional:** Core for New Product, Enhancement, Migration, Compliance. Optional for Integration.

**Purpose:** How the product reaches users. Phasing, rollout approach, and launch criteria.

**Release Approach:**

| Phase | What Ships | Audience | Success Gate to Proceed |
|-------|-----------|----------|------------------------|
| Alpha / Internal | [Core features] | [Internal team / dogfooding] | [Criteria to move forward] |
| Beta / Pilot | [MVP features] | [Selected users / cohort] | [Criteria to expand] |
| GA / Full Launch | [Complete MVP] | [All target users] | [Criteria met] |
| Post-Launch Iteration | [Post-MVP features] | [All users] | [Based on metrics] |

**Feature Flagging Strategy:**
- Which features will be behind flags?
- What's the default state (on/off) per audience?
- Who controls flag toggling? (PM, Eng, Ops)

**Rollback Plan:**
- What triggers a rollback? (error rate, critical bugs, user complaints)
- How quickly can we roll back? (instant flag toggle vs. deployment)
- Who makes the rollback decision?

**Launch Checklist (customize per project):**
```
□ All MVP stories pass acceptance criteria
□ Non-functional requirements met (performance, security, accessibility)
□ Documentation complete (user-facing and internal)
□ Support team briefed and ready
□ Monitoring and alerting configured
□ Rollback plan tested
□ Legal/compliance sign-off (if applicable)
□ Marketing/comms prepared (if applicable)
```

---

## Section 17: Risks & Mitigations

**Purpose:** Product-specific risks. Different lens from BRD — focused on adoption, usability, feasibility.

**Risk Categories for PRD:**

| Risk ID | Description | Category | Likelihood | Impact | RICE-Adjusted? | Mitigation | Owner |
|---------|------------|----------|-----------|--------|----------------|------------|-------|
| PR-001 | [What could go wrong] | Adoption / Usability / Technical Feasibility / Competitive / Dependency / Regulatory | L / M / H | L / M / H | [Does this risk lower confidence scores?] | [Strategy] | [Who monitors] |

**Category Definitions:**
- **Adoption Risk:** Users might not use the product as expected
- **Usability Risk:** The product might be confusing or frustrating
- **Technical Feasibility Risk:** The feature might be harder to build than estimated
- **Competitive Risk:** A competitor might ship something similar or better
- **Dependency Risk:** An external system or team might not deliver on time
- **Regulatory Risk:** Compliance requirements might change or be more complex than assumed

**Tips:**
- Tie risks back to RICE scores — a high adoption risk should lower the Confidence score
- Include "what we'll learn" from each risk — even negative outcomes teach us something
- Don't just list risks, assign concrete mitigations with owners

---

## Section 18: Open Questions & Decisions Log

**Purpose:** The most-referenced section during development. Tracks what's unresolved and what was decided.

**Open Questions:**

| ID | Question | Impact Area | Raised By | Owner | Deadline | Status |
|----|---------|-------------|-----------|-------|----------|--------|
| OQ-001 | [What needs answering] | [Which feature/module affected] | [Who raised it] | [Who will resolve] | [By when] | Open / In Progress / Blocked |

**Decisions Log:**

| ID | Decision | Rationale | Alternatives Considered | Decided By | Date | Reversible? |
|----|---------|-----------|------------------------|-----------|------|-------------|
| DL-001 | [What was decided] | [Why this option] | [What else was considered] | [Who made the call] | [Date] | Yes / No |

**Why This Section Matters:**
- During development, this is where engineers and designers look first when they hit ambiguity
- The Decisions Log prevents re-litigating settled debates
- "Reversible?" column helps teams know which decisions can be changed later vs. which are locked in

---

## Section 19: Glossary & Appendices

**Glossary:**

| Term | Definition | Context |
|------|-----------|---------|
| [Term] | [Plain-language definition] | [How used in this product specifically] |

**Rules:**
- Include product terms, domain terms, and technical terms from this PRD
- If the same word means different things to different teams, clarify which definition applies
- This glossary should carry forward into FSD, SDD, TSD

**Appendices (include what's relevant):**

### Appendix A: Implementation Gap Registry

**Purpose:** Business-level summary of all unimplemented or partially implemented stories. Derived from the FSD Gap Registry — the FSD is authoritative for technical detail; this appendix captures business impact and delivery phase.

| Gap ID | Story ID | FSD Ref | Gap Description | Business Impact | Phase | Status |
|--------|----------|---------|-----------------|-----------------|-------|--------|
| GAP-001 | US-[MOD]-001 | FR-3.x.x | [What is missing in plain language] | [What business value is blocked] | Phase 1 / 2 / 3 | Open / In Progress / Resolved |

**How to maintain:**
- A story moves from [GAP] / ⚠️ Partial to ✅ Implemented when all its FSD FRs are verified as implemented.
- When that happens: update the story's `Implementation Status` field above AND mark this row as `Resolved`.
- Keep resolved rows — they serve as an audit trail of what was built and when.

---

- B. User research summaries / interview transcripts
- C. Analytics data supporting the problem statement
- D. Wireframe or mockup references (link, don't embed)
- E. Competitive analysis deep-dives
- F. Technical spike or proof-of-concept results
- G. Related PRDs, BRDs, or design docs

---

## RICE Scoring Guide

### Quick Reference

```
RICE Score = (Reach × Impact × Confidence) ÷ Effort
```

### Factor Definitions

**Reach** — How many users will this affect in a defined time period?
- Use a consistent time period (per quarter is common)
- Count individual users, not companies or accounts
- Be specific: "3,000 users/quarter" not "a lot"
- For internal tools, count internal users the same way

**Impact** — How much will this improve the experience for each user who encounters it?
- 3.0 = Massive — completely changes their workflow, solves a major pain
- 2.0 = High — significant improvement, noticeable time/effort savings
- 1.0 = Medium — helpful improvement, some friction removed
- 0.5 = Low — minor improvement, nice-to-have
- 0.25 = Minimal — barely noticeable, edge case fix

**Confidence** — How confident are we in our Reach and Impact estimates?
- 1.0 = High — backed by quantitative data (analytics, A/B test, large survey)
- 0.8 = Medium — supported by qualitative data (interviews, small survey, expert opinion)
- 0.5 = Low — gut feeling, assumption, or very limited data
- Below 0.5 is rare — if you're that unsure, do research before scoring

**Effort** — How many person-weeks will this take to ship (design + dev + QA + docs)?
- Count ALL effort, not just engineering
- Use person-weeks, not calendar weeks
- Include testing, documentation, and deployment effort
- When unsure, estimate high — underestimation is the most common mistake

### Scoring Tips
- Score relative to each other within the same PRD — consistency matters more than absolute accuracy
- Revisit scores after user research, beta feedback, or when assumptions change
- A high RICE score with 0.5 confidence = run a quick validation before committing
- Effort is the most commonly underestimated factor — add 30% buffer for unknowns

---

## Prompt Template

Use this when invoking the PRD generator:

```
You are a Senior Product Manager creating a Product Requirements Document (PRD).

PRODUCT CONTEXT:
- Product/Feature Name: [INPUT]
- Project Type: [New Product / Enhancement / Migration / Compliance-Driven / Integration]
- Domain/Industry: [INPUT]
- Problem Statement: [INPUT — user problem, pain points, opportunity]
- Target Users: [INPUT — who are we building for?]
- Technical Constraints: [INPUT — platforms, existing systems, team capacity]
- Competitive Context: [INPUT — optional]

INSTRUCTIONS:
1. Generate a complete PRD following the 19-section structure.
2. Activate or skip conditional sections based on Project Type.
3. Group all user stories by Feature Module.
4. Calculate RICE scores for all features/stories.
5. Clearly separate MVP from Post-MVP scope.
6. Maintain 60% business / 40% technical balance.
7. Use domain/industry to calibrate personas, NFRs, risks, and terminology.
8. Flag gaps with [NEEDS INPUT: description].
9. Write Executive Summary LAST.
10. For Enhancement/existing systems: populate `Implementation Status` on every story and include Appendix A Gap Registry.

OUTPUT:
- Use exact section numbering (1-19)
- Include all tables in structured format
- Mark skipped sections: "[SKIPPED — Not applicable for {Project Type} projects]"
- End with completed Quality Checklist
```
