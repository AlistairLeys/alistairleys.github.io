"""
FINAL SIMPLE APPROACH: Manually copy the EXACT structure from Cyclistic for the first code block
Then you can see it working with colored syntax!
"""
import re

# Read current file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The EXACT replacement - find the FIRST code block and replace it with proper Jupyter cell structure
# This will serve as a working example you can see

old_first_block = '''                    <div class="result-card">
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

# Working Jupyter cell with syntax highlighting (EXACT copy from Cyclistic structure)
new_jupyter_cell = '''                    <!-- Code Cell: Data Import -->
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
<span class="keyword">print</span>(<span class="string">f"Shape: {X.shape}"</span>)
<span class="keyword">print</span>(<span class="string">f"Features: {diabetes.feature_names}"</span>)
<span class="keyword">print</span>(<span class="string">f"Target range: {y.min():.1f} to {y.max():.1f}"</span>)
<span class="keyword">print</span>(<span class="string">f"Missing values: {np.isnan(X).sum()}"</span>)</code></pre>
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

# Do the replacement
if old_first_block in content:
    content = content.replace(old_first_block, new_jupyter_cell)
    print("✅ SUCCESS! Replaced first code block with colored Jupyter cell")
    print("The first code block will now show Python syntax highlighting!")
    print("Keywords (import, from, as, print) = BLUE")
    print("Strings ('ignore', \"Dataset Overview\") = ORANGE")
    print("Comments (# lines) = GREEN")
else:
    print("❌ Could not find exact match. Trying with flexible whitespace...")
    # Try without exact whitespace matching
    if '</code></pre>' in content and 'import pandas as pd' in content:
        print("Found the general structure, but whitespace doesn't match exactly.")
        print("The CSS is ready, but manual HTML editing needed.")

# Write it back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ File saved!")
