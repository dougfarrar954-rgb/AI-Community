# POML Starter Kit for Pickaxe Creators ⛏️

Welcome! This kit contains everything you need to start building advanced AI assistants on Pickaxe using **POML** (Prompt Orchestration Markup Language).

## 📂 What's Inside?

1.  **`POML-Reference-Guide.md`**: The official syntax guide for writing POML prompts.
2.  **`Pickaxe-Manual.md`**: A comprehensive guide to the Pickaxe platform.
3.  **`template.poml`**: A ready-to-use template (Hybrid Architect Edition) with built-in reasoning guards.
4.  **`My-POML-Style-Guide.md`**: Custom rules for project organization and "Rebel" workflows.
5.  **`Git-Guide_for_Non_Coders.md`**: A cheat sheet for backing up your prompts using simple Git commands.

---

## 🚀 Setup Guide: VS Code & POML

To write POML effectively, you need **Visual Studio Code** (VS Code) and the official Microsoft extension. This gives you syntax highlighting, autocomplete, and error checking.

### Strict Mode & Architect Rules 🏗️
The included template uses **Strict Mode** (`<poml strict_mode="true">`). This logic:
- Prevents the AI from hallucinating generic XML.
- Enforces **"Named Selection"** (users must type keywords, not numbers).
- Injects a **Reasoning Protocol** so the AI thinks before speaking.

### Step 1: Install VS Code
If you don't have it, download and install valid [Visual Studio Code](https://code.visualstudio.com/).

### Step 2: Install the POML Extension
1.  Open VS Code.
2.  Click the **Extensions** icon on the left sidebar (or press `Ctrl+Shift+X`).
3.  Search for **"POML"**.
4.  Look for the extension by **Microsoft** (usually titled "Prompt Orchestration Markup Language").
5.  Click **Install**.

### Step 3: Configure settings (Optional but Recommended)
1.  Press `Ctrl+,` to open Settings.
2.  Search for "POML".
3.  You can configure API keys here if you want to run prompts directly in VS Code (e.g., OpenAI API key), but for **Pickaxe**, you mainly need the *syntax highlighting*.

---

## 📝 How to Use with Pickaxe

1.  **Write your prompt** in VS Code using the `.poml` format (use `template.poml` as a base).
2.  **Preview it** (if the extension supports it) or just ensure there are no red error squiggles.
3.  **Copy the content** (everything inside `<poml>...</poml>`).
4.  **Paste it** into the **Prompt** tab of your Pickaxe Builder.

### Why use POML?
- **Structure:** Keeps complex instructions organized (Identity, Task, Rules).
- **Clarity:** Semantic tags like `<role>` and `<stepwise-instructions>` help the AI understand you better.
- **Maintainability:** Easier to read and edit than a giant wall of text.

---

## 🔧 Utility: POML to TOON Converter

This kit includes a Python utility (`poml_to_toon_converter.py`) to convert your structured `.poml` files into a flat text format (TOON) if you prefer that style or need strict legacy compatibility.

**Usage:**
1. Open a terminal in this folder.
2. Run the command:
   ```bash
   python poml_to_toon_converter.py <input_file.poml> <output_file.txt>
   ```
   *Example:* `python poml_to_toon_converter.py template.poml template-converted.txt`

---

Happy building! 🚀
