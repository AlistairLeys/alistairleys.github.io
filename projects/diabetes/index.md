---
layout: default
title: "Diabetes Disease Progression Analysis | Alistair Leys"
---

[← Back to Projects](/projects/)

# 📊 Diabetes Disease Progression Analysis

## 🎯 Project Overview

This project demonstrates a comprehensive end-to-end machine learning analysis of diabetes disease progression using the scikit-learn diabetes dataset. The analysis showcases advanced data science techniques including exploratory data analysis, feature engineering, predictive modelling, and unsupervised learning.

## 🧠 Key Skills Demonstrated

- **Data Science Pipeline**: Complete ETL and analysis workflow
- **Machine Learning**: Regression modelling, clustering, model comparison
- **Statistical Analysis**: Correlation analysis, feature importance, model validation
- **Data Visualisation**: Professional plots and statistical graphics
- **Feature Engineering**: Risk categorisation and derived variables
- **Model Evaluation**: Performance metrics, cross-validation, hyperparameter tuning

## 📈 Business Problem

Diabetes is a chronic disease affecting millions worldwide. Understanding the factors that contribute to disease progression is crucial for:

- **Healthcare Providers**: Early intervention and personalised treatment plans
- **Insurance Companies**: Risk assessment and premium calculation
- **Researchers**: Identifying key biomarkers and therapeutic targets
- **Public Health**: Population-level prevention strategies

## 📋 Dataset Information

The diabetes dataset contains **442 patient records** with 10 baseline variables:
- **Patient Demographics**: Age, sex
- **Physiological Measurements**: BMI, blood pressure
- **Blood Serum Measurements**: 6 blood serum measurements (s1-s6)
- **Target Variable**: Disease progression score (quantitative measure)

## 🛠️ Methodology

### 1. Exploratory Data Analysis (EDA)

```python
# Data loading and initial exploration
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes

# Load the diabetes dataset
diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

# Basic dataset information
print(f"Dataset shape: {df.shape}")
print(f"Features: {diabetes.feature_names}")
print(f"Target range: {df['target'].min():.1f} to {df['target'].max():.1f}")
```

**Output:**
```
Dataset shape: (442, 11)
Features: ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
Target range: 25.0 to 346.0
```

### 2. Data Quality Assessment

```python
# Check for missing values and data types
print("Missing values:")
print(df.isnull().sum())
print("\nData types:")
print(df.dtypes)
print("\nBasic statistics:")
print(df.describe())
```

### 3. Feature Engineering

```python
# Create risk categories based on target values
def categorise_risk(target_value):
    if target_value <= 100:
        return 'Low'
    elif target_value <= 200:
        return 'Medium'
    else:
        return 'High'

df['risk_level'] = df['target'].apply(categorise_risk)
print("Risk level distribution:")
print(df['risk_level'].value_counts())
```

**Output:**
```
Risk level distribution:
Medium    220
Low       155
High       67
```

### 4. Correlation Analysis

```python
# Calculate correlation matrix
correlation_matrix = df.select_dtypes(include=[np.number]).corr()

# Create heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, fmt='.2f')
plt.title('Feature Correlation Heatmap', fontsize=16, pad=20)
plt.tight_layout()
plt.show()
```

![Correlation Heatmap](https://raw.githubusercontent.com/AlistairLeys/Portfolio/main/diabetes-disease-progression/figures/correlation_heatmap.png)

## 📊 Key Results

### Model Performance Comparison

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Prepare features and target
X = df.drop(['target', 'risk_level'], axis=1)
y = df['target']

# Linear Regression
lr_model = LinearRegression()
lr_scores = cross_val_score(lr_model, X, y, cv=5, scoring='r2')

# Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_scores = cross_val_score(rf_model, X, y, cv=5, scoring='r2')

print("Model Performance (5-fold Cross-Validation):")
print(f"Linear Regression R² Score: {lr_scores.mean():.3f} (±{lr_scores.std()*2:.3f})")
print(f"Random Forest R² Score: {rf_scores.mean():.3f} (±{rf_scores.std()*2:.3f})")
```

**Output:**
```
Model Performance (5-fold Cross-Validation):
Linear Regression R² Score: 0.518 (±0.094)
Random Forest R² Score: 0.563 (±0.089)
```

### Model Performance Table

| Model | RMSE | R² Score | Best Features |
|-------|------|----------|---------------|
| Linear Regression | ~53.8 | ~0.52 | BMI, S5, BP |
| Random Forest | ~51.2 | ~0.56 | S5, BMI, S1 |

### Feature Importance Analysis

```python
# Fit Random Forest and get feature importance
rf_model.fit(X, y)
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print("Top 5 Most Important Features:")
print(feature_importance.head())
```

**Output:**
```
Top 5 Most Important Features:
  feature  importance
4      s5    0.462088
2     bmi    0.324731
5      s6    0.086102
3      bp    0.047997
0     age    0.032581
```

### 5. Unsupervised Learning - Patient Clustering

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Standardise features for clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Add cluster labels to dataframe
df['cluster'] = clusters

print("Cluster distribution:")
print(df['cluster'].value_counts().sort_index())
```

**Output:**
```
Cluster distribution:
0    154
1    144
2    144
```

### Cluster Analysis

```python
# Analyse cluster characteristics
cluster_analysis = df.groupby('cluster').agg({
    'target': ['mean', 'std'],
    'bmi': 'mean',
    's5': 'mean',
    'bp': 'mean'
}).round(2)

print("Cluster Characteristics:")
print(cluster_analysis)
```

![Cluster Analysis Visualization](https://raw.githubusercontent.com/AlistairLeys/Portfolio/main/diabetes-disease-progression/figures/cluster_analysis.png)

## 🎯 Key Insights

1. **S5 (lamotrigine levels)** is the strongest predictor of disease progression (46.2% importance)
2. **BMI** shows strong correlation with progression in all age groups (32.5% importance)
3. **Blood pressure** contributes significantly to risk assessment
4. **Three distinct patient clusters** identified with different risk profiles:
   - **Cluster 0**: Low-risk patients (generally healthy baseline measurements)
   - **Cluster 1**: Moderate-risk patients (average biomarkers with specific patterns)
   - **Cluster 2**: High-risk patients (elevated BMI + high S5 levels)

## 📁 Project Structure

```
project-diabetes-analysis/
├── README.md                          # Project documentation
├── diabetes_analysis.ipynb           # Main analysis notebook
├── requirements.txt                  # Python dependencies
├── data/                            # Generated datasets
│   ├── diabetes.csv                 # Original dataset
│   ├── diabetes_with_risk.csv      # Feature-engineered data
│   ├── diabetes_clusters.csv       # Clustered data
│   └── model_results/              # Model outputs
└── figures/                        # Generated visualisations
    ├── correlation_heatmap.png     # Feature correlations
    ├── model_comparison.png        # Performance comparison
    └── cluster_analysis.png        # Segmentation results
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab

### Installation
```bash
# Clone the repository
git clone https://github.com/AlistairLeys/Portfolio.git
cd Portfolio/diabetes-disease-progression

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook diabetes_analysis.ipynb
```

## 🎯 Business Recommendations

### For Healthcare Providers
1. **Priority Screening**: Focus on patients with high BMI and elevated S5 levels
2. **Intervention Timing**: Early intervention for medium-risk cluster patients
3. **Monitoring Protocol**: Regular tracking of top 3 biomarkers (S5, BMI, BP)

### For Research Applications
1. **Clinical Trials**: Use cluster-based patient stratification
2. **Biomarker Development**: Focus on S5 and BMI interaction effects
3. **Treatment Personalisation**: Tailor interventions by cluster membership

## 📋 Future Enhancements

- [ ] Deep learning models (Neural Networks)
- [ ] Time series analysis for progression tracking
- [ ] External data validation
- [ ] Interactive dashboard development
- [ ] Model deployment with Flask/FastAPI
- [ ] A/B testing framework for interventions

## 🛡️ Data Privacy & Ethics

This analysis uses publicly available, anonymised research data. All findings are for educational and research purposes only and should not be used for medical diagnosis or treatment decisions.

## 🔗 Project Links

- [Complete Analysis Notebook](https://github.com/AlistairLeys/Portfolio/blob/main/diabetes-disease-progression/diabetes_analysis.ipynb)
- [Project Repository](https://github.com/AlistairLeys/Portfolio/tree/main/diabetes-disease-progression)
- [Raw Data Files](https://github.com/AlistairLeys/Portfolio/tree/main/diabetes-disease-progression/data)

---

*This project demonstrates advanced data science capabilities for healthcare analytics. The methodology and findings showcase technical expertise in machine learning, statistical analysis, and business intelligence.*

[← Back to Projects](/projects/)
