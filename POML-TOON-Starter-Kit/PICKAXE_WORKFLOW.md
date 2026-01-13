# Pickaxe Studio Workflow & Architecture

> **Best Practice**: Centralized Knowledge, Distributed Intelligence.

## 1. Studio Architecture Overview

The JP Manna Studio uses a **Hub-and-Spoke** model for knowledge management:

- **Hub**: The `knowledge-base/` folder and Studio-Level Knowledge Base.
- **Spokes**: Individual Pickaxes (Coach Lori, EventPRO, etc.) that consume specific knowledge files.

### The "Why"
- **Efficiency**: Upload once, use everywhere.
- **Consistency**: All agents quote the same source of truth.
- **Version Control**: Git tracks the history of your business logic.

---

## 2. Directory Structure

```text
JP-Manna/
├── knowledge-base/           <-- SINGLE SOURCE OF TRUTH
│   ├── business-strategy.pdf
│   ├── brand-voice.pdf
│   └── compliance-guide.docx
│
├── pickaxes/
│   ├── coach-lori-pickaxe/   <-- Agent Definition
│   │   ├── README.md         <-- Agent Manifest (Dependencies)
│   │   └── coach-lori.poml
│   │
│   ├── event-pro-pickaxe/    <-- Agent Definition
│   │   ├── README.md         <-- Agent Manifest (Dependencies)
│   │   ├── event-pro.poml
│   │   └── event-pro-toon.txt
│   │
│   └── ...
└── PICKAXE_WORKFLOW.md       <-- This Document
```

---

## 3. The Implementation Workflow

Follow this loop to update your AI Studio:

### Step 1: Edit Local Source
Modify your master documents inside the `knowledge-base/` folder.
- *Example*: Update Q3 goals in `business-strategy.pdf`.

### Step 2: Version Control (Git)
Commit your changes to lock in the version.
```bash
git add knowledge-base/
git commit -m "Updated Q3 Business Strategy docs"
git push
```

### Step 3: Platform Sync
1. Go to **Pickaxe Studio Dashboard**.
2. Navigate to **Studio Knowledge Base**.
3. **Re-upload** the modified file(s) from your local `knowledge-base/` folder.
    - *Note*: This replaces the old version for ALL agents using it.

### Step 4: Verification
Test a dependent Pickaxe (e.g., Business Strategist) to ensure it cites the new information correctly.

---

## 4. Pickaxe "Manifest" Maintenance
Every Pickaxe folder must contain a `README.md` that acts as a manifest.
**Purpose**: To track exactly which Studio Knowledge Base files are enabled for that specific agent.

### When to Update the Manifest
- **New Agent**: Create the `README.md` immediately using the standard template.
- **Changing Dependencies**: If you toggle a file ON/OFF in Pickaxe Studio builder, update the `README.md` table to match.
- **Why?** It prevents "drift" where we forget which PDF powers which agent.

---

## 5. Pickaxe Configuration

When building a new Pickaxe:
1. Go to the **Knowledge Tab** in the builder.
2. Select **"Studio Knowledge Base"**.
3. Toggle **ON** only the specific files relevant to that agent's role.

### Configuration Examples
| Agent | Enabled Files |
|-------|---------------|
| **Business Strategist** | `business-strategy.pdf`, `comp-plan.pdf` |
| **Content Coach** | `business-strategy.pdf`, `brand-voice.pdf`, `social-scripts.docx` |
| **EventPRO** | `event-playbook.pdf`, `compliance-guide.docx` |

---

## 6. Action Triggers

**Rule:** All action trigger prompts text **MUST** be stored in the central `actions/triggers.md` file.

- **Do NOT** save trigger text files inside individual Pickaxe folders (e.g., `manna-startpoint-action-trigger.txt`).
- **Do NOT** rely on memory or copy-pasting from old prompts.
- **Why?** Pickaxe Actions often share identical triggers (e.g., "Email Summary"), and editing them in one centralized place ensures valid JSON payloads and consistent behavior across all agents.

---

## 7. File Formats & Conversion (MANDATORY)

Every Pickaxe agent MUST have two files in its folder:
1. `[agent-name].poml` (The Source of Truth)
2. `[agent-name]-toon.txt` (The Platform-Ready Output)

**CRITICAL RULE:** NEVER manually transcribe POML to TOON. Always use the authorized Python script to ensure `100%` fidelity.

### How to Convert:
```bash
python "c:\Users\dougf\Documents\GitHUB\AI-Community-Shared\POML-TOON-Starter-Kit\poml_to_toon_converter.py" "<PATH_TO_POML>" "<PATH_TO_TOON>"
```
This script strips XML tags and formats the prompt into the official clean-text format required for the Pickaxe System Prompt field.

---

## 8. Platform Deployment & Optimization (MANDATORY PRE-FLIGHT)

Before clicking "Save" on any Pickaxe, you **MUST** verify the **Context Window & Token Settings**. Default settings are often insufficient for RAG-heavy agents.

### The "Content Coach" Standard (Example)
Use these baseline settings for any agent that uses RAG + Coaching Logic:

1.  **Output Length:** `~4,000 - 5,000 tokens`
    *   *Why?* Needed for full content calendars or long blog posts.
2.  **Input Length:** `~8,000 tokens`
    *   *Why?* Allows users to paste long transcripts or messy brain dumps.
3.  **Knowledge Base (RAG):** `8,000 - 10,000 tokens` (CRITICAL)
    *   *Why?* If this is too low (e.g., 2000), the bot cannot "read" the Compliance Guide AND the StoryBrand Guide at the same time. **Always maximize this.**
4.  **User Memories:** `2,000 - 3,000 tokens`
    *   *Why?* Ensures the bot remembers user-specific details (rank, niche, voice) over time.
5.  **Memory Buffer:** `20,000 tokens`
    *   *Why?* Keeps the "Coach" attentive during long planning sessions.
