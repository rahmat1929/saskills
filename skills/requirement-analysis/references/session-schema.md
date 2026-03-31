# Session Schema Reference

> This file defines the exact JSON structure the validation script expects. At
> Phase 3, construct this JSON from the data you tracked during the interview,
> then run the validation script against it.

---

## Full Schema

```json
{
  "allow_draft_with_gaps": true,
  "blocks": {
    "vision": {
      "answered_questions": 0,
      "total_applicable_questions": 0,
      "average_quality_score": 0.0,
      "deadline_is_fixed": false
    },
    "users": {
      "answered_questions": 0,
      "total_applicable_questions": 0,
      "average_quality_score": 0.0,
      "concurrent_users_peak": 0,
      "user_roles": []
    },
    "scope": {
      "answered_questions": 0,
      "total_applicable_questions": 0,
      "average_quality_score": 0.0,
      "scope_fully_defined": false,
      "features_mvp": []
    },
    "design": {
      "answered_questions": 0,
      "total_applicable_questions": 0,
      "average_quality_score": 0.0,
      "design_owner": "",
      "design_delivery_deadline": ""
    },
    "integrations": {
      "answered_questions": 0,
      "total_applicable_questions": 0,
      "average_quality_score": 0.0,
      "third_party_services": [],
      "has_data_migration": false,
      "migration_rollback_plan": false
    },
    "security": {
      "answered_questions": 0,
      "total_applicable_questions": 0,
      "average_quality_score": 0.0,
      "handles_pii": false,
      "handles_financial_data": false,
      "compliance_framework": "",
      "auth_method": ""
    },
    "technology": {
      "answered_questions": 0,
      "total_applicable_questions": 0,
      "average_quality_score": 0.0,
      "hosting_type": "",
      "architecture_style": "",
      "api_type": "",
      "mobile_platforms": [],
      "layers_in_scope": [],
      "has_staging_environment": true
    },
    "budget": {
      "answered_questions": 0,
      "total_applicable_questions": 0,
      "average_quality_score": 0.0,
      "total_mandays_budget": 0,
      "total_developers": 0,
      "dedicated_qa": false,
      "dedicated_devops": false,
      "contingency_buffer_included": false,
      "senior_backend_engineers": 0,
      "senior_frontend_engineers": 0
    },
    "post_launch": {
      "answered_questions": 0,
      "total_applicable_questions": 0,
      "average_quality_score": 0.0,
      "post_launch_owner": "",
      "monitoring_strategy": ""
    }
  }
}
```

---

## Field Reference

### Global Fields

| Field | Type | Description |
|-------|------|------------|
| `allow_draft_with_gaps` | boolean | If `true`, document can be generated as DRAFT even with critical issues. If `false`, output is blocked until all critical issues are resolved. Default: `true`. |

### Common Block Fields (present in every block)

| Field | Type | Description |
|-------|------|------------|
| `answered_questions` | integer | Number of questions the user answered substantively. GAPs don't count. |
| `total_applicable_questions` | integer | Total questions asked or determined applicable. Skipped-as-irrelevant questions don't count. |
| `average_quality_score` | float (0.0–1.0) | Average quality across answered questions. See quality scoring guide below. |

### Block-Specific Fields

#### vision
| Field | Type | Description | Used By |
|-------|------|------------|---------|
| `deadline_is_fixed` | boolean | Is the go-live date contractual / hard? | WARN-05 (fixed deadline + undefined scope) |

#### users
| Field | Type | Description | Used By |
|-------|------|------------|---------|
| `concurrent_users_peak` | integer | Expected peak simultaneous users | CONF-01 (scale vs infra) |
| `user_roles` | string[] | List of user role names | CONF-09 (roles without auth), mandays calc |

#### scope
| Field | Type | Description | Used By |
|-------|------|------------|---------|
| `scope_fully_defined` | boolean | Has every feature been classified as MVP or post-launch? | WARN-05 |
| `features_mvp` | object[] | MVP features with name and complexity | CONF-03, CONF-04, CONF-06, mandays calc |

**features_mvp item format:**
```json
{ "name": "User authentication", "complexity": "medium" }
```

Complexity values and their mandays floor:
| Value | Mandays Floor | Example |
|-------|--------------|---------|
| `simple` | 4 | Basic list page, simple form |
| `medium` | 7 | CRUD module with validation |
| `complex` | 12 | Multi-step flow with business logic |
| `xl` | 20 | Real-time system, complex dashboard |

#### design
| Field | Type | Description | Used By |
|-------|------|------------|---------|
| `design_owner` | string | Who provides design. Include "client" in string if client-provided. | CONF-07 |
| `design_delivery_deadline` | string | ISO date or empty string | CONF-07 (no deadline) |

#### integrations
| Field | Type | Description | Used By |
|-------|------|------------|---------|
| `third_party_services` | string[] | Names of third-party services (lowercase) | CONF-03, WARN-02, mandays calc |
| `has_data_migration` | boolean | Is data migration in scope? | WARN-12 |
| `migration_rollback_plan` | boolean | Is a rollback plan defined? | WARN-12 |

#### security
| Field | Type | Description | Used By |
|-------|------|------------|---------|
| `handles_pii` | boolean | Does the system handle personally identifiable information? | CONF-02 |
| `handles_financial_data` | boolean | Does the system handle financial data? | CONF-02 |
| `compliance_framework` | string | Name of compliance framework, or empty | CONF-02 |
| `auth_method` | string | Authentication method name, or empty | CONF-09 |

#### technology
| Field | Type | Description | Used By |
|-------|------|------------|---------|
| `hosting_type` | string | Hosting description. Low-capacity triggers: "shared", "single vps", "basic", "free tier" | CONF-01 |
| `architecture_style` | string | Complex triggers: "microservice", "kubernetes", "event-driven" | CONF-05 |
| `api_type` | string | Must include "websocket" or "sse" if real-time features exist | CONF-06 |
| `mobile_platforms` | string[] | `["ios"]`, `["android"]`, `["ios", "android"]`, or `[]` | CONF-08, mandays calc |
| `layers_in_scope` | string[] | Platform layers: "web_frontend", "backend_api", "admin_panel", "background_workers" | CONF-08, mandays calc |
| `has_staging_environment` | boolean | Is a staging env planned? Default `true` if not discussed. | WARN-07 |

#### budget
| Field | Type | Description | Used By |
|-------|------|------------|---------|
| `total_mandays_budget` | number | Total budget in mandays | CONF-04 |
| `total_developers` | integer | Total developer headcount | CONF-08 |
| `dedicated_qa` | boolean | Is there a dedicated QA engineer? | WARN-02 |
| `dedicated_devops` | boolean | Is there a dedicated DevOps engineer? | CONF-05 |
| `contingency_buffer_included` | boolean | Is buffer built into the estimate? | WARN-04 |
| `senior_backend_engineers` | integer | Count of senior BE engineers | CONF-05, WARN-14 |
| `senior_frontend_engineers` | integer | Count of senior FE engineers | WARN-14 |

#### post_launch
| Field | Type | Description | Used By |
|-------|------|------------|---------|
| `post_launch_owner` | string | Who maintains system after launch, or empty | WARN-01 |
| `monitoring_strategy` | string | Monitoring approach description, or empty | WARN-13 |

---

## Quality Score Guide

When assigning `average_quality_score` for a block, rate each answered question:

| Score | Criteria | Example |
|-------|----------|---------|
| 1.0 | Specific, measurable, confirmed by user | "500 concurrent users at peak, based on last year's analytics" |
| 0.7 | General but reasonable — workable, not precise | "Probably a few hundred users at peak" |
| 0.4 | Vague, assumed, or user seemed uncertain | "A lot of users, maybe" |
| 0.0 | Unanswered or explicitly skipped | — |

Then average across all answered questions in the block.

---

## Construction Example

After interviewing a user about an e-commerce project, you might construct:

```json
{
  "allow_draft_with_gaps": true,
  "blocks": {
    "vision": {
      "answered_questions": 7,
      "total_applicable_questions": 8,
      "average_quality_score": 0.85,
      "deadline_is_fixed": true
    },
    "users": {
      "answered_questions": 9,
      "total_applicable_questions": 10,
      "average_quality_score": 0.80,
      "concurrent_users_peak": 2000,
      "user_roles": ["admin", "seller", "buyer", "support"]
    },
    "scope": {
      "answered_questions": 12,
      "total_applicable_questions": 13,
      "average_quality_score": 0.90,
      "scope_fully_defined": true,
      "features_mvp": [
        { "name": "User authentication with social login", "complexity": "medium" },
        { "name": "Product catalog with search", "complexity": "complex" },
        { "name": "Shopping cart and checkout", "complexity": "complex" },
        { "name": "Order management", "complexity": "complex" },
        { "name": "Seller dashboard", "complexity": "xl" },
        { "name": "Admin panel", "complexity": "xl" },
        { "name": "Push notifications", "complexity": "simple" }
      ]
    },
    "design": {
      "answered_questions": 8,
      "total_applicable_questions": 9,
      "average_quality_score": 0.80,
      "design_owner": "in-house designer",
      "design_delivery_deadline": "2026-05-01"
    },
    "integrations": {
      "answered_questions": 8,
      "total_applicable_questions": 9,
      "average_quality_score": 0.85,
      "third_party_services": ["midtrans", "firebase", "sendgrid", "aws_s3", "algolia"],
      "has_data_migration": true,
      "migration_rollback_plan": true
    },
    "security": {
      "answered_questions": 9,
      "total_applicable_questions": 10,
      "average_quality_score": 0.85,
      "handles_pii": true,
      "handles_financial_data": true,
      "compliance_framework": "UU PDP + PCI-DSS awareness",
      "auth_method": "username_password + oauth2"
    },
    "technology": {
      "answered_questions": 10,
      "total_applicable_questions": 11,
      "average_quality_score": 0.85,
      "hosting_type": "AWS EC2 with ALB and auto-scaling",
      "architecture_style": "monolith with service separation",
      "api_type": "REST + WebSocket for notifications",
      "mobile_platforms": ["android"],
      "layers_in_scope": ["web_frontend", "backend_api", "admin_panel", "background_workers"],
      "has_staging_environment": true
    },
    "budget": {
      "answered_questions": 10,
      "total_applicable_questions": 11,
      "average_quality_score": 0.90,
      "total_mandays_budget": 120,
      "total_developers": 5,
      "dedicated_qa": true,
      "dedicated_devops": true,
      "contingency_buffer_included": true,
      "senior_backend_engineers": 2,
      "senior_frontend_engineers": 1
    },
    "post_launch": {
      "answered_questions": 7,
      "total_applicable_questions": 9,
      "average_quality_score": 0.75,
      "post_launch_owner": "client IT team with vendor on retainer for 3 months",
      "monitoring_strategy": "Sentry for errors, UptimeRobot for availability, CloudWatch for infra"
    }
  }
}
```

This example would likely pass validation with few or no critical issues, generating
a FINAL document status.
