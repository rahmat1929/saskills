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
- Produces an 11-section Source of Truth document with requirement IDs, traceability,
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
│   ├── validation-rules.md           # Cross-block conflict matrix & mandays guide
│   ├── dynamic-followups.md          # Context-triggered follow-up questions by domain
│   └── output-template.md            # Source of Truth template with ID schemes & Mermaid
└── scripts/
    └── validate_requirements.py      # Python validation script
```

---

## Workflow Phases

| Phase | Goal | Key Reference File |
|-------|------|-------------------|
| 1. Detect Context | Determine Path A (doc) or Path B (interview) | SKILL.md |
| 2. Structured Interview | Gather info across 9 blocks progressively | interview-flow.md, question-bank.md |
| 3. Validate | Catch cross-block conflicts, run mandays check | validation-rules.md |
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

```bash
# Demo mode (built-in example session)
python scripts/validate_requirements.py

# Validate a session file
python scripts/validate_requirements.py --input session.json

# Save JSON report
python scripts/validate_requirements.py --input session.json --output report.json

# Quiet mode (JSON only)
python scripts/validate_requirements.py --input session.json --quiet --output report.json
```

### Exit Codes
- `0` — Validation passed or draft can be generated
- `1` — Critical issues found that block output

---

## Session JSON Schema

The validation script expects a session JSON with the following structure.
All fields are optional — missing fields are treated as unanswered.

```json
{
  "allow_draft_with_gaps": true,
  "blocks": {
    "vision": {
      "answered_questions": 7,
      "total_applicable_questions": 9,
      "average_quality_score": 0.85,
      "deadline_is_fixed": true
    },
    "users": {
      "answered_questions": 8,
      "total_applicable_questions": 11,
      "average_quality_score": 0.80,
      "concurrent_users_peak": 1000,
      "user_roles": ["admin", "staff", "customer"]
    },
    "scope": {
      "answered_questions": 11,
      "total_applicable_questions": 13,
      "average_quality_score": 0.90,
      "scope_fully_defined": true,
      "features_mvp": [
        { "name": "User authentication", "complexity": "medium" },
        { "name": "Product catalog", "complexity": "medium" }
      ]
    },
    "design": {
      "answered_questions": 7,
      "total_applicable_questions": 10,
      "average_quality_score": 0.75,
      "design_owner": "in-house designer",
      "design_delivery_deadline": "2026-04-01"
    },
    "integrations": {
      "answered_questions": 8,
      "total_applicable_questions": 10,
      "average_quality_score": 0.85,
      "third_party_services": ["midtrans", "firebase"],
      "has_data_migration": false
    },
    "security": {
      "answered_questions": 9,
      "total_applicable_questions": 11,
      "average_quality_score": 0.85,
      "handles_pii": true,
      "handles_financial_data": false,
      "compliance_framework": "UU PDP",
      "auth_method": "username_password"
    },
    "technology": {
      "answered_questions": 9,
      "total_applicable_questions": 11,
      "average_quality_score": 0.80,
      "hosting_type": "AWS EC2 with load balancer",
      "architecture_style": "monolith",
      "api_type": "REST",
      "mobile_platforms": [],
      "layers_in_scope": ["web_frontend", "backend_api"]
    },
    "budget": {
      "answered_questions": 9,
      "total_applicable_questions": 11,
      "average_quality_score": 0.90,
      "total_mandays_budget": 60,
      "total_developers": 4,
      "dedicated_qa": true,
      "dedicated_devops": false,
      "contingency_buffer_included": true,
      "senior_backend_engineers": 2,
      "senior_frontend_engineers": 1
    },
    "post_launch": {
      "answered_questions": 6,
      "total_applicable_questions": 10,
      "average_quality_score": 0.70,
      "post_launch_owner": "client IT team",
      "monitoring_strategy": "uptime robot + sentry"
    }
  }
}
```

### Quality Score Guide

| Score | Meaning |
|-------|---------|
| 1.0 | Specific, measurable, confirmed by user |
| 0.7 | General but reasonable |
| 0.4 | Vague or assumed |
| 0.0 | Unanswered or skipped |

### Feature Complexity Guide

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
