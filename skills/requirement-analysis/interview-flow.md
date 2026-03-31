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

---

## Path A: Document & Reference-First Flow

When the user provides source material — formal documents (PRD, brief, meeting notes,
feature list, RFP, proposal) **or** informal references (competitor links, screenshots,
sketches, architectural ideas, app store links, Figma files) — follow this flow:

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
and reference material:

> "I've read through your materials. Here's what I extracted:
>
> **From your [document type]:**
> **Vision & Business Goal:** [summary]
> - Confirmed: [list]
> - Needs confirmation: [list]
> - Missing: [list]
>
> [repeat for each block]
>
> **From your references:**
> - From [reference 1]: [what patterns extracted, what it implies for scope/tech]
> - From [reference 2]: [what patterns extracted, what it implies]
> - Key divergences you noted: [list]
> - Hidden complexity flagged: [list]
>
> **Blocks with no information found:** [list blocks]
>
> I have [N] questions to fill the gaps. Shall I go through them now?"

### Step 4: Gap-Filling Interview

Only ask questions where the material was silent or ambiguous. Group gap questions
by block and ask 2–4 at a time, same as Path B. Skip blocks where the material
provided sufficient detail (confidence ≥ threshold).

### Step 5: Confirm Implied Items

For items marked IMPLIED (from both documents and references), present them as
assumptions and ask for confirmation:

> "I inferred [X] from your [document/reference]. Is that accurate, or should I
> adjust?"

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

**Opening questions:**
1. What is the total mandays budget? Fixed or estimate?
2. What's the team composition? (roles, seniority, availability)

**After receiving budget and team info, immediately run the mandays reality check
mentally.** Compare declared scope (Block 3) against the budget. If there's a gap:

> "Based on what you've described, the minimum realistic effort is approximately
> [X] mandays. Your budget is [Y]. That's a [Z]% gap. Before we continue, we need
> to align: cut scope, increase budget, or extend timeline?"

**Do not defer this conversation.** It must happen in this block.

**Then ask (if not covered):**
3. What happens when scope and budget don't align — which gives?
4. Hard milestone deadlines within the project?
5. Is there a contingency buffer?

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

### 4. Probe Limit
Maximum 3 follow-up probes per question. If still unresolved after 3 rounds, mark
as `[GAP: description — needs clarification from {owner}]` and continue. Do not
hold the session hostage on a single question.

---

## Block Transition Rules

Before moving from Block N to Block N+1:

1. ✅ Mirror-back completed and confirmed
2. ✅ Block confidence meets or exceeds minimum threshold
3. ✅ No unaddressed flags from previous blocks that this block should have resolved
4. ✅ Any cross-block implications noted for future blocks

If confidence is below threshold but the user can't provide more information:
- Mark specific questions as `[GAP]`
- Note the impact on document quality
- Proceed — don't loop indefinitely

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
