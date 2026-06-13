# 📊 RetailPulse — AI Retail Analytics & Forecasting Platform

> An end-to-end AI-powered retail analytics platform for demand forecasting, customer segmentation, churn analysis, and inventory optimization.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![Prophet](https://img.shields.io/badge/Prophet-Forecasting-green)
![License](https://img.shields.io/badge/License-MIT-yellow)


## 🌐 Live Demo
👉 [RetailPulse Live App](https://retailpulse-advanced-retail-analytics-forecasting-c5kfyjefbhjn.streamlit.app/)

## 📂 Dataset
- [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)
- 500K+ transactions · UK-based retail · 2010-2011

![RetailPulse Banner](reports/Streamlit%20Dashboard/RetailPulse%20—%20AI%20Retail%20Analytics.png)

---

## 🚀 What is RetailPulse?

RetailPulse is a full-stack Data Science project built on real-world retail transaction data (UCI Online Retail Dataset — 500K+ transactions). It transforms raw sales data into actionable business intelligence through interactive dashboards, predictive models, and AI-driven insights.

Whether you're a business analyst, data scientist, or product manager — RetailPulse gives you the tools to understand your customers, forecast revenue, and make smarter inventory decisions.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 Sales Analytics | Revenue trends, KPIs, top products & monthly breakdown |
| 👥 Customer Segmentation | RFM model + K-Means clustering (VIP, Loyal, Regular, Lost) |
| 📈 Demand Forecasting | Facebook Prophet — 30-day revenue forecast with confidence bands |
| ⚠️ Churn Prediction | 90-day inactivity-based churn detection |
| 📦 Inventory Optimization | Prophet-based stock value recommendations |
| ⬇️ Export Ready | Download forecast & segmentation CSV for stakeholder reporting |

---

## 🛠️ Tech Stack

**Languages**
- Python

**Data Science & ML**
- Pandas · NumPy · Scikit-learn · Facebook Prophet
- K-Means Clustering · RFM Modeling · Time-Series Forecasting

**Visualization & BI**
- Streamlit · Matplotlib · Seaborn · Power BI

**Tools**
- Git · GitHub · Jupyter Notebook · PyCharm

---

## 📁 Project Structure

```
RetailPulse/
├── app/
│   ├── main.py                  # Streamlit dashboard (main app)
│   └── utils/
│       └── preprocess.py        # Data cleaning & feature engineering
├── dashboards/
│   └── PowerBI dashboard.pbix   # Power BI dashboard
├── data/
│   ├── raw/
│   │   └── Online Retail.xlsx   # Original dataset
│   └── processed/
│       └── cleaned_retail.csv   # Cleaned dataset
├── notebooks/
│   ├── EDA.ipynb                # Exploratory Data Analysis
│   ├── RetailPulse.ipynb        # Main analysis notebook
│   └── NeuralRetail.ipynb       # Neural network experiments
├── reports/
│   └── Streamlit Dashboard/     # Dashboard screenshots
├── models/                      # Saved ML models
├── requirements.txt             # Dependencies
└── README.md
```

---

## 📸 Screenshots

### 🏠 Home
![Home](reports/Streamlit%20Dashboard/RetailPulse%20—%20AI%20Retail%20Analytics.png)

### 📁 Upload Dataset
![Upload](reports/Streamlit%20Dashboard/Upload%20Dataset%20Dashboard.png)

### 📊 Sales Analytics
![Sales](reports/Streamlit%20Dashboard/Sales%20Analytics%20Dashboard.png)

### 👥 Customer Segmentation
![Segmentation](reports/Streamlit%20Dashboard/Customer%20Segmentation.png)

### 📈 Demand Forecasting
![Forecast](reports/Streamlit%20Dashboard/Demand%20Forecasting%20Dashboard.png)

### ⚠️ Churn Analysis
![Churn](reports/Streamlit%20Dashboard/Customer%20Churn%20Analysis.png)

### 📦 Inventory Optimization
![Inventory](reports/Streamlit%20Dashboard/Inventory%20Optimization.png)

---

## 💡 What Does RetailPulse Tell You?

- 🏆 **Who are your best customers?** — VIP & Loyal segments drive most revenue
- 📉 **Who is about to leave?** — Churn prediction identifies at-risk customers before it's too late
- 📅 **What will your revenue look like next month?** — Prophet forecasting with daily confidence intervals
- 🛒 **Which products sell the most?** — Top 10 product analysis by quantity and revenue
- 📦 **How much stock should you hold?** — Data-driven inventory recommendations

---

## ⚙️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/harshitaarora0019/RetailPulse-Advanced-Retail-Analytics-Forecasting.git

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
cd app
streamlit run main.py
```

---

## 📦 Dependencies

```
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

## 👩‍💻 About the Author

**Harshita Arora**

<div align="center">

**Built with 💜 by Harshita**

*"Turning raw data into real decisions"*

</div>
