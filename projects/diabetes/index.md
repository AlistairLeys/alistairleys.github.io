---
layout: default
title: "Diabetes Disease Progression Analysis | Alistair Leys"
---

[← Back to Projects](/projects/)

# Diabetes Disease Progression Analysis 📊

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
- Data quality assessment and missing value analysis
- Statistical summaries and distribution analysis
- Correlation analysis and feature relationships

### 2. Feature Engineering
- Risk level categorisation (Low/Medium/High)
- Feature scaling and normalisation
- Correlation-based feature selection

### 3. Predictive Modelling
- **Linear Regression**: Baseline model with interpretable coefficients
- **Random Forest**: Ensemble method for feature importance
- **Model Validation**: Cross-validation and performance metrics
- **Hyperparameter Tuning**: Grid search optimisation

### 4. Unsupervised Learning
- **K-Means Clustering**: Patient segmentation
- **Cluster Analysis**: Risk profile identification
- **Cluster Validation**: Silhouette analysis and interpretation

## 📊 Key Results

### Model Performance
| Model | RMSE | R² Score | Best Features |
|-------|------|----------|---------------|
| Linear Regression | ~53.8 | ~0.52 | BMI, S5, BP |
| Random Forest | ~51.2 | ~0.56 | S5, BMI, S1 |

### Key Insights
1. **S5 (lamotrigine levels)** is the strongest predictor of disease progression
2. **BMI** shows strong correlation with progression in all age groups
3. **Blood pressure** contributes significantly to risk assessment
4. **Three distinct patient clusters** identified with different risk profiles

### Clinical Implications
- **High-risk patients** (cluster 2): Elevated BMI + high S5 levels
- **Moderate-risk patients** (cluster 1): Average biomarkers with specific patterns
- **Low-risk patients** (cluster 0): Generally healthy baseline measurements

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

### Running the Analysis
1. Open [diabetes_analysis.ipynb](https://github.com/AlistairLeys/Portfolio/blob/main/diabetes-disease-progression/diabetes_analysis.ipynb)
2. Run all cells sequentially
3. Generated outputs will be saved to `data/` and `figures/` directories

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
