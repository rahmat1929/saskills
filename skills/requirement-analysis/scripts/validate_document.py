#!/usr/bin/env python3
"""
AI Requirement Analysis — Document Validator
=============================================
Validates a generated Source of Truth document (.md) for structural
completeness, cross-reference integrity, and logical consistency.

This complements validate_requirements.py (which validates session data).
Use this script AFTER the document has been generated or manually edited.

Usage:
    python validate_document.py --input requirements.md
    python validate_document.py --input requirements.md --output report.json
    python validate_document.py --input requirements.md --quiet

Exit codes:
    0 — Document is valid or has warnings only
    1 — Critical issues found
"""

import json
import re
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
class DocIssue:
    code: str
    severity: Severity
    section: str
    message: str
    resolution: str


# ─────────────────────────────────────────────
# Document Parsing
# ─────────────────────────────────────────────

# ID patterns
ID_PATTERNS = {
    "BR":  re.compile(r"BR-(\d{3})"),
    "FT":  re.compile(r"FT-(\d{3})"),
    "NFR": re.compile(r"NFR-(\d{3})"),
    "INT": re.compile(r"INT-(\d{3})"),
    "RSK": re.compile(r"RSK-(\d{3})"),
    "GAP": re.compile(r"GAP-(\d{3})"),
    "UR":  re.compile(r"UR-(\d{3})"),
    "UJ":  re.compile(r"UJ-(\d{3})"),
    "REF": re.compile(r"REF-(\d{3})"),
}

# Section header patterns (flexible numbering)
SECTION_PATTERNS = {
    "executive_summary":  re.compile(r"^#+\s*(?:\d+\.)?\s*Executive Summary", re.MULTILINE),
    "reference_analysis": re.compile(r"^#+\s*(?:\d+\.)?\s*Reference Analysis", re.MULTILINE),
    "business_requirements": re.compile(r"^#+\s*(?:\d+\.)?\s*Business Requirements", re.MULTILINE),
    "ux_design":          re.compile(r"^#+\s*(?:\d+\.)?\s*UX\s*[&|and]\s*Design", re.MULTILINE),
    "technical_specs":    re.compile(r"^#+\s*(?:\d+\.)?\s*Technical Specifications", re.MULTILINE),
    "integration_map":    re.compile(r"^#+\s*(?:\d+\.)?\s*Integration Map", re.MULTILINE),
    "risk_register":      re.compile(r"^#+\s*(?:\d+\.)?\s*Risk Register", re.MULTILINE),
    "scope_boundary":     re.compile(r"^#+\s*(?:\d+\.)?\s*Scope Boundary", re.MULTILINE),
    "mandays_estimation": re.compile(r"^#+\s*(?:\d+\.)?\s*Mandays\s*Estimation", re.MULTILINE),
    "open_questions":     re.compile(r"^#+\s*(?:\d+\.)?\s*Open Questions", re.MULTILINE),
    "confidence_score":   re.compile(r"^#+\s*(?:\d+\.)?\s*Confidence Score", re.MULTILINE),
    "interview_coverage": re.compile(r"^#+\s*(?:\d+\.)?\s*Interview Coverage", re.MULTILINE),
}

REQUIRED_SECTIONS = [
    "executive_summary",
    "business_requirements",
    "ux_design",
    "technical_specs",
    "integration_map",
    "risk_register",
    "scope_boundary",
    "mandays_estimation",
    "open_questions",
    "confidence_score",
    "interview_coverage",
]


def parse_document(content: str) -> dict:
    """Parse the markdown document and extract structured data."""

    result = {
        "sections_found": [],
        "sections_missing": [],
        "ids": {prefix: set() for prefix in ID_PATTERNS},
        "document_status": "",
        "mandays_total": None,
        "mandays_budget": None,
        "confidence_scores": {},
        "features_in_scope": set(),
        "features_in_estimation": set(),
        "integrations_declared": set(),
        "risks_with_links": {},       # RSK-NNN -> [linked FT/INT IDs]
        "features_with_br_links": {}, # FT-NNN -> [linked BR IDs]
        "gaps_with_owners": {},       # GAP-NNN -> owner string
        "gap_priorities": {},         # GAP-NNN -> priority
        "raw_sections": {},
    }

    # ── Detect document status ──
    if "DRAFT" in content[:500]:
        result["document_status"] = "DRAFT"
    elif "FINAL" in content[:500]:
        result["document_status"] = "FINAL"
    else:
        result["document_status"] = "UNKNOWN"

    # ── Find sections ──
    for section_name, pattern in SECTION_PATTERNS.items():
        if pattern.search(content):
            result["sections_found"].append(section_name)
        elif section_name in REQUIRED_SECTIONS:
            result["sections_missing"].append(section_name)

    # ── Extract all IDs ──
    for prefix, pattern in ID_PATTERNS.items():
        result["ids"][prefix] = set(pattern.findall(content))

    # ── Split content into sections for targeted parsing ──
    section_positions = []
    for section_name, pattern in SECTION_PATTERNS.items():
        match = pattern.search(content)
        if match:
            section_positions.append((match.start(), section_name))
    section_positions.sort()

    for i, (start, name) in enumerate(section_positions):
        end = section_positions[i + 1][0] if i + 1 < len(section_positions) else len(content)
        result["raw_sections"][name] = content[start:end]

    # ── Parse feature traceability (FT -> BR links) ──
    tech_section = result["raw_sections"].get("technical_specs", "")
    # Look for patterns like "Linked Requirements** | BR-001, BR-003"
    ft_blocks = re.split(r"(?=\|\s*\*\*ID\*\*\s*\|\s*FT-)", tech_section)
    for block in ft_blocks:
        ft_match = re.search(r"FT-(\d{3})", block)
        if ft_match:
            ft_id = ft_match.group(0)
            br_links = ID_PATTERNS["BR"].findall(block)
            result["features_with_br_links"][ft_id] = [f"BR-{b}" for b in br_links]

    # ── Parse risk links (RSK -> FT/INT) ──
    risk_section = result["raw_sections"].get("risk_register", "")
    for line in risk_section.split("\n"):
        rsk_match = re.search(r"RSK-(\d{3})", line)
        if rsk_match:
            rsk_id = rsk_match.group(0)
            ft_links = [f"FT-{f}" for f in ID_PATTERNS["FT"].findall(line)]
            int_links = [f"INT-{i}" for i in ID_PATTERNS["INT"].findall(line)]
            result["risks_with_links"][rsk_id] = ft_links + int_links

    # ── Parse gaps (GAP -> owner, priority) ──
    gaps_section = result["raw_sections"].get("open_questions", "")
    for line in gaps_section.split("\n"):
        gap_match = re.search(r"GAP-(\d{3})", line)
        if gap_match:
            gap_id = gap_match.group(0)
            # Try to extract owner from table row
            cells = [c.strip() for c in line.split("|") if c.strip()]
            if len(cells) >= 4:
                result["gaps_with_owners"][gap_id] = cells[3] if len(cells) > 3 else ""
                result["gap_priorities"][gap_id] = cells[4] if len(cells) > 4 else ""

    # ── Parse scope boundary (features in MVP) ──
    scope_section = result["raw_sections"].get("scope_boundary", "")
    mvp_zone = scope_section.split("Post-Launch")[0] if "Post-Launch" in scope_section else scope_section
    for ft_id in ID_PATTERNS["FT"].findall(mvp_zone):
        result["features_in_scope"].add(f"FT-{ft_id}")

    # ── Parse mandays estimation ──
    mandays_section = result["raw_sections"].get("mandays_estimation", "")
    for ft_id in ID_PATTERNS["FT"].findall(mandays_section):
        result["features_in_estimation"].add(f"FT-{ft_id}")

    # Try to extract total mandays
    total_match = re.search(
        r"(?:Grand\s*Total|TOTAL)[^\d]*?(\d+(?:\.\d+)?)\s*(?:mandays)?",
        mandays_section, re.IGNORECASE
    )
    if total_match:
        result["mandays_total"] = float(total_match.group(1))

    # ── Parse confidence scores ──
    confidence_section = result["raw_sections"].get("confidence_score", "")
    score_pattern = re.compile(r"\|\s*([^|]+?)\s*\|\s*(\d+)\s*%")
    for match in score_pattern.finditer(confidence_section):
        dimension = match.group(1).strip()
        score = int(match.group(2))
        result["confidence_scores"][dimension] = score

    # ── Parse integration inventory ──
    int_section = result["raw_sections"].get("integration_map", "")
    for int_id in ID_PATTERNS["INT"].findall(int_section):
        result["integrations_declared"].add(f"INT-{int_id}")

    return result


# ─────────────────────────────────────────────
# Validators
# ─────────────────────────────────────────────

def validate_structure(parsed: dict) -> list[DocIssue]:
    """Check all required sections are present."""
    issues = []
    for section in parsed["sections_missing"]:
        display_name = section.replace("_", " ").title()
        issues.append(DocIssue(
            code="DOC-MISS",
            severity=Severity.CRITICAL,
            section=section,
            message=f"Required section '{display_name}' is missing from the document.",
            resolution=f"Add the {display_name} section following the output template."
        ))
    return issues


def validate_subsections(parsed: dict) -> list[DocIssue]:
    """Check key subsections are present within required sections."""
    issues = []
    content = ""
    for sec_text in parsed["raw_sections"].values():
        content += sec_text

    # Define expected subsections: (parent, subsection pattern, display name)
    subsection_checks = [
        # Section 3 — Business Requirements
        ("business_requirements", r"(?:3\.4|Stakeholder\s*Map)", "3.4 Stakeholder Map"),
        ("business_requirements", r"(?:3\.5|Success\s*Metrics|KPI)", "3.5 Success Metrics / KPIs"),
        ("business_requirements", r"(?:3\.6|Constraints\s*[&|and]\s*Assumptions)", "3.6 Constraints & Assumptions"),
        # Section 4 — UX & Design
        ("ux_design", r"(?:4\.1|Design\s*Ownership)", "4.1 Design Ownership & Resources"),
        ("ux_design", r"(?:4\.2|(?:User\s*)?Personas)", "4.2 User Personas"),
        ("ux_design", r"(?:4\.3|(?:Critical\s*)?User\s*Journeys)", "4.3 Critical User Journeys"),
        ("ux_design", r"(?:4\.4|UI/?UX\s*Constraints)", "4.4 UI/UX Constraints & Requirements"),
        # Section 5 — Technical Specifications
        ("technical_specs", r"(?:5\.1|System\s*Overview)", "5.1 System Overview"),
        ("technical_specs", r"(?:5\.2|Scope\s*of\s*Development)", "5.2 Scope of Development"),
        ("technical_specs", r"(?:5\.4|Non.?Functional)", "5.4 Non-Functional Requirements"),
        ("technical_specs", r"(?:5\.5|Architecture\s*Decisions)", "5.5 Architecture Decisions"),
        # Section 6 — Integration Map
        ("integration_map", r"(?:6\.2|Data\s*Flow)", "6.2 Data Flow Description"),
        ("integration_map", r"(?:6\.3|External\s*Dependencies\s*Risk)", "6.3 External Dependencies Risk"),
        # Section 8 — Scope Boundary
        ("scope_boundary", r"(?:8\.4|Pending\s*Scope\s*Decisions)", "8.4 Pending Scope Decisions"),
        # Section 9 — Mandays Estimation
        ("mandays_estimation", r"(?:9\.1|(?:Recommended\s*)?Team\s*Composition)", "9.1 Recommended Team Composition"),
        ("mandays_estimation", r"(?:9\.2|Progressive\s*Estimate)", "9.2 Progressive Estimate Build-Up"),
        ("mandays_estimation", r"(?:9\.3|Effort\s*Breakdown)", "9.3 Effort Breakdown per Feature"),
        ("mandays_estimation", r"(?:9\.4|(?:Team\s*)?Throughput|Timeline\s*Feasibility)", "9.4 Team Throughput & Timeline"),
        ("mandays_estimation", r"(?:9\.5|Cost\s*Projection)", "9.5 Cost Projection"),
        ("mandays_estimation", r"(?:9\.6|Budget\s*vs\s*Scope)", "9.6 Budget vs Scope Assessment"),
        # Section 12 — Interview Coverage
        ("interview_coverage", r"(?:12\.2|Source\s*of\s*Information)", "12.2 Source of Information"),
        ("interview_coverage", r"(?:12\.5|Coverage\s*Summary)", "12.5 Coverage Summary"),
    ]

    for parent_section, pattern, display_name in subsection_checks:
        # Only check subsections if the parent section exists
        parent_text = parsed["raw_sections"].get(parent_section, "")
        if not parent_text:
            continue  # Parent is already flagged by validate_structure
        if not re.search(pattern, parent_text, re.IGNORECASE):
            issues.append(DocIssue(
                code="DOC-SUB-MISS",
                severity=Severity.WARNING,
                section=parent_section,
                message=f"Subsection '{display_name}' is missing from {parent_section.replace('_', ' ').title()}.",
                resolution=f"Add '{display_name}' following the output template. If info is unavailable, include the subsection header with a GAP tag."
            ))

    # Check for Mermaid diagrams in key sections
    mermaid_checks = [
        ("technical_specs", "5.1 System Overview"),
    ]
    for section, display_name in mermaid_checks:
        sec_text = parsed["raw_sections"].get(section, "")
        if sec_text and "mermaid" not in sec_text.lower():
            issues.append(DocIssue(
                code="DOC-DIAGRAM",
                severity=Severity.WARNING,
                section=section,
                message=f"No Mermaid diagram found in {display_name}.",
                resolution=f"Add a system context Mermaid diagram to {display_name} as specified in the output template."
            ))

    return issues


def validate_id_sequences(parsed: dict) -> list[DocIssue]:
    """Check ID sequences are continuous (no gaps like BR-001, BR-003 missing BR-002)."""
    issues = []
    for prefix, ids in parsed["ids"].items():
        if not ids:
            continue
        nums = sorted(int(i) for i in ids)
        expected = list(range(1, max(nums) + 1))
        missing = set(expected) - set(nums)
        if missing:
            missing_ids = [f"{prefix}-{m:03d}" for m in sorted(missing)]
            issues.append(DocIssue(
                code="DOC-IDGAP",
                severity=Severity.WARNING,
                section="global",
                message=f"ID sequence gap in {prefix} series: missing {', '.join(missing_ids)}.",
                resolution="Fill the gap or renumber to keep IDs continuous."
            ))
    return issues


def validate_traceability(parsed: dict) -> list[DocIssue]:
    """Check that every feature traces to a BR and every risk traces to FT/INT."""
    issues = []

    # Features without BR links
    for ft_id, br_links in parsed["features_with_br_links"].items():
        if not br_links:
            issues.append(DocIssue(
                code="DOC-TRACE-FT",
                severity=Severity.WARNING,
                section="technical_specs",
                message=f"Feature {ft_id} has no linked Business Requirement (BR-NNN).",
                resolution=f"Add a 'Linked Requirements' field to {ft_id} mapping it to at least one BR."
            ))

    # If we found FT IDs in the document but none had BR links parsed,
    # it might mean the format wasn't followed — flag it
    ft_ids = parsed["ids"].get("FT", set())
    ft_with_links = set(parsed["features_with_br_links"].keys())
    ft_no_trace = {f"FT-{fid}" for fid in ft_ids} - ft_with_links
    if ft_no_trace and len(ft_no_trace) > 3:
        issues.append(DocIssue(
            code="DOC-TRACE-BULK",
            severity=Severity.WARNING,
            section="technical_specs",
            message=f"{len(ft_no_trace)} features have no traceability data: {', '.join(sorted(ft_no_trace)[:5])}{'...' if len(ft_no_trace) > 5 else ''}",
            resolution="Ensure each feature specification includes a 'Linked Requirements' row."
        ))

    # Risks without FT/INT links
    for rsk_id, links in parsed["risks_with_links"].items():
        if not links:
            issues.append(DocIssue(
                code="DOC-TRACE-RSK",
                severity=Severity.INFO,
                section="risk_register",
                message=f"Risk {rsk_id} is not linked to any Feature (FT) or Integration (INT).",
                resolution=f"Add the affected feature or integration ID to {rsk_id}."
            ))

    return issues


def validate_scope_estimation_alignment(parsed: dict) -> list[DocIssue]:
    """Check features in scope are also in the estimation matrix."""
    issues = []
    in_scope = parsed["features_in_scope"]
    in_estimation = parsed["features_in_estimation"]

    # Features in scope but not estimated
    missing_estimate = in_scope - in_estimation
    if missing_estimate:
        issues.append(DocIssue(
            code="DOC-SCOPE-EST",
            severity=Severity.CRITICAL,
            section="mandays_estimation",
            message=(
                f"Features in scope (MVP) but missing from estimation matrix: "
                f"{', '.join(sorted(missing_estimate))}."
            ),
            resolution="Add mandays estimates for these features or move them to post-launch."
        ))

    # Features estimated but not in scope
    extra_estimate = in_estimation - in_scope
    if extra_estimate and in_scope:  # only flag if scope section had FT IDs
        issues.append(DocIssue(
            code="DOC-EST-SCOPE",
            severity=Severity.WARNING,
            section="scope_boundary",
            message=(
                f"Features in estimation matrix but not listed in MVP scope: "
                f"{', '.join(sorted(extra_estimate))}."
            ),
            resolution="Add these to the scope section or remove from estimation."
        ))

    return issues


def validate_gaps(parsed: dict) -> list[DocIssue]:
    """Check all gaps have owners and priorities."""
    issues = []

    for gap_id, owner in parsed["gaps_with_owners"].items():
        if not owner or owner.lower() in ("", "-", "tbd", "n/a"):
            issues.append(DocIssue(
                code="DOC-GAP-OWNER",
                severity=Severity.WARNING,
                section="open_questions",
                message=f"Gap {gap_id} has no owner assigned.",
                resolution=f"Assign an owner (person or role) responsible for resolving {gap_id}."
            ))

    for gap_id, priority in parsed["gap_priorities"].items():
        if not priority or priority.lower() in ("", "-", "tbd", "n/a"):
            issues.append(DocIssue(
                code="DOC-GAP-PRI",
                severity=Severity.INFO,
                section="open_questions",
                message=f"Gap {gap_id} has no priority assigned.",
                resolution=f"Assign priority (Critical/High/Med) to {gap_id}."
            ))

    return issues


def validate_confidence(parsed: dict) -> list[DocIssue]:
    """Check confidence scores are present and within expected range."""
    issues = []

    if not parsed["confidence_scores"]:
        issues.append(DocIssue(
            code="DOC-CONF-MISS",
            severity=Severity.WARNING,
            section="confidence_score",
            message="No confidence scores found in the document.",
            resolution="Add the Confidence Score Card with per-dimension percentages."
        ))
        return issues

    overall = parsed["confidence_scores"].get("Overall") or parsed["confidence_scores"].get("**Overall**")
    if overall is not None and overall < 55:
        issues.append(DocIssue(
            code="DOC-CONF-LOW",
            severity=Severity.CRITICAL,
            section="confidence_score",
            message=f"Overall confidence is {overall}% — below 55% threshold.",
            resolution="Additional discovery session required before development begins."
        ))

    return issues


def validate_document_status_consistency(parsed: dict) -> list[DocIssue]:
    """Check document status matches its content."""
    issues = []

    has_gaps = bool(parsed["ids"].get("GAP"))
    has_critical_gaps = any(
        p.lower() in ("critical", "high")
        for p in parsed["gap_priorities"].values()
        if p
    )
    status = parsed["document_status"]

    if status == "FINAL" and has_critical_gaps:
        issues.append(DocIssue(
            code="DOC-STATUS",
            severity=Severity.CRITICAL,
            section="executive_summary",
            message="Document is marked FINAL but has Critical/High priority gaps.",
            resolution="Either resolve the gaps or change status to DRAFT."
        ))

    if status == "FINAL" and has_gaps:
        issues.append(DocIssue(
            code="DOC-STATUS-GAP",
            severity=Severity.WARNING,
            section="executive_summary",
            message="Document is marked FINAL but Open Questions section has unresolved gaps.",
            resolution="Resolve all gaps or change status to DRAFT."
        ))

    return issues


def validate_integration_completeness(parsed: dict) -> list[DocIssue]:
    """Check integrations referenced in features exist in integration map."""
    issues = []

    # Collect all INT-NNN references from feature specs
    tech_section = parsed["raw_sections"].get("technical_specs", "")
    int_refs_in_features = {f"INT-{i}" for i in ID_PATTERNS["INT"].findall(tech_section)}

    # Compare against integration map
    int_declared = parsed["integrations_declared"]

    missing = int_refs_in_features - int_declared
    if missing:
        issues.append(DocIssue(
            code="DOC-INT-MISS",
            severity=Severity.CRITICAL,
            section="integration_map",
            message=(
                f"Integrations referenced in features but missing from Integration Map: "
                f"{', '.join(sorted(missing))}."
            ),
            resolution="Add these integrations to the Integration Map with full details."
        ))

    return issues


# ─────────────────────────────────────────────
# Cross-Validation with Session JSON
# ─────────────────────────────────────────────

def cross_validate_with_session(parsed: dict, session: dict) -> list[DocIssue]:
    """
    If a session JSON is provided alongside the document, check that the
    document accurately reflects the session data.
    """
    issues = []
    blocks = session.get("blocks", {})

    # Feature count mismatch
    session_features = blocks.get("scope", {}).get("features_mvp", [])
    doc_feature_count = len(parsed["ids"].get("FT", set()))
    if session_features and doc_feature_count > 0:
        diff = abs(len(session_features) - doc_feature_count)
        if diff > 2:
            issues.append(DocIssue(
                code="XVAL-FT-COUNT",
                severity=Severity.WARNING,
                section="technical_specs",
                message=(
                    f"Session has {len(session_features)} MVP features but document "
                    f"has {doc_feature_count} feature specs. Difference of {diff}."
                ),
                resolution="Reconcile feature list — were features added, split, or removed?"
            ))

    # Integration count mismatch
    session_integrations = blocks.get("integrations", {}).get("third_party_services", [])
    doc_int_count = len(parsed["ids"].get("INT", set()))
    if session_integrations and doc_int_count > 0:
        diff = abs(len(session_integrations) - doc_int_count)
        if diff > 1:
            issues.append(DocIssue(
                code="XVAL-INT-COUNT",
                severity=Severity.WARNING,
                section="integration_map",
                message=(
                    f"Session has {len(session_integrations)} integrations but document "
                    f"has {doc_int_count}. Difference of {diff}."
                ),
                resolution="Reconcile integration list with session data."
            ))

    # Budget mismatch
    session_budget = blocks.get("budget", {}).get("total_mandays_budget", 0)
    doc_total = parsed.get("mandays_total")
    if session_budget and doc_total and abs(session_budget - doc_total) > session_budget * 0.1:
        issues.append(DocIssue(
            code="XVAL-BUDGET",
            severity=Severity.CRITICAL,
            section="mandays_estimation",
            message=(
                f"Session budget was {session_budget} mandays but document total "
                f"is {doc_total} mandays. More than 10% deviation."
            ),
            resolution="Update either the budget field or the estimation matrix."
        ))

    return issues


# ─────────────────────────────────────────────
# Report Generation
# ─────────────────────────────────────────────

def generate_report(parsed: dict, all_issues: list[DocIssue]) -> dict:
    """Compile validation report."""

    criticals = [i for i in all_issues if i.severity == Severity.CRITICAL]
    warnings = [i for i in all_issues if i.severity == Severity.WARNING]
    infos = [i for i in all_issues if i.severity == Severity.INFO]

    id_summary = {
        prefix: len(ids)
        for prefix, ids in parsed["ids"].items()
        if ids
    }

    return {
        "validation_passed": len(criticals) == 0,
        "document_status": parsed["document_status"],
        "summary": {
            "critical_count": len(criticals),
            "warning_count": len(warnings),
            "info_count": len(infos),
            "sections_found": len(parsed["sections_found"]),
            "sections_missing": len(parsed["sections_missing"]),
        },
        "id_counts": id_summary,
        "sections_found": parsed["sections_found"],
        "sections_missing": parsed["sections_missing"],
        "confidence_scores": parsed["confidence_scores"],
        "critical_issues": [
            {"code": i.code, "section": i.section, "message": i.message, "resolution": i.resolution}
            for i in criticals
        ],
        "warnings": [
            {"code": i.code, "section": i.section, "message": i.message, "resolution": i.resolution}
            for i in warnings
        ],
        "info": [
            {"code": i.code, "section": i.section, "message": i.message, "resolution": i.resolution}
            for i in infos
        ],
    }


def print_report(report: dict) -> None:
    """Print a human-readable report."""

    print("\n" + "═" * 64)
    print("  AI REQUIREMENT ANALYSIS — DOCUMENT VALIDATION REPORT")
    print("═" * 64)

    s = report["summary"]
    print(f"\n  Document Status:     {report['document_status']}")
    print(f"  Sections Found:      {s['sections_found']}")
    print(f"  Sections Missing:    {s['sections_missing']}")
    print(f"  Critical Issues:     {s['critical_count']}")
    print(f"  Warnings:            {s['warning_count']}")
    print(f"  Info:                {s['info_count']}")

    if report["id_counts"]:
        print("\n" + "─" * 64)
        print("  ENTITY COUNTS")
        print("─" * 64)
        for prefix, count in sorted(report["id_counts"].items()):
            print(f"  {prefix}-NNN:  {count}")

    if report["confidence_scores"]:
        print("\n" + "─" * 64)
        print("  CONFIDENCE SCORES (from document)")
        print("─" * 64)
        for dim, score in report["confidence_scores"].items():
            bar = "█" * (score // 10)
            pad = "░" * (10 - score // 10)
            print(f"  {dim:<25} {score:>3}%  {bar}{pad}")

    if report["sections_missing"]:
        print("\n" + "─" * 64)
        print("  MISSING SECTIONS")
        print("─" * 64)
        for sec in report["sections_missing"]:
            print(f"  ❌ {sec.replace('_', ' ').title()}")

    if report["critical_issues"]:
        print("\n" + "─" * 64)
        print("  🚨 CRITICAL ISSUES")
        print("─" * 64)
        for issue in report["critical_issues"]:
            print(f"\n  [{issue['code']}] Section: {issue['section']}")
            print(f"  Problem:    {issue['message']}")
            print(f"  Resolution: {issue['resolution']}")

    if report["warnings"]:
        print("\n" + "─" * 64)
        print("  ⚠️  WARNINGS")
        print("─" * 64)
        for w in report["warnings"]:
            print(f"\n  [{w['code']}] Section: {w['section']}")
            print(f"  {w['message']}")

    if report["info"]:
        print("\n" + "─" * 64)
        print("  ℹ️  INFO")
        print("─" * 64)
        for i in report["info"]:
            print(f"  [{i['code']}] {i['message']}")

    print("\n" + "─" * 64)
    if report["validation_passed"]:
        print("  ✅ Document passes validation.")
    else:
        print("  ❌ Document has critical issues. Resolve before proceeding.")
    print("═" * 64 + "\n")


# ─────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────

def run_document_validation(content: str, session: Optional[dict] = None) -> dict:
    """Run full document validation and return report."""
    parsed = parse_document(content)
    all_issues = []

    all_issues.extend(validate_structure(parsed))
    all_issues.extend(validate_subsections(parsed))
    all_issues.extend(validate_id_sequences(parsed))
    all_issues.extend(validate_traceability(parsed))
    all_issues.extend(validate_scope_estimation_alignment(parsed))
    all_issues.extend(validate_gaps(parsed))
    all_issues.extend(validate_confidence(parsed))
    all_issues.extend(validate_document_status_consistency(parsed))
    all_issues.extend(validate_integration_completeness(parsed))

    if session:
        all_issues.extend(cross_validate_with_session(parsed, session))

    return generate_report(parsed, all_issues)


def main():
    parser = argparse.ArgumentParser(
        description="Validate a Source of Truth requirements document (.md)."
    )
    parser.add_argument("--input", "-i", required=True, help="Path to requirements .md file")
    parser.add_argument("--session", "-s", help="Optional: path to session JSON for cross-validation")
    parser.add_argument("--output", "-o", help="Path to write JSON report")
    parser.add_argument("--quiet", "-q", help="JSON only, no human output", action="store_true")
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    session = None
    if args.session:
        try:
            with open(args.session, "r") as f:
                session = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load session file: {e}", file=sys.stderr)

    report = run_document_validation(content, session)

    if not args.quiet:
        print_report(report)

    if args.output:
        with open(args.output, "w") as f:
            json.dump(report, f, indent=2)
        print(f"Report saved to: {args.output}")

    sys.exit(0 if report["validation_passed"] else 1)


if __name__ == "__main__":
    main()
