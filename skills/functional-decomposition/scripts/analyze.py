#!/usr/bin/env python3
"""
Functional Decomposition Analyzer v2

Validates STRUCTURAL compliance and CONTENT quality of a decomposition .md file.
Outputs to terminal and generates a separate analysis .md file.

Usage:
    python3 scripts/analyze.py <decomposition-file.md>
    python3 scripts/analyze.py <decomposition-file.md> --output <analysis.md>
    python3 scripts/analyze.py <decomposition-file.md> --strict

Flags:
    --strict    Treat warnings as errors (exit code 1 if any warnings)
    --output    Specify output file path (default: *-analysis.md)

No external dependencies -- pure Python stdlib.
"""

import re, sys
from collections import defaultdict, Counter
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CANONICAL_CATEGORIES = [
    "Boundary Values", "State Conflicts", "Permission Boundaries",
    "Data Integrity", "Integration Failures", "Temporal",
    "Multi-Device / Context", "Scale / Volume",
]
CAT_SHORT = ["Bound", "State", "Perms", "Data", "Integ", "Tempo", "Multi", "Scale"]

REQUIRED_SECTIONS = [
    "Dashboard", "Feature Inventory", "Roles", "Decomposition",
    "Cross-Feature Dependencies", "Open Questions", "Summary",
]
REQUIRED_SUBSECTIONS = [
    "Story Overview", "Story Details", "Acceptance Criteria",
    "Edge Cases", "Error Scenarios",
]

PLACEHOLDERS = [
    r'\bTBD\b', r'\bTODO\b', r'\bTBC\b', r'\bFIXME\b',
    r'\[placeholder\]', r'\[insert\b', r'\bLorem ipsum\b', r'\bXXX\b',
]

VAGUE = [
    "handle gracefully", "as appropriate", "handle properly", "should be fast",
    "should be secure", "in a timely manner", "user-friendly", "intuitive",
    "seamless", "robust", "handle correctly", "work properly", "perform well",
    "as needed", "if necessary", "reasonable time", "adequate", "sufficient",
]

DEPTH = {
    "S": {"stories": 2, "ac_per": 2, "ec": 2, "err": 1, "cat": 3},
    "M": {"stories": 3, "ac_per": 2, "ec": 4, "err": 2, "cat": 5},
    "L": {"stories": 5, "ac_per": 3, "ec": 6, "err": 3, "cat": 6},
}


# Module-level feature prefix — set by detect_prefix() before any parsing.
FP = "FT"  # default; overwritten at runtime


def detect_prefix(text):
    """Auto-detect the feature ID prefix used in the document.

    Scans for patterns like 'XX-001' in feature inventory tables, section
    headers (### XX-001:), and story references (**XX-001-US-001:).
    Returns the most common prefix found, or 'FT' as fallback.
    """
    candidates = re.findall(
        r'(?:###\s+|(?:\|\s*)|(?:\*\*\s*))([A-Z][A-Z0-9]{0,5})-\d{2,4}(?:-US-\d+)?',
        text
    )
    if not candidates:
        return "FT"
    counts = Counter(candidates)
    # Exclude "US", "AC", "EC", "ERR", "INT" — those are sub-IDs, not feature prefixes
    for skip in ("US", "AC", "EC", "ERR", "INT", "BR"):
        counts.pop(skip, None)
    if not counts:
        return "FT"
    return counts.most_common(1)[0][0]


def norm_cat(raw):
    """Normalize a raw edge case category to canonical name."""
    raw_l = raw.strip().lower()
    mapping = {
        "boundary": "Boundary Values", "state": "State Conflicts",
        "permission": "Permission Boundaries", "data": "Data Integrity",
        "integration": "Integration Failures", "temporal": "Temporal",
        "multi-device": "Multi-Device / Context", "multi device": "Multi-Device / Context",
        "context": "Multi-Device / Context", "accessibility": "Multi-Device / Context",
        "connectivity": "Multi-Device / Context",
        "scale": "Scale / Volume", "volume": "Scale / Volume",
    }
    for k, v in mapping.items():
        if k in raw_l:
            return v
    return raw.strip()


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def parse(text):
    """Parse the .md file into structured data."""
    d = {
        "features": [], "stories": [], "acs": [], "ecs": [], "errs": [],
        "open_questions": [], "summary_stated": {}, "raw": text,
    }

    # Features from inventory table
    for m in re.finditer(
        rf'\|\s*({FP}-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([SML])\s*\|',
        text
    ):
        d["features"].append({
            "id": m[1].strip(), "name": m[2].strip(), "complexity": m[5].strip(),
        })

    # Stories (prose)
    seen = set()
    for m in re.finditer(rf'\*\*\s*({FP}-\d+-US-\d+)\s*:\s*(.+?)\s*\*\*', text):
        sid = m[1].strip()
        if sid not in seen:
            seen.add(sid)
            d["stories"].append({
                "id": sid, "title": m[2].strip(),
                "feature": re.match(rf'({FP}-\d+)', sid)[1],
            })

    # Stories (table) + metadata
    cur_ft = None
    for line in text.split('\n'):
        fh = re.match(rf'###\s+({FP}-\d+)', line)
        if fh:
            cur_ft = fh[1]
        sm = re.search(
            r'\|\s*(US-\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|'
            r'\s*(Must|Should|Could|Won\'t)\s*\|\s*(\d+)\s*\|', line
        )
        if sm and cur_ft:
            fid = f"{cur_ft}-{sm[1].strip()}"
            found = False
            for s in d["stories"]:
                if s["id"] == fid:
                    s["priority"] = sm[4].strip()
                    s["points"] = int(sm[5])
                    found = True
                    break
            if not found and fid not in seen:
                seen.add(fid)
                d["stories"].append({
                    "id": fid, "title": sm[2].strip(), "feature": cur_ft,
                    "priority": sm[4].strip(), "points": int(sm[5]),
                })

    # Points/priority from prose lines
    lines = text.split('\n')
    for i, line in enumerate(lines):
        pm = re.search(r'Points:\s*(\d+)', line)
        prm = re.search(r'Priority:\s*(Must|Should|Could|Won\'t)', line)
        if pm or prm:
            for j in range(max(0, i - 5), i):
                sm2 = re.search(rf'\*\*\s*({FP}-\d+-US-\d+):', lines[j])
                if sm2:
                    for s in d["stories"]:
                        if s["id"] == sm2[1].strip():
                            if pm: s["points"] = int(pm[1])
                            if prm: s["priority"] = prm[1].strip()

    # ACs
    cur_story = None
    for line in lines:
        sc = re.search(rf'\*\*\s*(?:{FP}-\d+-)?(US-\d+)\s*:', line)
        if sc and '|' not in line:
            cur_story = sc[1].strip()
        am = re.search(r'\|\s*(AC-\d+)\s*\|', line)
        if am:
            aid = am[1].strip()
            if aid not in [a["id"] for a in d["acs"]]:
                d["acs"].append({"id": aid, "story_ref": cur_story, "line": line.strip()})

    # ECs
    for m in re.finditer(
        r'\|\s*(EC-\d+)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|', text
    ):
        eid = m[1].strip()
        if eid not in [e["id"] for e in d["ecs"]]:
            d["ecs"].append({
                "id": eid, "desc": m[2].strip(), "expected": m[4].strip(),
                "category": norm_cat(m[5]),
            })

    # ERRs
    for m in re.finditer(
        r'\|\s*(ERR-\d+)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|',
        text
    ):
        eid = m[1].strip()
        if eid not in [e["id"] for e in d["errs"]]:
            d["errs"].append({
                "id": eid, "title": m[2].strip(), "trigger": m[3].strip(),
                "user_sees": m[4].strip(), "system_does": m[5].strip(),
                "recovery": m[6].strip(),
            })

    # Open questions
    in_oq = False
    for line in lines:
        if '## Open Questions' in line:
            in_oq = True; continue
        if in_oq and line.startswith('## '):
            in_oq = False
        if in_oq:
            qm = re.search(r'\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', line)
            if qm and qm[1].strip().isdigit() and not qm[2].strip().startswith('Question'):
                d["open_questions"].append({"num": int(qm[1]), "question": qm[2].strip()})

    # Summary stated
    ss = re.search(r'## Summary\s*\n(.*?)(?=\n## |\n### Points|\Z)', text, re.DOTALL)
    if ss:
        for line in ss[1].split('\n'):
            sm3 = re.search(r'\|\s*(.+?)\s*\|\s*(\d+)\s*\|', line)
            if sm3:
                k = sm3[1].strip().lower().replace(' ', '_').lstrip('-_').strip()
                d["summary_stated"][k] = int(sm3[2])

    return d


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_structure(text):
    """Structural compliance checks."""
    errs, warns = [], []

    # Required top sections
    for sec in REQUIRED_SECTIONS:
        if not re.search(r'^##\s+' + re.escape(sec), text, re.MULTILINE):
            errs.append(f'Missing required section: "## {sec}"')

    # Feature subsections
    for sec in re.split(rf'(?=### {FP}-\d+:)', text):
        fm = re.match(rf'### ({FP}-\d+):', sec)
        if not fm:
            continue
        fid = fm[1]
        for sub in REQUIRED_SUBSECTIONS:
            if f'#### {sub}' not in sec:
                errs.append(f'{fid}: Missing subsection "#### {sub}"')

    # Table format enforcement
    for sec in re.split(rf'(?=### {FP}-\d+:)', text):
        fm = re.match(rf'### ({FP}-\d+):', sec)
        if not fm:
            continue
        fid = fm[1]
        for label, tag in [
            ("Acceptance Criteria", "AC"),
            ("Edge Cases", "EC"),
            ("Error Scenarios", "ERR"),
        ]:
            sub = re.search(rf'#### {label}\s*\n(.*?)(?=####|\Z)', sec, re.DOTALL)
            if sub and len(sub[1].strip()) > 20:
                if not re.search(rf'\|\s*{tag}-\d+\s*\|', sub[1]):
                    warns.append(f'{fid}: "{label}" not in table format')

    # Placeholder detection
    for i, line in enumerate(text.split('\n'), 1):
        if 'NEEDS CLARIFICATION' in line:
            continue
        for pat in PLACEHOLDERS:
            if re.search(pat, line, re.I):
                warns.append(f'Line {i}: Placeholder text -- "{line.strip()[:70]}"')
                break

    # Empty sections
    all_sec = list(re.finditer(r'^(#{2,4})\s+(.+?)$', text, re.MULTILINE))
    for i, m in enumerate(all_sec):
        nxt = all_sec[i + 1].start() if i + 1 < len(all_sec) else len(text)
        content = text[m.end():nxt].strip()
        real = [l for l in content.split('\n')
                if l.strip() and not re.match(r'^[\|\-\s:]+$', l)]
        if len(real) == 0 and m[2].strip() not in ('Decomposition',):
            warns.append(f'Empty section: "{m[2].strip()}"')

    return errs, warns


def check_quality(data):
    """Content quality checks."""
    errs, warns = [], []
    text = data["raw"]

    # Vague language in ACs
    for ac in data["acs"]:
        for v in VAGUE:
            if v in ac.get("line", "").lower():
                warns.append(f'{ac["id"]}: Vague term "{v}" -- use measurable criteria')
                break

    # Vague in edge case expected behavior
    for ec in data["ecs"]:
        for v in VAGUE:
            if v in ec.get("expected", "").lower():
                warns.append(f'{ec["id"]}: Vague expected behavior "{v}" -- be specific')
                break

    # Error recovery completeness
    for err in data["errs"]:
        r = err.get("recovery", "").strip()
        if not r or r in ("-", "—", "N/A", ""):
            errs.append(f'{err["id"]}: No recovery path')
        u = err.get("user_sees", "").strip()
        if u and re.search(r'(something went wrong|error occurred)', u, re.I):
            warns.append(f'{err["id"]}: Generic error message -- use feature-specific text')

    # Negative AC per feature
    for sec in re.split(rf'(?=### {FP}-\d+:)', text):
        fm = re.match(rf'### ({FP}-\d+):', sec)
        if not fm:
            continue
        ac_sec = re.search(r'#### Acceptance Criteria\s*\n(.*?)(?=####|\Z)', sec, re.DOTALL)
        if ac_sec:
            t = ac_sec[1].lower()
            neg = any(w in t for w in [
                'should not', 'must not', 'cannot', 'does not', 'disabled',
                'blocked', 'rejected', 'denied', 'invalid', 'fail', 'prevent',
                'error', 'not allowed',
            ])
            if not neg:
                warns.append(f'{fm[1]}: No negative AC found -- add a "should NOT" test case')

    # "So that" quality
    for m in re.finditer(r'So that\s+(.+?)(?:\n|$)', text, re.I):
        val = m[1].strip().rstrip('.')
        for term in ['the system', 'the database', 'data is stored',
                     'the server', 'the api', 'the backend']:
            if term in val.lower():
                pre = text[max(0, m.start() - 300):m.start()]
                sids = re.findall(rf'({FP}-\d+-US-\d+)', pre)
                sid = sids[-1] if sids else "?"
                warns.append(f'{sid}: "So that" is system-focused -- rewrite for user value')
                break

    return errs, warns


def check_quantity(data):
    """Quantity and depth checks."""
    errs, warns = [], []
    text = data["raw"]

    # AC per story
    sac = Counter()
    for ac in data["acs"]:
        r = ac.get("story_ref")
        if r:
            sac[r] += 1
    for s in data["stories"]:
        short = re.search(r'(US-\d+)', s["id"])
        if short:
            c = sac.get(short[1], 0)
            if c == 0:
                errs.append(f'{s["id"]}: 0 acceptance criteria')
            elif c < 2:
                warns.append(f'{s["id"]}: {c} AC (minimum: 2)')

    # 13-pointers
    for s in data["stories"]:
        p = s.get("points", 0)
        if p >= 13:
            errs.append(f'{s["id"]}: {p} points -- must split')
        elif p == 8:
            warns.append(f'{s["id"]}: 8 points -- consider splitting')

    # Per-feature stats
    fstats = {}
    for sec in re.split(rf'(?=### {FP}-\d+:)', text):
        fm = re.match(rf'### ({FP}-\d+):', sec)
        if not fm:
            continue
        fid = fm[1]
        cats = set()
        for ecm in re.finditer(
            r'\|\s*EC-\d+\s*\|[^|]*\|[^|]*\|[^|]*\|\s*([^|]+)\|', sec
        ):
            cats.add(norm_cat(ecm[1]))
        fstats[fid] = {
            "stories": max(
                len(re.findall(rf'\*\*{FP}-\d+-US-\d+:', sec)),
                len(re.findall(r'\|\s*US-\d+\s*\|', sec)),
            ),
            "acs": len(re.findall(r'\|\s*AC-\d+\s*\|', sec)),
            "ecs": len(re.findall(r'\|\s*EC-\d+\s*\|', sec)),
            "errs": len(re.findall(r'\|\s*ERR-\d+\s*\|', sec)),
            "cats": cats,
        }

    # Depth vs complexity
    for f in data["features"]:
        fid, comp = f["id"], f["complexity"]
        tgt = DEPTH.get(comp, DEPTH["M"])
        fs = fstats.get(fid, {"stories": 0, "acs": 0, "ecs": 0, "errs": 0, "cats": set()})
        if fs["stories"] < tgt["stories"]:
            warns.append(f'{fid} ({comp}): {fs["stories"]} stories (min {tgt["stories"]})')
        if fs["ecs"] < tgt["ec"]:
            warns.append(f'{fid} ({comp}): {fs["ecs"]} edge cases (min {tgt["ec"]})')
        if fs["errs"] < tgt["err"]:
            warns.append(f'{fid} ({comp}): {fs["errs"]} error scenarios (min {tgt["err"]})')
        cc = len(fs["cats"])
        if cc < tgt["cat"]:
            missing = [c for c in CANONICAL_CATEGORIES if c not in fs["cats"]]
            warns.append(
                f'{fid} ({comp}): {cc}/8 categories (min {tgt["cat"]}). '
                f'Missing: {", ".join(missing[:3])}'
            )

    # Summary accuracy
    actual = {
        "features": len(data["features"]),
        "stories": len(data["stories"]),
        "points": sum(s.get("points", 0) for s in data["stories"]),
        "acs": len(data["acs"]),
        "ecs": len(data["ecs"]),
        "errs": len(data["errs"]),
        "open_questions": len(data["open_questions"]),
    }
    sumcheck = {}
    for sk, ak in [
        ("features", "features"), ("user_stories", "stories"),
        ("total_story_points", "points"), ("acceptance_criteria", "acs"),
        ("edge_cases", "ecs"), ("error_scenarios", "errs"),
        ("open_questions", "open_questions"),
    ]:
        if sk in data["summary_stated"]:
            sv, av = data["summary_stated"][sk], actual[ak]
            st = "OK" if sv == av else f"MISMATCH (stated {sv}, actual {av})"
            sumcheck[sk] = {"stated": sv, "actual": av, "status": st}
            if sv != av:
                errs.append(
                    f'Summary: {sk.replace("_", " ").title()} stated {sv}, actual {av}'
                )

    return errs, warns, actual, sumcheck, fstats


def score_features(features, fstats, all_errs, all_warns):
    """Calculate quality scores per feature."""
    scores = {}
    for f in features:
        fid, comp = f["id"], f["complexity"]
        tgt = DEPTH.get(comp, DEPTH["M"])
        fs = fstats.get(fid, {"stories": 0, "acs": 0, "ecs": 0, "errs": 0, "cats": set()})
        sc = 100

        if fs["stories"] > 0:
            ratio = fs["acs"] / fs["stories"]
            if ratio < tgt["ac_per"]:
                sc -= int((tgt["ac_per"] - ratio) * 15)
        cc = len(fs.get("cats", set()))
        if cc < tgt["cat"]:
            sc -= (tgt["cat"] - cc) * 5
        if fs["errs"] < tgt["err"]:
            sc -= (tgt["err"] - fs["errs"]) * 8
        if fs["stories"] < tgt["stories"]:
            sc -= (tgt["stories"] - fs["stories"]) * 5

        sc -= sum(3 for e in all_errs if fid in e)
        sc -= sum(1 for w in all_warns if fid in w)

        sc = max(0, min(100, sc))
        g = "A" if sc >= 90 else "B" if sc >= 75 else "C" if sc >= 60 else "D" if sc >= 40 else "F"
        scores[fid] = {"score": sc, "grade": g}
    return scores


# ---------------------------------------------------------------------------
# Output: Terminal
# ---------------------------------------------------------------------------

def fmt_terminal(f, path):
    L = []
    st = f["stats"]
    iss = f["issues"]

    must = sum(1 for s in f["data"]["stories"] if s.get("priority") == "Must")
    should = sum(1 for s in f["data"]["stories"] if s.get("priority") == "Should")
    could = sum(1 for s in f["data"]["stories"] if s.get("priority") == "Could")
    ar = round(st['acs'] / max(st['stories'], 1), 1)

    L.append("")
    L.append("=" * 62)
    L.append("  DECOMPOSITION QUALITY REPORT")
    L.append("=" * 62)
    L.append(f"  Source:    {path}")
    L.append(f"  Score:     {f['grade']} ({f['score']}/100)")
    L.append(f"  Errors:    {len(iss['errors'])}")
    L.append(f"  Warnings:  {len(iss['warnings'])}")
    L.append("=" * 62)

    L.append("")
    L.append("COUNTS")
    L.append(f"  Features:            {st['features']}")
    L.append(f"  Stories:             {st['stories']}  (Must:{must} Should:{should} Could:{could})")
    L.append(f"  Points:              {st['points']}")
    L.append(f"  Acceptance Criteria: {st['acs']}  (avg {ar}/story)")
    L.append(f"  Edge Cases:          {st['ecs']}")
    L.append(f"  Error Scenarios:     {st['errs']}")
    L.append(f"  Open Questions:      {st['open_questions']}")

    L.append("")
    L.append("FEATURE SCORES")
    for fid, sc in sorted(f["fscores"].items()):
        pad = "." * (35 - len(fid))
        L.append(f"  {fid} {pad} {sc['grade']}  ({sc['score']})")

    L.append("")
    L.append("EDGE CASE COVERAGE")
    L.append("              " + "  ".join(f"{s:>5}" for s in CAT_SHORT))
    for fid, cov in sorted(f["coverage"].items()):
        row = f"  {fid:12s}"
        for c in CANONICAL_CATEGORIES:
            row += f'  {"  [x]" if cov["cats"].get(c) else "  [ ]"}'
        row += f"  ({cov['checked']}/{cov['target']}+)"
        L.append(row)

    if iss["errors"]:
        L.append(f"\nERRORS ({len(iss['errors'])})")
        for e in iss["errors"]:
            L.append(f"  !! {e}")
    if iss["warnings"]:
        L.append(f"\nWARNINGS ({len(iss['warnings'])})")
        for w in iss["warnings"]:
            L.append(f"  -- {w}")

    if f["sumcheck"]:
        L.append("\nSUMMARY VERIFICATION")
        for k, ch in f["sumcheck"].items():
            dn = k.replace("_", " ").title()
            s = " -- OK" if ch["status"] == "OK" else f" -- {ch['status']}"
            L.append(f"  {dn}: {ch['actual']}{s}")

    L.append("")
    L.append("=" * 62)
    return "\n".join(L)


# ---------------------------------------------------------------------------
# Output: Analysis .md
# ---------------------------------------------------------------------------

def fmt_md(f, path):
    L = []
    st = f["stats"]
    iss = f["issues"]

    must = sum(1 for s in f["data"]["stories"] if s.get("priority") == "Must")
    should = sum(1 for s in f["data"]["stories"] if s.get("priority") == "Should")
    could = sum(1 for s in f["data"]["stories"] if s.get("priority") == "Could")
    ar = round(st['acs'] / max(st['stories'], 1), 1)

    L.append(f"# Decomposition Quality Report\n")
    L.append(f"**Source:** {path}")
    L.append(f"**Score:** {f['grade']} ({f['score']}/100)")
    L.append(f"**Errors:** {len(iss['errors'])}")
    L.append(f"**Warnings:** {len(iss['warnings'])}")
    L.append(f"\n---\n")

    L.append("## Verified Counts\n")
    L.append("| Metric | Count | Notes |")
    L.append("|--------|-------|-------|")
    L.append(f"| Features | {st['features']} | |")
    L.append(f"| Stories | {st['stories']} | Must:{must} Should:{should} Could:{could} |")
    L.append(f"| Points | {st['points']} | |")
    L.append(f"| Acceptance Criteria | {st['acs']} | avg {ar}/story |")
    L.append(f"| Edge Cases | {st['ecs']} | |")
    L.append(f"| Error Scenarios | {st['errs']} | |")
    L.append(f"| Open Questions | {st['open_questions']} | |\n")

    L.append("## Feature Scores\n")
    L.append("| Feature | Grade | Score | Stories | ACs | ECs | ERRs |")
    L.append("|---------|-------|-------|---------|-----|-----|------|")
    for fid, sc in sorted(f["fscores"].items()):
        fs = f["fstats"].get(fid, {})
        L.append(
            f"| {fid} | {sc['grade']} | {sc['score']}/100 "
            f"| {fs.get('stories', 0)} | {fs.get('acs', 0)} "
            f"| {fs.get('ecs', 0)} | {fs.get('errs', 0)} |"
        )
    L.append("")

    L.append("## Edge Case Coverage\n")
    hdr = "| Feature | " + " | ".join(CAT_SHORT) + " | Hit | Min |"
    sep = "|---------|" + "|".join(["-----"] * 8) + "|-----|-----|"
    L.append(hdr)
    L.append(sep)
    for fid, cov in sorted(f["coverage"].items()):
        parts = ["x" if cov["cats"].get(c) else "-" for c in CANONICAL_CATEGORIES]
        L.append(
            f"| {fid} | " + " | ".join(parts) +
            f" | {cov['checked']} | {cov['target']}+ |"
        )
    L.append("")

    if iss["errors"]:
        L.append("## Errors\n\nThese must be fixed.\n")
        L.append("| # | Issue |")
        L.append("|---|-------|")
        for i, e in enumerate(iss["errors"], 1):
            L.append(f"| {i} | {e} |")
        L.append("")

    if iss["warnings"]:
        L.append("## Warnings\n\nThese should be reviewed.\n")
        L.append("| # | Issue |")
        L.append("|---|-------|")
        for i, w in enumerate(iss["warnings"], 1):
            L.append(f"| {i} | {w} |")
        L.append("")

    if f["sumcheck"]:
        L.append("## Summary Verification\n")
        L.append("| Metric | Stated | Actual | Status |")
        L.append("|--------|--------|--------|--------|")
        for k, ch in f["sumcheck"].items():
            L.append(
                f"| {k.replace('_', ' ').title()} | {ch['stated']} "
                f"| {ch['actual']} | {ch['status']} |"
            )
        L.append("")

    return "\n".join(L)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/analyze.py <file.md> [--output <out.md>] [--strict]")
        sys.exit(1)

    inp = Path(sys.argv[1])
    if not inp.exists():
        print(f"Error: {inp} not found")
        sys.exit(1)

    strict = "--strict" in sys.argv
    outp = None
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            outp = Path(sys.argv[idx + 1])
    if not outp:
        outp = inp.parent / f"{inp.stem}-analysis.md"

    text = inp.read_text(encoding="utf-8")

    # Auto-detect feature ID prefix (FT-, FD-, FEAT-, etc.)
    global FP
    FP = detect_prefix(text)
    if FP != "FT":
        print(f"Note: Detected feature prefix '{FP}-' (default is 'FT-')")

    data = parse(text)
    data["raw"] = text

    # Run all checks
    s_errs, s_warns = check_structure(text)
    q_errs, q_warns = check_quality(data)
    n_errs, n_warns, actual, sumcheck, fstats = check_quantity(data)

    all_errs = list(dict.fromkeys(s_errs + q_errs + n_errs))
    all_warns = list(dict.fromkeys(s_warns + q_warns + n_warns))

    fscores = score_features(data["features"], fstats, all_errs, all_warns)

    coverage = {}
    for feat in data["features"]:
        fid, comp = feat["id"], feat["complexity"]
        tgt = DEPTH.get(comp, DEPTH["M"])["cat"]
        fs = fstats.get(fid, {"cats": set()})
        cats_map = {c: (c in fs.get("cats", set())) for c in CANONICAL_CATEGORIES}
        coverage[fid] = {"cats": cats_map, "checked": sum(cats_map.values()), "target": tgt}

    avg = sum(s["score"] for s in fscores.values()) / max(len(fscores), 1)
    grade = "A" if avg >= 90 else "B" if avg >= 75 else "C" if avg >= 60 else "D" if avg >= 40 else "F"

    findings = {
        "stats": actual, "issues": {"errors": all_errs, "warnings": all_warns},
        "fscores": fscores, "fstats": fstats, "coverage": coverage,
        "sumcheck": sumcheck, "score": round(avg), "grade": grade, "data": data,
    }

    # Terminal output
    print(fmt_terminal(findings, inp.name))

    # File output
    outp.write_text(fmt_md(findings, inp.name), encoding="utf-8")
    print(f"\nAnalysis saved to: {outp}")

    # Exit codes
    if len(all_errs) > 0:
        sys.exit(1)
    if strict and len(all_warns) > 0:
        print(f"\n--strict: {len(all_warns)} warnings treated as errors")
        sys.exit(1)


if __name__ == "__main__":
    main()
