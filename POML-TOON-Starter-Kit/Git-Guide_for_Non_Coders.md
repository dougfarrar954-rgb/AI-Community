# Git Guide for Solo Non-Coders: AI/SaaS Developer Workflow

## Your Role: "Vibe Coder" Managing Prompts & Tools
This guide is for solopreneurs building AI tools (Pickaxe, POML, no-code APIs) who copy-paste code but need organized backups. No terminal wizardry required.

## The 7-Command Workflow (Copy-Paste Ready)

### 1. START NEW PROJECT

```bash
mkdir ai-prompt-library
cd ai-prompt-library
git init
echo "# AI Prompt Library" > README.md
git add .
git commit -m "Initial project setup"
```

### 2. DAILY SAVE (Your Main Command)

```bash
git add .
git commit -m "Updated prompts and docs"
git push
```
**Run this every time you edit POML files, Pickaxe exports, or API configs.**

### 3. UPDATE FROM GITHUB (Before Editing)

```bash
git pull
```
**Always run first to avoid conflicts.**

### 4. CHECK WHAT CHANGED

```bash
git status
```
**Green = ready to save. Red = untracked files.**

### 5. SEE HISTORY

```bash
git log --oneline
```
**Shows all your saves with short messages.**

### 6. UNDO MISTAKES (Safe Version)

```bash
git checkout -- prompts/my-broken-file.poml
```
**Restores one file to last save.**

### 7. FIRST GITHUB LINK (One-Time Setup)

```bash
git remote add origin https://github.com/yourusername/your-repo-name.git
git branch -M main
git push -u origin main
```

## Folder Structure for AI/SaaS Solos

```text
my-ai-project/
├── README.md           # What this project does
├── prompts/            # POML files, system prompts
│   ├── v1.0-reviewer.poml
│   └── v1.1-api-doc.poml
├── pickaxe/            # Exported Pickaxe configs
├── examples/           # Working code snippets
├── docs/               # Your style guides, cheatsheets
└── api/                # Python API files (if any)
```

## Pro Tips for Non-Coders
- **Commit message rule**: "Updated X, fixed Y" (under 50 chars)
- **Never edit on GitHub.com** - Always local → push
- **Backup rule**: Commit before big changes (new Pickaxe tool, POML experiment)
- **VS Code bonus**: Use the Git panel (Source Control tab) - click buttons instead of typing

## Common Panic Fixes
- "Nothing to commit": Run `git status` - you're clean!
- "Merge conflict": Don't panic. Copy your version, delete conflict markers, commit
- "Repo gone": Clone it back: `git clone https://github.com/...`

## AI/SaaS Specific Patterns

**Save Pickaxe export**
```bash
git add pickaxe/new-tool.json
git commit -m "Added Pickaxe pricing calculator"
```

**Save POML updates**
```bash
git add prompts/
git commit -m "Improved POML syntax checker"
```

**Save API example**
```bash
git add api/calculator.py
git commit -m "Added Stripe pricing API example"
```

## When to Make New Repos (Not Folders)
- Each major AI tool/toolset gets its own repo
- Example: "pickaxe-pricing-tools", "poml-prompt-library", "saas-api-examples"
- Keep repos under 100 files each

---
*This workflow takes 30 seconds daily and gives you pro version control without coding Git knowledge.*

