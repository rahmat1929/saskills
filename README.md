# SaSkills

A premium collection of expert-level AI skills designed for system analysis, technical architecture, documentation, and product management. These skills empower your AI coding assistant with highly structured, professional workflows tailored for the complete software development lifecycle.

## 🌟 Available Skills

| Skill | Description | Use Case |
|-------|-------------|----------|
| **[api-documentation](./skills/api-documentation)** | Generates comprehensive, developer-ready API documentation (REST, GraphQL, SDKs). | OpenAPI/Swagger generation, interactive docs, API references. |
| **[database-design](./skills/database-design)** | Designs and optimizes production-grade database schemas for SQL and NoSQL databases. | Table/collection design, relationships, indexing strategies, and performance optimization. |
| **[functional-decomposition](./skills/functional-decomposition)** | Decomposes software requirements into granular user stories, acceptance criteria, edge cases, and error scenarios. | Backlog generation, sprint planning, and deep edge-case detection. |
| **[requirement-analysis](./skills/requirement-analysis)** | Conducts structured requirement gathering and analysis for robust software projects. | Project scoping, discovery sessions, defining business goals, and identifying architectural constraints. |
| **[system-documentation](./skills/system-documentation)** | Generates Business Requirements Documents (BRD) and Functional Specification Documents (FSD). | Formalizing project requirements, system behavior specs, and achieving stakeholder alignment. |

---

## 💻 Installation

You can install these skills directly into your AI assistant's workspace using the `npx skills` command.

### Install All Skills (Recommended)

To install the entire suite of `SaSkills` into your project:

```bash
npx skills add rahmat1929/saskills
```

### Install Specific Skills Only

If you only need specific capabilities, you can specify them using the `--skill` flag:

```bash
npx skills add rahmat1929/saskills --skill api-documentation database-design
```

*Available individual skills:* `api-documentation`, `database-design`, `functional-decomposition`, `requirement-analysis`, `system-documentation`.

## 🚀 How to Use

Once installed, your AI assistant will inherently recognize these capabilities. You can trigger them naturally by mentioning the workflows in your prompts. 

For example, type to your AI assistant:
- *"I need to map out user stories and do a **functional decomposition** for our new checkout feature."*
- *"Help me write an **FSD** (Functional Specification Document) based on these meeting notes."*
- *"Let's do some **requirement analysis** for a new mental wellbeing app before we start coding."*
- *"Based on this PRD, help me **design the database** schema."*

For detailed workflows, boundaries, and internal rules of each skill, refer to the `SKILL.md` file located inside each respective skill directory.
