#!/usr/bin/env python3
"""
AI Requirement Analysis — Validation Script
============================================
Validates requirement session data for completeness, consistency, and
confidence before generating the Source of Truth document.

Usage:
    python validate_requirements.py --input session.json
    python validate_requirements.py                          # runs example session
    python validate_requirements.py --input s.json --output report.json
    python validate_requirements.py --input s.json --quiet --output report.json

Exit codes:
    0 — Validation passed or draft can be generated
    1 — Critical issues found that block output
"""

import json
import sys
import argparse
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


# ─────────────────────────────────────────────
# Data Structures
# ─────────────────────────────────────────────

class Severity(Enum):
    CRITICAL = "CRITICAL"
    WARNING  = "WARNING"
    INFO     = "INFO"


@dataclass
class ValidationIssue:
    code: str
    severity: Severity
    block: Optional[str]
    message: str
    resolution: str


@dataclass
class BlockConfidence:
    block_name: str
    answered: int
    total: int
    quality_score: float
    minimum_threshold: float
    score: float = field(init=False)

    def __post_init__(self):
        if self.total == 0:
            self.score = 0.0
        else:
            self.score = round((self.answered / self.total) * self.quality_score, 3)

    @property
    def passes(self) -> bool:
        return self.score >= self.minimum_threshold

    @property
    def status(self) -> str:
        if self.score >= 0.85:
            return "✅ Strong"
        elif self.score >= 0.70:
            return "⚠️  Adequate"
        elif self.score >= 0.55:
            return "⚠️  Weak"
        else:
            return "🚨 Insufficient"


@dataclass
class ManDaysAnalysis:
    stated_budget: float
    estimated_floor: float
    gap_percent: float = field(init=False)
    passes: bool = field(init=False)

    def __post_init__(self):
        if self.stated_budget > 0:
            self.gap_percent = round(
                (self.estimated_floor - self.stated_budget) / self.stated_budget * 100, 1
            )
        else:
            self.gap_percent = 100.0
        self.passes = self.gap_percent <= 30.0


# ─────────────────────────────────────────────
# Confidence Thresholds
# ─────────────────────────────────────────────

BLOCK_THRESHOLDS = {
    "vision":        {"min": 0.80, "priority": "Critical"},
    "users":         {"min": 0.75, "priority": "High"},
    "scope":         {"min": 0.90, "priority": "Critical"},
    "design":        {"min": 0.70, "priority": "High"},
    "integrations":  {"min": 0.85, "priority": "Critical"},
    "security":      {"min": 0.80, "priority": "High"},
    "technology":    {"min": 0.75, "priority": "High"},
    "budget":        {"min": 0.85, "priority": "Critical"},
    "post_launch":   {"min": 0.65, "priority": "Medium"},
}

# Feature complexity floor estimates (in mandays)
COMPLEXITY_FLOORS = {
    "simple": 4,
    "medium": 7,
    "complex": 12,
    "xl": 20,
}

INTEGRATION_EFFORT = 4  # average mandays per integration
AUTH_SYSTEM_EFFORT = 6
DEVOPS_SETUP_EFFORT = 4
ADMIN_PANEL_EFFORT = 12
MOBILE_MULTIPLIER = 0.5  # +50% per platform
QA_PERCENTAGE = 0.22
BUFFER_PERCENTAGE = 0.15

# Implied integration mapping
IMPLIED_INTEGRATIONS = {
    "payment": ["payment", "checkout", "billing", "subscription", "invoice", "cart"],
    "sms":     ["otp", "sms", "verification code", "phone verification"],
    "maps":    ["location", "map", "tracking", "route", "geofence", "delivery tracking"],
    "oauth":   ["login with google", "social login", "sso", "oauth", "login with facebook"],
    "email":   ["email notification", "password reset", "email verification", "send email"],
    "push":    ["push notification", "mobile notification"],
    "storage": ["file upload", "image upload", "media upload", "attachment"],
    "search":  ["full-text search", "elasticsearch", "advanced search"],
}


# ─────────────────────────────────────────────
# Validators
# ─────────────────────────────────────────────

def validate_block_presence(session: dict) -> list[ValidationIssue]:
    """Check all 9 blocks are present in session data."""
    issues = []
    for block in BLOCK_THRESHOLDS:
        if block not in session.get("blocks", {}):
            issues.append(ValidationIssue(
                code=f"MISS-{block.upper()[:4]}",
                severity=Severity.CRITICAL,
                block=block,
                message=f"Block '{block}' is missing from session data.",
                resolution=f"Complete the {block} block before generating output."
            ))
    return issues


def validate_confidence_scores(session: dict) -> tuple[list[ValidationIssue], list[BlockConfidence]]:
    """Validate confidence scores per block against minimum thresholds."""
    issues = []
    confidences = []
    blocks = session.get("blocks", {})

    for block_name, config in BLOCK_THRESHOLDS.items():
        block_data = blocks.get(block_name, {})
        answered = block_data.get("answered_questions", 0)
        total = block_data.get("total_applicable_questions", 1)
        quality = block_data.get("average_quality_score", 0.5)

        bc = BlockConfidence(
            block_name=block_name,
            answered=answered,
            total=total,
            quality_score=quality,
            minimum_threshold=config["min"]
        )
        confidences.append(bc)

        if not bc.passes:
            severity = (
                Severity.CRITICAL if config["priority"] == "Critical"
                else Severity.WARNING
            )
            issues.append(ValidationIssue(
                code=f"CONF-{block_name.upper()[:4]}",
                severity=severity,
                block=block_name,
                message=(
                    f"Block '{block_name}' confidence {bc.score:.0%} is below "
                    f"threshold {config['min']:.0%}."
                ),
                resolution=(
                    f"Probe further in {block_name}. "
                    f"{bc.total - bc.answered} questions unanswered or low-quality."
                )
            ))

    return issues, confidences


def _get_feature_names(scope_block: dict) -> list[str]:
    """Extract lowercase feature names from scope block."""
    raw = scope_block.get("features_mvp", [])
    return [(f["name"] if isinstance(f, dict) else f).lower() for f in raw]


def validate_cross_block_conflicts(session: dict) -> list[ValidationIssue]:
    """Detect cross-block inconsistencies that would cause project failure."""
    issues = []
    blocks = session.get("blocks", {})

    users = blocks.get("users", {})
    tech = blocks.get("technology", {})
    security = blocks.get("security", {})
    scope = blocks.get("scope", {})
    integrations = blocks.get("integrations", {})
    budget = blocks.get("budget", {})
    design = blocks.get("design", {})

    features = _get_feature_names(scope)
    features_text = " ".join(features)
    declared_integrations = [i.lower() for i in integrations.get("third_party_services", [])]

    # CONF-01: Scale vs Infrastructure
    concurrent = users.get("concurrent_users_peak", 0)
    hosting = tech.get("hosting_type", "").lower()
    low_capacity = ["shared", "single vps", "basic", "free tier"]
    if concurrent > 1000 and any(h in hosting for h in low_capacity):
        issues.append(ValidationIssue(
            code="CONF-01",
            severity=Severity.CRITICAL,
            block="users/technology",
            message=(
                f"Scale mismatch: {concurrent:,} concurrent users declared, "
                f"but hosting '{hosting}' cannot support this load."
            ),
            resolution="Scale up infrastructure, revise user estimates, or add caching strategy."
        ))

    # CONF-02: Sensitive Data Without Compliance
    has_pii = security.get("handles_pii", False)
    has_financial = security.get("handles_financial_data", False)
    compliance = security.get("compliance_framework", "").strip()
    if (has_pii or has_financial) and not compliance:
        data_type = []
        if has_pii:
            data_type.append("PII")
        if has_financial:
            data_type.append("financial data")
        issues.append(ValidationIssue(
            code="CONF-02",
            severity=Severity.CRITICAL,
            block="security",
            message=(
                f"System handles {' and '.join(data_type)} but no compliance "
                f"framework declared."
            ),
            resolution="Define compliance framework (UU PDP, GDPR, PCI-DSS, HIPAA, OJK)."
        ))

    # CONF-03: Feature Implies Undeclared Integration
    for service, keywords in IMPLIED_INTEGRATIONS.items():
        feature_implies = any(k in features_text for k in keywords)
        service_declared = any(service in i for i in declared_integrations)
        if feature_implies and not service_declared:
            issues.append(ValidationIssue(
                code="CONF-03",
                severity=Severity.CRITICAL,
                block="scope/integrations",
                message=(
                    f"Features imply '{service}' integration needed, "
                    f"but not declared in integrations block."
                ),
                resolution=(
                    f"Confirm '{service}' integration scope, add to integration map "
                    f"with vendor selection and effort estimate."
                )
            ))

    # CONF-05: Architecture vs Team Maturity
    architecture = tech.get("architecture_style", "").lower()
    senior_be = budget.get("senior_backend_engineers", 0)
    has_devops = budget.get("dedicated_devops", False)
    complex_arch = ["microservice", "kubernetes", "event-driven", "event driven"]
    if any(a in architecture for a in complex_arch) and (senior_be < 2 or not has_devops):
        issues.append(ValidationIssue(
            code="CONF-05",
            severity=Severity.CRITICAL,
            block="technology/budget",
            message=(
                f"Architecture '{architecture}' requires strong DevOps and "
                f"senior backend expertise. Team composition insufficient."
            ),
            resolution=(
                "Simplify to monolith, add senior resources, "
                "or use managed services."
            )
        ))

    # CONF-06: Real-Time Feature with REST-Only Stack
    rt_keywords = ["real-time", "real time", "live", "chat", "websocket", "live tracking"]
    has_realtime = any(k in features_text for k in rt_keywords)
    api_type = tech.get("api_type", "").lower()
    if has_realtime and "rest" in api_type and "websocket" not in api_type and "sse" not in api_type:
        issues.append(ValidationIssue(
            code="CONF-06",
            severity=Severity.CRITICAL,
            block="scope/technology",
            message="Real-time features declared but stack is REST-only (no WebSocket/SSE).",
            resolution="Add WebSocket/SSE to stack or accept polling-based near-real-time."
        ))

    # CONF-07: Client Design with No Delivery SLA
    design_owner = design.get("design_owner", "").lower()
    design_deadline = design.get("design_delivery_deadline", "")
    if "client" in design_owner and not design_deadline:
        issues.append(ValidationIssue(
            code="CONF-07",
            severity=Severity.WARNING,
            block="design",
            message="Design is client-provided but no delivery deadline defined.",
            resolution="Define design delivery date and escalation path if missed."
        ))

    # CONF-08: Multi-Platform with Small Team
    platforms = []
    if tech.get("mobile_platforms"):
        platforms.extend(tech["mobile_platforms"])
    layers_in_scope = tech.get("layers_in_scope", [])
    total_layers = len(platforms) + len(layers_in_scope)
    team_size = budget.get("total_developers", 0)
    if total_layers >= 3 and 0 < team_size < 4:
        issues.append(ValidationIssue(
            code="CONF-08",
            severity=Severity.WARNING,
            block="technology/budget",
            message=(
                f"{total_layers} platform layers with {team_size} developers. "
                f"Capacity risk for timeline."
            ),
            resolution="Prioritize platforms, use cross-platform, or increase team."
        ))

    # CONF-09: Multiple Roles without Auth
    roles = users.get("user_roles", [])
    auth_method = security.get("auth_method", "").strip()
    if len(roles) >= 2 and not auth_method:
        issues.append(ValidationIssue(
            code="CONF-09",
            severity=Severity.CRITICAL,
            block="users/security",
            message=f"{len(roles)} user roles declared but no authentication method defined.",
            resolution="Define auth method and authorization model (RBAC, ABAC)."
        ))

    return issues


def validate_warnings(session: dict) -> list[ValidationIssue]:
    """Detect warning-level patterns that don't block output but must be flagged."""
    issues = []
    blocks = session.get("blocks", {})

    post_launch = blocks.get("post_launch", {})
    budget = blocks.get("budget", {})
    scope = blocks.get("scope", {})
    vision = blocks.get("vision", {})
    integrations = blocks.get("integrations", {})
    technology = blocks.get("technology", {})

    # WARN-01: No post-launch owner
    if not post_launch.get("post_launch_owner"):
        issues.append(ValidationIssue(
            code="WARN-01", severity=Severity.WARNING, block="post_launch",
            message="No post-launch owner defined. System may be orphaned after go-live.",
            resolution="Define who maintains and operates the system after launch."
        ))

    # WARN-02: No QA + many integrations
    has_qa = budget.get("dedicated_qa", False)
    integration_count = len(integrations.get("third_party_services", []))
    if not has_qa and integration_count >= 3:
        issues.append(ValidationIssue(
            code="WARN-02", severity=Severity.WARNING, block="budget/integrations",
            message=f"No dedicated QA with {integration_count} integrations. High defect risk.",
            resolution="Allocate QA resource or define developer-owned testing strategy."
        ))

    # WARN-04: No contingency buffer
    if not budget.get("contingency_buffer_included", False):
        issues.append(ValidationIssue(
            code="WARN-04", severity=Severity.WARNING, block="budget",
            message="No contingency buffer in mandays estimate.",
            resolution="Add 10–20% buffer for discovered complexity and rework."
        ))

    # WARN-05: Fixed deadline + undefined scope
    if vision.get("deadline_is_fixed", False) and not scope.get("scope_fully_defined", False):
        issues.append(ValidationIssue(
            code="WARN-05", severity=Severity.WARNING, block="vision/scope",
            message="Fixed deadline with undefined scope — classic scope creep setup.",
            resolution="Fix the scope firmly or make the deadline flexible."
        ))

    # WARN-07: No staging environment
    if not technology.get("has_staging_environment", True):
        issues.append(ValidationIssue(
            code="WARN-07", severity=Severity.WARNING, block="technology",
            message="No staging environment mentioned. Risky direct-to-production deploys.",
            resolution="Plan a staging environment that mirrors production."
        ))

    # WARN-12: Data migration without rollback
    has_migration = integrations.get("has_data_migration", False)
    has_rollback = integrations.get("migration_rollback_plan", False)
    if has_migration and not has_rollback:
        issues.append(ValidationIssue(
            code="WARN-12", severity=Severity.WARNING, block="integrations",
            message="Data migration planned but no rollback strategy defined.",
            resolution="Define rollback plan and acceptable downtime window."
        ))

    # WARN-13: No monitoring strategy
    if not post_launch.get("monitoring_strategy"):
        issues.append(ValidationIssue(
            code="WARN-13", severity=Severity.WARNING, block="post_launch",
            message="No monitoring or alerting strategy defined.",
            resolution="Plan monitoring (uptime, errors, performance) before go-live."
        ))

    # WARN-14: Junior-only team on large project
    senior_count = budget.get("senior_backend_engineers", 0) + budget.get("senior_frontend_engineers", 0)
    total_mandays = budget.get("total_mandays_budget", 0)
    if senior_count == 0 and total_mandays > 60:
        issues.append(ValidationIssue(
            code="WARN-14", severity=Severity.WARNING, block="budget",
            message="No senior engineers on a project exceeding 60 mandays.",
            resolution="Add senior technical leadership or reduce project scope."
        ))

    return issues


def validate_mandays(session: dict) -> tuple[Optional[ManDaysAnalysis], Optional[ValidationIssue]]:
    """Compare stated budget against estimated floor from features."""
    budget_block = session.get("blocks", {}).get("budget", {})
    scope_block = session.get("blocks", {}).get("scope", {})

    stated_budget = budget_block.get("total_mandays_budget", 0)
    if stated_budget == 0:
        return None, None

    # Calculate floor from features
    features = scope_block.get("features_mvp", [])
    floor = 0.0

    for feature in features:
        complexity = feature.get("complexity", "medium").lower() if isinstance(feature, dict) else "medium"
        floor += COMPLEXITY_FLOORS.get(complexity, 7)

    # Integration effort
    integrations = session.get("blocks", {}).get("integrations", {})
    floor += len(integrations.get("third_party_services", [])) * INTEGRATION_EFFORT

    # Auth system if multi-role
    users = session.get("blocks", {}).get("users", {})
    if len(users.get("user_roles", [])) > 1:
        floor += AUTH_SYSTEM_EFFORT

    # DevOps setup
    floor += DEVOPS_SETUP_EFFORT

    # Admin panel (check if in scope)
    tech = session.get("blocks", {}).get("technology", {})
    layers = tech.get("layers_in_scope", [])
    if "admin" in " ".join(layers).lower():
        floor += ADMIN_PANEL_EFFORT

    # Mobile multiplier
    mobile_platforms = tech.get("mobile_platforms", [])
    if mobile_platforms:
        floor *= (1 + len(mobile_platforms) * MOBILE_MULTIPLIER * 0.3)

    # QA
    floor *= (1 + QA_PERCENTAGE)

    # Buffer
    floor *= (1 + BUFFER_PERCENTAGE)
    floor = round(floor, 1)

    analysis = ManDaysAnalysis(stated_budget=stated_budget, estimated_floor=floor)
    issue = None

    if not analysis.passes:
        issue = ValidationIssue(
            code="CONF-04",
            severity=Severity.CRITICAL,
            block="budget/scope",
            message=(
                f"Budget mismatch: stated {stated_budget} mandays, "
                f"estimated floor {floor} mandays "
                f"(gap: {analysis.gap_percent:+.1f}%)."
            ),
            resolution=(
                "Resolve via: (A) Cut scope — defer features to post-launch, "
                "(B) Increase budget, or (C) Extend timeline."
            )
        )

    return analysis, issue


# ─────────────────────────────────────────────
# Report Generation
# ─────────────────────────────────────────────

def generate_report(
    session: dict,
    all_issues: list[ValidationIssue],
    confidences: list[BlockConfidence],
    mandays: Optional[ManDaysAnalysis]
) -> dict:
    """Compile full validation report."""

    criticals = [i for i in all_issues if i.severity == Severity.CRITICAL]
    warnings = [i for i in all_issues if i.severity == Severity.WARNING]

    overall = (
        sum(bc.score for bc in confidences) / len(confidences)
        if confidences else 0.0
    )

    if overall >= 0.85:
        readiness = "Ready to proceed"
        icon = "✅"
    elif overall >= 0.70:
        readiness = "Proceed with caution — resolve flagged gaps in Sprint 1"
        icon = "⚠️"
    elif overall >= 0.55:
        readiness = "Significant gaps — resolve before development begins"
        icon = "⚠️"
    else:
        readiness = "Not ready — additional discovery session required"
        icon = "🚨"

    can_generate = len(criticals) == 0 or session.get("allow_draft_with_gaps", True)
    doc_status = "FINAL" if len(criticals) == 0 else "DRAFT — Pending Gap Resolution"

    return {
        "validation_passed": len(criticals) == 0,
        "can_generate_output": can_generate,
        "document_status": doc_status,
        "summary": {
            "critical_count": len(criticals),
            "warning_count": len(warnings),
            "overall_confidence": round(overall * 100, 1),
            "readiness": f"{icon} {readiness}",
        },
        "block_confidence": [
            {
                "block": bc.block_name,
                "score": f"{bc.score:.0%}",
                "threshold": f"{bc.minimum_threshold:.0%}",
                "status": bc.status,
                "answered": bc.answered,
                "total": bc.total,
            }
            for bc in confidences
        ],
        "mandays_analysis": {
            "stated_budget": mandays.stated_budget,
            "estimated_floor": mandays.estimated_floor,
            "gap_percent": f"{mandays.gap_percent:+.1f}%",
            "passes": mandays.passes,
        } if mandays else None,
        "critical_issues": [
            {
                "code": i.code,
                "block": i.block,
                "message": i.message,
                "resolution": i.resolution,
            }
            for i in criticals
        ],
        "warnings": [
            {
                "code": i.code,
                "block": i.block,
                "message": i.message,
                "resolution": i.resolution,
            }
            for i in warnings
        ],
    }


def print_report(report: dict) -> None:
    """Print a human-readable validation report."""

    print("\n" + "═" * 64)
    print("  AI REQUIREMENT ANALYSIS — VALIDATION REPORT")
    print("═" * 64)

    s = report["summary"]
    print(f"\n  Overall Confidence:  {s['overall_confidence']}%")
    print(f"  Readiness:           {s['readiness']}")
    print(f"  Document Status:     {report['document_status']}")
    print(f"  Critical Issues:     {s['critical_count']}")
    print(f"  Warnings:            {s['warning_count']}")

    print("\n" + "─" * 64)
    print("  BLOCK CONFIDENCE SCORES")
    print("─" * 64)
    for bc in report["block_confidence"]:
        score_val = float(bc["score"].strip("%"))
        bar = "█" * int(score_val / 10)
        pad = "░" * (10 - int(score_val / 10))
        print(f"  {bc['block']:<15} {bc['score']:>5}  {bar}{pad}  {bc['status']}")

    if report.get("mandays_analysis"):
        md = report["mandays_analysis"]
        print("\n" + "─" * 64)
        print("  MANDAYS REALITY CHECK")
        print("─" * 64)
        print(f"  Stated Budget:    {md['stated_budget']} mandays")
        print(f"  Estimated Floor:  {md['estimated_floor']} mandays")
        print(f"  Gap:              {md['gap_percent']}")
        status = "✅ Within range" if md["passes"] else "🚨 Exceeds 30% threshold"
        print(f"  Status:           {status}")

    if report["critical_issues"]:
        print("\n" + "─" * 64)
        print("  🚨 CRITICAL ISSUES (must resolve before FINAL)")
        print("─" * 64)
        for issue in report["critical_issues"]:
            print(f"\n  [{issue['code']}] Block: {issue['block']}")
            print(f"  Problem:    {issue['message']}")
            print(f"  Resolution: {issue['resolution']}")

    if report["warnings"]:
        print("\n" + "─" * 64)
        print("  ⚠️  WARNINGS (added to Risk Register)")
        print("─" * 64)
        for w in report["warnings"]:
            print(f"\n  [{w['code']}] Block: {w['block']}")
            print(f"  {w['message']}")

    print("\n" + "─" * 64)
    if report["can_generate_output"]:
        print(f"  ✅ Document can be generated as: {report['document_status']}")
    else:
        print("  ❌ OUTPUT BLOCKED: Resolve critical issues first.")
    print("═" * 64 + "\n")


# ─────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────

def run_validation(session: dict) -> dict:
    """Run full validation pipeline and return report."""
    all_issues = []

    all_issues.extend(validate_block_presence(session))
    conf_issues, confidences = validate_confidence_scores(session)
    all_issues.extend(conf_issues)
    all_issues.extend(validate_cross_block_conflicts(session))
    all_issues.extend(validate_warnings(session))

    mandays, mandays_issue = validate_mandays(session)
    if mandays_issue:
        all_issues.append(mandays_issue)

    return generate_report(session, all_issues, confidences, mandays)


def main():
    parser = argparse.ArgumentParser(
        description="Validate AI requirement analysis session data."
    )
    parser.add_argument("--input", "-i", help="Path to session JSON file", type=str)
    parser.add_argument("--output", "-o", help="Path to write JSON report", type=str)
    parser.add_argument("--quiet", "-q", help="JSON only, no human output", action="store_true")
    args = parser.parse_args()

    if args.input:
        try:
            with open(args.input, "r") as f:
                session = json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found: {args.input}", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("No input file. Running example session for demonstration.\n")
        session = _example_session()

    report = run_validation(session)

    if not args.quiet:
        print_report(report)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(report, f, indent=2)
        print(f"Report saved to: {args.output}")

    sys.exit(0 if report["can_generate_output"] else 1)


def _example_session() -> dict:
    """Example session that triggers multiple validation checks."""
    return {
        "allow_draft_with_gaps": True,
        "blocks": {
            "vision": {
                "answered_questions": 7,
                "total_applicable_questions": 9,
                "average_quality_score": 0.85,
                "deadline_is_fixed": True,
            },
            "users": {
                "answered_questions": 8,
                "total_applicable_questions": 11,
                "average_quality_score": 0.80,
                "concurrent_users_peak": 5000,
                "user_roles": ["admin", "manager", "staff", "customer"],
            },
            "scope": {
                "answered_questions": 10,
                "total_applicable_questions": 13,
                "average_quality_score": 0.75,
                "scope_fully_defined": False,
                "features_mvp": [
                    {"name": "User authentication", "complexity": "medium"},
                    {"name": "Product catalog", "complexity": "medium"},
                    {"name": "Shopping cart & checkout", "complexity": "complex"},
                    {"name": "Order management", "complexity": "complex"},
                    {"name": "Admin dashboard", "complexity": "xl"},
                    {"name": "Real-time order tracking", "complexity": "complex"},
                ],
            },
            "design": {
                "answered_questions": 5,
                "total_applicable_questions": 10,
                "average_quality_score": 0.70,
                "design_owner": "client provides mockups",
                "design_delivery_deadline": "",
            },
            "integrations": {
                "answered_questions": 6,
                "total_applicable_questions": 10,
                "average_quality_score": 0.80,
                "third_party_services": ["midtrans", "firebase", "sendgrid"],
                "has_data_migration": False,
            },
            "security": {
                "answered_questions": 7,
                "total_applicable_questions": 11,
                "average_quality_score": 0.75,
                "handles_pii": True,
                "handles_financial_data": True,
                "compliance_framework": "",
                "auth_method": "username_password",
            },
            "technology": {
                "answered_questions": 7,
                "total_applicable_questions": 11,
                "average_quality_score": 0.80,
                "hosting_type": "AWS EC2",
                "architecture_style": "monolith with service separation",
                "api_type": "REST + WebSocket",
                "mobile_platforms": ["android"],
                "layers_in_scope": ["web_frontend", "backend_api", "admin_panel"],
            },
            "budget": {
                "answered_questions": 8,
                "total_applicable_questions": 11,
                "average_quality_score": 0.85,
                "total_mandays_budget": 45,
                "total_developers": 3,
                "dedicated_qa": False,
                "dedicated_devops": False,
                "contingency_buffer_included": False,
                "senior_backend_engineers": 1,
                "senior_frontend_engineers": 0,
            },
            "post_launch": {
                "answered_questions": 4,
                "total_applicable_questions": 10,
                "average_quality_score": 0.65,
                "post_launch_owner": "",
                "monitoring_strategy": "",
            },
        }
    }


if __name__ == "__main__":
    main()
