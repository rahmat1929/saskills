---
name: system-documentation
description: Generate a comprehensive Product Requirements Document (PRD), Business Requirements Document (BRD), or Functional Specification Document (FSD) from project requirements, briefs, or interactive interviews. Use this skill whenever the user mentions PRD, product requirements, BRD, business requirements, functional specs, FSD, software specification, feature specification, system specification, functional requirements document, or wants to document business needs or how a system should behave. Also trigger when users ask to "spec out" a feature, write up requirements, or create a detailed plan for stakeholders or developers — even if they don't use the exact terms explicitly.
---

# Product, Business & Functional Specification Document Generator

This skill produces three types of structured documents:
- **PRD (Product Requirements Document)** — product-focused spec defining user problems, personas, user stories, RICE prioritization, and release strategy. The primary planning artifact for product teams; written from the user's perspective.
- **BRD (Business Requirements Document)** — business-focused spec defining the business problem, goals, stakeholders, and high-level business rules. Written for business stakeholders; strictly avoids technical implementation details.
- **FSD (Functional Specification Document)** — implementation-ready spec bridging stakeholder needs and engineering requirements. Answers "what does the system do and how should it behave" without dictating internal architecture.

## Content Rules

These rules govern every document this skill produces. Follow them strictly:

- **Distinguish Document Types** — Know which document you are writing. The PRD focuses on the user and product strategy (the "why" and "what" from a user perspective). The BRD focuses on business priorities (the "why" and "what" from a business perspective), strictly avoiding technical constraints and implementation details. The FSD focuses on system behavior (the "how it behaves") translating those constraints to actionable scopes that developers understand.
- **NO CODE SAMPLES** — Provide only explanations, conceptual descriptions, and structured information. Never include source code, pseudo-code, or implementation snippets.
- **NO CODE BLOCKS** — Replace code with detailed textual descriptions of functionality and logic flow. The only permitted fenced blocks are Mermaid diagrams.
- **"What" and "why", not "how"** — Use clear, developer-friendly language that focuses on system behavior and business rationale, not implementation mechanics.
- **Architectural understanding first** — Prioritize system relationships, module interactions, and data flow over technical details.
- **Mermaid exclusively for visuals** — Use Mermaid format for all diagrams: flowcharts, sequence diagrams, state diagrams, entity relationships, and architecture overviews. No ASCII art, no plaintext diagrams, no embedded images.
- **Exclude API & Database** — The FSD does not cover API endpoint specifications or database schema design. Those belong in separate API Specification and Database Design documents respectively. The FSD references them but does not define them.

## When to use this skill

- A user wants to **create a PRD** — a product requirements document with user stories, RICE scoring, personas, and release strategy
- A user wants to define the business goals and high-level requirements for an initiative (BRD)
- A user wants to create a functional specification for a new product, feature, or system (FSD)
- A user has a PRD, project brief, or set of requirements and needs them turned into a detailed BRD or FSD
- A user asks to "spec out" or "write up" how something should work or what it should achieve
- A user needs to document business goals, functional requirements, use cases, or acceptance criteria
- A user provides a PRD and asks for an FSD that is more implementation-ready (still excluding API and DB specs)

## Workflow

### Phase 1: Gather Context

Before writing anything, understand what you're specifying. There are two paths depending on what the user provides:

**Path A — User provides a source document (PRD, brief, requirements list, etc.):**
Read the document thoroughly. Extract the core requirements, identify gaps, and list clarifying questions. Present the questions to the user before proceeding. Don't guess at ambiguous requirements — ask.

If the source is a **PRD**, treat it as product-level intent and translate it into:

- BRD: business goals, stakeholders, scope boundaries, business rules (as applicable)
- FSD: system behaviors, functional requirements, UI requirements, error handling, and measurable NFRs

**Path B — No source document (interactive interview):**
Walk through these questions to build a mental model of the system:

1. What is the product/feature? (one-sentence elevator pitch)
2. Who are the users? (roles, personas, access levels)
3. What are the core workflows? (the 3-5 things users will actually do)
4. What external systems does this interact with? (third-party services, other internal modules)
5. Are there constraints? (regulatory, platform, timeline, tech stack)
6. What does success look like? (KPIs, acceptance criteria)

Don't ask all questions at once — use the first couple of answers to tailor follow-ups. The goal is to get enough information to write a solid first draft, not to exhaustively document everything upfront.

### Phase 2: Write the Document

Determine which document type the user needs:

- **PRD** — user problem + personas + user stories + RICE prioritization + release strategy → read `references/prd-template.md`
- **BRD** — business goals + stakeholders + business rules → read `references/brd-template.md`
- **FSD** — system behavior + functional requirements + error handling → read `references/fsd-template.md`

Read the appropriate template for the full document structure and section-by-section guidance. Follow that template structure, but adapt it to the project — skip sections that genuinely don't apply and expand sections that need more depth.

**When writing a PRD:**
- Use the 19-section structure from `references/prd-template.md`
- Activate or skip conditional sections based on Project Type (New Product / Enhancement / Migration / Compliance / Integration) using the Conditional Section Matrix
- Group all user stories by **Feature Module** with IDs in `US-[Module]-001` format
- Calculate RICE scores for all features and stories
- Clearly separate MVP from Post-MVP scope
- Write the Executive Summary LAST (after all other sections are complete)
- Flag gaps as `[NEEDS INPUT: description]` rather than guessing

**Key principles while writing (all document types):**

- **Be specific.** "The system should be fast" is not a requirement. "Search results return within 200ms for up to 10,000 records" is.
- **Use consistent language.** "SHALL" = mandatory, "SHOULD" = recommended, "MAY" = optional. Define this in the Document Conventions section and stick to it.
- **Every feature gets acceptance criteria.** If you can't write a test for it, the requirement isn't clear enough.
- **Describe behavior, not implementation.** State what the system does and why, never how it does it internally.
- **Assign priority to each requirement.** Use MoSCoW: Must / Should / Could / Won't. This prevents scope creep and helps teams negotiate tradeoffs.
- **Number every requirement.** Use a hierarchical ID scheme (e.g., FR-3.2.1) so requirements are traceable from spec to test to implementation.
- **Use Mermaid for all diagrams.** State machines, user flows, system context, sequence diagrams — all in Mermaid format.

### Phase 3: Output

Save the document as a Markdown file. Use the naming convention:
- `PRD-[Project-Name].md` for PRDs
- `BRD-[Project-Name].md` for BRDs
- `FSD-[Project-Name].md` for FSDs

After generating the document, run the validation script to check structural completeness. The script validates required sections, requirement ID format, acceptance criteria presence, MoSCoW labels, Mermaid diagram presence, and flags any code blocks that shouldn't be there.

If validation reports issues, fix them before presenting the final document to the user. Show the user the validation summary alongside the finished document so they know it's been checked.

### Phase 4: Review & Iterate

Present the draft to the user. Highlight:
- Sections where you made assumptions (flag these explicitly)
- Areas that need more detail from stakeholders
- Requirements you marked as "Could" or "Won't" that the user might want to reconsider
- (PRD only) Stories where Confidence score is 0.5 — these should be validated before committing to build

Incorporate feedback and regenerate. Each revision should re-run validation.

## Document Structure Summary

### Product Requirements Document (PRD)
The PRD follows a 19-section structure (see `references/prd-template.md` for full details and guidance):

1. **Document Control** — ID, version, status, authors, change log
2. **Executive Summary** — Product, problem, users, key features, success metric (write last)
3. **Product Vision & Strategic Context** — Vision statement, strategic alignment, positioning (conditional)
4. **Problem Statement & Opportunity** — User problem, evidence, opportunity sizing, jobs-to-be-done
5. **Target Users & Personas** — Primary/secondary personas, anti-personas (conditional)
6. **User Stories & Use Cases** — Stories grouped by Feature Module with `US-[Module]-001` IDs, RICE scores, acceptance criteria
7. **Functional Overview** — Feature map, core workflows, feature interaction matrix
8. **User Flows & Interaction Model** — Key user journeys with happy path, error paths, decision branches (conditional)
9. **Requirements Prioritization (RICE)** — Scored table: Reach × Impact × Confidence ÷ Effort; MVP vs. Post-MVP thresholds
10. **Non-Functional Requirements** — Performance, scalability, security, accessibility, reliability
11. **Scope & Boundaries** — MVP scope, post-MVP scope, explicitly out of scope
12. **Success Metrics & KPIs** — Adoption, engagement, satisfaction, performance metrics
13. **Competitive Feature Comparison** — Feature matrix vs. competitors (conditional)
14. **Assumptions & Constraints** — Product assumptions, technical constraints, resource constraints
15. **Dependencies & Integrations** — External deps, integration points, internal team deps
16. **Release Strategy** — Phases, feature flagging, rollback plan, launch checklist (conditional)
17. **Risks & Mitigations** — Adoption, usability, technical feasibility, competitive, dependency, regulatory risks
18. **Open Questions & Decisions Log** — Unresolved questions, settled decisions with rationale
19. **Glossary & Appendices** — Terms, research references, wireframe links

### Business Requirements Document (BRD)
The BRD follows this top-level structure (see `references/brd-template.md` for details):
1. **Executive Summary** — Purpose, background, and problem statement
2. **Business Goals & Objectives** — Project goals and success metrics (KPIs)
3. **Project Scope** — In scope and out of scope
4. **Stakeholders** — Roles, influence, and responsibilities
5. **Business Requirements** — High-level requirements mapped to MoSCoW priorities and business rules
6. **Assumptions, Constraints & Dependencies**
7. **Glossary of Terms**

### Functional Specification Document (FSD)
The FSD follows this top-level structure (see `references/fsd-template.md` for details):

1. **Introduction** — Purpose, scope, definitions, references, conventions
2. **Product Overview** — Context, high-level functions, users, environment, constraints, assumptions
3. **Functional Requirements** — Feature breakdown with IDs, descriptions, acceptance criteria, priority, business rules; use cases with main/alternative/exception flows
4. **User Interface Requirements** — Screen descriptions, interaction behavior, navigation, accessibility
5. **Non-Functional Requirements** — Performance, security, reliability, scalability, maintainability, accessibility
6. **System Behavior & Error Handling** — State transitions (Mermaid), error matrix, edge cases
7. **Approval & Sign-Off** — Stakeholder table, revision history
8. **Appendices** — Mermaid diagrams, supplementary material

## Output Quality Checklist

Before delivering the final document, mentally verify:

**All document types:**
- [ ] Every requirement has a unique ID and priority (MoSCoW)
- [ ] No section is left as a placeholder or TODO
- [ ] Cross-references between sections are consistent
- [ ] All diagrams use Mermaid format (no code blocks, no ASCII art)
- [ ] No code samples or code blocks appear anywhere in the document
- [ ] The document serves its audience correctly (PRD for product teams, BRD for business stakeholders, FSD for developers/QA)

**PRD only:**
- [ ] All user stories grouped by Feature Module with correct `US-[Module]-001` ID format
- [ ] Every story has a RICE score with explicit Reach, Impact, Confidence, Effort values
- [ ] MVP vs. Post-MVP scope is clearly delineated
- [ ] Conditional sections activated/skipped per Project Type using the matrix
- [ ] Executive Summary written last and matches rest of document
- [ ] Stories with Confidence ≤ 0.5 flagged for validation before commitment
- [ ] Open Questions log captures all unresolved items

**FSD only:**
- [ ] Every feature has testable acceptance criteria
- [ ] Use cases cover main flow + at least one alternative/error flow
- [ ] Error handling is specified for user-facing operations
- [ ] Non-functional requirements have measurable targets
- [ ] No API endpoint definitions or database schemas are included
