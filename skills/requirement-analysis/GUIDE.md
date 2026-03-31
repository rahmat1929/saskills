# User Guide — AI for Requirement Analysis

**Who this is for:** Anyone scoping a software project — sales, project managers,
business analysts, product owners, or founders who need to turn an idea into a
development-ready document.

---

## What to Expect

This is not a form. It's a structured conversation with an experienced consultant.

The session works like sitting down with a senior Business Analyst who has seen dozens
of projects go wrong — and who asks the questions that most people skip. Depending on
your project's complexity and how much you already have prepared, the session takes
**30 to 90 minutes**.

At the end, you receive a **Source of Truth document** — a single reference that your
sales team, designers, and engineers can all work from.

---

## Two Ways to Start

### Option A: You Have Existing Material
Upload or paste any of the following: a project brief, PRD, meeting notes, feature
list, RFP, or proposal. The AI will read it, extract everything it can, and then ask
only the questions your document doesn't answer.

This is faster. If you have a 2-page brief, the AI might only need 15–20 minutes of
follow-up questions to produce a complete document.

### Option B: Starting from Scratch
No preparation needed. The AI will walk you through everything from "what are you
building?" to "who maintains it after launch?" — one block at a time.

This is more thorough. Expect 45–90 minutes, but the result is comprehensive.

---

## Before You Start (Optional but Helpful)

The more you've thought about these, the faster the session:

- A description of what you want to build and why
- Who will use the system (user types/roles)
- A rough budget in mandays, or at least a range
- Any existing mockups, designs, or reference systems
- Technical constraints (must-use technologies, hosting requirements)
- Hard deadlines
- **References you admire** — competitor apps, screenshots, sketches, links to
  systems you want to learn from, or your own architectural ideas. These are
  extremely valuable. The AI will analyze what patterns to extract and what
  complexity they imply.

You don't need all of this to be precise — that's what the session is for. And you
can share references at **any point** during the session, not just at the start.

---

## How the Session Works

The session covers **9 dimensions** of your project. The AI works through them
sequentially, and after each one it **reflects back what it understood** for you to
confirm before moving on.

### The 9 Blocks

| # | Block | What It Covers | Why It Matters |
|---|-------|---------------|----------------|
| 1 | Vision & Business Goal | Why you're building this | Prevents building the wrong thing |
| 2 | Users & Usage Patterns | Who uses it, how many, how often | Defines scale and UI complexity |
| 3 | Features & Scope | What it does — and what it doesn't | The #1 source of scope creep |
| 4 | Design & UX | How it looks and feels | Prevents design bottlenecks |
| 5 | Integrations & Data | External services and data flows | Hidden complexity lives here |
| 6 | Security & Compliance | Data protection and regulation | Legal risk if missed |
| 7 | Technology & Architecture | Stack, hosting, deployment | Aligns team to constraints |
| 8 | Team, Budget & Timeline | Mandays, composition, deadlines | Reality check |
| 9 | Launch & Post-Launch | Go-live strategy and maintenance | Who owns it after it's built? |

### What Makes This Different

**Progressive questioning.** The AI doesn't dump 90 questions on you. It asks 2–4
at a time, and uses your answers to decide what to ask next. If you mention payment
processing, it asks about refund flows. If you mention mobile, it asks about
cross-platform vs native. Your answers shape the conversation.

**Mirror-back at each step.** After each block, the AI summarizes what it understood
and asks you to confirm. This catches misunderstandings early — before they become
problems in the document.

**Conflict detection.** The AI checks your answers against each other. If you say
50,000 users but plan shared hosting, it flags it. If you list payment features but
don't mention a payment gateway, it catches it. If your budget can't cover your scope,
it tells you.

**Reference analysis.** When you share competitor apps, screenshots, or your own ideas,
the AI doesn't just note them — it analyzes what patterns to extract, what hidden
complexity they imply, and where your project should diverge. "Like Tokopedia" becomes
a precise list of patterns adopted, rejected, and modified.

---

## What the AI Will Push Back On

This tool is designed to **not accept vague answers**:

| What you say | What you'll be asked |
|-------------|---------------------|
| "We need a dashboard" | What data? Who reads it? How often? Filterable? |
| "Standard security" | Do you handle personal data? Financial data? Which regulations? |
| "Like Tokopedia" | Which specific flows — not the entire platform |
| "AI-powered" | What specifically should AI do? For which users? |
| "Simple app" | Define the simplest acceptable version |
| "Real-time" | Acceptable latency? What if the connection drops? |
| "Just a CRUD" | How many entities? What business rules? What validations? |

The AI probes up to **3 times** per question. After 3 rounds, it flags the item as
a gap and moves on.

---

## Validation Before Output

Before generating your document, the AI runs a **cross-block validation**:

- **Scale mismatches** — 50,000 users but shared hosting
- **Compliance gaps** — collecting KTP numbers with no data protection framework
- **Hidden integrations** — checkout feature but no payment gateway declared
- **Budget impossibility** — 15 complex features in 30 mandays
- **Team mismatch** — microservices proposed for a 2-developer team

Critical issues must be resolved or explicitly accepted as gaps before the document
is finalized.

---

## What You Get at the End

A **11-section Source of Truth document** in Markdown:

| Section | For |
|---------|-----|
| Executive Summary | Sales, client, leadership |
| Reference Analysis | Everyone — aligns team on "like X" meaning |
| Business Requirements | PM, Business Analyst |
| UX & Design Requirements | Designer, Frontend Dev |
| Technical Specifications | Development team |
| Integration Map | Architect, Tech Lead |
| Risk Register | PM, Tech Lead |
| Scope Boundary Statement | Everyone (prevents scope creep) |
| Mandays Estimation Matrix | PM, Sales |
| Open Questions & Gaps Log | PM, Sales — resolve before dev |
| Confidence Score Card | PM, Tech Lead — readiness assessment |

Every requirement, feature, risk, and gap has a unique ID for traceability. Complex
flows include Mermaid diagrams.

---

## Draft vs Final Documents

**FINAL** — All critical gaps resolved, confidence thresholds met. Development can
begin.

**DRAFT — Pending Gap Resolution** — Gaps exist but enough information for a useful
document. Includes a **Pre-Development Checklist** of everything to confirm before
a single line of code is written.

> **For Sales:** If you receive a DRAFT, the Pre-Development Checklist items are not
> optional. They represent decisions not made during discovery. Development should not
> begin on Critical-priority gaps until resolved and the document is re-issued as FINAL.

---

## After the Session

The document is a living artifact. You can:

- Ask the AI to re-open any specific block with updated information
- Request a regenerated document with changes incorporated
- Use the document as input for PRD, FSD, SDD, or TSD generation

---

## Common Mistakes to Avoid

**Don't rush.** Vague answers produce vague documents. The time you invest here saves
weeks of rework.

**Don't skip blocks.** Every block feeds the others. Missing integration info affects
technology decisions. Missing compliance info affects architecture.

**Don't say "standard" without defining it.** Standard means different things to
different people.

**Don't omit post-launch planning.** The most common failure isn't bad development —
it's a system with no owner, no maintenance plan, and no support structure after launch.
