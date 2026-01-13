---
description: 
---

# JP Manna: Pickaxe Migration & Consolidation Master Plan

> **Objective**: Systematically migrate remaining Pickaxes, convert prompts to POML, and establish a clean, version-controlled Knowledge Base.

## Phase 0: Knowledge Base Discovery & Documentation (DO THIS FIRST!)
*Goal: Before touching anything, document EXACTLY what each Pickaxe currently uses so we don't lose track.*

### Step 1: Create the Master Inventory Spreadsheet
- [ ] Open a new spreadsheet (Excel or Google Sheets): `KB-Audit-Worksheet.xlsx`
- [ ] Create these column headers:
    - **Agent Name** | **KB File Name (in Pickaxe)** | **File Type** | **Description/Contents** | **Downloaded?** | **Local Filename** | **Notes**

### Step 2: Audit Each Pickaxe (One at a time - 13 total)
For **each of the 13 agents** listed in Phase 2, do the following:

- [ ] **Open the Pickaxe** in the Builder (pickaxe.co/builder)
- [ ] **Go to the Knowledge Tab**
- [ ] **Screenshot the entire Knowledge Base list** (for visual backup)
    - Save as: `pickaxes/[agent-name]/kb-screenshot-[date].png`
- [ ] **For each enabled file**, record in your spreadsheet:
    - Agent name (e.g., "Manna")
    - Exact filename as shown in Pickaxe (e.g., "Compensation Plan 2025 COMPLETE 20251003.pdf")
    - File type (PDF, DOCX, TXT, CSV, etc.)
    - Brief description of contents (1-2 sentences - what's inside?)
    - Mark "Downloaded?" as NO for now
    - Leave "Local Filename" blank for now

**Repeat for all 13 agents.** This should take 30-60 minutes total.

### Step 3: Download/Locate Originals
Now that you have the complete list, track down the source files:

- [ ] **Check your local computer** first (Documents, Downloads, Desktop folders)
- [ ] **Check Pickaxe Studio Knowledge Base** - you can download files from there:
    - Go to Studio Dashboard → Knowledge Base tab
    - Click on each file → "Download" button (if available)
    - Save to a temp folder: `temp-kb-downloads/`
- [ ] **For files you CAN'T download from Pickaxe:**
    - Check email attachments from team/corporate
    - Check shared drives (Google Drive, Dropbox, OneDrive)
    - Reach out to your upline/corporate contact if needed
- [ ] **Update spreadsheet** as you find each file:
    - Mark "Downloaded?" as YES
    - Record where you found it in "Notes" column

### Step 4: Initial Organization (Before Renaming)
- [ ] Move all downloaded files to: `knowledge-base/ORIGINALS-UNPROCESSED/`
- [ ] **DO NOT rename yet** - keep original names so you can match to spreadsheet
- [ ] **Cross-check**: Make sure every file in your spreadsheet inventory is now in the ORIGINALS folder

### Step 5: Update the Knowledge Base README
Now that you know what you have:

- [ ] Open `knowledge-base/README.md`
- [ ] For each unique file in your inventory spreadsheet, add an entry like:
    ```markdown
    ### `[future-kebab-case-name].pdf`
    - **Original Name:** "Compensation Plan 2025 COMPLETE 20251003.pdf"
    - **Description:** [paste from your spreadsheet]
    - **Used By:** [list all agents from spreadsheet that use it]
    ```

**✅ Checkpoint: You now have a complete inventory before touching anything!**

---

## Phase 1: The "Great Knowledge Base Audit" (Foundation First)
*Goal: Stop the "can of worms" before it spreads. We need a clean source of truth before linking agents.*

- [ ] **Review the spreadsheet** from Phase 0 - you should see duplicate filenames across agents
- [ ] **Identify unique files** - how many distinct documents are there really?
- [ ] **Migrate from ORIGINALS-UNPROCESSED**:
    - [ ] Copy each unique file to `knowledge-base/` (root level)
    - [ ] **Rename using kebab-case**: `business-strategy-q3.pdf` (no spaces, no version numbers)
    - [ ] Update the spreadsheet "Local Filename" column with the new clean name
- [ ] **Audit & Sanitize**:
    - [ ] **Dedupe**: If two agents use "Comp Plan v1" and "Comp Plan v2", decide which is current
    - [ ] **Version Check**: Archive old versions to `knowledge-base/ARCHIVE/` - don't delete yet
- [ ] **Commit**: `git add knowledge-base/` and `git commit -m "Phase 1: Clean KB baseline established"`

---

## Phase 2: Agent Inventory & Staging
*Goal: List exactly what needs to be moved so we don't miss anything.*

- [ ] **List the Missing Agents**: Write down the names of the 14 Pickaxes to be migrated.
    - Agent 1: Manna
    - Agent 2: DMO PRO
    - Agent 3: PromoPRO
    - Agent 4: Content Coach [ ] Migration Started (KB Updated)
    - Agent 5: EventPro
    - Agent 6: Coach Lori
    - Agent 7: Eat More Plants!
    - Agent 8: BibleGPT
    - Agent 9: Mistral Medium [x] Migrated
    - Agent 10: Gemini 3
    - Agent 11: Claude
    - Agent 12: ChatGPT
    - Agent 13: jp2026 and beyond
- [ ] **Create Folders**: Create a directory for each in `pickaxes/` (e.g., `pickaxes/content-coach-pickaxe/`).

---

## Phase 3: The Migration Loop (Repeat for Each Agent)
*Goal: Systematically process one agent at a time.*

### 1. Extraction
- [ ] Copy the current System Prompt from the Pickaxe platform.
- [ ] Paste it into a new file: `pickaxes/[agent-name]/[agent-name].poml` (as raw text first).

### 2. POML Conversion
- [ ] **Structure**: Wrap the raw text in `<poml>` tags.
- [ ] **Tagging**: Convert sections to POML tags (`<identity>`, `<context>`, `<constraints>`, `<knowledge>`).
    - Add references in the POML:
      ```xml
      <knowledge>
        <source>business-strategy-q3.pdf</source>
      </knowledge>
      ```
- [ ] **Standard Features**: Inject the **Email Summary Protocol** block into the `<operational_directives>` (or equivalent) section.
    - *Purpose*: Enables users to request chat summaries via email.
    - *Action*: Ensure "Email User" action is configured in studio.

### 2a. TOON Formatting (MANDATORY)
- [ ] **Convert**: NEVER manually transcribe POML to TOON.
- [ ] **Run Script**: Use the python converter to generate the clean `.txt` file:
    ```bash
    python "c:\Users\dougf\Documents\GitHUB\AI-Community-Shared\POML-TOON-Starter-Kit\poml_to_toon_converter.py" "<PATH_TO_POML>" "<PATH_TO_TOON>"
    ```
- [ ] **Verify**: Ensure the output `.toon.txt` is created/updated.

### 3. Manifest Creation
- [ ] Create `README.md` in the agent's folder.
- [ ] Document the dependencies (which KB files it uses).

---

## Phase 4: Platform Sync
*Goal: accurate reflection in the cloud.*

- [ ] **Upload KB**: Go to Pickaxe Studio -> Knowledge Base -> Remove old files -> Upload clean files from Phase 1.
- [ ] **Update Agents**:
    - Paste the new POML code into the System Prompt.
    - Go to Knowledge Tab -> Toggle ON the specific files listed in the agent's `README.md`.

---

## Phase 5: Final Verification
- [ ] Test each migrated agent with a question that requires a specific KB document to ensure the link works.
