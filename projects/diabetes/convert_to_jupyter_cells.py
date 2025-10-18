import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the first code block to convert as example
# Replace: <pre class="code-block"><code class="language-python">
# With proper Jupyter cell structure

first_code_block = '''                    <div class="result-card">
                        <h3>1. Data Import & Initial Exploration</h3>
                        <pre class="code-block"><code class="language-python">
# Import essential libraries for comprehensive analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.inspection import permutation_importance
import warnings
warnings.filterwarnings('ignore')

# Load the diabetes dataset
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

print("Dataset Overview:")
print(f"Shape: {X.shape}")
print(f"Features: {diabetes.feature_names}")
print(f"Target range: {y.min():.1f} to {y.max():.1f}")
print(f"Missing values: {np.isnan(X).sum()}")
                        </code></pre>
                        
                        <div class="output">
Dataset Overview:
Shape: (442, 10)
Features: ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
Target range: 25.0 to 346.0
Missing values: 0
                        </div>
                    </div>'''

# New Jupyter cell structure with manual syntax highlighting
new_jupyter_cell = '''                    <!-- Markdown Cell: Section Header -->
                    <div class="jp-Cell jp-MarkdownCell">
                        <div class="jp-Editor">
                            <h2>1. Data Import & Initial Exploration</h2>
                            <p>Load the diabetes dataset and perform initial data quality checks.</p>
                        </div>
                    </div>

                    <!-- Code Cell: Data Import -->
                    <div class="jp-Cell jp-CodeCell">
                        <div class="jp-InputArea">
                            <div class="jp-InputPrompt">In [1]:</div>
                            <div class="jp-CodeMirrorEditor">
                                <div class="jp-Editor">
                                    <pre><code><span class="comment"># Import essential libraries for comprehensive analysis</span>
<span class="keyword">import</span> pandas <span class="keyword">as</span> pd
<span class="keyword">import</span> numpy <span class="keyword">as</span> np
<span class="keyword">import</span> matplotlib.pyplot <span class="keyword">as</span> plt
<span class="keyword">import</span> seaborn <span class="keyword">as</span> sns
<span class="keyword">from</span> sklearn.datasets <span class="keyword">import</span> load_diabetes
<span class="keyword">from</span> sklearn.model_selection <span class="keyword">import</span> train_test_split, cross_val_score
<span class="keyword">from</span> sklearn.ensemble <span class="keyword">import</span> RandomForestRegressor
<span class="keyword">from</span> sklearn.linear_model <span class="keyword">import</span> LinearRegression, Ridge
<span class="keyword">from</span> sklearn.cluster <span class="keyword">import</span> KMeans
<span class="keyword">from</span> sklearn.metrics <span class="keyword">import</span> mean_squared_error, r2_score
<span class="keyword">from</span> sklearn.inspection <span class="keyword">import</span> permutation_importance
<span class="keyword">import</span> warnings
warnings.filterwarnings(<span class="string">'ignore'</span>)

<span class="comment"># Load the diabetes dataset</span>
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

<span class="keyword">print</span>(<span class="string">"Dataset Overview:"</span>)
<span class="keyword">print</span>(<span class="string">f"Shape: <span class="number">{X.shape}</span>"</span>)
<span class="keyword">print</span>(<span class="string">f"Features: <span class="number">{diabetes.feature_names}</span>"</span>)
<span class="keyword">print</span>(<span class="string">f"Target range: <span class="number">{y.min():.1f}</span> to <span class="number">{y.max():.1f}</span>"</span>)
<span class="keyword">print</span>(<span class="string">f"Missing values: <span class="number">{np.isnan(X).sum()}</span>"</span>)</code></pre>
                                </div>
                            </div>
                        </div>
                        <div class="jp-OutputArea">
                            <div class="jp-OutputPrompt">Out[1]:</div>
                            <div class="jp-OutputArea-output">
                                <pre>Dataset Overview:
Shape: (442, 10)
Features: ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
Target range: 25.0 to 346.0
Missing values: 0</pre>
                            </div>
                        </div>
                    </div>'''

# Replace in content
if first_code_block in content:
    content = content.replace(first_code_block, new_jupyter_cell)
    print("✓ Converted first code block to Jupyter cell structure with syntax highlighting")
else:
    print("✗ Could not find first code block to replace")
    # Let's try to find what's actually there
    print("\nSearching for code-block pattern...")
    pattern = re.search(r'<pre class="code-block"><code class="language-python">', content)
    if pattern:
        print(f"Found at position: {pattern.start()}")
    else:
        print("Pattern not found")

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ File updated")
