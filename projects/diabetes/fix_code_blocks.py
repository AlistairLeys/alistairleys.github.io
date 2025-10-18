import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace opening code block tags
content = content.replace('<div class="code-block">', '<pre class="code-block"><code class="language-python">')

# Replace closing tags - need to find </div> that closes code-block
# Pattern: code content followed by </div> (closing code-block) then another </div> (closing result-card wrapper)
content = re.sub(
    r'(</code></pre>|</div>)\s*</div>\s*(<div class="output">)',
    r'</code></pre>\n                        </div>\n                        \n                        <div class="output">',
    content
)

# Fix any remaining standalone </div> after code blocks that should be </code></pre>
lines = content.split('\n')
new_lines = []
in_code_block = False

for i, line in enumerate(lines):
    if '<pre class="code-block"><code class="language-python">' in line:
        in_code_block = True
        new_lines.append(line)
    elif in_code_block and '                        </div>' in line and 'output' not in lines[i+1] if i+1 < len(lines) else True:
        # This is the closing tag for code-block
        new_lines.append(line.replace('</div>', '</code></pre>'))
        in_code_block = False
    else:
        new_lines.append(line)

content = '\n'.join(new_lines)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Converted all code blocks to use Prism.js syntax highlighting")
