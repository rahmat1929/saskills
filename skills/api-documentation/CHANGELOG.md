# Changelog

All notable changes to the `api-documentation` skill will be documented in this file.

## [1.1.0] - 2026-03-31
### Added
- Added `references/api_template.md` describing standard API documentation architecture (Headers, Endpoint Methods, Request/Response Tables, Errors).
- Added `README.md` using the standard README template.
- Added `CHANGELOG.md`.

### Changed
- Adjusted default output location of generated artifacts from `docs/` to `docs/api/`.
- Modified expected output workflow to prioritize writing a single unifying `documentation.md` document following the reference template format, rather than only utilizing a fragmented multi-directory approach.

## [1.0.0] - Initial Release
### Added
- Created foundational instructions for generating comprehensive developer documentation.
- Integrated generation rules for OpenAPI 3 (Swagger), Express/TypeScript decorators, rate limits, pagination, and multi-file guides.
