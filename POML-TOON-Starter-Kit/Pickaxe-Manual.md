# Pickaxe Platform User Manual

**Source:** https://pickaxe.co/post/pickaxe-user-manual-how-to-do-everything-in-pickaxe  
**Saved:** 2025-12-06  
**Purpose:** Reference documentation for building custom AI assistants on Pickaxe

---

## Overview

**Pickaxe** is a no-code, self-serve platform for creating AI tools, sharing them with users, and monetizing them with paywalls and usage limits. If you want to build AI tools for yourself, your company, your clients, or your customers, Pickaxe is a simple place to do that.

📺 **Quick Start:** [10-min video tour of Pickaxe](https://www.youtube.com/watch?v=MZ-u8r_Mbsg)  
💬 **Help:** [Pickaxe Doorman AI](https://studio.pickaxe.co/STUDIO73CVEX31DUTEC3J/3FZIUGIATE) (chatbot trained on Pickaxe materials)  
❓ **FAQ:** [Frequently Asked Questions](https://beta.pickaxeproject.com/FAQ)  
🧑‍💼 **Hire experts:** [Pickaxe Expert Directory](https://beta.pickaxeproject.com/experts)

---

## Table of Contents

1. [How to Build a Pickaxe](#how-to-build-a-pickaxe)
   - [Forms vs Chatbots](#forms-vs-chatbots)
   - [The Builder](#the-builder)
   - [Image Generation & File Upload](#image-generation--file-upload)
2. [The Knowledge Base](#the-knowledge-base)
   - [How it Works (RAG)](#how-does-the-knowledge-base-work)
   - [Uploading Files](#uploading-files)
   - [Knowledge Base Settings](#knowledge-base-settings)
3. [Actions](#actions-connecting-apis)
4. [Studios](#studios)
   - [Studio Websites](#studio-websites)
   - [Public vs Invite-Only](#public-vs-invite-only-studios)
   - [Monetizing & Paywalling](#monetizing-paywalling--restricting-usage)
5. [Embedding Pickaxes](#embedding-pickaxes)

---

# How to Build a Pickaxe

## Forms vs Chatbots

A **Pickaxe** is an AI tool built on top of an LLM (like OpenAI's GPT-4 or Anthropic's Claude Sonnet). You can write special instructions (prompts), give it special knowledge (upload data), and connect it to other software/APIs via **Actions**.

### Two Types of Pickaxes:

| **Chatbot** | **Form** |
|-------------|----------|
| Open-ended conversation box like ChatGPT | Structured series of input fields |
| User types whatever they want, back-and-forth chat | User fills out fields, hits "submit", gets output |
| Most popular type | Preferred when you want more structure |

**Note:** The difference is mainly in the end-user experience. Building a Form or Chatbot is very similar on the backend.

---

## The Builder

🔗 **Access:** [Pickaxe Builder](https://pickaxe.co/builder)

The Builder is a **two-panel interface**:
- **Left panel:** Build your tool (write prompt, add files, configure settings)
- **Right panel:** Test your tool live in real-time

This rapid build-test loop lets you iterate quickly.

### Builder Tabs:

#### 1. **Prompt Tab**
- Write your **prompt** (instructions for how your tool should behave)
- Prompting is "prompt engineering" or "prompt design"
- **Best practice:** Write clearly and explicitly about what you want the AI to do
- **Model Dropdown:** Select which AI model powers your tool
  - **Default:** GPT-4o mini (smart, fast, cheap, capable)
  - Only change if you have a specific reason
  - Example: Copywriters often prefer Claude for prose style

#### 2. **Configure Tab**
- Adjust settings (token limits, etc.)
- Customize icon/image
- Change placeholder text
- Default settings work for most use cases

#### 3. **Knowledge Tab**
- Add files to your **Knowledge Base** (RAG system)
- Upload PDFs, docs, spreadsheets, websites, YouTube videos
- Your tool uses this knowledge to better inform responses

#### 4. **Actions Tab**
- Connect external APIs and services
- Let your tool send emails, generate images, trigger webhooks, etc.
- Extends your tool beyond just generating text

📺 **Tutorials:**
- [Chatbot builder tutorial](https://www.youtube.com/watch?v=-a2kvpdPguY)
- [Form builder tutorial](https://www.youtube.com/watch?v=NmIKTEBUsD8)

---

## Image Generation & File Upload

### End-User File Upload

**Toggle:** "Allow users to upload files" in the Prompt tab

- Adds a paperclip icon to your Pickaxe
- Users can upload text files (Word docs, PDFs, txt, spreadsheets)
- **Session-based:** Uploads don't persist across conversations
- **How it works:**
  - Small files: Entire content dumped into conversation
  - Large files: Converted to vector embeddings, accessed via RAG

📖 [Detailed explanation of end-user upload](https://community.pickaxeproject.com/t/how-are-files-uploaded-by-the-end-user-handled-an-answer/3649)

### Image Recognition

**Requirements:**
- Enable end-user upload
- Use an OpenAI model (e.g., GPT-4o)
- Only OpenAI models support image recognition

📺 [Video tutorial: Image recognition Pickaxe](https://www.youtube.com/watch?v=xM_jZIKiNVo)

### Image Generation

**Toggle:** "Use default image generation"

- Uses **Flux** AI image model
- Only generates images when appropriate
- Smart at following instructions about when to generate images
- Can connect other image models (DALL-E) in the Actions tab

---

# The Knowledge Base

## How Does the Knowledge Base Work?

The Knowledge Base is a **RAG (Retrieval Augmented Generation)** system that lets you upload documents too large for an AI model to read directly.

### How it Works:

1. **Upload a file** → System breaks it into small uniform chunks
2. **Chunks → Vector embeddings** → Stored for fast semantic search
3. **User sends message** → System scans chunks, scores them by relevance
4. **Most relevant chunks** (usually a few paragraphs) → Inserted into chatbot's context
5. Chatbot answers using that context

**Key Point:** Your Pickaxe doesn't read/memorize the entire document every time. It only looks at the most relevant chunks.

> You can upload **millions of words**, and your Pickaxe will look at the most relevant **few thousand** each time.

📖 [Learn more about RAG](https://www.pinecone.io/learn/retrieval-augmented-generation/)

---

## Uploading Files

**Location:** Knowledge tab in the Builder

### Supported File Types:

| **Type** | **What Gets Added** |
|----------|---------------------|
| Text files (txt, Word, PDF, PowerPoint) | All text (images ignored) |
| Spreadsheets | Special handling: Each row = chunk, headers = properties |
| Webpages | Scraped text (not all webpages cooperate) |
| YouTube videos | Audio transcript |

### Special Handling:

**Spreadsheets:** Pickaxe converts each row into a chunk using the header row as properties. This keeps rows intact within the context of their headers.

📖 [How spreadsheets are added to Knowledge Base](https://community.pickaxeproject.com/t/how-upload-a-large-spreadsheet-csv-file-into-the-knowledge-base/2355/4)

### Viewing Chunks:

- Click on a file in Knowledge Base → Opens **Chunk Explorer**
- See exactly what's being pulled from the file
- View every chunk individually

### Knowledge Base Limits:

| **Plan** | **Files per Studio** |
|----------|---------------------|
| Free | 3 files |
| Gold | 50 files |
| Pro | Unlimited |

**Note:** Each Studio has its own Knowledge Base. On a Pickaxe-by-Pickaxe basis, specify which files your Pickaxe pulls from.

---

## Knowledge Base Settings

**Location:** Knowledge tab → Settings

### Two Main Controls:

#### 1. **Relevance Cutoff**
- Filter for how semantically relevant a chunk must be to get pulled
- **High number (0.9):** Only highly relevant chunks
- **Low number (0.4):** Many more chunks referenced
- Recommendation: Experiment with these settings

#### 2. **Amount**
- Limit on total chunks that can be referenced
- Controls how much text from Knowledge Base added to context at once
- **More chunks:** More information, but can dilute response quality

### Chunk Explorer:

- **Purpose:** See how your Knowledge Base is working
- Click on a file → View all chunks
- Enter sample queries → See which chunks come up + relevance scores

### Message Insights:

- Magnifying glass icon under any response in Builder test screen
- Shows which chunks were pulled for that response

📖 [Learn about Message Insights](https://community.pickaxeproject.com/t/message-insights-look-at-knowledge-base-citations/2025)

### Context Field:

- **Default setting:** Leave alone
- **Use case:** Provide extra context to uploaded information
- Example: If uploading highly formatted JSON, explain shorthand/abbreviations

📺 [Video tutorial: Knowledge Base setup](https://www.youtube.com/watch?v=SlWfzz9NRo4)

---

# Actions (Connecting APIs)

## What are Actions?

**Actions** let your Pickaxe do things beyond generating text—like sending emails, posting to Slack, generating PDFs, or triggering webhooks.

> **Analogy:** An Action is like giving your Pickaxe a button it can press to trigger an outside service.

### How Actions Work:

1. Write **natural-language instructions** (trigger prompt)
2. Tell Pickaxe **when and how** to press that button
3. Pickaxe calls external tools, passes info, or pulls results back

**Key Point:** Pickaxe still runs off a no-code prompt, but can now **act** on what it knows.

📖 [Full Actions walkthrough](https://beta.pickaxeproject.com/post/how-to-use-api-actions-walkthrough)

---

## Connecting an Action

**Location:** Actions tab in Builder

### Steps:

1. Select an existing Action
2. Fill out setup fields (different per Action)
3. Write a **trigger prompt** (tells Pickaxe when/how to use the Action)

### Creating Your Own Action:

- For **advanced users**
- Write your own Action in **Python**
- Teach your Pickaxe to call and use it

📺 [Video: Creating advanced Actions](https://www.youtube.com/watch?v=O3oNk9prTjs)

---

## Action Limits by Plan:

| **Plan** | **Actions per Tool** |
|----------|---------------------|
| Free | 1 Action |
| Gold | 3 Actions |
| Pro | Unlimited Actions |

---

## Automation Workflow Shortcut:

**Popular approach:** Connect an Action to automation software like:
- **Zapier**
- **Make**
- **Pabbly**
- **IFTTT**

Build advanced workflows in these tools, then connect a single Action to trigger the automation.

📺 [Video: Make webhook Action tutorial](https://www.youtube.com/watch?v=oV5z2_surcc)

---

## Need Help with Actions?

💬 [Actions section of community forum](https://community.pickaxeproject.com/c/actions/9)

📺 [Video: Setting up Actions](https://www.youtube.com/watch?v=lKrC3LTnfcA)

---

# Studios

## What is a Studio?

**Studios** are workspaces that contain your Pickaxes. This is where you:
- Manage tools
- Share them
- Embed them
- Limit usage
- Monetize
- Monitor activity

**Important:** Whenever you build a Pickaxe, it must go into a Studio.

### Studio Navigation Tabs:

| **Tab** | **Purpose** |
|---------|-------------|
| **Pickaxes** | List of all tools, edit, view info, create embeds |
| **Design** | Customize visual look (colors, fonts, logos, white-labeling) |
| **Users** | See all users, activity, manage users, user memories |
| **Knowledge Base** | Manage files in Studio's Knowledge Base |
| **Access** | Control restrictions: public/invite-only, usage limits, paywalls |
| **Settings** | Miscellaneous: name, logo, custom domain, API key settings, header/footer code |
| **Website** | Studio website where end-users see all Pickaxes |

---

## Studio Websites

Each Studio has a **basic website** where end-users can see all your Pickaxes in one place.

- Tools listed in left-hand navigation
- Click a tool to open it
- Built-in functionality: user auth, payments, user management, usage limiting

---

## Listed vs Unlisted Pickaxes

### Listed
- **Appears** in Studio website
- Sharing link = sharing link to Studio Website with left-nav visible

### Unlisted
- **Does not appear** in Studio website
- Sharing link = standalone tool page only
- Still inherits Studio-level styling and restrictions
- Good for one-off pages

**Note:** You can list/unlist a tool anytime from the Pickaxes tab.

---

## Editing Your Studio Website

**Location:** Website tab → Click "Edit"

Opens **Visual Website Editor** where you can customize your website.

### Adding Pages:

Click the "+" button to add:

1. **Pickaxes** – Your tools (can bulk add)
2. **Content Pages** – Text, images, video embeds
   - Add blocks: Markdown or HTML sections
   - 📖 [Learn more about Content Pages](https://community.pickaxeproject.com/t/announcement-add-custom-content-pages-to-studios/1812)
3. **Folders** – Organize Pickaxes and Content Pages (collapsible/expandable)

### Re-ordering:

- **Drag and drop** pages up/down in left-hand menu
- Changes automatically reflected in Studio Website

**Important:** 
- Click **"Edit Page"** to change text
- Click **"Save Edits"** when done

---

## Public vs Invite-Only Studios

**Location:** Access tab → Studio type setting

### Public
- Anyone can visit (with link)
- Not listed anywhere special in Pickaxe
- Users still subject to your Access settings (e.g., usage limits, paywalls)

### Invite-Only
- Only invited/approved users can access
- Un-approved users hit a login wall
- Users gain access by:
  - Being invited by owner
  - Requesting access (owner approves via email)

### Inviting Users:

**Steps:** Users tab → Manage Users → "+ Add User"
- Invite by email
- Set automatic access level
- Same process for Public and Invite-Only Studios

---

## Monetizing, Paywalling, & Restricting Usage

**Location:** Access tab

### Credits System

**1 credit = 1 use**

Whenever an end-user causes your Pickaxe to generate a response, they spend **1 credit**.

### Guest Settings

**Where:** Access tab → Guest Settings

Control restrictions for visitors who haven't logged in or purchased.

- Set number of credits Guests get
- Credits refresh every 30 days
- Choose: 0 credits, 1 credit, 100 credits, etc.

### Products

**Where:** Access tab → Products & Paywalls section

**Products** are bundles of credits and access you can sell to end-users.

#### When Creating a Product, Set:
- **Price**
- **Number of credits**
- **List of Pickaxes it unlocks**

#### Paywalling:
- If you put a Pickaxe in a Product, it's **paywalled**
- Only users who purchased that Product can access it
- Pickaxes NOT in Products remain available to all users (including Guests)

#### Product Customizations:
- **Billing frequency:** One-time, monthly, yearly
- **Visibility:** Hidden or visible

#### Using Products:
- Products appear on Studio for end-users to purchase
- Visible across backend for admin operations
- When managing users, you can manually upgrade them to any Product

### Connecting Stripe:

To charge for Products, connect your Stripe account.

📖 [How to set up Stripe monetization](https://beta.pickaxeproject.com/post/how-to-set-up-monetization-in-pickaxe-studio-with-stripe)

---

## Managing Users

**Location:** Users tab

### Activity Tab
- See usage across Studio
- Each conversation has AI-generated summary
- Click to see actual conversation

### User Memories Tab
- Set User Memories your Studio will collect/remember about users
- Provides more customized experience per user
- 📖 [Learn about User Memory feature](https://community.pickaxeproject.com/t/user-memory-new-feature-beta/2348)

### Manage Users Tab
- See all users
- Check usage
- Perform admin actions
- **Click on a user:**
  - Give extra credits
  - Manually assign a Product
  - More admin actions

---

# Embedding Pickaxes

One of the most popular features: **Embed your tools into third-party websites**.

Pickaxe lets you customize a slick iframe or script embed, white-label it, and set usage restrictions.

## How to Embed:

1. **Click on a Pickaxe** in your Studio → Opens overview page
2. **Click "+ Create Embed"** button
3. Opens **Embed Customization screen**

### Customize:
- Font, color, sizing
- White-labeling
- Embed type
- Live preview in center of screen

### Usage Limit:
- Set a unique usage limit for this embed
- When user hits limit, they get a custom message redirecting to location of your choice

### Save & Copy:

1. Click **"Save"**
2. Copy/paste embed code (at top of page)
3. If you edit stylization later, **no need to re-embed** (automatically updates)

---

# Still Have Questions?

💬 **Ask the Doorman:** [Pickaxe Doorman AI](https://studio.pickaxe.co/STUDIO73CVEX31DUTEC3J/3FZIUGIATE)  
📧 **Email:** info@pickaxeproject.com

---

**End of Pickaxe User Manual**
