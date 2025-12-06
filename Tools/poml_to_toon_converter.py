import sys
import re
import os

def convert_poml_to_toon(file_path):
    """
    Converts a POML file to TOON format.
    v3: Improved robustness for newlines and nested structure.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Remove XML Comments <!-- ... -->
        content = re.sub(r'<!--[\s\S]*?-->', '', content)

        # 2. Extract Captions from ANY tag
        # Matches <tag ... caption="Something" ...> and replaces with "Something:"
        # We assume the tag opening might span multiple lines, though usually it's one.
        # We'll do a specific pass for known container tags to replace them with their caption or a default label.
        
        # Specific Tag Replacements
        
        # Role -> role:
        content = re.sub(r'<role[^>]*>', 'role:', content)
        content = content.replace('</role>', '')

        # Task -> task:
        content = re.sub(r'<task[^>]*>', 'task:', content)
        content = content.replace('</task>', '')

        # Captions handling (Transform <cp caption="Foo"> into "Foo:")
        # We use a lambda to replace the match with the captured group + ":"
        def caption_replacer(match):
            return f"\n{match.group(1)}:"
            
        content = re.sub(r'<[\w-]+[^>]*caption="([^"]*)"[^>]*>', caption_replacer, content)

        # Cleaning up closing tags for captioned sections
        for tag in ['cp', 'stepwise-instructions', 'context']:
            content = content.replace(f'</{tag}>', '')

        # 3. Lists and Items
        # Remove <list> (and type attributes)
        content = re.sub(r'<list[^>]*>', '', content)
        content = content.replace('</list>', '')

        # Items -> "  - "
        # We first replace <item> with a marker, then clean up newlines later
        content = re.sub(r'\s*<item>\s*', '\n  - ', content)
        content = content.replace('</item>', '')

        # 4. Examples
        content = re.sub(r'<example[^>]*>', '\n*** Example ***', content)
        content = content.replace('</example>', '')
        
        content = re.sub(r'<HumanMessage[^>]*>', '\nUser:', content)
        content = content.replace('</HumanMessage>', '')
        
        content = re.sub(r'<AiMessage[^>]*>', '\nAI:', content)
        content = content.replace('</AiMessage>', '')

        # 5. Clean HTML formatting (b, i, p) but keep the content
        # We replace <b>Text</b> with Text
        content = re.sub(r'</?(b|i|strong|em|p|poml)[^>]*>', '', content)

        # 6. Final Whitespace Cleanup
        # Valid output usually has 1 instruction per line or a list.
        # We split by lines, strip each line, and join them back if they aren't empty.
        
        lines = content.splitlines()
        clean_lines = []
        for line in lines:
            stripped = line.strip()
            # If line is not empty, append it. 
            # If it starts with a bullet "-", preserve the indentation we added earlier (\n  - )
            # Wait, line.strip() removes the indentation we just added!
            # Let's be smarter.
            
            if not stripped:
                continue
                
            # If we added our own indent for items, we want to keep it.
            # Our regex added "\n  - ", so let's look for lines starting with "- " or indented.
            
            # Re-indentation logic:
            if stripped.startswith("- "):
                clean_lines.append(f"  {stripped}")
            else:
                clean_lines.append(stripped)

        # Print result
        print("\n".join(clean_lines))

    except Exception as e:
        print(f"Error converting file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python poml_to_toon_converter.py <path_to_poml_file>")
    else:
        convert_poml_to_toon(sys.argv[1])
