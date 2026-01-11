---
description: Guide for creating RAG-optimized markdown documents for Pickaxe
---

# Knowledge Base (RAG) Style Guide

**Purpose:** Ensure all documents uploaded to the Pickaxe Knowledge Base are optimized for Semantic Search (RAG).
**Target Audience:** Humans writing documentation for the AI.

---

## 1. Global Principles (The "Golden Rules")

1.  **Strict Markdown:** Always use valid Markdown (`#`, `##`, `-`, `|`). No custom HTML or complex styling.
2.  **No Fluff:** Remove introductions, "welcome" text, apologies, or conversational filler. The AI does not need them.
3.  **Self-Contained Chunks:** Every section (under a `##` header) must make sense if read in isolation.
    *   *Bad:* "As mentioned above..."
    *   *Good:* "In the [Enrollment Rules](#) section..."
4.  **One Topic Per Header:** Do not mix multiple distinct concepts in one paragraph. Break them with headers.

---

## 2. File Structure

Every file must follow this skeleton:

```markdown
# [Clear, Descriptive Document Title]

**Source**: [Origin of data, e.g., "Policy Manual"]
**Domain**: [Topic, e.g., "Compass Compensation Plan"]
**Version**: [e.g., "2026-01-10"]

## [Major Concept A]
[Fact-dense paragraph]

### [Detailed Sub-concept]
[Specific rules or data]

## [Major Concept B]
...
```

### Critical Heading Rules
*   **No Numbers in Headers:** Use `## The Four Mindsets`, NOT `## 1. The Four Mindsets`. Numbers confuse the semantic search.
*   **Hierarchy:** Use `#` for Title, `##` for Sections, `###` for Subsections. Never skip levels.
*   **Descriptive:** Headers should describe the *content*, not the structure.
    *   *Bad:* `## Section 1`
    *   *Good:* `## Eligibility Requirements for Senior Partner`

---

## 3. Formatting Standards

### Paragraphs
*   **Short & Punchy:** 1-3 sentences maximum.
*   **Fact-First:** Start with the core noun/verb. Avoid "In this section we will discuss..."

### Lists
*   **Bulleted (`-`):** For collections of facts, pros/cons, or features.
*   **Numbered (`1.`):** ONLY for sequential steps in a process.
*   **Flat Structure:** Avoid nesting more than 2 levels deep.

### Tables
*   **Markdown Only:** Use standard `| Col 1 | Col 2 |` syntax.
*   **Small & Focused:** Split large tables into smaller ones by topic.
*   **Context Rows:** Each row must be understandable on its own.

### Images & Screenshots
*   **No Images:** The RAG system cannot "see" images in Markdown.
*   **Alt-Text Strategy:** If an image is critical, describe it in text:
    *   *Example:* "The dashboard displays three metrics: Leads, Sales, and Retention."

---

## 4. Pickaxe-Specific Optimizations

### Token Limits
*   **Chunk Size:** Pickaxe ingests text in chunks of roughly 300-500 words.
*   **Section Length:** Keep `##` sections under **500 words**. If longer, introduce `###` breaks.

### Compliance & Constraints
*   **Repetition is Okay:** If a compliance warning (e.g., "Not medical advice") applies to multiple distinct sections, **repeat it** in each section. Do not rely on a single disclaimer at the top of the file (it might not be retrieved).

### Navigation
*   **No Links:** Do not include "Table of Contents", "Back to Top", or internal page navigation. These are noise to the AI.

---

## 5. Document Type Templates

### A. How-To / SOP
```markdown
# Process: [Name]

## Purpose
[Why do this?]

## Prerequisites
[What is needed before starting?]

## Step-by-Step Instructions
1. [Step 1]
2. [Step 2]

## Troubleshooting
- [Common Error]: [Fix]
```

### B. Policy / Reference
```markdown
# Policy: [Name]

## Scope
[Who does this apply to?]

## Core Rules
- [Rule 1]
- [Rule 2]

## Exceptions
- [Exception case]
```

### C. Concept / Framework
```markdown
# Framework: [Name]

## Definition
[What is it?]

## Key Principles
- [Principle A]
- [Principle B]

## Examples
*   **Scenario:** [Context] -> **Application:** [How to use]
```

---

## 6. Pre-Flight Checklist (The "AI Audit")
*Before saving, ask:*
1.  [ ] Is there exactly ONE `#` title?
2.  [ ] Are all headers stripped of chapter numbers?
3.  [ ] Are paragraphs short and factual?
4.  [ ] Is "fluff" removed?
5.  [ ] Would a retrieved paragraph make sense if you didn't read the one before it?
