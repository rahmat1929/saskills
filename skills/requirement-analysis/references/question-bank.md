# Question Bank — All 9 Blocks

> This is the master question list. Questions are organized into tiers:
> - **Tier 1 (Core):** Always ask. These are the opening questions per block.
> - **Tier 2 (Adaptive):** Ask based on answers to Tier 1 — selection logic in interview-flow.md.
> - **Tier 3 (Deep Dive):** Ask when the project's complexity warrants it or when
>   Tier 1/2 answers are vague.
>
> Never ask all questions at once. Follow the progressive flow in interview-flow.md.
> Never skip a question because the answer seems obvious — obvious answers still need
> to be stated explicitly.

---

## Block 1 — Vision & Business Goal

**Tier 1 — Always ask first:**
1. What business problem does this system solve? What is failing or missing today?
2. What happens if this project is NOT built? What is the cost of inaction?
3. What does success look like in 6 months? Give me measurable outcomes.

**Tier 2 — Based on Tier 1 answers:**
4. Is this replacing a manual process, an existing system, or creating something new?
5. Is the go-live deadline fixed (contractual, regulatory) or flexible?
6. Is there a defined budget ceiling, or is it to be determined?
7. Who is the business owner — the person with final sign-off authority?

**Tier 3 — When deeper context is needed:**
8. Are there other internal projects that overlap? Any risk of duplication?
9. What triggered this project now — why not 6 months ago or 6 months from now?

**Follow-up probes (when answers are vague):**
- "You said improve efficiency — by how much? What's the current baseline?"
- "You said stakeholders want this — which stakeholders specifically?"
- "You said Q3 deadline — is that a hard commitment or a target?"

---

## Block 2 — Users & Usage Patterns

**Tier 1 — Always ask first:**
1. List every type of user who will interact with this system. Include minor roles.
2. For each role: what do they need to SEE, DO, and APPROVE?
3. How many total users at launch? At 12 months?

**Tier 2 — Based on Tier 1 answers:**
4. What is the expected peak concurrent users? When does peak traffic occur?
5. Are users internal (staff), external (customers/public), or both?
6. What is the technical literacy level of the primary users?
7. What devices do users primarily use? Desktop, mobile, tablet, or a mix?

**Tier 3 — When relevant:**
8. What operating systems and browsers need to be supported?
9. Is multilingual support required? Which languages?
10. Are there users with accessibility needs requiring WCAG compliance?
11. Are there different feature sets per user segment?

**Follow-up probes:**
- "You said managers need to approve — approve what? What triggers it? What if rejected?"
- "You said mobile — iOS only, Android only, or both?"
- "You said 500 users — registered users or active daily users?"

---

## Block 3 — Features & Scope

**Tier 1 — Always ask first:**
1. Brain dump — list every feature you think this system needs. No filtering.
2. Prioritize: for each feature, is it MVP (must-have at launch) or post-launch?
3. What are the explicit NON-goals? What will this system deliberately never do?

**Tier 2 — After receiving feature list:**
4. Which feature, if not delivered, would make the whole project a failure?
5. Is there a reference system or competitor you admire? Which specific flows?
6. Are there features that sound simple but might be more complex than they appear?

**Tier 3 — Probe based on feature types declared:**
7. Notification requirements: email, SMS, push, in-app — which are needed?
8. Reporting and export: what data, what format, who consumes it?
9. Does any part of the system need to work offline?
10. Search requirements: basic filter, full-text, or advanced with facets?
11. Bulk operations needed? (bulk import, export, update)
12. Versioning or audit history on any data?
13. Scheduled jobs or background automation?

**Follow-up probes:**
- "You said dashboard — what data? Who sees it? How often refreshed? Filterable?"
- "You said search — filter bar or Elasticsearch-level full-text?"
- "You listed [N] features for MVP — let's reality-check against your budget later."

---

## Block 4 — Design & UX

**Tier 1 — Always ask first:**
1. Who is responsible for UX/UI design — dev team, separate designer, or client-provided?
2. Are there existing mockups, wireframes, or a design system?

**Tier 2 — Based on design ownership:**
3. If client-provided: in what format, and what is the delivery timeline?
4. Is there an existing brand guideline or component library to follow?
5. What are the 3–5 most critical user journeys? Walk me through each step.

**Tier 3 — When UI complexity warrants it:**
6. Complex UI interactions required? (drag-and-drop, real-time updates, rich text,
   data visualization)
7. Acceptable page load time for primary screens?
8. Dark mode, RTL languages, or theme customization?
9. Animation or micro-interaction requirements?
10. Design handoff process needed? (e.g., Figma to dev)

**Follow-up probes:**
- "Client provides design — what happens to the timeline if design is delayed?"
- "You said charts — what type? Real-time or static? Exportable?"
- "You said mobile-first — is desktop secondary or equally important?"

---

## Block 5 — Integrations & Data

**Tier 1 — Always ask first:**
1. Does this system connect to any existing internal systems? (ERP, CRM, HRIS, legacy DB)
2. What third-party services are needed? (payment, maps, email, SMS, push, storage,
   analytics, identity/SSO)

**Before asking Tier 2, cross-check against Block 3 features.** If features imply
integrations not mentioned, surface them now.

**Tier 2 — Based on integration landscape:**
3. Does this system expose an API for external consumption? Public or partner-only?
4. Where does the primary data come from? Who owns it?
5. Is there a data migration requirement? How much historical data?
6. File and media handling: types, max size, storage location?

**Tier 3 — When data complexity warrants it:**
7. Real-time data requirements? (live updates, websocket, SSE)
8. Estimated data volume: rows per major table, total GB, growth rate?
9. Data synchronization needs between systems?
10. Webhook requirements — inbound or outbound?

**Follow-up probes:**
- "You mentioned payment — which gateway? Recurring or one-time?"
- "Connect to existing system — via DB access, REST API, or file exchange?"
- "You said real-time — define acceptable latency."

---

## Block 6 — Security & Compliance

**Tier 1 — Always ask first:**
1. Does the system handle PII? (name, email, phone, ID number, address)
2. Does it handle financial data? (bank accounts, transactions, card numbers)
3. What authentication method is required? (username/password, SSO, OAuth2, MFA)

**Cross-check Tier 1 answers against Blocks 3 and 5.** Push back if features
imply sensitive data that the user just denied handling.

**Tier 2 — Based on data sensitivity:**
4. What regulatory or compliance framework applies? (PDPA, GDPR, HIPAA, PCI-DSS, OJK)
5. What authorization model? (RBAC, ABAC, row-level security)
6. Audit trail requirement — who did what, when?
7. Data retention policy: how long kept? Archived vs deleted?

**Tier 3 — When security depth warrants it:**
8. Penetration test or security audit required before go-live?
9. Password policies, session timeout, IP whitelisting requirements?
10. Data encrypted at rest, in transit, or both?
11. Does it handle health or other sensitive personal data?

**Follow-up probes:**
- "You said no compliance, but users enter KTP numbers — that triggers PDPA."
- "You said RBAC — how many roles? Fixed or admin-configurable?"
- "MFA — for all users or just admin roles?"

---

## Block 7 — Technology & Architecture

**Tier 1 — Always ask first:**
1. Is there a mandatory tech stack, or is it open for recommendation?
2. Which layers are in scope: web frontend, backend API, mobile (iOS/Android),
   admin panel, background workers?

**Tier 2 — Based on tech landscape:**
3. Greenfield or extending an existing codebase?
4. Hosting preference: AWS, GCP, Azure, on-premise, managed hosting?
5. Deployment model: containerized (Docker/K8s), serverless, traditional VPS?
6. Monolith or microservices? If microservices, DevOps maturity to support it?

**Cross-check against Block 3:** Confirm stack supports any real-time, offline,
or heavy-computation features declared.

**Tier 3 — When architecture depth warrants it:**
7. CI/CD pipeline required? Who manages deployments?
8. Performance targets: API response time, requests/second at peak?
9. Caching requirements: CDN, Redis, in-memory?
10. Database preference: relational, NoSQL, or mixed?
11. Technology constraints from client side? (firewall, no cloud, on-prem DB)

**Follow-up probes:**
- "Team knows Laravel — must be Laravel, or open to other stacks if justified?"
- "You said Kubernetes — does the team have DevOps to manage a cluster?"
- "On-premise — who manages the server? Is there an IT/ops team?"

---

## Block 8 — Team, Budget & Timeline

**Tier 1 — Always ask first:**
1. What is the total mandays budget? Fixed (contractual) or estimate?
2. [PRESENT recommended team composition first, then ask:] This is what the project
   needs. What does your ACTUAL team look like — roles, seniority, availability?

**After Tier 1, immediately do THREE things:**
- Compare recommended team vs actual team → surface gaps
- Run refined mandays reality check → surface budget gap
- Present both to user → force resolution before continuing

**Tier 2 — Based on team and budget:**
3. For each role gap: how do you want to address it — hire, outsource, or adjust scope?
4. Is there a dedicated QA, or does testing fall to developers?
5. Are team members full-time on this project or split across others?
6. What happens when scope and mandays don't align — cut scope, increase budget,
   or extend timeline?
7. Is there a contingency buffer in the estimate?
8. Are there roles you haven't mentioned that you're planning to bring in?
   (Especially: PM, BA/SA, DevOps, Designer)

**Tier 3 — When project management depth warrants it:**
9. Seniority level per role? (junior, mid, senior, lead)
10. Hard milestone deadlines within the project? (sprint demos, partial go-lives)
11. Parallel workstreams allowed or strictly sequential?
12. Team methodology — Scrum, Kanban, waterfall, hybrid?
13. Who is the day-to-day technical decision-maker on the team?
14. Is there a dedicated UX/UI designer, or does the dev team handle it?
15. For shared/part-time team members: what percentage of their time is on this project?

**Follow-up probes:**
- "30 mandays total — that includes design, dev, QA, and deployment, correct?"
- "2 junior devs — have they worked with the chosen stack before?"
- "PM is shared — what percentage of time is dedicated to this project?"
- "No QA engineer — who writes test cases? Who does UAT?"
- "No DevOps — who handles deployments, server setup, monitoring?"
- "You said the team can handle design — have they done UI/UX before, or just
  frontend implementation?"

---

## Block 9 — Launch & Post-Launch

**Tier 1 — Always ask first:**
1. Who maintains and operates the system after go-live?
2. What is the rollout strategy? (big bang, phased, pilot group first)

**Tier 2 — Based on launch context:**
3. How will UAT be conducted? Who performs it? What defines "accepted"?
4. End-user training required? What format?
5. What is the incident response plan? First contact when something breaks?

**Tier 3 — When post-launch depth warrants it:**
6. Uptime/SLA requirements? (99.9%, business hours only, best-effort)
7. Technical documentation required? (API docs, runbook, deployment guide)
8. Hypercare period post-launch? (dedicated support window with faster SLA)
9. Planned major features in first 3 months post-launch that should influence
   architecture now?
10. Bug reporting and tracking — ticketing system in place?

**Follow-up probes:**
- "Client IT maintains — do they have codebase access? Familiar with the stack?"
- "No training needed — confident the UI is intuitive for ALL user roles?"
- "Phased rollout — what defines phase 1 vs 2? Success metric to advance?"
