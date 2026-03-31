# Interview Flow — Progressive Questioning Logic

> Read this file at the start of Phase 2. It governs HOW you ask questions —
> not just WHAT you ask (that's in question-bank.md).

---

## Table of Contents

1. [Core Principle: Progressive Disclosure](#core-principle)
2. [Path A: Document-First Flow](#path-a-document-first)
3. [Path B: Interactive Interview Flow](#path-b-interactive-interview)
4. [Adaptive Question Selection](#adaptive-question-selection)
5. [Mirror-Back Protocol](#mirror-back-protocol)
6. [Answer Quality Gates](#answer-quality-gates)
7. [Block Transition Rules](#block-transition-rules)
8. [Session Pacing](#session-pacing)

---

## Core Principle

**Never dump all questions at once.** Ask 2–4 questions per turn. Use the answers
to decide which questions come next. Early answers reveal project shape — use that
shape to skip irrelevant questions and inject important ones.

The interview should feel like a conversation with an experienced consultant, not
a form with 90 fields.

### Question Formatting Rule

**ALWAYS number your questions.** When asking questions, use numbered format so the
user can easily reference which question they're answering:

✅ **Correct — numbered:**
> **Block 7 — Technology & Architecture:**
>
> 1. Is there a mandatory tech stack, or is it open for recommendation?
> 2. Which layers are in scope: web frontend, backend API, mobile (iOS/Android),
>    admin panel, background workers?
> 3. Hosting preference: AWS, GCP, Azure, on-premise, managed hosting?

❌ **Wrong — bullet points:**
> **Block 7 — Technology & Architecture:**
>
> - Is there a mandatory tech stack, or is it open for recommendation?
> - Which layers are in scope?
> - Hosting preference?

**Why this matters:** When users answer "for question 2, we need web and mobile",
it's unambiguous. With bullet points, they have to quote the question text.

This rule applies to ALL questions across ALL blocks — Tier 1, Tier 2, Tier 3,
follow-ups, and confirmation questions. Always numbered, never bullet points.

---

## Path A: Document & Reference-First Flow

When the user provides source material — formal documents (PRD, brief, meeting notes,
feature list, RFP, proposal) **or** informal references (competitor links, screenshots,
sketches, architectural ideas, app store links, Figma files) — follow this flow:

⛔ **MANDATORY MULTI-TURN RULE:** Path A requires AT MINIMUM these conversation turns:
1. **Turn 1 (Claude):** Present block-by-block extraction summary + ask for confirmation
2. **Turn 2 (User):** Confirms/corrects the extraction
3. **Turns 3–N (Claude ↔ User):** Interview through all 9 blocks (2–4 questions at a
   time, user responds, follow-ups asked). Blocks well-covered by the document get
   confirmation + 1–3 follow-ups. Blocks NOT covered get the full Path B interview.
4. **Turn N+1 (Claude):** Present full summary (Phase 3b) + ask for final approval
5. **Turn N+2 (User):** Approves
6. **Turn N+3 (Claude):** Generate document

**If your very first response to a user who provided a document contains a generated
.md file or output document → you are doing it WRONG. Stop and redo from Step 1.**

### Step 1: Categorize the Input

Separate everything the user has shared into two buckets:

**Specification material** — contains facts about THIS project:
- PRDs, briefs, feature lists, meeting notes, proposals, RFPs
- Process: Extract facts into the 9-block structure (Step 2)

**Reference material** — shows what the user wants to learn from or emulate:
- Competitor apps, screenshots, sketches, links, Figma files, architectural concepts
- Process: Analyze for patterns (Step 2a)

### Step 2: Extract from Specification Material

Read the documents. For each of the 9 blocks, extract every fact that can be mapped:

```
For each block:
  - What is explicitly stated? → mark as CONFIRMED
  - What is implied but not stated? → mark as IMPLIED (needs confirmation)
  - What is absent? → mark as GAP (needs asking)
```

### Step 2a: Analyze Reference Material

For each reference the user shares (competitor app, screenshot, sketch, link, idea):

1. **Identify what they admire.** Don't assume they want to copy everything. Ask:
   > "You shared [reference]. What specifically do you want to take from this —
   > the overall flow, the visual style, specific features, or something else?"

2. **Extract relevant patterns.** For each reference, note:
   - Which user journeys or flows are demonstrated
   - Which features are visible
   - What design patterns or UI conventions are used
   - What scale/complexity the reference implies
   - What integrations the reference likely uses (payment, maps, real-time, etc.)

3. **Identify divergences.** Ask:
   > "What should be DIFFERENT from [reference]? Where does your vision diverge?"

4. **Map to blocks.** For each pattern extracted from references:
   - Features → Block 3 (Scope)
   - Visual style / flows → Block 4 (Design)
   - Integrations implied → Block 5 (Integrations)
   - Scale implied → Block 2 (Users) and Block 7 (Technology)

5. **Flag "iceberg" references.** When a user says "like [large platform]", surface
   the hidden complexity:
   > "The part of [reference] you're pointing at looks simple on the surface, but
   > behind it there's [hidden complexity]. Are you aware of this, and is it in scope?"

**Common iceberg examples:**

| Reference says... | Hidden complexity |
|------------------|-------------------|
| "Like Gojek's booking flow" | Real-time driver matching, location tracking, dynamic pricing, ETA calculation, surge pricing |
| "Like Tokopedia's product page" | Product variants, seller ratings, reviews with images, Q&A, inventory sync, wishlists |
| "Like Google Docs collaboration" | Operational Transform or CRDT, conflict resolution, presence indicators, version history |
| "Like Instagram stories" | Ephemeral content lifecycle, media processing pipeline, viewer tracking, auto-expiry |
| "Notion-like editor" | Block-based content model, drag-reorder, embeds, real-time collab, slash commands |

### Step 3: Present Extraction Summary

Show the user a block-by-block summary of what you found from BOTH specification
and reference material. This is the most important step — the user must confirm
before you proceed.

> "I've read through your materials. Here's what I extracted and what I still need
> to confirm with you:
>
> **Block 1 — Vision & Business Goal:**
> ✅ Confirmed: [facts explicitly stated in the document]
> ❓ Needs your confirmation: [things I inferred but aren't stated clearly]
> ❌ Missing: [questions the document doesn't answer]
>
> **Block 2 — Users & Usage Patterns:**
> ✅ Confirmed: [facts]
> ❓ Needs your confirmation: [inferences]
> ❌ Missing: [gaps]
>
> [repeat for ALL 9 blocks — even blocks where the document seems complete]
>
> **From your references:**
> - From [reference 1]: [patterns extracted, implications for scope/tech]
> - From [reference 2]: [patterns extracted, implications]
> - Key divergences you noted: [list]
> - Hidden complexity flagged: [list]
>
> Let me walk through each block to confirm what I extracted and ask what the
> document didn't cover. Ready?"

**Wait for user confirmation before proceeding to Step 4.**

### Step 4: Per-Block Confirmation Interview

**A document accelerates the interview — it does not replace it.** For every block,
even ones where the document seems comprehensive, follow this sequence:

**For blocks with strong document coverage:**
1. Present what you extracted: "From your document, I understood [X]. Is that accurate?"
2. Present inferences: "I also inferred [Y]. Correct, or should I adjust?"
3. Ask 1–3 deeper follow-up questions that the document didn't address.
   Use Tier 2 or Tier 3 questions from `question-bank.md` that probe nuance.
4. Mirror back the combined understanding (document + answers).

**For blocks with partial coverage:**
1. Present what you extracted and get confirmation.
2. Ask the missing Tier 1 questions first, then Tier 2 based on answers.
3. Mirror back.

**For blocks with no coverage:**
1. State clearly: "The document didn't cover [block topic] at all."
2. Run the full Path B interview flow for this block.
3. Mirror back.

**Example — Block 3 (Scope) with good document coverage:**
> "Your document lists 8 features for MVP. Here's what I extracted:
>
> 1. User authentication (social login + email)
> 2. Product catalog with search
> 3. Shopping cart & checkout
> 4. Order management
> 5. Seller dashboard
> 6. Admin panel
> 7. Push notifications
> 8. Reporting module
>
> Is this list accurate and complete?
>
> Even with this list, I have a few questions the document didn't cover:
> - What are the explicit NON-goals? What will this system deliberately never do?
> - Which single feature, if not delivered, would make the whole project a failure?
> - Are there any features that sound simple here but might be more complex than
>   they appear?"

**Why this matters:** Documents often reflect one person's understanding at one point
in time. By confirming every block, you catch outdated information, missing context,
and unstated assumptions that would otherwise become problems during development.

### Step 5: Confirm Implied Items

After running through all blocks, present any remaining implied items as a batch:

> "I made [N] inferences from your documents that I want to confirm:
>
> 1. I inferred [X] from [source]. Correct?
> 2. I inferred [Y] from [source]. Correct?
> 3. [...]
>
> Which of these need correction?"

Only proceed to Phase 3 after all confirmations are received.

### Handling References Shared Mid-Session

Users may share references at any point during the interview, not just at the
start. When this happens:

1. Pause the current block momentarily.
2. Apply the reference analysis protocol (Step 2a) to the new reference.
3. Note any impacts on blocks already completed:
   > "This reference suggests [implication] which affects what we discussed in
   > Block [N]. I'll note that and we can revisit if needed."
4. Resume the current block.

---

## Path B: Interactive Interview Flow

When no document exists, walk through the 9 blocks using progressive questioning.

### Block 1 — Vision & Business Goal

**Opening question set (always ask these first):**
1. What are you trying to build, and what problem does it solve?
2. What happens if this project is NOT built?

**Based on the answer, select the next questions:**

| If the user mentions... | Follow up with... |
|------------------------|-------------------|
| Replacing an existing system | What's wrong with the current system? What must the new system preserve? |
| Replacing a manual process | Walk me through the current manual workflow step by step |
| New product / new idea | Who validated the need? Is there market research or user feedback? |
| Regulatory or compliance driver | Which regulation? What's the compliance deadline? |
| Revenue opportunity | What's the revenue model? What are the unit economics? |

**Then ask (if not yet covered):**
3. What does success look like in 6 months? Give me measurable outcomes.
4. Is the go-live deadline fixed or flexible?
5. Is there a defined budget ceiling?

**Mirror back, then proceed to Block 2.**

### Block 2 — Users & Usage Patterns

**Opening questions:**
1. List every type of user who will interact with this system — include minor roles.
2. For each role: what do they need to SEE, DO, and APPROVE?

**Adaptive follow-ups based on answer:**

| If user lists... | Follow up with... |
|-----------------|-------------------|
| 3+ roles | Is there a role hierarchy? Can admins create custom roles? |
| "Customers" or external users | How many at launch? At 12 months? Peak concurrent? |
| Internal-only users | What's the team size? Will it grow? |
| Both internal and external | Which group is primary? Different feature sets per group? |

**Then ask (if not yet covered):**
3. What devices do users primarily use?
4. What is their technical literacy level?
5. Multilingual or accessibility requirements?

**Mirror back, then proceed to Block 3.**

### Block 3 — Features & Scope

**This is the highest-stakes block (90% confidence required). Take extra time here.**

**Opening questions:**
1. Do a brain dump — list every feature you think this system needs. No filtering yet.
2. Now prioritize: which are MVP (must-have at launch) vs post-launch?
3. What will this system deliberately NEVER do?

**After receiving the feature list, do NOT ask all remaining questions. Instead:**

**Step 1: Scan the feature list for complexity signals.** For each feature, silently
assess:
- Does this imply an integration not yet discussed? (flag for Block 5)
- Does this involve real-time behavior? (flag for Block 7)
- Does this involve user-generated content or file uploads? (flag for Block 5)
- Is the user using a "simple" label on something that's actually complex?

**Step 2: Probe the top 3 most complex features individually:**
> "Let's dig into [feature]. What exactly should it do? Walk me through what a user
> experiences step by step."

**Step 3: Then ask (if relevant to this project):**
- Notification requirements: email, SMS, push, in-app?
- Reporting and export needs?
- Search requirements: basic filter or full-text?
- Bulk operations needed?
- Audit trail or versioning on any data?

**Mirror back the full scope with MVP vs post-launch separation. Get explicit
confirmation.**

**After confirming scope, present a preliminary mandays estimate immediately:**

> "Based on the features you've described, here's a rough estimate before we dig
> into integrations, tech stack, and team:
>
> | Feature | Complexity | Estimated Floor |
> |---------|-----------|----------------|
> | [feature 1] | Medium | ~7 mandays |
> | [feature 2] | Complex | ~12 mandays |
> | ... | ... | ... |
> | **Subtotal (features only)** | | **~[N] mandays** |
>
> This is features-only — it doesn't include integrations, QA, DevOps, mobile
> multiplier, or buffer yet. Those will add 40–80% on top. So the ballpark is
> roughly **[N × 1.5] to [N × 1.8] total mandays**.
>
> Does this range feel aligned with your budget expectations, or should we talk
> about scope adjustments now before going deeper?"

**Why estimate here:** Surfacing the number early prevents the user from committing
5 more blocks of mental energy only to discover at Block 8 that the scope is 3×
their budget. If there's a massive gap, negotiate scope NOW — don't wait.

**If the user's budget is dramatically lower (>50% gap):**
- Stop and negotiate scope immediately
- Use the MoSCoW labels from Block 3 to identify what moves to post-launch
- Re-confirm the adjusted MVP scope before proceeding to Block 4

**If the gap is moderate (20–40%):**
- Note it, continue — integrations and tech decisions may change the picture
- Flag that you'll revisit at Block 8 with a refined number

**If aligned or close (<20% gap):**
- Note it positively and continue to Block 4

### Block 4 — Design & UX

**Opening questions:**
1. Who is responsible for UX/UI design — dev team, separate designer, or client-provided?
2. Are there existing mockups, wireframes, or a design system?

**Adaptive routing:**

| If... | Then ask... |
|-------|------------|
| Client provides design | In what format? What is the delivery timeline? What if it's delayed? |
| Dev team handles design | Is there a design system/brand guide? What's the quality expectation? |
| Separate designer | Are they available now? What's their delivery cadence? |
| No design exists yet | What reference apps/sites capture the look and feel you want? |

**Then ask about the top 3–5 user journeys identified in Block 3:**
> "Walk me through [journey] step by step. What does the user see at each point?
> What can go wrong?"

**Mirror back, then proceed to Block 5.**

### Block 5 — Integrations & Data

**Opening questions:**
1. Does this system connect to any existing internal systems?
2. What third-party services are needed?

**Before asking, review your flags from Block 3.** If features implied integrations
the user hasn't mentioned, surface them now:
> "In Block 3, you mentioned [feature]. That typically requires [integration]. Is
> that in scope?"

**Adaptive follow-ups:**

| If user mentions... | Then ask... |
|--------------------|------------|
| Payment gateway | Which provider? Recurring billing? Refund flow? |
| Data migration | How much data? What format? One-time or parallel run? |
| File uploads | What types? Max size? Storage location? Processing needed? |
| Real-time data | What is the acceptable latency? Fallback if connection drops? |
| API exposure | Public or partner-only? Rate limiting? Authentication method? |

**Also ask (if not covered):**
3. Estimated data volume: rows per major table, storage in GB, growth rate?
4. Any webhook requirements — inbound or outbound?

**Mirror back, then proceed to Block 6.**

### Block 6 — Security & Compliance

**Opening questions:**
1. Does the system handle PII, financial data, or health data?
2. What authentication and authorization model is needed?

**This block has a critical cross-check:** Compare the answer to question 1 against
what was revealed in Blocks 3 and 5. If the user says "no sensitive data" but
Block 3 includes features that collect KTP numbers, bank details, or health records,
push back:
> "In Block 3 you mentioned [feature] which handles [data type]. That qualifies as
> [PII/financial/health] data and has compliance implications. Let's address that."

**Adaptive follow-ups based on data sensitivity:**

| Data type | Follow up with... |
|-----------|-------------------|
| PII (names, IDs, contact info) | Which data protection regulation applies? |
| Financial data | PCI-DSS awareness? Transaction encryption? |
| Health data | HIPAA or local equivalent? Data isolation requirements? |
| No sensitive data confirmed | Audit trail still needed? Session management rules? |

**Mirror back, then proceed to Block 7.**

### Block 7 — Technology & Architecture

**Opening questions:**
1. Is there a mandatory tech stack, or is it open for recommendation?
2. Which layers are in scope: web frontend, backend API, mobile, admin panel?

**Adaptive follow-ups:**

| If user mentions... | Then ask... |
|--------------------|------------|
| Mobile app | iOS, Android, or both? Native or cross-platform? |
| Microservices | Does the team have DevOps maturity for this? |
| Specific framework | Is the team experienced with it? |
| "Whatever you recommend" | What's the team most experienced with? Any constraints? |
| On-premise hosting | Who manages the server? Is there an IT team? |

**Cross-check against Block 3:** If real-time features were declared, confirm the
stack supports WebSocket or SSE.

**Mirror back, then proceed to Block 8.**

### Block 8 — Team, Budget & Timeline

**This block has THREE jobs, in this order:**
1. Present a recommended team composition based on scope
2. Compare against the user's actual team and surface gaps
3. Run the refined mandays reality check

**Step A — Present recommended team BEFORE asking about theirs:**

Based on everything gathered in Blocks 1–7, build a recommended team composition
and present it to the user. This flips the conversation from "what team do you have?"
to "here's what this project needs — does your team match?"

> "Based on what we've discussed, here's the team composition this project needs:
>
> **Recommended Team:**
>
> | Role | Why Needed | Seniority | Allocation | Mandays |
> |------|-----------|-----------|------------|---------|
> | Backend Developer | [N] API endpoints, [M] integrations, business logic | Senior | Full-time | [est] |
> | Frontend Developer | Web app with [complexity level] | Mid–Senior | Full-time | [est] |
> | Mobile Developer | [platforms] — [native/cross-platform] | Mid–Senior | Full-time | [est] |
> | QA Engineer | [N] integrations, [M] user roles, critical payment flow | Mid | Full-time | [est] |
> | DevOps Engineer | CI/CD, [hosting], monitoring setup | Mid–Senior | Part-time | [est] |
> | UI/UX Designer | [N] screens, [M] user journeys | Mid | Part-time | [est] |
> | Project Manager | Coordination across [N] stakeholders, [M] platforms | Mid–Senior | Part-time | [est] |
> | System/Business Analyst | Requirements refinement, UAT support | Mid–Senior | Part-time | [est] |
>
> Now — **what does your actual team look like?** Who do you have, and at what
> seniority and availability?"

**Use this role recommendation matrix:**

| Scope Signal (from Blocks 1–7) | Roles Needed |
|-------------------------------|-------------|
| Web frontend in scope | Frontend Developer |
| Backend API in scope | Backend Developer |
| Mobile app (any platform) | Mobile Developer |
| 3+ integrations OR payment/sensitive data | QA Engineer (dedicated) |
| Complex deployment, multiple envs, CI/CD | DevOps Engineer |
| 5+ screens, custom design, complex UX | UI/UX Designer |
| 3+ stakeholders, client-facing, multi-vendor | Project Manager |
| Complex business rules, multi-role system, compliance | System/Business Analyst |
| Data migration from legacy system | Data Engineer / DBA (part-time) |
| AI/ML features | ML Engineer / Data Scientist |
| 60+ total mandays | At least 1 Senior per discipline |
| 100+ total mandays | Technical Lead / Architect |
| Multi-vendor project | Integration Lead |

**Step B — Compare and surface gaps:**

After the user describes their actual team, compare it against the recommendation:

> "Comparing your team against what the project needs:
>
> | Role | Recommended | You Have | Gap |
> |------|-----------|----------|-----|
> | Backend Dev (Senior) | 1 | 1 ✅ | — |
> | Frontend Dev | 1 | 1 ✅ | — |
> | Mobile Dev | 1 | 0 ❌ | **Need to hire or outsource** |
> | QA Engineer | 1 | 0 ❌ | **Risk: no dedicated testing** |
> | DevOps | 0.5 (part-time) | 0 ⚠️ | **Who handles deployment?** |
> | Designer | 0.5 | Client-provided ⚠️ | **Design dependency risk** |
> | PM | 0.5 | 0.3 (shared) ⚠️ | **Coordination bottleneck risk** |
> | SA/BA | 0.5 | User ✅ | — |
>
> You have gaps in: Mobile Dev, QA, DevOps.
> How do you want to address these — hire, outsource, or adjust scope?"

**Do not accept "we'll figure it out later" for Critical roles.** If scope includes
mobile and there's no mobile dev, this must be resolved or the mobile scope gets
deferred.

**Step C — Refined mandays reality check:**

Now present the full progressive mandays build-up:

> "Here's how the mandays break down with everything we've discussed:
>
> **Progressive Estimate:**
>
> | Layer | Mandays | Notes |
> |-------|---------|-------|
> | Features (from Block 3) | [N] | [feature count] features at estimated complexity |
> | + Integrations (Block 5) | +[N] | [count] third-party services |
> | + Auth system (Block 6) | +[N] | [roles] roles, [auth method] |
> | + Mobile multiplier (Block 7) | +[N] | [platforms] at [native/cross-platform] |
> | + Admin panel (Block 7) | +[N] | [basic/advanced] |
> | + DevOps setup | +[N] | [hosting], CI/CD, staging |
> | = Development subtotal | **[N]** | |
> | + QA (22% of dev) | +[N] | |
> | + Design | +[N] | [in-scope/client-provided] |
> | + PM coordination (12% of total) | +[N] | |
> | + Buffer (15%) | +[N] | |
> | = **Grand Total** | **[N] mandays** | |
>
> Your stated budget: **[Y] mandays**
> Gap: **[Z] mandays ([%])**"

**Then force resolution if gap > 30%:**
- (A) Cut scope — which MVP features move to post-launch?
- (B) Increase budget — what is the ceiling?
- (C) Extend timeline — what is the latest go-live?
- (D) Adjust team — can you add resources to parallelize work?

**Do not proceed to Block 9 without a resolution.**

**Then ask remaining questions (if not covered):**
3. What happens when scope and budget don't align — which gives?
4. Hard milestone deadlines within the project?
5. Is there a contingency buffer?
6. Are team members full-time or split across projects?
7. Team methodology — Scrum, Kanban, waterfall?

**Mirror back, then proceed to Block 9.**

### Block 9 — Launch & Post-Launch

**Opening questions:**
1. Who maintains the system after go-live?
2. What's the rollout strategy — big bang, phased, or pilot?

**Adaptive follow-ups:**

| If... | Then ask... |
|-------|------------|
| No post-launch owner | This is a critical risk. Who will handle bugs? Security patches? |
| Client IT maintains | Do they have access to codebase? Familiar with the stack? |
| Vendor on retainer | What's the SLA? Response time commitment? |
| Phased rollout | What defines each phase? Success criteria to advance? |

**Then ask (if not covered):**
3. UAT plan: who performs it, how long, what defines "accepted"?
4. End-user training needed?
5. Planned features in first 3 months post-launch that affect architecture now?

**Mirror back. Session complete — proceed to Phase 3 (Validation).**

---

## Adaptive Question Selection

Not every question in the question bank applies to every project. Use this decision
logic to skip questions that are clearly irrelevant:

**Skip when:**
- Question asks about mobile and the project is web-only (confirmed in Block 7)
- Question asks about compliance framework and no sensitive data is handled (confirmed
  in Block 6)
- Question asks about data migration and the system is entirely greenfield (confirmed
  in Block 1)
- Question asks about multilingual and the user confirmed single-language (Block 2)

**Never skip when:**
- The answer "seems obvious" — obvious answers still need to be stated explicitly
- The user says "standard" or "normal" — always define what that means
- The question covers risk — even low-probability risks should be acknowledged

---

## Mirror-Back Protocol

After each block, reflect back before proceeding:

> "Here's what I understood about [block topic]:
> - [point 1]
> - [point 2]
> - [point 3]
>
> Is this accurate? Anything I misunderstood or missed?"

**Rules:**
- Only proceed after explicit user confirmation.
- If user says "close but..." — update and re-mirror.
- Never assume silence means confirmation. If the user doesn't respond to the
  mirror-back, ask again.
- Keep the mirror-back concise — summarize, don't repeat verbatim.

**Confirmation tracking:** After each block's mirror-back, record the confirmation
status internally:

```
Block [N] confirmation status:
  - Confirmed by user: YES / NO / PARTIAL
  - Items confirmed: [list]
  - Items user corrected: [list]
  - Items still unconfirmed: [list]
  - Items marked as GAP: [list]
```

This tracking feeds directly into Phase 3b (Full Summary & Confirmation Gate) and
Section 12 (Interview Coverage Checklist) in the output document.

**The confirmation status determines what goes into the document:**
- **Confirmed = FACT** → written as a definitive statement
- **Corrected = FACT** → use the corrected version, not the original
- **Unconfirmed = ASSUMPTION** → marked with `[ASSUMPTION: ...]` tag
- **GAP = GAP** → marked with `[GAP: ...]` tag with owner

**Never promote an unconfirmed item to a fact.** If the user didn't say "yes, that's
right" to a specific point, it remains an assumption in the document.

---

## Answer Quality Gates

Before accepting any answer, check:

### 1. Specificity Check
- ❌ "We need standard features" → "What does standard mean for your users?"
- ❌ "It should be scalable" → "Scalable to how many users? In what timeframe?"
- ❌ "Normal security" → "Do you handle personal data? Financial transactions?"

### 2. Numeric Sanity Check
- Flag: 5 mandays for 15 features
- Flag: 2-month deadline for mobile + web + admin panel
- Flag: 100k concurrent users on shared hosting

### 3. Buzzword Detection
When you hear these, always probe:
- "AI-powered" → what specifically should AI do? For which users?
- "Real-time" → real-time what? Acceptable latency? What if delayed?
- "Like [big app]" → which specific flows? Not the whole product
- "Blockchain" → why blockchain specifically? What problem does it solve here?
- "Simple" → simple is relative. Describe the simplest acceptable version.
- "Just a CRUD" → how many entities? What business rules? What validations?

### 4. Probe Limit & Gap Escalation

Maximum 3 follow-up probes per question. But after 3 rounds, do NOT silently mark
as GAP. Follow this escalation:

**Probe 1–3:** Ask the question, rephrase if needed, give examples of good answers.

**After 3 probes — Escalate, don't surrender:**
> "I've asked about [topic] a few times and we haven't been able to pin it down.
> This matters because [specific consequence — e.g., 'without knowing the auth
> model, we can't estimate the security work accurately'].
>
> Here's what I need — pick one:
> (A) [Give a specific answer now — suggest options if possible]
> (B) Tell me who on your team can answer this, and by when
> (C) Confirm this is an open question — I'll mark it as a gap that blocks
>     [specific feature/decision] until resolved"

**The user must explicitly choose A, B, or C.** Never mark a GAP on your own.

**If user chooses (A):** Accept the answer, confirm, continue.
**If user chooses (B):** Mark as GAP with the named owner and deadline.
**If user chooses (C):** Mark as GAP, state the consequence, assign priority:
- **Critical GAP:** Blocks a feature or architectural decision. Must resolve before dev.
- **High GAP:** Doesn't block immediately but will cause rework if wrong. Resolve in Sprint 1.
- **Medium GAP:** Nice to know. Can be resolved during development.

---

## Block Transition Rules

Before moving from Block N to Block N+1:

1. ✅ Mirror-back completed and confirmed
2. ✅ Block confidence meets or exceeds minimum threshold
3. ✅ No unaddressed flags from previous blocks that this block should have resolved
4. ✅ Any cross-block implications noted for future blocks
5. ✅ **Every question that was asked has either an answer or an explicit GAP**
   (no silently skipped questions)

If confidence is below threshold but the user can't provide more information:
- For each unanswered question, run the gap escalation (Probe Limit step above)
- The user must explicitly confirm each item as GAP with owner and priority
- Note the impact on document quality
- Proceed — but flag in the Coverage Checklist that this block is ⚠️ Partial

---

## Session Pacing

**Target session length:** 30–90 minutes depending on project complexity.

**Pacing signals to watch for:**
- If the user gives very detailed answers → they know their project well. Accelerate
  by asking more questions per turn (3–4 instead of 2).
- If the user gives vague answers → they're still forming their thinking. Slow down,
  ask 1–2 questions at a time, and provide examples of what good answers look like.
- If the user seems fatigued → acknowledge it. Offer to save progress and continue
  later. Summarize what's been covered and what remains.

**Progress indicator:** After every 3 blocks, give a brief progress update:
> "Good progress — we've covered [blocks completed]. [N] blocks remain. The areas
> still to cover are: [list]. Roughly [estimate] minutes left."

---

## Handling Special Cases

### User wants to skip a block entirely
> "I understand you want to move on. I'll mark [block] as incomplete — this means
> the final document will have gaps in [area], which could affect [consequence].
> We can come back to it later if needed."

Mark the block as skipped, note it in the gaps log, and proceed.

### User provides contradictory information
Surface it immediately, don't wait for Phase 3:
> "Earlier you mentioned [X], but now you're saying [Y]. These conflict — which
> one is correct? This matters because [consequence]."

### User asks to go back and revise a previous block
Always allow it. Re-mirror the revised block and note any downstream impacts:
> "Got it — I've updated Block [N]. Note that this change may affect [downstream
> blocks/decisions]. I'll flag those when we get there."

### Multiple stakeholders in the session
If more than one person is providing answers, track who said what. When
contradictions arise between stakeholders, surface them as decisions needed:
> "I'm hearing different perspectives on [topic]. [Person A] suggests [X],
> [Person B] suggests [Y]. This needs a decision — who has final authority here?"

---

## Session Data Tracking

As you work through each block, track the structured data fields listed below. You
will need these at Phase 3 to construct the session JSON for the validation script.

You don't need to show this tracking to the user — it's internal bookkeeping. But
accuracy matters: the validation script uses these exact fields to detect conflicts.

See `references/session-schema.md` for the full JSON schema.

### What to Track Per Block

**Block 1 — Vision:**
- `answered_questions` / `total_applicable_questions` — count of questions asked vs answered
- `average_quality_score` — your assessment (1.0 / 0.7 / 0.4 / 0.0), averaged across answers
- `deadline_is_fixed` — boolean: is the go-live deadline contractual/hard?

**Block 2 — Users:**
- `answered_questions` / `total_applicable_questions`
- `average_quality_score`
- `concurrent_users_peak` — numeric estimate of peak simultaneous users
- `user_roles` — list of role names (e.g., `["admin", "staff", "customer"]`)

**Block 3 — Scope:**
- `answered_questions` / `total_applicable_questions`
- `average_quality_score`
- `scope_fully_defined` — boolean: has every feature been confirmed as MVP or post-launch?
- `features_mvp` — list of objects: `{"name": "feature name", "complexity": "simple|medium|complex|xl"}`
  Assign complexity based on the user's description and your judgment:
  - `simple` (3–5 mandays): basic CRUD, list page, simple form
  - `medium` (6–10 mandays): CRUD + business rules, validations, states
  - `complex` (10–15 mandays): multi-step flow, integrations, conditional logic
  - `xl` (15–25 mandays): real-time, AI features, complex dashboards

**Block 4 — Design:**
- `answered_questions` / `total_applicable_questions`
- `average_quality_score`
- `design_owner` — who provides design: "in-house designer" / "client provides mockups" / "dev team handles"
- `design_delivery_deadline` — date string if client-provided, empty string if not set

**Block 5 — Integrations:**
- `answered_questions` / `total_applicable_questions`
- `average_quality_score`
- `third_party_services` — list of service names (e.g., `["midtrans", "firebase", "sendgrid"]`)
- `has_data_migration` — boolean
- `migration_rollback_plan` — boolean (only relevant if has_data_migration is true)

**Block 6 — Security:**
- `answered_questions` / `total_applicable_questions`
- `average_quality_score`
- `handles_pii` — boolean
- `handles_financial_data` — boolean
- `compliance_framework` — string: "UU PDP", "GDPR", "PCI-DSS", "HIPAA", etc. or empty
- `auth_method` — string: "username_password", "sso", "oauth2", "mfa", etc. or empty

**Block 7 — Technology:**
- `answered_questions` / `total_applicable_questions`
- `average_quality_score`
- `hosting_type` — string describing hosting (e.g., "AWS EC2 with load balancer", "shared hosting")
- `architecture_style` — string: "monolith", "microservices", "serverless", etc.
- `api_type` — string: "REST", "REST + WebSocket", "GraphQL", etc.
- `mobile_platforms` — list: `["ios", "android"]` or empty list
- `layers_in_scope` — list: `["web_frontend", "backend_api", "admin_panel", "background_workers"]`
- `has_staging_environment` — boolean (default true if not discussed)

**Block 8 — Budget:**
- `answered_questions` / `total_applicable_questions`
- `average_quality_score`
- `total_mandays_budget` — numeric
- `total_developers` — numeric (total dev headcount)
- `dedicated_qa` — boolean
- `dedicated_devops` — boolean
- `contingency_buffer_included` — boolean
- `senior_backend_engineers` — count
- `senior_frontend_engineers` — count

**Block 9 — Post-Launch:**
- `answered_questions` / `total_applicable_questions`
- `average_quality_score`
- `post_launch_owner` — string describing who maintains the system, or empty
- `monitoring_strategy` — string describing monitoring approach, or empty

### How to Count Questions

- `total_applicable_questions`: Count only the questions you actually asked or determined
  were applicable for this project. If you skipped a question because it's irrelevant
  (e.g., mobile questions for a web-only project), don't count it.
- `answered_questions`: Count questions where the user gave a substantive answer.
  Questions marked as `[GAP]` do not count as answered.

### How to Score Quality

Average across all answered questions in the block:
- **1.0** — User gave a specific, measurable, confirmed answer
- **0.7** — Answer is general but reasonable (workable, not precise)
- **0.4** — Answer is vague, assumed, or the user seemed uncertain
- **0.0** — Unanswered or explicitly skipped

For example, if a block has 8 answered questions with scores [1.0, 1.0, 0.7, 0.7,
0.7, 0.4, 1.0, 0.7], the average quality is 0.78.
