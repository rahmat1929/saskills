# api-documentation

Create comprehensive API documentation for developers. Use this skill when documenting REST APIs, GraphQL schemas, or SDK methods. It expertly handles OpenAPI/Swagger specifications, interactive docs, examples, and API reference guides using structured templates.

---

## Installation

```bash
npx skills add https://github.com/rahmat1929/skill-api-documentation --skill api-documentation
```

### Manual install

Clone and copy to your preferred scope:

| Scope | Path |
|-------|------|
| Project (shared) | `.agents/skills/api-documentation/` |
| Personal (local) | `~/.cursor/skills/api-documentation/` |

```bash
git clone https://github.com/rahmat1929/skill-api-documentation.git
cp -r skill-api-documentation/ .agents/skills/api-documentation/
```

### Verify installation

Ask the agent:

> "Create api documentation based on..."

If it responds correctly by generating a `docs/api/documentation.md` alongside proper schemas, the skill is active.

---

## Skill Contents

```text
api-documentation/
├── SKILL.md                          # Main skill instructions & workflow
├── README.md                         # This file
├── CHANGELOG.md                      # Version history
└── references/                       
    └── api_template.md               # Standardized markdown format template
```

---

## How It Works

| Phase | What happens |
|-------|-------------|
| **1. Analysis** | The agent evaluates the codebase, provided endpoints, or document references to understand the API design. |
| **2. Generation** | It standardizes the endpoints into a single, cohesive `documentation.md` format using `references/api_template.md`. |
| **3. Boilerplate** | Supplemental documents like OpenAPI specs, `README.md`, `getting-started.md`, and guides are created around it. |

---

## Usage Examples

### Example 1: Documenting a New API

**Prompt:**

> "Create api documentation based on the user-management.js Express file"

**What you get:**

- A generated `docs/api/documentation.md` breaking down the User Management endpoints.
- A fully populated `docs/api/openapi.yaml` OpenAPI 3.0 specification.
- Usage examples and authentication details in markdown formats.

---

### Example 2: Structuring from External Docs

**Prompt:**

> "create api documentation based on https://fcn.sg.larksuite.com/wiki/..."

The agent will read the provided document URL using MCP tools, map it to the reference structure, and output a pristine documentation bundle perfectly scoped for the project architecture.

---

## Output Structure / Format

By default, the skill creates assets inside `docs/api/` with one primary consolidated file:
- `docs/api/documentation.md` (Contains Title, Authentication, Flow, JSON Requests/Responses, error standards)

---

## Supported Platforms

| Platform | Status |
|---|---|
| Claude | ✅ |
| ChatGPT | ✅ |
| Gemini | ✅ |

---

## Requirements

No strict technical dependencies. Works entirely through prompt execution and file generation capabilities.

---

## License

MIT
