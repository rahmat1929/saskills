# AI for Requirement Analysis — Skill

A structured requirement gathering and analysis skill for software projects. Conducts
a phased discovery session, validates answers for completeness and consistency, and
generates a Source of Truth document that serves as the single reference for sales,
design, and engineering.

---

## What This Skill Does

This skill acts as a **senior Business Analyst** who conducts thorough discovery
before any document is produced. It:

- Detects whether source material exists (Path A) or starts from scratch (Path B)
- Asks progressive questions across 9 blocks — adapting based on answers, not dumping
  all questions at once
- Probes vague answers up to 3 times before marking them as gaps
- Injects domain-specific follow-ups when answers trigger known complexity areas
  (payments, mobile, real-time, Indonesian market, etc.)
- Detects cross-block contradictions (scale vs infrastructure, scope vs budget, etc.)
- Runs a mandays reality check before generating output
- Produces an 12-section Source of Truth document with requirement IDs, traceability,
  Mermaid diagrams, and a dedicated Reference Analysis section

---

## File Structure

```
ai-requirement-analysis/
├── SKILL.md                          # Core skill instructions — workflow & philosophy
├── README.md                         # This file — technical documentation
├── GUIDE.md                          # User-facing guide: what to expect
├── references/
│   ├── interview-flow.md             # Progressive questioning logic & adaptive routing
│   ├── question-bank.md              # Full question list (tiered) for all 9 blocks
│   ├── manpower.md                   # Role catalog (11 roles × 3 seniority), IDR rate card, custom reference workflow
│   ├── mandays.md                    # Complexity tiers (T1–T4), effort tables, progressive estimation, cost projection
│   ├── session-schema.md             # JSON schema for validation script input
│   ├── validation-rules.md           # Cross-block conflict matrix & mandays guide
│   ├── dynamic-followups.md          # Context-triggered follow-up questions by domain
│   └── output-template.md            # Source of Truth template with ID schemes & Mermaid
└── scripts/
    ├── validate_requirements.py      # Session validation — validates interview data
    └── validate_document.py          # Document validation — validates the output .md
```

---

## Workflow Phases

| Phase | Goal | Key Reference Files |
|-------|------|-------------------|
| 1. Detect Context | Determine Path A (doc/ref) or Path B (interview) | SKILL.md |
| 2. Structured Interview | Gather info across 9 blocks progressively | interview-flow.md, question-bank.md, dynamic-followups.md |
| 3. Validate | Construct session JSON, run script, catch conflicts | session-schema.md, validation-rules.md, validate_requirements.py |
| 4. Generate & Review | Produce document, present to user, iterate | output-template.md |

---

## The 9 Blocks

| # | Block | Min Confidence | Priority |
|---|-------|---------------|----------|
| 1 | Vision & Business Goal | 80% | Critical |
| 2 | Users & Usage Patterns | 75% | High |
| 3 | Features & Scope | 90% | Critical |
| 4 | Design & UX | 70% | High |
| 5 | Integrations & Data | 85% | Critical |
| 6 | Security & Compliance | 80% | High |
| 7 | Technology & Architecture | 75% | High |
| 8 | Team, Budget & Timeline | 85% | Critical |
| 9 | Launch & Post-Launch | 65% | Medium |

---

## Running the Validation Script

### Requirements
- Python 3.10+
- No external dependencies (standard library only)

### Usage

**Note:** These scripts live in this skill's `scripts/` directory. Run them using
the full path to the skill directory (e.g., `/mnt/skills/user/ai-requirement-analysis/scripts/`).

```bash
# Demo mode (built-in example session)
python3 {SKILL_DIR}/scripts/validate_requirements.py

# Validate a session file — terminal output
python3 {SKILL_DIR}/scripts/validate_requirements.py --input /tmp/session.json
```

The script outputs results directly to the terminal. JSON report output is available
via `--output report.json` and `--quiet` flags for CI/CD integration, but the
standard workflow uses terminal output only.

### Exit Codes
- `0` — Validation passed or draft can be generated
- `1` — Critical issues found that block output

---

## Running the Document Validator

Use this script to validate a generated or manually edited requirements `.md` file.
This is the primary tool for **post-edit validation** — when someone changes the
document outside of a Claude session and needs to verify it's still consistent.

### Requirements
- Python 3.10+
- No external dependencies (standard library only)

### Usage

```bash
# Validate document structure, traceability, and consistency
python3 {SKILL_DIR}/scripts/validate_document.py --input requirements.md

# Cross-validate against session data (if available)
python3 {SKILL_DIR}/scripts/validate_document.py --input requirements.md --session session.json
```

The script outputs results directly to the terminal. This is the command to share
with users so they can re-validate after manual edits. JSON report output is
available via `--output` and `--quiet` flags for CI/CD integration.

### What It Checks

| Code | Check | Severity |
|------|-------|----------|
| DOC-MISS | Required section missing from document | Critical |
| DOC-SCOPE-EST | Feature in MVP scope but not in estimation matrix | Critical |
| DOC-INT-MISS | Integration referenced in features but missing from Integration Map | Critical |
| DOC-STATUS | Document marked FINAL but has Critical/High gaps | Critical |
| DOC-CONF-LOW | Overall confidence below 55% | Critical |
| DOC-SUB-MISS | Required subsection missing (e.g., 3.4, 4.2, 9.1, 12.2) | Warning |
| DOC-DIAGRAM | Expected Mermaid diagram missing from section | Warning |
| DOC-TRACE-FT | Feature has no linked Business Requirement | Warning |
| DOC-TRACE-BULK | Multiple features missing traceability data | Warning |
| DOC-GAP-OWNER | Gap has no owner assigned | Warning |
| DOC-EST-SCOPE | Feature in estimation but not in scope | Warning |
| DOC-STATUS-GAP | Document marked FINAL but has unresolved gaps | Warning |
| DOC-IDGAP | ID sequence has gaps (e.g., FT-001, FT-003, no FT-002) | Warning |
| DOC-CONF-MISS | No confidence scores found | Warning |
| DOC-TRACE-RSK | Risk not linked to any Feature or Integration | Info |
| DOC-GAP-PRI | Gap has no priority assigned | Info |

### Cross-Validation Checks (when --session provided)

| Code | Check | Severity |
|------|-------|----------|
| XVAL-FT-COUNT | Feature count mismatch between session and document | Warning |
| XVAL-INT-COUNT | Integration count mismatch | Warning |
| XVAL-BUDGET | Budget deviation >10% between session and document | Critical |

### Exit Codes
- `0` — Document passes validation (warnings and info only)
- `1` — Critical issues found

---

## Two Validation Scripts: When to Use Which

| Script | Input | When to Use | Output |
|--------|-------|-------------|--------|
| `validate_requirements.py` | Session JSON (internal) | After interview, before generating document | Terminal only |
| `validate_document.py` | Requirements .md | After generating document, after every update, OR after manual edits | Terminal only |

**Typical flow:**
```
Interview → Session JSON (internal, /tmp) → validate_requirements.py (terminal)
                                                    ↓
                                            Generate .md file
                                                    ↓
                                     validate_document.py (terminal) ← ALWAYS RUN
                                                    ↓
                                            Deliver to team
                                                    ↓
                                     User requests changes OR team edits .md
                                                    ↓
                                     validate_document.py (terminal) ← RE-RUN
```

**Key rules:**
- The session JSON is constructed internally in `/tmp` — it is NOT saved as an output file
- Both validators output to terminal only — no JSON report files are generated
- `validate_document.py` runs after EVERY document generation or update
- Share the `validate_document.py` command with the user for self-service re-validation

---

## Session JSON Schema

The `validate_requirements.py` script expects a session JSON file as input. During
Phase 3, Claude constructs this JSON internally from data tracked during the interview,
saves it to `/tmp/session.json`, and runs the script. **The session JSON is not saved
as an output file** — it is used only for validation and then discarded.

For the full schema with all fields, types, validation triggers, quality scoring guide,
and a complete construction example, see **`references/session-schema.md`**.

**Quick reference — feature complexity values:**

| Value | Mandays Floor | Example |
|-------|--------------|---------|
| `simple` | 4 | Basic list page, simple form |
| `medium` | 7 | CRUD module with validation and business rules |
| `complex` | 12 | Multi-step flow with logic, states, integrations |
| `xl` | 20 | Real-time system, complex dashboard, AI feature |

---

## Validation Checks

### Block Presence
All 9 blocks must be present.

### Confidence Scores
Each block checked against its minimum threshold.

### Critical Conflicts

| Code | Conflict |
|------|---------|
| CONF-01 | High concurrent users + low-capacity hosting |
| CONF-02 | PII/financial data + no compliance framework |
| CONF-03 | Feature implies undeclared integration |
| CONF-04 | Mandays floor exceeds budget by >30% |
| CONF-05 | Complex architecture + inexperienced team |
| CONF-06 | Real-time features + REST-only API |
| CONF-07 | Client-provided design + no delivery deadline |
| CONF-08 | Multi-platform + small team |
| CONF-09 | Multiple roles + no authentication defined |

### Warnings

| Code | Warning |
|------|---------|
| WARN-01 | No post-launch owner |
| WARN-02 | No QA + many integrations |
| WARN-04 | No contingency buffer |
| WARN-05 | Fixed deadline + undefined scope |
| WARN-07 | No staging environment |
| WARN-12 | Data migration without rollback plan |
| WARN-13 | No monitoring strategy |
| WARN-14 | Junior-only team on large project |

---

## ID Scheme

The output document uses these ID formats for traceability:

| Entity | Format | Example |
|--------|--------|---------|
| Business Requirement | BR-NNN | BR-001 |
| Feature | FT-NNN | FT-001 |
| Non-Functional Req | NFR-NNN | NFR-001 |
| Integration | INT-NNN | INT-001 |
| Risk | RSK-NNN | RSK-001 |
| Gap | GAP-NNN | GAP-001 |
| User Role | UR-NNN | UR-001 |
| User Journey | UJ-NNN | UJ-001 |
| Reference | REF-NNN | REF-001 |

---

## Output Document Status

| Condition | Status |
|-----------|--------|
| No critical issues | FINAL — Ready for Development |
| Critical issues exist | DRAFT — Pending Gap Resolution |

Draft documents include a Pre-Development Checklist. Development should not begin
on Critical-priority gaps until resolved.

---

## Updating This Skill

1. Preserve the `name` field in SKILL.md frontmatter
2. Copy to a writable location before editing if path is read-only
3. Update `references/validation-rules.md` when new conflict patterns are found
4. Update `references/dynamic-followups.md` for new domain patterns
5. Update `scripts/validate_requirements.py` for new validation checks
6. Test with the example session after changes
