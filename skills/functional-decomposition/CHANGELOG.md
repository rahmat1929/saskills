# Changelog

All notable changes to the functional-decomposition skill.

---

## [3.0.0] - 2026-03-26

### Added
- **Phase 4: Redo & Improve workflow** — iterative improvement loop that reads
  analyzer output and fixes specific issues without regenerating from scratch.
  Supports targeted fixes ("fix FT-004"), category fixes ("edge cases are weak"),
  and full improvement runs ("get it to A score"). Shows score trajectory.
- **Worked example** (`references/worked-example.md`) — gold standard
  decomposition of one complete feature (Authentication) that Claude uses as a
  pattern for format, depth, and specificity.
- **Analyzer v2** (`scripts/analyze.py`) — complete rewrite with structural
  compliance checks, content quality checks, and `--strict` flag.
- **CHANGELOG.md** — this file.

### Changed
- **Output header format** — Source, Date, Features, Stories, Total Points now
  each on their own line instead of cramped on one line.
- **Output template** — all repeating sections (AC, EC, ERR) now use table
  format instead of prose blocks for better scannability.
- **Dashboard section** added to output — quick quality indicators at the top.
- **Analyzer checks expanded** from 7 to 16 checks including structural
  compliance, vague language detection, placeholder detection, negative AC
  presence, "So that" value check, and table format enforcement.

### Fixed
- Analyzer regex for table format detection no longer false-positives on
  markdown table separators.

---

## [2.0.0] - 2026-03-26

### Added
- **Table-based output format** — AC, edge cases, error scenarios all in tables.
- **Story overview table** per feature — scannable summary before detailed prose.
- **Dashboard section** in output — health indicators at a glance.
- **Analyzer script** (`scripts/analyze.py`) — validates output quality with
  feature scoring, coverage matrix, and summary verification.
- **Complexity scaling** — depth targets (S/M/L) determine how many stories,
  ACs, edge cases, and error scenarios each feature gets.

### Changed
- Phase 3 output template completely redesigned for readability.
- Feature sections now open with a metadata card (complexity, risk, context).

---

## [1.0.0] - 2026-03-25

### Added
- Initial skill with 3-phase workflow (Observe, Decompose, Output).
- Two parsing paths: structured requirements and semi-structured notes.
- 8-step decomposition process per feature.
- INVEST validation with auto-split for 13-point stories.
- Reference files: story-writing-guide.md, detection-matrices.md.
- Integration points with RefoundAI/lenny-skills.
