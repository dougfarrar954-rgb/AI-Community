# My POML Style Guide (For Small Projects & Pickaxe Integration)

## Core Structure (Always Use This Order)
<role>Define the AI persona clearly (1 sentence)</role>
<task>List 1-3 specific actions (bullet points)</task>
<cp caption="Constraints">3-5 hard rules (numbered)</cp>
<cp caption="Output Format">Markdown tables/lists only</cp>

## Required Tags for My Workflow
- <Document src="api_endpoint" preprocess="json"> for Python APIs
- <table headers="true"> for data extraction
- <example> blocks with 1-2 few-shot examples
- {{ variable }} substitution: snake_case only (e.g., {{ project_name }})

## Naming & Organization Rules
- Files: lowercase-with-dashes.poml
- Sections: [section: UPPERCASE]
- Variables: {{ input_data }}, {{ output_path }}
- Git folder: /prompts/{project_name}/

## Prohibited Patterns
- No <img> tags (text-only projects)
- No complex CSS styling
- Max 500 lines per POML file
- No advanced React processing unless specified

## Formatting Best Practices
- **Strict Lists:** Always use newlines for list items. Avoid running multiple items into a single paragraph.
  - *Why?* AI models often shrink lists into paragraphs.
- *Fix:* Explicitly instruct: "ALWAYS put each item on its OWN NEW LINE."

## Standard Protocols
- **Artifact Creation:** For agents that generate long plans or strategies, ALWAYS include the `Artifact Creation Protocol` (see Style Guide). 
  - *Proactive Offer:* Agent should ask to turn long content into a downloadable document.
  - *Keywords:* "create a document", "save this", "artifact".

## Example Template (Copy-Paste Ready)
<role>You are a Git workflow expert for solo developers.</role>
<task>
- Review my git commands
- Suggest only beginner commands
</task>
<cp caption="Constraints">
1. Only use: git init, add, commit, push, pull, status
2. Never suggest rebase or merge
</cp>
<cp caption="Output Format">Checklist format</cp>

## Integration with Pickaxe
- Store in Pickaxe as "system prompt"
- Version with Git tags: v1.0-project-name
- Link to Python API examples in /examples/

## Performance Optimization & Limits

### Token Management
- **Context Window:** While modern models have large windows (128k+ tokens), Pickaxe's RAG system limits the *retrieved* context to a "few thousand" words (approx 2k-4k tokens) of Knowledge Base chunks per query to ensure speed and relevance.
- **System Prompt Size:** Keep your `.poml` file (System Prompt) under **1,500 words** (~2,000 tokens) to leave room for RAG chunks and conversation history.
- **Memory:** Session history grows. Ensure your prompt reiterates critical constraints often if they are getting lost in long chats.

### Latency Tips
- **Model Selection:** Use `GPT-4o mini` (Default) for fastest responses. Only switch to `GPT-4o` or `Claude 3.5 Sonnet` if complex reasoning or specific prose style is required.
- **Action Handlers:** External Actions (APIs) add latency. Inform the user you are "checking..." if the action is slow.

## FAQ: Pickaxe Specifics

### 1. Official vs. Custom Tags
- **Official:** `<role>`, `<task>`, `<stepwise-instructions>`, `<cp>` (Captioned Paragraph), `<Document>`.
- **Custom (Deprecated):** `<identity>`, `<traits>`, `<operational_directives>`. 
  - *Fix:* Use `<role>` instead of `<identity>`. Use `<cp caption="Traits">` instead of `<traits>`. Use `<stepwise-instructions>` instead of `<operational_directives>`.

### 2. How Actions Work in Prompt
- You do not write `<action>` tags in POML to execute code. 
- **Setup:** Configured in the "Actions" tab of Pickaxe.
- **Trigger:** In your POML, write **Natural Language Instructions** (e.g., "When the user asks for stock prices, call the 'GetStockPrice' tool").

### 3. References Knowledge Base Files
- **Upload:** Files go into the "Knowledge" tab.
- **Reference:** You don't *need* to manually reference them in POML; RAG handles it. 
- **Explicit Override:** If you want to force focus, use: `<cp caption="Knowledge Focus">Prioritize information from 'Training_Manual_v1.pdf' in the knowledge base.</cp>`.

### 4. Lint Warnings
- "Component traits not found" is a common warning if you use custom tags like `<traits>`.
- **Solution:** Refactor to `<cp caption="Traits">` to be strictly compliant, or ignore if it works (LLMs are flexible).
