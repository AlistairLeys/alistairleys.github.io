"""
Add syntax highlighting to diabetes page code blocks using simple regex
"""
import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all code blocks
code_block_pattern = re.compile(
    r'<pre class="code-block"><code class="language-python">\s*(.*?)\s*</code></pre>',
    re.DOTALL
)

def add_highlighting(code):
    """Add syntax highlighting spans to Python code"""
    
    # Highlight comments first (before other replacements)
    code = re.sub(r'(#[^\n]*)', r'<span class="comment">\1</span>', code)
    
    # Highlight strings (single and double quotes)
    code = re.sub(r"'([^']*)'", r"<span class=\"string\">'\\1'</span>", code)
    code = re.sub(r'"([^"]*)"', r'<span class="string">"\\1"</span>', code)
    
    # Highlight keywords (word boundaries to avoid partial matches)
    keywords = ['import', 'from', 'as', 'def', 'class', 'if', 'else', 'elif', 
                'for', 'while', 'print', 'return', 'in', 'not', 'and', 'or',
                'True', 'False', 'None', 'with', 'try', 'except', 'finally',
                'raise', 'assert', 'break', 'continue', 'pass', 'yield']
    
    for keyword in keywords:
        code = re.sub(rf'\b({keyword})\b', r'<span class="keyword">\1</span>', code)
    
    # Highlight numbers
    code = re.sub(r'\b(\d+\.?\d*)\b', r'<span class="number">\1</span>', code)
    
    return code

def replace_code_block(match):
    code = match.group(1)
    highlighted_code = add_highlighting(code)
    return f'<pre class="code-block"><code class="language-python">\n{highlighted_code}\n</code></pre>'

# Apply highlighting
content = code_block_pattern.sub(replace_code_block, content)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Added syntax highlighting to all code blocks")
