This analysis explores diabetes disease progression using machine learning to identify key risk factors and develop predictive models. Working with a dataset of 442 patients, I built models to predict disease progression and segmented patients into risk groups.

## Dataset Overview

The diabetes dataset contains 442 patients with 10 baseline measurements (age, sex, BMI, blood pressure, and six serum measurements) and a target variable representing disease progression one year later.

```python
# Load and examine the data
diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

print(f"Dataset shape: {df.shape}")
print(f"Target range: {df['target'].min():.0f} - {df['target'].max():.0f}")
print(f"Mean progression: {df['target'].mean():.1f}")
```

**Output:**
```
Dataset shape: (442, 11)
Target range: 25 - 346
Mean progression: 152.1
```

## Risk Categorisation

I created risk categories based on disease progression scores to enable practical clinical interpretation:

```python
def categorize_risk(target_value):
    if target_value <= 100:
        return 'Low'
    elif target_value <= 200:
        return 'Medium'
    else:
        return 'High'

df['risk_level'] = df['target'].apply(categorize_risk)
```

**Risk Distribution:**
- **Medium Risk:** 49.8% (220 patients)
- **Low Risk:** 35.1% (155 patients)  
- **High Risk:** 15.2% (67 patients)

![Risk Level Distribution - Bar chart showing distribution of patients across low, medium, and high risk categories](assets/img/diabetes-notebook/risk_level_distribution.png)

## Correlation Analysis

Feature correlation analysis revealed the relationships between clinical measurements and disease progression:

![Correlation Heatmap - Matrix showing correlations between clinical features and disease progression](assets/img/diabetes-notebook/correlation_heatmap.png)

### Strongest Predictors

The analysis identified key factors for disease progression:

1. **BMI:** 0.586 correlation with progression
2. **S5 (serum measurement):** 0.566 correlation
3. **Blood Pressure:** 0.441 correlation

Key visualisations of the strongest predictors:

![BMI vs Disease Progression - Scatter plot showing positive correlation between BMI and target values](assets/img/diabetes-notebook/scatter_bmi_target.png)

![S5 vs Disease Progression - Scatter plot showing strong positive correlation between S5 serum measurement and target values](assets/img/diabetes-notebook/scatter_s5_target.png)

## Predictive Modelling

I compared Linear Regression and Random Forest models using 5-fold cross-validation:

```python
# Model comparison results
Linear Regression: R² = 0.518 (±0.094)
Random Forest: R² = 0.563 (±0.089)
```

**Random Forest achieved 8.7% better performance** than Linear Regression, with more stable predictions across different data splits.

### Model Performance Visualisation

![Linear Regression Actual vs Predicted - Scatter plot comparing actual disease progression values with linear regression predictions](assets/img/diabetes-notebook/linear_reg_actual_vs_pred.png)

![Random Forest Actual vs Predicted - Scatter plot comparing actual disease progression values with random forest predictions, showing better fit](assets/img/diabetes-notebook/random_forest_actual_vs_pred.png)

### Feature Importance Analysis

Random Forest feature importance revealed:

1. **S5:** 46.2% importance
2. **BMI:** 32.5% importance  
3. **S6:** 8.6% importance

The top three features account for **87.3% of total importance**, suggesting these should be prioritised in clinical monitoring.

## Patient Segmentation

K-means clustering identified three distinct patient groups based on clinical features:

- **Cluster 0:** 154 patients (34.8%) - Lower progression risk
- **Cluster 1:** 144 patients (32.6%) - Higher progression risk  
- **Cluster 2:** 144 patients (32.6%) - Moderate progression risk

![Patient Clusters vs Risk Level - Stacked bar chart showing distribution of risk levels within each patient cluster](assets/img/diabetes-notebook/clusters_vs_risk_level.png)

**Cluster 1** showed the highest average disease progression (168.5 vs 144.2 and 142.8 for other clusters), with 22.2% of patients in the high-risk category.

## Clinical Implications

### Risk Monitoring
- **S5 levels** should be monitored most closely as the strongest single predictor
- **BMI management** is crucial, showing both high correlation and feature importance
- **Blood pressure control** remains important for progression management

### Treatment Personalisation
The clustering analysis suggests patients can be segmented into groups with different risk profiles, enabling more targeted treatment approaches.

### Model Validation
Cross-validation results demonstrate the models are robust and generalisable, with Random Forest providing the most reliable predictions for clinical decision support.

## Technical Implementation

This analysis used Python with scikit-learn, pandas, and numpy. All models achieved statistically significant performance and were validated using proper train/test splits and cross-validation to ensure clinical applicability.

**Key Libraries:**
- **scikit-learn:** Machine learning algorithms and evaluation
- **pandas:** Data manipulation and analysis  
- **numpy:** Numerical computations
- **matplotlib/seaborn:** Data visualisation

The complete analysis demonstrates end-to-end machine learning workflow from data exploration through model deployment considerations.
