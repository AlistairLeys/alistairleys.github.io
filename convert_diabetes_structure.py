"""
Convert diabetes page from old result-card structure to clean jp-Cell structure like Cyclistic page
"""
import re

# Read the file
with open('projects/diabetes/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the "Complete Analysis Workflow" section
workflow_start = content.find('<h2>Complete Analysis Workflow</h2>')
workflow_section_end = content.find('<!-- Footer Section -->', workflow_start)

if workflow_start == -1 or workflow_section_end == -1:
    print("Could not find workflow section markers")
    exit(1)

# Extract before, workflow, and after sections
before_workflow = content[:workflow_start]
workflow_section = content[workflow_start:workflow_section_end]
after_workflow = content[workflow_section_end:]

print(f"Found workflow section: {len(workflow_section)} characters")

# Convert result-card structure to jp-Cell structure
# Pattern: <div class="result-card"> with h3, code-block, and output
def convert_cell(match):
    full_cell = match.group(0)
    
    # Extract h3 title (becomes markdown cell)
    h3_match = re.search(r'<h3>(.*?)</h3>', full_cell, re.DOTALL)
    if not h3_match:
        return full_cell  # Skip if no h3
    
    title = h3_match.group(1)
    
    # Check if this cell has code
    has_code = '<pre class="code-block">' in full_cell or '<code class="language-python">' in full_cell
    
    if not has_code:
        # Just a markdown cell
        markdown_cell = f'''        <!-- Markdown Cell: {title.strip()} -->
        <div class="jp-Cell jp-MarkdownCell">
            <div class="jp-Editor">
                <h3>{title}</h3>
            </div>
        </div>'''
        return markdown_cell
    
    # Extract code content
    code_match = re.search(r'<pre class="code-block"><code class="language-python">(.*?)</code></pre>', full_cell, re.DOTALL)
    if not code_match:
        return full_cell  # Skip if can't find code
    
    code_content = code_match.group(1).strip()
    
    # Extract output if exists
    output_match = re.search(r'<div class="output">(.*?)</div>', full_cell, re.DOTALL)
    output_content = output_match.group(1).strip() if output_match else None
    
    # Generate cell number based on position
    cell_num = convert_cell.counter
    convert_cell.counter += 1
    
    # Build new structure
    new_cell = f'''        <!-- Markdown Cell: {title.strip()} -->
        <div class="jp-Cell jp-MarkdownCell">
            <div class="jp-Editor">
                <h3>{title}</h3>
            </div>
        </div>

        <!-- Code Cell: {title.strip()} -->
        <div class="jp-Cell jp-CodeCell">
            <div class="jp-InputArea">
                <div class="jp-InputPrompt">In [{cell_num}]:</div>
                <div class="jp-CodeMirrorEditor">
                    <div class="jp-Editor">
                        <pre><code>{code_content}</code></pre>
                    </div>
                </div>
            </div>'''
    
    # Add output if exists
    if output_content:
        # Clean up output content
        output_clean = output_content.replace('</code></pre>', '').replace('<pre><code>', '').strip()
        new_cell += f'''
            <div class="jp-OutputArea">
                <div class="jp-OutputPrompt">Out[{cell_num}]:</div>
                <div class="jp-OutputArea-output">
                    <pre>{output_clean}</pre>
                </div>
            </div>'''
    
    new_cell += '''
        </div>'''
    
    return new_cell

# Initialize counter
convert_cell.counter = 1

# Replace all result-card divs in workflow section
# Match result-card div with all its content until the closing </div>
pattern = r'<div class="result-card">.*?</div>\s*(?=<div class="result-card">|<!-- Footer Section -->|$)'
workflow_converted = re.sub(pattern, convert_cell, workflow_section, flags=re.DOTALL)

# Reconstruct the file
new_content = before_workflow + workflow_converted + after_workflow

# Write back
with open('projects/diabetes/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"✅ Converted {convert_cell.counter - 1} cells")
print("✅ Diabetes page now uses clean jp-Cell structure like Cyclistic page")
