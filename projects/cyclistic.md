---
layout: default
title: "Cyclistic Bike-Share Analysis | Alistair Leys"
---

# Cyclistic Bike-Share Analysis 🚴‍♀️

## 🎯 Project Overview

This project presents a **comprehensive data analysis case study** using real Chicago bike-share data to understand customer behavior and drive business strategy. Following the **Google Data Analytics Certificate methodology**, this analysis examines 5.7 million authentic trips from Chicago's Divvy system to identify key differences between casual riders and annual members, ultimately informing targeted marketing strategies for membership conversion.

## 🧠 Key Skills Demonstrated

- **End-to-End Data Analysis**: Complete Ask → Prepare → Process → Analyze → Share → Act methodology
- **Real Data Processing**: Downloaded and processed 5.7M trips from Chicago's Divvy API
- **Statistical Analysis**: Descriptive statistics, trend analysis, customer segmentation
- **Data Visualisation**: Professional charts and executive-level presentations
- **Business Intelligence**: Strategic recommendations based on data-driven insights
- **Python Analytics**: Pandas, Matplotlib, Seaborn for large-scale data processing
- **Data Cleaning**: Robust data quality assurance and transformation pipelines

## 📈 Business Problem

**Cyclistic**, a fictional Chicago bike-share company, seeks to maximize annual memberships by understanding how casual riders and annual members use bikes differently. The company believes converting casual riders represents the greatest opportunity for future growth, as these users are already familiar with the service.

**Key Business Questions:**
- How do annual members and casual riders use Cyclistic bikes differently?
- What usage patterns suggest conversion opportunities?
- How can temporal trends inform targeted marketing campaigns?

## 📊 Dataset Information

**Data Source:** Real Chicago Divvy bike-share system (2023)  
**Total Records:** 5,719,877 authentic trips  
**Analysis Sample:** 499,176 trips (balanced stratified sample)  
**Data Provider:** Motivate International Inc.  
**Coverage:** Complete calendar year with geographic and temporal patterns

**Key Variables:**
- **Trip Details**: Duration, start/end times, station locations
- **User Classification**: Member vs Casual rider designation  
- **Temporal Patterns**: Hourly, daily, weekly, and seasonal usage
- **Geographic Data**: Station-based trip origins and destinations

## 🛠️ Methodology

### 1. Ask - Business Problem Definition
- Stakeholder identification (Marketing Director Lily Moreno, Executive Team)
- Clear business objectives for membership conversion strategy
- Key analytical questions formulated for actionable insights

### 2. Prepare - Real Data Acquisition
- Downloaded 12 months of authentic Chicago Divvy data (5.7M trips)
- Data credibility assessment using ROCCC principles
- Licensing and privacy considerations addressed
- Stratified sampling for computational efficiency while maintaining statistical validity

### 3. Process - Data Cleaning & Transformation
- Invalid trip removal (negative durations, outliers)
- Feature engineering: `ride_length`, `day_of_week`, temporal variables
- Data quality verification and integrity checks
- Standardised format preparation for analysis

### 4. Analyze - Statistical Investigation
- **Descriptive Statistics**: Trip duration, frequency patterns by user type
- **Temporal Analysis**: Hourly, daily, weekly, and seasonal trends
- **Comparative Analysis**: Member vs casual rider behavioral differences
- **Pattern Recognition**: Peak usage identification and trend analysis

### 5. Share - Executive Visualizations
- Professional chart creation for stakeholder presentation
- Clear narrative development linking data to business insights
- Executive-level summary with actionable intelligence

### 6. Act - Strategic Recommendations
- Data-driven marketing strategy development
- Targeted conversion campaign recommendations
- Business impact quantification and next steps

## 🔍 Key Findings

### **Trip Duration Patterns**
- **Casual riders take 1.7x longer trips** (20.7 vs 12.1 minutes average)
- Indicates leisure-focused usage vs utility-focused member behavior
- Suggests different value propositions for conversion strategies

### **Temporal Usage Differences**
- **Weekend Concentration**: 36.3% of casual trips occur on weekends vs 24.2% for members
- **Peak Hour Alignment**: Both groups peak at 5-6 PM, but with different contexts
- **Seasonal Sensitivity**: Strong patterns indicating conversion opportunity windows

### **Service Engagement**
- **Equal Representation**: 50/50 split demonstrates strong casual engagement
- **High Conversion Potential**: Active casual users already familiar with service value

## 📈 Data Visualizations

### Trip Duration Analysis
![Average Trip Duration by User Type](/assets/img/cyclistic/avg_duration_by_user_type.png)

**Business Insight:** The significant duration difference (1.7x) reveals distinct usage patterns - casual riders engage in longer, leisure-focused trips while members prefer shorter, utility-based journeys.

### Weekly Usage Patterns  
![Weekly Usage Patterns](/assets/img/cyclistic/weekly_usage_patterns.png)

**Business Insight:** Weekend concentration among casual riders (36.3% vs 24.2%) presents a clear opportunity for weekend-focused conversion campaigns.

### Seasonal Trends
![Seasonal Trends](/assets/img/cyclistic/seasonal_trends.png)

**Business Insight:** Seasonal variation provides predictable high-engagement periods for targeted marketing campaigns, particularly during summer months.

### Hourly Patterns
![Hourly Usage Patterns](/assets/img/cyclistic/hourly_patterns.png)

**Business Insight:** While both groups peak during rush hours, the context differs - members show commuting patterns while casual riders demonstrate leisure usage timing.

## 💡 Strategic Recommendations

### 1. **Weekend Warrior Campaigns** 🌟
**Target:** 36% of casual riders who prefer weekend leisure rides  
**Strategy:** Deploy weekend-specific membership promotions highlighting leisure benefits  
**Expected Impact:** Convert high-engagement weekend users to annual memberships

### 2. **Commuter Conversion Incentives** 🚀  
**Target:** Rush-hour casual users showing commuting behavior  
**Strategy:** Emphasize cost savings and guaranteed bike availability during peak hours  
**Expected Impact:** Capture utility-focused casual riders transitioning to regular commuting

### 3. **Seasonal Engagement Campaigns** 📅
**Target:** High summer usage periods and weather-dependent riders  
**Strategy:** Leverage peak engagement seasons for membership promotions  
**Expected Impact:** Convert seasonally-active users during their highest engagement periods

## 🎯 Business Impact

**Quantified Insights:**
- **1.7x trip duration difference** provides clear segmentation for targeted messaging
- **12 percentage point weekend difference** enables precise campaign timing
- **Equal service engagement** (50/50 split) validates conversion potential

**Strategic Value:**
- Evidence-based marketing strategy development
- Clear customer personas for targeted campaigns  
- Seasonal and temporal optimization opportunities
- ROI-focused conversion recommendations

## 🔧 Technical Implementation

**Programming Languages:** Python  
**Key Libraries:** Pandas, Matplotlib, Seaborn, NumPy  
**Data Processing:** 5.7M record ETL pipeline  
**Analysis Framework:** Google Data Analytics Certificate methodology  
**Visualization:** Executive-quality charts with business narrative  
**Documentation:** Complete methodology with reproducible analysis

## 📁 Project Resources

- **[Complete Case Study Report](/projects/cyclistic/analysis)** - Full analytical methodology and findings
- **[Executive Summary](/projects/cyclistic/summary)** - Key insights for stakeholders  
- **[Data Pipeline Documentation](/projects/cyclistic/methodology)** - Technical implementation details
- **[GitHub Repository](https://github.com/AlistairLeys/cyclistic-analysis)** - Complete source code and datasets

## 🏆 Portfolio Highlights

This project demonstrates **professional-level data analysis capabilities** suitable for:
- **Marketing Analytics** roles requiring customer segmentation and conversion strategy
- **Business Intelligence** positions focused on data-driven decision making  
- **Transportation Analytics** roles in mobility and urban planning sectors
- **Consulting** positions requiring client-facing analytical presentations

**Key Differentiators:**
- ✅ Real data from major metropolitan bike-share system (5.7M records)
- ✅ Industry-standard methodology (Google Data Analytics Certificate framework)
- ✅ Executive-ready deliverables with business context
- ✅ End-to-end analysis pipeline from raw data to strategic recommendations
- ✅ Quantified business impact with actionable insights

---

## 📋 View Complete Analysis

Ready to dive deeper into the methodology, statistical findings, and strategic recommendations?

### **[📊 View Complete Business Case & Analysis →](/projects/cyclistic/analysis)**

**What you'll find:**
- **Executive Summary** with quantified business impact
- **Complete Methodology** following Google Data Analytics Certificate framework  
- **Statistical Analysis** with significance testing and validation
- **Professional Visualizations** with business narrative
- **Strategic Recommendations** with ROI projections and implementation timeline
- **Technical Documentation** for reproducible analysis

### **[⚡ Quick Executive Summary →](/projects/cyclistic/summary)**
*Perfect for stakeholders - key insights and recommendations in 5 minutes*

### **[🔧 Technical Implementation →](/projects/cyclistic/methodology)**  
*Detailed code documentation and analytical framework for technical review*

---

*This analysis showcases the application of data science techniques to real-world business challenges, demonstrating both technical proficiency and strategic thinking capabilities essential for senior analytical roles.*
