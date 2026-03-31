# Mood Based Recommendation App — Requirements & Analysis Document

**Version:** 1.0  
**Prepared by:** Requirement Analysis (AI-assisted)  
**Date:** 2026-03-17  
**Status:** FINAL — Ready for Development  

## 1. Executive Summary

This project will deliver a mobile application that provides **instant mood-based recommendations** to support **wellbeing and content discovery**. Users will select a mood (preset buttons) and may provide free text; the system will return recommendations across two MVP categories: **Music** and **Activities**.

The MVP will launch on **iOS (14+) and Android (8+)** for **SEA markets** and targets **50,000 installs in the first month after go-live** and average user engagement of **at least 3 sessions per week**. Users may continue as **Guest** or sign in to enable secure storage of mood history, recommendation history, and behavioral feedback signals.

The largest delivery risk is third-party dependency: **Spotify and YouTube Music integration** is included in MVP and requires OAuth connectivity and stable external APIs. The go-live target is therefore **flexible**.

## 2. Reference Analysis

The following references were discussed as benchmarks for patterns and differentiation:

| ID | Reference | Type | What's Relevant | What's Different |
|----|-----------|------|----------------|-----------------|
| REF-001 | Moodfit | Benchmark app | Mood tracking and history patterns | This project focuses on instant recommendations, not deep tracking |
| REF-002 | Replika | Benchmark app | Emotional engagement and personalization | This project avoids chat-first, and prioritizes fast actions |
| REF-003 | Fabulous | Benchmark app | Calming UX patterns and engagement | This project is mood-driven and lighter weight |
| REF-004 | Spotify | Benchmark app | Recommendation patterns and personalization | This project uses explicit mood input and adds Activities |

**Differentiation positioning (confirmed):**
- Instant recommendations based on current mood
- Multi-category suggestions (MVP: Music + Activities)
- Lightweight interaction (swipe, feedback, refresh) instead of journaling/chat-heavy flows
- Personalization improves over time using mood history and behavioral signals

## 3. Business Requirements

### 3.1 Problem Statement

Users want quick, relevant suggestions aligned with how they feel in the moment. Existing solutions are either heavy (tracking/journaling), slow (chat-based), or single-domain. This app provides a simple, calming experience to translate a mood into actionable recommendations immediately.

### 3.2 Business Objectives

1. Achieve **50,000 installs** in the **first month** after go-live.
2. Achieve average engagement of **≥ 3 sessions per week per user**.
3. Provide fast recommendation results suitable for mobile usage in-the-moment.

### 3.3 Stakeholder Map

| ID | Stakeholder | Role | Involvement | Decision Authority |
|----|-------------|------|-------------|-------------------|
| UR-001 | Ana | PM | Day-to-day product owner | Product scope, UAT sign-off |
| UR-002 | Jira | Sales | Stakeholder | Commercial alignment |
| UR-003 | Mr Tom | Client | Stakeholder | Client approval |

### 3.4 Business Requirements (BR)

| Field | Value |
|-------|-------|
| **ID** | BR-001 |
| **Title** | Mood-based recommendations |
| **Description** | The system shall allow users to input their current mood and receive recommendations aligned to that mood across MVP categories (Music and Activities). |
| **Priority** | Must |
| **Rationale** | Core value proposition for wellbeing and content discovery. |
| **Source** | UR-001 (Ana), UR-003 (Mr Tom) |
| **Linked Objective** | Obj-1, Obj-2 |
| **Acceptance Criteria** | Given a user selects a mood, When they request recommendations, Then the system displays Music and Activities recommendations for that mood. |
| **Linked Features** | FT-001, FT-004, FT-005 |

| Field | Value |
|-------|-------|
| **ID** | BR-002 |
| **Title** | Lightweight interaction and feedback |
| **Description** | The system shall allow users to like, skip, refresh, bookmark, and provide helpful/not helpful feedback for recommendations. |
| **Priority** | Must |
| **Rationale** | Drives engagement and supports iterative personalization. |
| **Source** | UR-001 (Ana) |
| **Linked Objective** | Obj-2 |
| **Acceptance Criteria** | Given a recommendation is displayed, When the user interacts (like/skip/helpful/bookmark/refresh), Then the action is recorded and reflected in UI state. |
| **Linked Features** | FT-006, FT-007, FT-008 |

| Field | Value |
|-------|-------|
| **ID** | BR-003 |
| **Title** | History and personalization signals |
| **Description** | The system shall store mood history and recommendation history for logged-in users and use recent/similar mood context to improve recommendations. |
| **Priority** | Must |
| **Rationale** | Improves relevance over time and enables user review of past interactions. |
| **Source** | UR-001 (Ana) |
| **Linked Objective** | Obj-2 |
| **Acceptance Criteria** | Given a logged-in user, When they view history, Then they can see mood entries and recommendation history. |
| **Linked Features** | FT-009, FT-010 |

| Field | Value |
|-------|-------|
| **ID** | BR-004 |
| **Title** | Secure account access with guest option |
| **Description** | The system shall support guest access and authenticated access using Email OTP and Password, with MFA enforced for Admin accounts. |
| **Priority** | Must |
| **Rationale** | Balances low-friction onboarding with secure data storage. |
| **Source** | UR-001 (Ana) |
| **Linked Objective** | Obj-2 |
| **Acceptance Criteria** | Given a user chooses login, When they authenticate via OTP/password, Then they can access their stored history and actions; Admin login requires MFA. |
| **Linked Features** | FT-002, FT-003, FT-012 |

| Field | Value |
|-------|-------|
| **ID** | BR-005 |
| **Title** | Content safety and supportive handling |
| **Description** | The system shall enforce content safety rules for curated content and show supportive messaging with helpline/resources links for sensitive moods. |
| **Priority** | Must |
| **Rationale** | Mood data is sensitive; the app must handle extreme states carefully. |
| **Source** | UR-001 (Ana), UR-003 (Mr Tom) |
| **Linked Objective** | Obj-2 |
| **Acceptance Criteria** | Given a sensitive/extreme mood scenario, When triggered by configured rules, Then the user sees supportive messaging and resource links. |
| **Linked Features** | FT-011, FT-013 |

### 3.5 Constraints & Assumptions

| ID | Type | Description | Impact if Wrong | Validation Method |
|----|------|------------|----------------|-------------------|
| C-001 | Constraint | MVP targets iOS 14+ and Android 8+ | May increase support load if market expects older OS | Confirm device analytics / market needs |
| C-002 | Constraint | Hosting is AWS | Limits hosting choices | Confirm with client IT |
| A-001 | Assumption | Final mood taxonomy and mapping rules will be finalized before implementation | Recommendation quality may be inconsistent | Define mood taxonomy + mapping workshop |
| A-002 | Assumption | “Sensitive mood” detection will be implemented via configured rules (not clinical assessment) | Risk of over/under-trigger | Review policy with stakeholders |

## 4. UX & Design Requirements

### 4.1 Design Ownership & Resources

UX/UI design is delivered by an **internal designer**. The UI must be calming, fast, and accessible.

### 4.2 Personas

**UR-004: Guest User**
- Who they are: New user trying the app with minimal friction.
- Primary job in the system: Enter mood and get recommendations quickly.
- Critical need: Immediate value without account creation.

**UR-005: Logged-in User**
- Who they are: Returning user who wants saved history and personalization.
- Primary job in the system: Track interactions over time and revisit saved content.
- Critical need: Consistent recommendations and visible history.

**UR-006: Admin / Content Manager**
- Who they are: Internal operator managing curated activities and safety rules.
- Primary job in the system: Maintain content quality and safety.
- Critical need: Fast content updates without app releases.

### 4.3 Critical User Journeys

**UJ-001: Get recommendations**
1. User opens app.
2. User continues as guest or logs in.
3. User selects a mood (preset) and optionally enters free text.
4. System generates recommendations (Music + Activities).
5. User swipes through cards and takes actions (like/skip/helpful/bookmark).

**UJ-002: View history**
1. Logged-in user opens History.
2. User views mood history and recommendation history.
3. User opens a saved item (link) for playback/consumption in provider.

**UJ-003: Admin manages curated activities and safety rules**
1. Admin logs in (MFA required).
2. Admin creates/edits curated activity entries.
3. Admin updates content safety rules.

### 4.4 UI/UX Constraints & Requirements

| Requirement | Specification | Notes |
|-------------|--------------|-------|
| Accessibility | WCAG-level accessibility | Minimum: accessible contrast, labels, focus, screen reader support |
| Dark mode | Required | Must be supported across core screens |
| Minimal motion | Required | Provide reduced motion option / default minimal animations |
| Primary interaction | Swipeable cards | List/grid may also be offered |
| Language | English for MVP | Additional languages may be added later |

## 5. Technical Specifications

### 5.1 System Overview

```mermaid
graph LR
  U1[Guest / Logged-in User\n(iOS/Android)] --> API[Backend API]
  Admin[Admin (Web Dashboard)] --> API
  API --> DB[(Primary Database)]
  API --> Cache[(Cache - optional)]
  API --> SP[Spotify API]
  API --> YTM[YouTube Music API]
  API --> Email[Email OTP Service]
```

### 5.2 Scope of Development

| Layer | In Scope | Notes |
|-------|----------|-------|
| Mobile (iOS) | Yes | Native Swift, iOS 14+ |
| Mobile (Android) | Yes | Native Kotlin, Android 8+ |
| Backend (API) | Yes | Auth, history, recommendation service, provider integrations |
| Admin Panel (Web) | Yes | Content + safety rules management |
| Background Workers | [ASSUMPTION: Yes — needed for token refresh, sync jobs, and analytics events processing] | Confirm job list during implementation |
| DevOps / Infra | Yes | AWS environments, CI/CD, monitoring |

### 5.3 Feature Specifications (FT)

| Field | Value |
|-------|-------|
| **ID** | FT-001 |
| **Name** | Mood input (preset + free text) |
| **Description** | Users can select from predefined moods and optionally provide free text to refine context. |
| **User Roles** | UR-004, UR-005 |
| **Linked Requirements** | BR-001 |
| **Business Rules** | Free text is optional; preset mood selection remains required. |
| **Dependencies** | — |
| **Complexity** | M |

| Field | Value |
|-------|-------|
| **ID** | FT-002 |
| **Name** | Authentication (Email OTP + Password) |
| **Description** | Users can continue as guest or authenticate using Email OTP and Password to enable history and persistence. |
| **User Roles** | UR-004, UR-005 |
| **Linked Requirements** | BR-004 |
| **Business Rules** | Guest users may use core recommendation flow; persistence requires login. |
| **Dependencies** | INT-003 |
| **Complexity** | L |

| Field | Value |
|-------|-------|
| **ID** | FT-003 |
| **Name** | Admin authentication with MFA |
| **Description** | Admin accounts must authenticate and satisfy MFA before accessing the dashboard. |
| **User Roles** | UR-006 |
| **Linked Requirements** | BR-004 |
| **Business Rules** | MFA is mandatory for Admin; failure blocks access. |
| **Dependencies** | INT-003 |
| **Complexity** | M |

| Field | Value |
|-------|-------|
| **ID** | FT-004 |
| **Name** | Recommendation generation |
| **Description** | System generates recommendations for Music and Activities based on selected mood, optional text, and recent/similar mood context. |
| **User Roles** | UR-004, UR-005 |
| **Linked Requirements** | BR-001, BR-003 |
| **Business Rules** | Recommendation response must be returned quickly for interactive UX. |
| **Dependencies** | FT-001, INT-001, INT-002 |
| **Complexity** | L |

| Field | Value |
|-------|-------|
| **ID** | FT-005 |
| **Name** | Recommendation display (cards + list/grid) |
| **Description** | Recommendations are displayed as swipeable cards by default; list/grid may also be available. |
| **User Roles** | UR-004, UR-005 |
| **Linked Requirements** | BR-001 |
| **Dependencies** | FT-004 |
| **Complexity** | M |

| Field | Value |
|-------|-------|
| **ID** | FT-006 |
| **Name** | Actions: Like / Skip |
| **Description** | Users can like or skip items and the system records the action. |
| **User Roles** | UR-004, UR-005 |
| **Linked Requirements** | BR-002 |
| **Dependencies** | FT-005 |
| **Complexity** | M |

| Field | Value |
|-------|-------|
| **ID** | FT-007 |
| **Name** | Feedback: Helpful / Not helpful |
| **Description** | Users can provide helpful/not helpful feedback for recommendations. |
| **User Roles** | UR-004, UR-005 |
| **Linked Requirements** | BR-002 |
| **Dependencies** | FT-005 |
| **Complexity** | S |

| Field | Value |
|-------|-------|
| **ID** | FT-008 |
| **Name** | Refresh recommendations |
| **Description** | Users can request a refreshed set of recommendations for the same mood. |
| **User Roles** | UR-004, UR-005 |
| **Linked Requirements** | BR-002 |
| **Dependencies** | FT-004 |
| **Complexity** | M |

| Field | Value |
|-------|-------|
| **ID** | FT-009 |
| **Name** | Bookmark / Saved collection |
| **Description** | Users can save recommended items into an in-app collection. |
| **User Roles** | UR-004, UR-005 |
| **Linked Requirements** | BR-002 |
| **Dependencies** | FT-005 |
| **Complexity** | M |

| Field | Value |
|-------|-------|
| **ID** | FT-010 |
| **Name** | History: mood + recommendation history |
| **Description** | Logged-in users can view mood history and recommendation history. |
| **User Roles** | UR-005 |
| **Linked Requirements** | BR-003 |
| **Dependencies** | FT-002 |
| **Complexity** | M |

| Field | Value |
|-------|-------|
| **ID** | FT-011 |
| **Name** | Curated activities management |
| **Description** | Admin can create/update curated activity content used in recommendations. |
| **User Roles** | UR-006 |
| **Linked Requirements** | BR-005 |
| **Dependencies** | FT-003 |
| **Complexity** | M |

| Field | Value |
|-------|-------|
| **ID** | FT-012 |
| **Name** | Provider account connection (OAuth) |
| **Description** | Users connect Spotify and YouTube Music accounts to enable tailored link-based recommendations. |
| **User Roles** | UR-005 |
| **Linked Requirements** | BR-001 |
| **Dependencies** | INT-001, INT-002 |
| **Complexity** | L |

| Field | Value |
|-------|-------|
| **ID** | FT-013 |
| **Name** | Content safety rules + supportive resources |
| **Description** | Admin-configured safety rules constrain content; the app displays supportive messaging with resource links in sensitive cases. |
| **User Roles** | UR-004, UR-005, UR-006 |
| **Linked Requirements** | BR-005 |
| **Dependencies** | FT-003, FT-011 |
| **Complexity** | M |

### 5.4 Non-Functional Requirements (NFR)

| ID | Requirement | Specification | Notes |
|----|-------------|--------------|-------|
| NFR-001 | Recommendation response time | Results should appear within a few seconds | Aligns to MoM NFR and swipe UX |
| NFR-002 | Accessibility | WCAG-level accessibility | Applies to mobile and admin web |
| NFR-003 | Minimum OS | iOS 14+, Android 8+ | MVP constraint |
| NFR-004 | Uptime | 99.5% | Applies to backend services |
| NFR-005 | Data security | Mood history treated as sensitive; secure storage and transport | Encryption in transit required; at-rest best practice |
| NFR-006 | Calm UX | Dark mode and minimal motion supported | Accessibility + brand UX |

## 6. Integration Map

| ID | Integration | Type | Direction | Protocol | Auth | Complexity |
|----|-------------|------|-----------|----------|------|------------|
| INT-001 | Spotify API | Content provider | Outbound | API/SDK | OAuth | L |
| INT-002 | YouTube Music API | Content provider | Outbound | API/SDK | OAuth | L |
| INT-003 | Email OTP service | Messaging | Outbound | API | API key / vendor auth | M |

**Fallback expectations (initial):**
- If Spotify/YTM are unavailable, the app should still function for Activities recommendations and show a clear error state for Music recommendations.  
  `[ASSUMPTION: Partial degradation is acceptable — confirm expected fallback behavior]`

## 7. Risk Register

| ID | Risk Description | Category | Likelihood | Impact | Severity | Mitigation | Owner |
|----|------------------|----------|------------|--------|----------|------------|-------|
| RSK-001 | Third-party API limitations/instability (Spotify/YTM) delay MVP or degrade experience (INT-001, INT-002; impacts FT-004, FT-012) | External | M | H | High | Prototype OAuth + key endpoints early; define fallback states; monitor quotas | UR-001 (Ana) |
| RSK-002 | Sensitive mood handling perceived as medical advice (impacts FT-013) | Product/Legal | M | H | High | Clear disclaimers; resources links; avoid diagnostic language | UR-001 (Ana), UR-003 (Mr Tom) |
| RSK-003 | Accessibility requirements not met (WCAG) (impacts FT-005, Admin dashboard) | Quality | M | M | Medium | Accessibility acceptance checklist; testing with screen readers; reduced motion | UR-001 (Ana) |
| RSK-004 | Shared team availability reduces throughput vs 6-month plan (impacts FT-001 through FT-013) | People/Timeline | M | M | Medium | Confirm allocations per sprint; protect critical path; buffer | UR-001 (Ana) |

## 8. Scope Boundary Statement

### 8.1 In Scope (MVP)
- FT-001 Mood input (preset + free text)
- FT-002 Authentication (guest + login with Email OTP + Password)
- FT-003 Admin auth with MFA
- FT-004 Recommendation generation (Music + Activities)
- FT-005 Recommendation display (cards + list/grid)
- FT-006 Like/Skip
- FT-007 Helpful/Not helpful
- FT-008 Refresh
- FT-009 Bookmarks / saved collection
- FT-010 Mood + recommendation history
- FT-011 Curated activities management (admin)
- FT-012 Provider account connection (OAuth)
- FT-013 Content safety rules + supportive resources

### 8.2 In Scope (Post-Launch)
- Maps integration (location optional with consent)

### 8.3 Explicitly Out of Scope
- Therapy, diagnosis, or clinical claims and features.
- Editing/creating Spotify/YTM playlists from the app (MVP uses in-app bookmarks only).

## 9. Mandays Estimation Matrix

### 9.1 Declared Budget & Team

| Item | Value |
|------|-------|
| Budget (effort) | ~120 mandays |
| Budget (cost) | ~IDR 200,000,000 |
| Target timeline | ~6 months from 2026-03-17 (flexible) |

**Team availability (per-person allocation):**
- Mobile Dev #1: 50%
- Mobile Dev #2: 50%
- Backend Dev (API + Admin): 60%
- QA: 40%
- Designer: 40%
- DevOps: 30%
- PM: 60%

`[ASSUMPTION: 1 manday = 1 person-day (≈8 hours); monthly capacity ≈ 20 workdays/person]`

### 9.2 MVP Effort Breakdown (fits 120 mandays)

This breakdown allocates the MVP scope into a **120-manday** plan to match the declared budget. It is intended as a planning baseline; individual sprint estimates may vary after technical spikes.

| ID | Feature / Component | Total Mandays |
|----|----------------------|--------------:|
| FT-001 | Mood input (preset + free text) | 6 |
| FT-002 | Auth (guest + Email OTP + Password) | 14 |
| FT-003 | Admin auth with MFA | 5 |
| FT-004 | Recommendation generation (music + activities) | 14 |
| FT-005 | Recommendation UI (cards + list/grid) | 10 |
| FT-006 | Like / Skip | 4 |
| FT-007 | Helpful / Not helpful | 3 |
| FT-008 | Refresh | 3 |
| FT-009 | Bookmarks / saved collection | 6 |
| FT-010 | Mood + recommendation history | 8 |
| FT-011 | Admin: curated activities management | 10 |
| FT-012 | Provider account connection (OAuth) | 12 |
| FT-013 | Content safety + supportive resources | 6 |
| — | Core backend platform (DB schema, API foundation, authz, logging) | 8 |
| — | DevOps (AWS envs, CI/CD, monitoring baseline) | 6 |
| — | QA & UAT support (test cycles, regression, release verification) | 6 |
| — | Design support (handoff, iterations, accessibility review) | 5 |
| — | PM / coordination overhead | 4 |
| **—** | **TOTAL** | **120** |

**Notes:**
- The above assumes “Save” remains **in-app bookmarks** only (no provider playlist writes).
- A technical spike is recommended in Sprint 1 for **INT-001/INT-002 OAuth + key endpoints** to de-risk FT-012 and FT-004.

### 9.3 Effort Estimate Note

This document captures the confirmed feature scope and team allocations. Feature-level mandays are provided as a baseline plan; a sprint-level estimate should still be produced during technical planning once the integration approach is validated (e.g., exact mood taxonomy, exact provider endpoints, OTP vendor, database design).

## 10. Open Questions & Gaps Log

No blocking gaps remain from the discovery session.

## 11. Confidence Score Card

| Dimension | Score | Status | Notes |
|-----------|-------|--------|-------|
| Business Clarity | 85% | ✅ | KPIs stated; goal is clear |
| User Definition | 80% | ✅ | Audience + MAU targets + regions defined |
| Scope Completeness | 80% | ⚠️ | Mood taxonomy and mapping rules pending finalization |
| Design Readiness | 75% | ✅ | Owner confirmed; key UX constraints confirmed |
| Integration Coverage | 75% | ⚠️ | Provider capabilities/quotas need early validation |
| Security & Compliance | 80% | ✅ | Sensitive data handling and Admin MFA confirmed |
| Technical Feasibility | 75% | ⚠️ | Requires early spike on OAuth + provider endpoints |
| Budget Realism | 65% | ⚠️ | Shared allocations may reduce throughput; estimate refinement needed |
| Post-Launch Planning | 70% | ✅ | Owner and uptime target confirmed |
| **Overall** | **76%** | ⚠️ | Ready to proceed with early technical validation |

## 12. Interview Coverage Checklist

| # | Block | Status | Confidence | Asked | Answered | Threshold | Key Gaps |
|---|-------|--------|-----------|-------|----------|-----------|----------|
| 1 | Vision & Business Goal | ✅ | 85% | 4/4 | 4/4 | 80% | None |
| 2 | Users & Usage Patterns | ✅ | 80% | 6/6 | 6/6 | 75% | None |
| 3 | Features & Scope | ✅ | 80% | 8/8 | 8/8 | 90% | Mood taxonomy/mapping specifics pending |
| 4 | Design & UX | ✅ | 80% | 4/4 | 4/4 | 70% | None |
| 5 | Integrations & Data | ✅ | 80% | 5/5 | 5/5 | 85% | Provider specifics (capabilities/quotas) |
| 6 | Security & Compliance | ✅ | 85% | 5/5 | 5/5 | 80% | None |
| 7 | Technology & Architecture | ✅ | 80% | 4/4 | 4/4 | 75% | None |
| 8 | Team, Budget & Timeline | ✅ | 75% | 3/3 | 3/3 | 85% | Sprint capacity / throughput math to refine |
| 9 | Launch & Post-Launch | ✅ | 80% | 4/4 | 4/4 | 65% | None |

**Blocks fully covered (✅):** 9 of 9  
**Blocks partially covered (⚠️):** 0 of 9  
**Blocks not covered (❌):** 0 of 9  

