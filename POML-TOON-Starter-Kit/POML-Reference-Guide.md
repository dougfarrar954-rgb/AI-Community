# POML (Prompt Orchestration Markup Language) Reference Guide

**Source:** [Microsoft Official Documentation (v0.0.8)](https://microsoft.github.io/poml/0.0.8/)  
**Status:** Official Microsoft Open Source Technology

---

## 1. Core Syntax Structure

A standard `.poml` file MUST be wrapped in the root `<poml>` tag.

```xml
<poml>
  <!-- Content goes here -->
</poml>
```

## 2. Intention Components (The "Why" & "What")

These tags define the prompt's core purpose.

| Tag | Usage | Attributes |
|-----|-------|------------|
| `<role>` | Sets the persona (System Identity). | `caption` (default "Role") |
| `<task>` | Defines the primary objective. | `caption` (default "Task") |
| `<stepwise-instructions>` | Detailed operational protocols/steps. | `caption` (default "Stepwise Instructions") |
| `<example>` | Few-shot training examples. | N/A |

### Example
```xml
<role>You are a senior python engineer.</role>
<task>Refactor the usage of the following function.</task>
```

## 3. Structural Components

| Tag | Usage | Attributes |
|-----|-------|------------|
| `<cp>` | **Captioned Paragraph**. The universal container for named sections. **Replaces custom `<area>` or `<section>` tags.** | `caption="My Section Title"` (Required) |
| `<list>` | Container for list items. | `type="bullet"` (default) or `"number"` |
| `<item>` | Individual list items. | N/A |

### Example: Custom Section
```xml
<!-- Instead of <voice_guidelines> -->
<cp caption="Voice & Tone Guidelines">
  <list>
    <item>Be empathetic but firm.</item>
    <item>Avoid jargon.</item>
  </list>
</cp>
```

## 4. Data Components (Context Logic)

| Tag | Usage | Attributes |
|-----|-------|------------|
| `<Document>` | Embeds external files (PDF, DOCX, TXT). | `src="path/to/file.pdf"`, `multimedia="false"` |
| `<table>` | Embeds CSV/TSV data. | `src="data.csv"` |
| `<img>` | Embeds images (Multimodal). | `src="image.png"` |

## 5. Logic & Control Flow

POML supports logic within the prompt construction (handled by the POML rendering engine).

| Feature | Syntax | Usage |
|---------|--------|-------|
| **Variables** | `{{ var_name }}` | Dynamic value injection. |
| **Definitions** | `<let>` | `<let name="user_name" value="Alice" />` |
| **Loops** | `for` | `<item for="rule in rules">{{ rule }}</item>` |
| **Conditionals** | `if` | `<p if="{{ is_admin }}">Wait for approval.</p>` |

## 6. Official Tag Mapping Strategy (For Refactoring)

When migrating custom XML system prompts to POML:

| Custom Tag | Official POML Replacement |
|------------|---------------------------|
| `<identity>`, `<persona>` | `<role>` |
| `<mission>`, `<objective>` | `<task>` or `<task><list>...</list></task>` |
| `<directive name="X">` | `<cp caption="X">` |
| `<operational_directives>` | `<stepwise-instructions>` |
| `<context>`, `<knowledge>` | `<cp caption="Context">` or `<Document>` |
| `<output_format>` | `<cp caption="Output Format">` (or custom `<output-format>` if supported in newer versions, but `<cp>` is safest) |

---

## 7. The "Hybrid Architect" Standard (Advanced)

For advanced users following "Architect" principles, use these constraints to ensure high-reasoning performance while staying valid:

### Strict Mode
Always start your file with:
```xml
<poml version="3.0" strict_mode="true">
```
This signals the AI to stop suggesting generic XML and enforce logic.

### Input Constraints (Named Selection)
To prevent "I choose option 1" errors, **ALWAYS** include this block after your protocols:

```xml
<stepwise-instructions caption="Input Constraints">
  <list>
      <item><b>Rule:</b> STRICTLY PROHIBIT numeric inputs (1, 2, 3).</item>
      <item><b>Rule:</b> User must type the <b>Name</b> or <b>Keyword</b> to confirm choice.</item>
  </list>
</stepwise-instructions>
```
