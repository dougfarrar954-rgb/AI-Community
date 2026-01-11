# POML (Pickaxe Object Markup Language) - Key Insights

**Date:** 2025-12-06  
**Source:** Pickaxe Platform Manual + User's POML Files

---

## What I Now Understand About POML

After reviewing the Pickaxe documentation, here's what I've learned about POML and how it relates to your workflow:

---

## 🔍 **Important Discovery: POML is NOT in the Official Documentation**

**Key Finding:** The official Pickaxe User Manual does **NOT mention POML at all**.

This suggests:
1. **POML might be a custom format** you (or Pickaxe community) created for organizing prompts
2. **Or** it's an advanced/undocumented feature not covered in the main manual
3. **Or** it's terminology from another platform you're adapting for Pickaxe use

---

## 📋 **What the Manual DOES Say About Prompts**

From the Pickaxe documentation:

### The Prompt Tab (in Builder)
> "In the Prompt tab you can write your prompt, or the instructions for how your tool should behave. Prompting is the practice of writing instructions for an AI model in normal language. It's often called 'Prompt engineering' or 'Prompt Design'. It's about using the right words, format, and structure to guide the AI's output."

**Best practice from Pickaxe:**
> "The best advice is to write clearly and explicitly about what you want the AI to do."

### No XML/Structured Format Mentioned

The manual doesn't reference:
- XML-based prompt formatting
- Tags like `<identity>`, `<traits>`, `<operational_directives>`
- Any structured prompt language

**This means your POML files are likely:**
- A **personal/community innovation** for organizing complex prompts
- Converted to plain text before being pasted into Pickaxe's Prompt field
- Or processed by a tool that converts POML → Pickaxe-ready prompts

---

## 🧩 **How Your POML Files Likely Work in Pickaxe**

Based on your `coach-lori.poml` structure and Pickaxe's features:

### POML Structure → Pickaxe Features Mapping:

| **POML Section** | **Pickaxe Feature** | **How It Works** |
|------------------|---------------------|------------------|
| `<identity>`, `<role>`, `<mission>` | **Prompt Tab** | Defines AI personality/purpose in plain text |
| `<traits>` | **Prompt Tab** | Voice and behavior guidelines |
| `<operational_directives>` | **Prompt Tab** | Detailed instructions for responses |
| `<knowledge><source file="...">` | **Knowledge Base Tab** | Upload PDFs/files; RAG system retrieves relevant chunks |
| `<action>` elements | **Actions Tab** | Connect external APIs/services (Zapier, email, etc.) |
| `<output_format>` | **Prompt Tab** | Instructions for response structure |

---

## ⚙️ **What I Can Now Help You With:**

### ✅ I Understand:
1. **How Pickaxe works** (two-panel Builder, prompt engineering, Knowledge Base RAG, Actions)
2. **How Knowledge Base files are referenced** (upload to Knowledge tab, system auto-retrieves chunks)
3. **How Actions work** (connect external APIs with trigger prompts in plain language)
4. **Studio structure** (workspaces, embedding, monetization, user management)

### ❓ I Still Need Clarification:

1. **Is POML your personal format?** Or is it documented somewhere else?
2. **How do you convert POML → Pickaxe?**
   - Do you manually copy sections into the Prompt tab?
   - Is there a tool that parses POML and generates a Pickaxe-ready prompt?
3. **Are POML tags functional** (parsed by Pickaxe) or **organizational** (just for your own prompt management)?

---

## 💡 **Insights on Your Coach Lori POML File:**

### Multi-Assistant Integration (Lines 65-86)

Your POML had:
```xml
<action>Call EventPRO.</action>
```

**What I now know from Pickaxe docs:**
- Actions in Pickaxe are **external API calls** (webhooks, Zapier, etc.)
- They use **trigger prompts** (natural language instructions)
- The AI decides when to trigger them based on context

**Therefore:**
- If you want Coach Lori to suggest switching to EventPRO, that's **prompt instruction** (not an Action)
- If you want to **automatically trigger** a workflow (e.g., send notification to EventPRO system), that would be an **Action** connected in the Actions tab

**My previous refactoring was correct:**
```xml
<action>Recommend switching to the EventPRO assistant for detailed event planning.</action>
```
This is an **instruction** to the AI, not a technical Action call.

---

### Knowledge Base References

Your POML had:
```xml
<source file="AI_LIFECOACH_TRAINING_Part1.pdf">
    <usage>Primary source for mindset coaching...</usage>
</source>
```

**What I now know:**
- You upload files to the **Knowledge Base tab**
- Pickaxe automatically chunks them and uses **RAG (semantic search)**
- The AI retrieves relevant chunks when needed
- You don't need special syntax in the prompt—just upload the file

**Therefore:**
- The `<source file="...">` tags in POML are **instructional** (telling the AI what files contain)
- In actual Pickaxe usage, you'd upload those files to the Knowledge Base, and the AI accesses them automatically

---

## 🎯 **Recommendations Moving Forward:**

### 1. Clarify POML Workflow
Help me understand:
- How you actually use your `.poml` files with Pickaxe
- Is there a conversion step, or do you copy/paste sections?

### 2. Optimize for Pickaxe
If POML is your organizational tool, I can help:
- **Streamline POML → Plain text conversion** for Pickaxe Prompt tab
- **Map POML sections to Pickaxe tabs** more clearly
- **Create templates** for different Pickaxe component types

### 3. Leverage Pickaxe Features
Based on Coach Lori's goals:
- **Knowledge Base:** Upload `AI_LIFECOACH_TRAINING_Part1.pdf` → automatic RAG retrieval
- **Actions:** Connect Zapier/webhook to notify other assistants (if multi-assistant workflow is automated)
- **User Memories:** Use Pickaxe's User Memory feature to remember partner-specific info across sessions

---

## 📚 **What I've Saved for You:**

✅ **Full Pickaxe Manual:** `c:\Users\dougf\Documents\GitHUB\AI Studios\JP-Manna\pickaxes\.docs\pickaxe-platform-manual.md`

This includes:
- Complete Builder interface guide
- Knowledge Base (RAG) deep dive
- Actions system explanation
- Studio features (monetization, embedding, user management)
- All official Pickaxe documentation consolidated

---

## 🚀 **Next Steps:**

**Tell me:**
1. Is POML your custom format for organizing prompts before putting them in Pickaxe?
2. How do you actually use the `.poml` files with the Pickaxe platform?
3. Are there other Pickaxe docs I should know about (e.g., POML-specific documentation)?

Then I can provide **much more targeted guidance** on optimizing your POML files for Pickaxe! 🎯
