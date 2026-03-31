# Changelog: v1 → v2

## What Changed and Why

### Architecture Changes

| Aspect | v1 | v2 | Why |
|--------|----|----|-----|
| SKILL.md length | ~200 lines (heavy) | 210 lines (lean) | Moved interview logic to reference file |
| Reference files | 4 files | 5 files (+interview-flow.md) | Separated HOW to ask from WHAT to ask |
| Workflow | Ask everything → generate | 4-phase: Detect → Interview → Validate → Generate+Review | Matches your FSD workflow reference |
| Document detection | None | Path A (doc) vs Path B (scratch) | Handles both "I have a brief" and "start from nothing" |

### New: Phased Workflow (Phase 1–4)

v1 had one mode: sequential interview → output. v2 has 4 distinct phases:
- **Phase 1:** Detect if user has source material. If yes, extract first, ask gaps only.
- **Phase 2:** Progressive interview (2–4 questions at a time, not all at once).
- **Phase 3:** Validate cross-block conflicts, present to user, force resolution.
- **Phase 4:** Generate document, present with assumptions highlighted, iterate.

### New: interview-flow.md (426 lines)

This is the biggest structural addition. It contains:
- Path A (document-first) flow: read → extract → summarize → gap-fill
- Path B (interactive) flow: progressive questioning per block
- Adaptive question selection tables (if user says X, ask Y)
- Mirror-back protocol rules
- Answer quality gates (specificity, numeric sanity, buzzword detection)
- Block transition rules
- Session pacing guidance
- Special case handling (skip block, contradictions, go-back, multi-stakeholder)

### New: Tiered Questions in question-bank.md

v1 listed all questions flat. v2 organizes into tiers:
- **Tier 1 (Core):** Always ask first — the opening questions.
- **Tier 2 (Adaptive):** Ask based on Tier 1 answers.
- **Tier 3 (Deep Dive):** Ask when complexity warrants it.

This prevents the "90 questions dumped at once" problem.

### New: Requirement IDs & Traceability in output-template.md

v1 output had no IDs. v2 adds:
- BR-NNN (Business Requirements)
- FT-NNN (Features)
- NFR-NNN (Non-Functional Requirements)
- INT-NNN (Integrations)
- RSK-NNN (Risks)
- GAP-NNN (Gaps)
- UR-NNN (User Roles)
- UJ-NNN (User Journeys)

With traceability rules: every FT → BR, every RSK → FT or INT, every GAP → owner.

### New: Mermaid Diagrams in output-template.md

v1 output was text-only. v2 includes templates for:
- System context diagram (Section 4.1)
- User journey flowcharts (Section 3.3)
- Integration sequence diagrams (Section 5.2)
- Data flow overview (Appendix A.4)
- State machine diagrams (Appendix A.5)

### New: Iterative Review Loop (Phase 4)

v1 generated once and stopped. v2 after generation:
- Highlights assumptions made
- Flags areas needing more stakeholder input
- States top 3 concerns about the project
- Invites user to revise any block
- Re-runs validation on each revision

### Improved: Validation Script

New checks added:
- **CONF-04:** Budget vs scope mismatch (was referenced but not coded in v1)
- **CONF-08:** Multi-platform with small team
- **CONF-09:** Multiple roles without authentication defined
- **WARN-07:** No staging environment
- **WARN-13:** No monitoring strategy
- **WARN-14:** Junior-only team on large project

Better report formatting:
- Progress bars with filled + empty blocks (█░)
- Clearer severity labels
- Block name in issue output

### Improved: dynamic-followups.md

New domain trees added:
- AI / Machine Learning features
- E-Commerce / Marketplace
- Notification & Communication

Existing trees enhanced with additional questions (payment failure retry,
biometric auth, virus scanning on uploads, etc.)

### Improved: validation-rules.md

- Added CONF-04, CONF-08, CONF-09 conflict definitions
- Added WARN-13, WARN-14, WARN-15 warning flags
- Added complete mandays estimation guide with quick formula
- Added confidence threshold reference table
- Clearer resolution options for each conflict

### Removed / Simplified

- Removed pipeline references (BRD → PRD → FSD → SDD → TSD) — skill is standalone
- Removed "persona" framing in SKILL.md ("15 years of experience") — replaced with
  concise behavioral rules
- Simplified confidence formula documentation (was repeated in 3 places, now in 2)

---

## v2.1 Patches

### Reference Analysis Support

- **SKILL.md Phase 1:** Path A now accepts informal references (screenshots, competitor
  links, sketches, architectural ideas) alongside formal documents. Opening prompt
  invites users to share references anytime.
- **interview-flow.md:** Path A rewritten from "Document-First" to "Document &
  Reference-First." Added full reference analysis protocol: categorize inputs, extract
  patterns, surface "iceberg" complexity (with common examples table), handle references
  shared mid-session, probe divergences.
- **output-template.md:** New Section 2: Reference Analysis with 5 subsections (REF-NNN
  IDs, patterns extracted, divergences, hidden complexity, user's original ideas).
  All subsequent sections renumbered (3–11).
- **GUIDE.md:** Updated "Before You Start" and "What Makes This Different" sections.
  Output table updated to 12 sections.
- REF-NNN added to ID conventions across all relevant files.

### Dual Validation Pipeline

- **SKILL.md Phase 2:** Added mental validation instructions — surface contradictions
  as they're discovered during the interview, don't wait for Phase 3.
- **SKILL.md Phase 3:** Rewritten as two explicit steps: (1) mental cross-block review,
  (2) construct session JSON and run validation script. Includes exact bash commands
  and a validation summary presentation template.
- **interview-flow.md:** New "Session Data Tracking" section — exact fields to capture
  per block during the interview, how to count questions, how to score quality.
- **references/session-schema.md (NEW):** Full JSON schema reference with field types,
  validation trigger mapping, quality scoring guide, and a complete construction example
  for an e-commerce project.
- **README.md:** Session schema section trimmed to a brief pointer to session-schema.md.
  File structure and workflow phases table updated.

---

## v2.2 — Document Validation

### Problem Solved
Previously, validation only worked on the session JSON (interview data). If someone
edited the output requirements.md outside of Claude — adding features, changing budget,
removing integrations — there was no way to re-validate. The document could silently
become internally inconsistent.

### New: `scripts/validate_document.py`
A standalone script that parses a requirements `.md` file and validates it for:
- **Structural completeness** — all 10+ required sections present
- **ID sequence integrity** — no gaps like FT-001, FT-003 without FT-002
- **Traceability** — every FT links to a BR, every RSK links to a FT or INT
- **Scope-estimation alignment** — every feature in MVP scope has a mandays estimate
- **Gap integrity** — every GAP has an owner and priority
- **Status consistency** — FINAL document shouldn't have Critical/High gaps
- **Integration completeness** — integrations referenced in features exist in the map
- **Confidence thresholds** — overall confidence above 55%
- **Cross-validation with session** (optional) — feature count, integration count,
  and budget match between session JSON and document

### Updated: SKILL.md
- Phase 4 now runs document validation after generating the `.md`
- New "Re-Validating an Edited Document" section with usage instructions
- Reference files table updated with both validation scripts

### Updated: README.md
- New "Running the Document Validator" section with full check catalog
- New "Two Validation Scripts: When to Use Which" section with flow diagram
- File structure updated

---

# Changelog: v2 → v3

## What Changed and Why

### New: references/manpower.md

Role catalog and rate card for team composition and cost estimation. Contains:
- **10 standard roles** across 3 seniority levels: PM, SA, DDA, QA, FE, BE, UIUX, GD, MGD, DO
- **Default IDR hourly rates** per role × seniority
- **Scope trigger definitions** — which scope signals require which role at which seniority
- **Custom reference workflow** — at Block 8 start, ask the user if they have their own rate card. If yes, use theirs. If no, present defaults for confirmation.
- **Template for custom rate card** — shareable template for users to fill in their own rates

**Why:** Previously, team composition recommendations were implicit. Now there's a structured reference that makes recommendations traceable and allows users to override defaults with their own company data.

### New: references/mandays.md

Complexity and effort estimation guide. Contains:
- **4 complexity tiers:** T1 Low (0–3), T2 Medium (4–7), T3 High (8–14), T4 Complex (15+)
- **Feature complexity matrix** — common feature types mapped to tiers with mandays ranges and roles needed
- **Role allocation by complexity** — minimum role set and seniority per tier
- **Integration effort reference** — per integration type (aligned with validation-rules.md)
- **Cross-cutting effort** — QA, PM, SA, Design, DevOps percentages
- **Platform multipliers** — mobile, admin panel, background workers
- **Project-level classification** — Simple/Standard/Complex/Enterprise with team sizing
- **Progressive estimation workflow** — exact formulas for Block 3 → Block 8 build-up
- **Cost projection formula** — mandays × roles × rates from manpower.md
- **Custom reference workflow** — ask user for their own estimation benchmarks
- **Template for custom mandays reference** — shareable template

**Why:** Mandays estimation was previously embedded in validation-rules.md as floor estimates only. Now it's a complete, standalone reference with progressive workflow, role mapping, cost projection, and support for custom overrides.

### Updated: SKILL.md

- Reference Files table expanded with manpower.md and mandays.md entries
- Progressive mandays estimation section now references mandays.md formulas
- Block 8 team recommendation section now includes custom reference check workflow from manpower.md before recommending team composition

### Updated: references/output-template.md

- Section 9.1 (Team Composition) uses all 10 roles from manpower.md with role codes, IDR rates, and Rate Card Source tag
- Section 9.3 (Effort Breakdown) uses role codes and complexity tiers from mandays.md
- New Section 9.5 (Cost Projection) converts mandays to IDR using manpower.md rates
- Section 9.5 (Budget vs Scope) renumbered to 9.6

### Updated: README.md

- File structure updated with manpower.md and mandays.md descriptions

### Cross-Skill Alignment

- `functional-decomposition` skill now references manpower.md and mandays.md as shared references
- Story Points ↔ Mandays alignment table added to functional-decomposition SKILL.md
- Consistent role codes (PM, SA, DDA, QA, FE, BE, UIUX, GD, MGD, DO) across both skills

---

# Changelog: v3 → v3.1 (Bugfix — Confirmation Gate Hardening)

## Problem

When given detailed input (MoM, PRD, feature list), the skill was generating the
output document immediately without interviewing the user or asking for confirmation.
This violated the core principle: "ask first, document second."

## Root Cause

The instructions for multi-turn behavior were present but not prominent enough.
Claude was optimizing for "helpfulness" by producing the deliverable immediately
when the input seemed sufficient, bypassing all confirmation gates.

## Fix: 4 Reinforcement Layers Added

### Layer 1: HARD STOP rule in Core Rules (SKILL.md)
- New top-level rule with ⛔ markers: "NEVER generate the output document in the same turn as receiving input"
- New Phase Completion Checklist — all checkboxes must be TRUE before generation
- New Rule 7: "The conversation MUST be multi-turn" with minimum turn count

### Layer 2: Known Failure Modes section (SKILL.md)
- Three explicitly named failure patterns with "why it's wrong" and "correct behavior"
- Failure Mode 1: "Complete input = skip interview"
- Failure Mode 2: "Extraction summary = confirmation"
- Failure Mode 3: "User said 'generate' so I skip the interview"

### Layer 3: Path A hardening (SKILL.md)
- Triple ⛔ CRITICAL markers at top of Path A section
- Explicit "Your first response MUST look like this" template
- Explicit "Your first response MUST NOT contain" list (no .md files, no output templates)
- Added explanation of WHY interview is mandatory even for detailed documents

### Layer 4: interview-flow.md Path A enforcement
- Added MANDATORY MULTI-TURN RULE with minimum 6 conversation turns described
- Added explicit "if your first response contains a generated document → you are doing it WRONG"

### Updated: Phase 4 prerequisite (SKILL.md)
- 5-point verification checklist before generation
- New "fewer than 4 back-and-forth exchanges = have NOT completed" heuristic
- New handling for "user's first message says generate" scenario
