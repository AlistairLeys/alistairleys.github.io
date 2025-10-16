---
layout: default
title: "Alistair Leys | Data Analysis Portfolio"
---

# Alistair Leys

<p class="tagline">Data Scientist focused on clear, actionable insight</p>

I build end-to-end data products that turn complex information into practical business decisions. My approach combines statistical rigour with pragmatic problem-solving, ensuring analyses are both technically sound and genuinely useful.

I care deeply about reproducibility and clear communication. Whether developing predictive models or exploring new datasets, I prioritise methods that stakeholders can understand and trust. Based in Birmingham, UK, I'm open to data and AI roles where analytical thinking drives real impact.

## Diabetes Disease Progression Analysis 📊

### 🎯 Project Overview

This project demonstrates a comprehensive end-to-end machine learning analysis of diabetes disease progression using the scikit-learn diabetes dataset. The analysis showcases advanced data science techniques including exploratory data analysis, feature engineering, predictive modelling, and unsupervised learning.

### 🧠 Key Skills Demonstrated

- **Data Science Pipeline**: Complete ETL and analysis workflow
- **Machine Learning**: Regression modelling, clustering, model comparison
- **Statistical Analysis**: Correlation analysis, feature importance, model validation
- **Data Visualisation**: Professional plots and statistical graphics
- **Feature Engineering**: Risk categorisation and derived variables
- **Model Evaluation**: Performance metrics, cross-validation, hyperparameter tuning

### 📈 Business Problem

Diabetes is a chronic disease affecting millions worldwide. Understanding the factors that contribute to disease progression is crucial for:

- **Healthcare Providers**: Early intervention and personalised treatment plans
- **Insurance Companies**: Risk assessment and premium calculation
- **Researchers**: Identifying key biomarkers and therapeutic targets
- **Public Health**: Population-level prevention strategies

### 📊 Key Results

**Model Performance**
| Model | RMSE | R² Score | Best Features |
|-------|------|----------|---------------|
| Linear Regression | ~53.8 | ~0.52 | BMI, S5, BP |
| Random Forest | ~51.2 | ~0.56 | S5, BMI, S1 |

**Key Insights**
1. **S5 (lamotrigine levels)** is the strongest predictor of disease progression
2. **BMI** shows strong correlation with progression in all age groups
3. **Blood pressure** contributes significantly to risk assessment
4. **Three distinct patient clusters** identified with different risk profiles

### 🚀 View the Analysis

- [Complete Analysis Notebook](https://github.com/AlistairLeys/Portfolio/blob/main/diabetes-disease-progression/diabetes_analysis.ipynb)
- [Project Repository](https://github.com/AlistairLeys/Portfolio/tree/main/diabetes-disease-progression)

### 🎯 Business Impact

**For Healthcare Providers**
1. **Priority Screening**: Focus on patients with high BMI and elevated S5 levels
2. **Intervention Timing**: Early intervention for medium-risk cluster patients
3. **Monitoring Protocol**: Regular tracking of top 3 biomarkers (S5, BMI, BP)

**For Research Applications**
1. **Clinical Trials**: Use cluster-based patient stratification
2. **Biomarker Development**: Focus on S5 and BMI interaction effects
3. **Treatment Personalisation**: Tailor interventions by cluster membership

---

*This project demonstrates advanced data science capabilities for healthcare analytics. The methodology and findings showcase technical expertise in machine learning, statistical analysis, and business intelligence.*
