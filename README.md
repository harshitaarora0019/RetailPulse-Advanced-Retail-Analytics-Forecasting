# 📊 RetailPulse – AI Retail Analytics & Forecasting Platform

<p align="center">
An AI-powered retail analytics platform for customer segmentation, demand forecasting, churn analysis, and inventory optimization.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue">
<img src="https://img.shields.io/badge/Streamlit-Dashboard-red">
<img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange">
<img src="https://img.shields.io/badge/Prophet-Forecasting-green">
<img src="https://img.shields.io/badge/PowerBI-Business%20Intelligence-yellow">
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-purple">
</p>

---

## 🌐 Live Demo

**RetailPulse Dashboard**

https://retailpulse-advanced-retail-analytics-forecasting-c5kfyjefbhjn.streamlit.app/

---

## 🏠 Dashboard Preview

📈 Business Intelligence Dashboard
![Business Intelligence Dashboard](dashboards/📊RetailPulse_Business_Intelligence_Dashboard.png)

---

## 📌 Project Overview

RetailPulse is an end-to-end Retail Analytics and Forecasting Platform built using Python, Machine Learning, Forecasting, and Business Intelligence techniques.

The platform transforms retail transaction data into actionable business insights through:

* 📊 Sales Analytics
* 👥 Customer Segmentation
* 📈 Demand Forecasting
* ⚠️ Churn Analysis
* 📦 Inventory Optimization

Built on the UCI Online Retail Dataset containing more than **500,000 retail transactions**, RetailPulse demonstrates real-world Data Analytics and Data Science workflows.

---

## 🚀 Key Features

### 📊 Sales Analytics

* Revenue KPI Monitoring
* Daily Sales Trend Analysis
* Top Product Analysis
* Customer Purchase Behaviour Analysis
* Revenue Insights

### 👥 Customer Segmentation

* RFM Analysis
* K-Means Clustering
* VIP Customer Identification
* Loyal Customer Detection
* Lost Customer Detection
* Revenue Contribution Analysis

### 📈 Demand Forecasting

* Facebook Prophet Forecasting
* 30-Day Revenue Prediction
* Trend Analysis
* Seasonality Analysis
* Forecast Visualization

### ⚠️ Churn Analysis

* Customer Inactivity Detection
* At-Risk Customer Identification
* Churn Monitoring Dashboard

### 📦 Inventory Optimization

* Forecast-Based Inventory Planning
* Future Stock Recommendations
* Inventory Insight Generation

---

## 🛠️ Technology Stack

| Category              | Technology                             |
| --------------------- | -------------------------------------- |
| Programming Language  | Python                                 |
| Data Processing       | Pandas, NumPy                          |
| Machine Learning      | Scikit-Learn                           |
| Customer Segmentation | RFM Analysis, K-Means                  |
| Forecasting           | Facebook Prophet                       |
| Dashboard             | Streamlit                              |
| Visualization         | Matplotlib, Seaborn                    |
| Business Intelligence | Power BI                               |
| Development Tools     | Git, GitHub, Jupyter Notebook, PyCharm |

---

## 📂 Dataset

### UCI Online Retail Dataset

* 500K+ Retail Transactions
* UK-Based E-Commerce Store
* Customer Purchase History
* Product Sales Data
* Transaction Records

Dataset Source:

https://archive.ics.uci.edu/ml/datasets/online+retail

---

## 📊 Project Workflow

```text
Raw Retail Dataset
      |
      ▼
Data Cleaning & Preprocessing
      |
      ▼
Exploratory Data Analysis
      |
      ▼
RFM Analysis
      |
      ▼
Customer Segmentation
(K-Means Clustering)
      |
      ▼
Demand Forecasting
(Facebook Prophet)
      |
      ▼
Churn Analysis
      |
      ▼
Inventory Optimization
      |
      ▼
Interactive Streamlit Dashboard
      |
      ▼
Power BI Dashboard
(Business Intelligence Reporting)
```

---

## 📁 Project Structure

```text
RetailPulse/
│
├── app/
│   ├── main.py
│   └── utils/
│       └── preprocess.py
│
├── dashboards/
│   └── PowerBI dashboard.pbix
│
├── data/
│   ├── raw/
│   │   └── Online Retail.xlsx
│   │
│   └── processed/
│       └── cleaned_retail.csv
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── RetailPulse.ipynb
│   └── NeuralRetail.ipynb
│
├── report/
│   └── Streamlit Dashboard/
│
├── requirements.txt
│
└── README.md
```

---
 # 📊 Power BI Dashboard

### 📈 Business Intelligence Dashboard ]

![Business Intelligence Dashboard](dashboards/📊RetailPulse_Business_Intelligence_Dashboard.png)

**Insights:**
- Total Revenue Analysis
- Total Orders & Customers
- Revenue by Country
- Top Selling Products
- Sales by Hour
- Revenue Trend Analysis

---

### 👥 Customer Intelligence Dashboard

![Customer Intelligence Dashboard](dashboards/Customer%20Intelligence%20Dashboard.png)

**Insights:**
- Customer Segmentation using RFM Analysis
- VIP, Lost, Regular & Loyal Customers
- Revenue Contribution by Segment
- Recency vs Monetary Analysis
- Customer Distribution Analysis

---

### 📦 Forecast & Inventory Intelligence Dashboard

![Forecast Dashboard](dashboards/Forecast%20%26%20Inventory%20Intelligence%20Dashboard.png)

**Insights:**
- 30-Day Revenue Forecast
- Forecast Confidence Intervals
- Expected Daily Revenue
- Peak & Lowest Revenue Prediction
- Inventory Recommendation System

## 💡 Key Business Insights

* Identifies high-value customer segments using RFM analysis.
* Detects churn-risk customers based on inactivity patterns.
* Forecasts future revenue trends using Facebook Prophet.
* Supports inventory planning through predictive analytics.
* Enables data-driven decision making using interactive dashboards.

---

# 📸  Streamlit Dashboard 
### 🏠 Home
![Home](report/Streamlit%20Dashboard/RetailPulse%20—%20AI%20Retail%20Analytics.png)
 
### 📁 Upload Dataset
![Upload](report/Streamlit%20Dashboard/Upload%20Dataset%20Dashboard.png)
 
### 📊 Sales Analytics
![Sales](report/Streamlit%20Dashboard/Sales%20Analytics%20Dashboard.png)
 
### 👥 Customer Segmentation
![Segmentation](report/Streamlit%20Dashboard/Customer%20Segmentation.png)
 
### 📈 Demand Forecasting
![Forecast](report/Streamlit%20Dashboard/Demand%20Forecasting%20Dashboard.png)
 
### ⚠️ Churn Analysis
![Churn](report/Streamlit%20Dashboard/Customer%20Churn%20Analysis.png)
 
### 📦 Inventory Optimization
![Inventory](report/Streamlit%20Dashboard/Inventory%20Optimization.png)





## ⚙️ Installation

```bash
# Clone Repository

git clone https://github.com/harshitaarora0019/RetailPulse-Advanced-Retail-Analytics-Forecasting.git

# Move To Project Directory

cd RetailPulse-Advanced-Retail-Analytics-Forecasting

# Install Dependencies

pip install -r requirements.txt

# Launch Application

cd app

streamlit run main.py
```

---

## 📦 Requirements

```text
streamlit
pandas
numpy
scikit-learn
prophet
matplotlib
seaborn
openpyxl
```

---

## 👩‍💻 Author

### Harshita Arora

B.Tech Computer Science Engineering

Data Analytics • Machine Learning • Business Intelligence • Forecasting

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

<p align="center">
<b>Built with ❤️ by Harshita Arora</b>
</p>
