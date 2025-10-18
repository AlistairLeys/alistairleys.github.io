"""
Use Pygments to properly highlight Python code in diabetes page
"""
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token
import re

# Read file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def highlight_python_code(code):
    """Use Pygments to add syntax highlighting spans"""
    lexer = PythonLexer()
    tokens = list(lex(code, lexer))
    
    result = []
    for ttype, value in tokens:
        # Map token types to our CSS classes
        if ttype in Token.Keyword:
            result.append(f'<span class="keyword">{value}</span>')
        elif ttype in Token.String:
            result.append(f'<span class="string">{value}</span>')
        elif ttype in Token.Comment:
            result.append(f'<span class="comment">{value}</span>')
        elif ttype in Token.Number or ttype in Token.Literal.Number:
            result.append(f'<span class="number">{value}</span>')
        elif ttype in Token.Name.Function or ttype in Token.Name.Builtin:
            result.append(f'<span class="function">{value}</span>')
        else:
            result.append(value)
    
    return ''.join(result)

# Find all code blocks
pattern = re.compile(
    r'<pre class="code-block"><code class="language-python">\s*(.*?)\s*</code></pre>',
    re.DOTALL
)

def process_code_block(match):
    code = match.group(1)
    highlighted = highlight_python_code(code)
    return f'<pre class="code-block"><code class="language-python">\n{highlighted}\n</code></pre>'

# Apply to all code blocks
new_content = pattern.sub(process_code_block, content)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Successfully added Python syntax highlighting to all code blocks!")
print("Keywords = keyword class")
print("Strings = string class")
print("Comments = comment class")
print("Numbers = number class")
print("Functions = function class")
