import sys
import re
import os

def convert_poml_to_toon(input_path, output_path):
    """
    Converts a POML file to TOON format with improved tag handling.
    """
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.")
        return

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Remove structure comments
        content = re.sub(r'<!--[\s\S]*?-->', '', content)

        # 2. Tag to Header Mappings
        # Maps <tag> to "\nHEADER:"
        headers = {
            'identity': 'IDENTITY',
            'traits': 'TRAITS',
            'operational_directives': 'OPERATIONAL DIRECTIVES',
            'knowledge': 'KNOWLEDGE BASE',
            'output_format': 'OUTPUT FORMAT',
            'safety': 'SAFETY & GUARDRAILS',
            'guardrails': 'GUARDRAILS',
            'income_claims_protocol': 'INCOME CLAIMS PROTOCOL',
            'structure': 'STRUCTURE',
            'presentation': 'PRESENTATION',
            'vision_invitation': 'VISION INVITATION',
            'vision_parsing': 'VISION PARSING',
            'mode_options': 'MODE OPTIONS',
            'instant_blueprint_assumptions': 'INSTANT BLUEPRINT ASSUMPTIONS',
            'planning_phase': 'PLANNING PHASE',
            'promotion_phase': 'PROMOTION PHASE',
            'event_execution': 'EVENT EXECUTION',
            'follow_up_system': 'FOLLOW UP SYSTEM',
            'sources': 'SOURCES',
            'expertise': 'EXPERTISE',
            'format': 'FORMAT',
        }

        for tag, header in headers.items():
            content = re.sub(f'<{tag}[^>]*>', f'\n{header}: ', content)
            content = content.replace(f'</{tag}>', '')

        # 3. Tag to Label Mappings (inline keys)
        # Maps <tag> to "Label:"
        labels = {
            'role': 'role',
            'description': 'description',
            'mission': 'mission',
            'task': 'task',
            'context': 'Context',
            'opening': 'Opening',
            'closing': 'Closing',
            'reassurance': 'Reassurance',
            'benefit': 'Benefit',
            'approach': 'Approach',
            'trigger_phrases': 'Trigger Phrases',
            'blueprint': 'Blueprint',
            'resources': 'Resources',
            'tips': 'Tips',
            'action': 'Action',
            'integration': 'Integration',
            'follow_up': 'Follow Up',
            'collaboration_principle': 'Collaboration Principle',
            'decision_tree': 'Decision Tree',
        }

        for tag, label in labels.items():
            content = re.sub(f'<{tag}[^>]*>', f'\n{label}: ', content)
            content = content.replace(f'</{tag}>', '')

        # 4. Directive Names
        # <directive name="Foo"> -> Foo:
        def directive_replacer(match):
            return f"\n{match.group(1)}: "
        content = re.sub(r'<directive[^>]*name="([^"]*)"[^>]*>', directive_replacer, content)
        content = content.replace('</directive>', '')

        # 4.5 IF Conditions (Decision Trees)
        # <if condition="XYZ">Value</if> -> - If XYZ: Value
        def if_replacer(match):
            return f"\n- If {match.group(1)}: "
        content = re.sub(r'<if[^>]*condition="([^"]*)"[^>]*>', if_replacer, content)
        content = content.replace('</if>', '')

        # 5. Captions (Generic)
        # <cp caption="Foo"> -> Foo:
        def caption_replacer(match):
            return f"\n{match.group(1)}: "
        content = re.sub(r'<[\w-]+[^>]*caption="([^"]*)"[^>]*>', caption_replacer, content)

        # 6. List Items and Rules
        # Maps <tag> to bullet point
        bullets = ['trait', 'rule', 'prompt', 'extract', 'interpret', 'assume', 'mirror', 
                   'item', 'element', 'step', 'source', 'area', 'section', 'case', 'trigger']
        
        for tag in bullets:
            content = re.sub(f'<{tag}[^>]*>', '\n- ', content)
            content = content.replace(f'</{tag}>', '')

        # 7. Generic Strip of unknown tags (HTML/XML) but keep content
        content = re.sub(r'<[^>]+>', '', content)

        # 8. Formatting Cleanup
        lines = content.splitlines()
        clean_lines = []
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            
            # Re-apply indentation for structure
            if stripped.endswith(':'):
                clean_lines.append(f"\n{stripped}") # Extra newline before headers
            elif stripped.startswith('- '):
                clean_lines.append(f"  {stripped}")
            else:
                clean_lines.append(stripped)

        # Join and Write
        final_output = "\n".join(clean_lines).strip()
        # Decode HTML entities (e.g. &amp; -> &) for clean text output
        final_output = final_output.replace('&amp;', '&')
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_output)
            
        print(f"Successfully converted to {output_path}")

    except Exception as e:
        print(f"Error converting file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python poml_to_toon_converter.py <input_poml> <output_txt>")
    else:
        convert_poml_to_toon(sys.argv[1], sys.argv[2])
