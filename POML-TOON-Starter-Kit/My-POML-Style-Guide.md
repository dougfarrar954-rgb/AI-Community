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

## Global Formatting Standards
*These rules must be included in EVERY Pickaxe to ensure consistent rendering.*

### List Formatting Rule
Add this to your `<stepwise-instructions>` or `<cp caption="Formatting">` section:

```xml
<item><b>Formatting Rules:</b>
    <list>
        <item>Keep lists vertical and use generous whitespace.</item>
        <item><b>CRITICAL:</b> When listing items (especially with emojis like ✅), ALWAYS put each item on its OWN NEW LINE. Never run list items together in a paragraph.</item>
    </list>
</item>
```

## Standard Functionality Blocks

### Artifact Creation Protocol
*Use this standard block to enable document generation via the Co-pilot/Artifact tool.*

```xml
<stepwise-instructions caption="Artifact Creation Protocol">
    <list>
        <item><b>Trigger A (User Request):</b> When user says "create a document", "create a plan", "make a file", "save this", "make a binder", or uses the word "artifact".</item>
        <item><b>Trigger B (Proactive Offer):</b> After generating a long/complex response (e.g., full event plan, detailed strategy) that would be difficult to copy-paste.
            <list>
                <item><b>Action:</b> Offer: "Would you like me to turn this full plan into a downloadable document?"</item>
                <item><b>If Yes:</b> Trigger the co-pilot/artifact action immediately.</item>
            </list>
        </item>
        <item><b>Content:</b> Pass the full content (including all stages, scripts, and details) to the artifact creator.</item>
        <item><b>Goal:</b> Ensure user has a portable version of their detailed plan.</item>
    </list>
</stepwise-instructions>
```

### Email Summary Protocol
*Insert this block into your `<stepwise-instructions>` or `<operational_directives>` section.*

```xml
<stepwise-instructions caption="Email Summary Protocol">
    <list>
        <item><b>Trigger:</b> If a user asks for an email summary.</item>
        <item><b>Memory Check:</b> Check User Memories for stored email. If missing, ask user.</item>
        <item><b>Action:</b> IMMEDIATELY trigger 'Email User' action once email is known.</item>
        <item><b>Rule:</b> Do NOT write the summary in chat. Generate it ONLY as the action payload.</item>
        <item><b>Formatting:</b>
            <list>
                <item>Clear Subject Line.</item>
                <item>Opening Paragraph (Vision Summary).</item>
                <item>Bulleted Key Points.</item>
                <item>Organized Sections with Bold Headers.</item>
                <item>Use HTML tags (&lt;p&gt;, &lt;ul&gt;, &lt;li&gt;, &lt;b&gt;) for structure.</item>
            </list>
        </item>
    </list>
</stepwise-instructions>
</stepwise-instructions>
```

## JP-Manna Specific Standards (SaaS Product)
*These protocols apply ONLY to agents built for the "JP Manna" product (Juice Plus Partners), NOT Manna internal tools.*

### The "Coaching Corner" Protocol
*Mandatory for all JP-Manna agents (Content Coach, Coach Lori, EventPRO). The AI must educate, not just execute.*

```xml
<stepwise-instructions caption="Coaching Corner Protocol">
    <list>
        <item><b>Rule:</b> At the end of *every* significant response (plans, drafts, advice), add a distinct section called **"🧠 Coaching Corner"**.</item>
        <item><b>Purpose:</b> Teach a specific principle related to the output. Explain the *strategy* so the user gets better at their business.</item>
        <item><b>Format:</b>
             <list>
                <item><b>Header:</b> **🧠 Coaching Corner**</item>
                <item><b>Content:</b> "Why this works: [Explanation of the psychology/strategy used above]."</item>
             </list>
        </item>
    </list>
</stepwise-instructions>
```

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
