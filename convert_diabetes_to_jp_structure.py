"""
Convert diabetes page from result-card structure to jp-Cell structure (match Cyclistic)
"""
import re
from html.parser import HTMLParser

# Read the file
with open('projects/diabetes/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the "Complete Analysis Workflow" section
workflow_marker = '<h2>Complete Analysis Workflow</h2>'
workflow_start = content.find(workflow_marker)

if workflow_start == -1:
    print("❌ Could not find workflow section")
    exit(1)

# Find where the footer starts
footer_marker = '</main>'
footer_start = content.find(footer_marker, workflow_start)

if footer_start == -1:
    print("❌ Could not find closing main tag")
    exit(1)

# Extract sections
before_workflow = content[:workflow_start]
workflow_html = content[workflow_start:footer_start]
after_workflow = content[footer_start:]

print(f"✓ Found workflow section: {len(workflow_html)} chars")

# Convert each result-card to jp-Cell structure
cell_counter = 1

def convert_result_card(match):
    global cell_counter
    
    card_html = match.group(0)
    
    # Extract h3 title
    h3_match = re.search(r'<h3>(.*?)</h3>', card_html, re.DOTALL)
    if not h3_match:
        return card_html
    
    title = h3_match.group(1).strip()
    
    # Check for code block
    code_match = re.search(r'<pre class="code-block"><code[^>]*>(.*?)</code></pre>', card_html, re.DOTALL)
    
    if not code_match:
        # Just a markdown cell with title
        return f'''
                    <div class="jp-Cell jp-MarkdownCell">
                        <div class="jp-Editor">
                            <h3>{title}</h3>
                        </div>
                    </div>'''
    
    code_content = code_match.group(1).strip()
    
    # Check for output
    output_match = re.search(r'<div class="output">(.*?)</div>', card_html, re.DOTALL)
    
    # Build the new structure
    result = f'''
                    <!-- Markdown Cell: {title} -->
                    <div class="jp-Cell jp-MarkdownCell">
                        <div class="jp-Editor">
                            <h3>{title}</h3>
                        </div>
                    </div>

                    <!-- Code Cell: {title} -->
                    <div class="jp-Cell jp-CodeCell">
                        <div class="jp-InputArea">
                            <div class="jp-InputPrompt">In [{cell_counter}]:</div>
                            <div class="jp-CodeMirrorEditor">
                                <div class="jp-Editor">
                                    <pre><code>{code_content}</code></pre>
                                </div>
                            </div>
                        </div>'''
    
    # Add output if exists
    if output_match:
        output_content = output_match.group(1).strip()
        # Clean up output (remove nested pre/code tags if present)
        output_content = re.sub(r'</?pre[^>]*>', '', output_content)
        output_content = re.sub(r'</?code[^>]*>', '', output_content)
        output_content = output_content.strip()
        
        result += f'''
                        <div class="jp-OutputArea">
                            <div class="jp-OutputPrompt">Out[{cell_counter}]:</div>
                            <div class="jp-OutputArea-output">
                                <pre>{output_content}</pre>
                            </div>
                        </div>'''
    
    result += '''
                    </div>'''
    
    cell_counter += 1
    return result

# Match result-card divs (with proper nesting handling)
# This regex finds <div class="result-card"> and tries to match to its closing </div>
pattern = r'<div class="result-card">.*?(?=<div class="result-card">|<!-- Footer|<footer>|$)'

new_workflow = re.sub(pattern, convert_result_card, workflow_html, flags=re.DOTALL)

# Reconstruct file
new_content = before_workflow + new_workflow + after_workflow

# Write back
with open('projects/diabetes/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"✅ Converted {cell_counter - 1} cells to jp-Cell structure")
print("✅ Diabetes page now matches Cyclistic's tile structure!")
