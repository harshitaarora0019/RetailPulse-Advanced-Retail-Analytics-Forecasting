import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from prophet import Prophet
from utils.preprocess import clean_data

# -------------------------------------------------
# PAGE CONFIG & THEME
# -------------------------------------------------
st.set_page_config(page_title="📊 RetailPulse — AI Retail Analytics", layout="wide", page_icon="📊")

BG    = "#0D0F14"
CARD  = "#161B27"
LINE  = "#232B3E"
TEAL  = "#00D4AA"   # primary accent — pops on dark
ORANGE= "#FF6B35"   # secondary accent
YELLOW= "#FFD166"   # tertiary
RED   = "#EF4565"
GREEN = "#06D6A0"
TEXT  = "#E8EDF5"
MUTED = "#7B8DB0"

mpl.rcParams.update({
    "figure.facecolor": CARD,
    "axes.facecolor":   CARD,
    "axes.edgecolor":   LINE,
    "axes.labelcolor":  TEXT,
    "xtick.color":      MUTED,
    "ytick.color":      MUTED,
    "text.color":       TEXT,
    "grid.color":       LINE,
    "grid.alpha":       0.6,
})

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

html, body, [class*="css"] {{
    background-color: {BG};
    color: {TEXT};
    font-family: 'Inter', sans-serif;
}}
.stApp {{ background-color: {BG}; }}

section[data-testid="stSidebar"] {{
    background: {CARD} !important;
    border-right: 1px solid {LINE};
}}
section[data-testid="stSidebar"] * {{ color: {TEXT} !important; }}

/* Hide default Streamlit page nav if multipage */
[data-testid="stSidebarNavItems"] {{ display: none; }}

.metric-card {{
    background: {CARD};
    border: 1px solid {LINE};
    border-radius: 14px;
    padding: 20px 24px;
    text-align: center;
    border-left: 4px solid {TEAL};
    margin-bottom: 8px;
}}
.metric-value {{
    font-size: 1.9rem;
    font-weight: 900;
    color: {TEAL};
    margin: 6px 0 4px;
    letter-spacing: -0.02em;
}}
.metric-label {{
    font-size: 0.78rem;
    color: {MUTED};
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-weight: 600;
}}
.section-header {{
    font-size: 1.2rem;
    font-weight: 800;
    color: {TEXT};
    margin: 28px 0 14px;
    padding-left: 12px;
    border-left: 4px solid {TEAL};
    display: block;
}}
.hero-title {{
    font-size: 3rem;
    font-weight: 900;
    color: {TEAL};
    letter-spacing: -0.03em;
    line-height: 1.1;
}}
.hero-badge {{
    display: inline-block;
    background: {TEAL}22;
    color: {TEAL};
    border: 1px solid {TEAL}55;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    margin-bottom: 14px;
}}
.hero-sub {{ color: {MUTED}; font-size: 1rem; margin-top: 10px; max-width: 600px; line-height: 1.6; }}
.feature-card {{
    background: {CARD};
    border: 1px solid {LINE};
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 12px;
    transition: border-color 0.2s;
}}
.feature-icon {{ font-size: 1.6rem; margin-bottom: 8px; }}
.feature-title {{ font-weight: 700; color: {TEXT}; margin-bottom: 4px; font-size: 0.95rem; }}
.feature-desc {{ color: {MUTED}; font-size: 0.82rem; line-height: 1.5; }}
div[data-testid="stDownloadButton"] button {{
    background: {TEAL}22 !important;
    color: {TEAL} !important;
    border: 1px solid {TEAL}55 !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
}}
h1, h2, h3 {{ color: {TEXT} !important; }}
.stDataFrame {{ border-radius: 10px; overflow: hidden; }}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
with st.sidebar:
    st.markdown(f"""
    <div style='padding: 8px 0 20px'>
        <div style='font-size:1.3rem;font-weight:900;color:{TEAL}'>📊 RetailPulse</div>
        <div style='color:{MUTED};font-size:0.75rem;margin-top:2px;letter-spacing:0.08em'>— AI RETAIL ANALYTICS</div>
    </div>
    <hr style='border-color:{LINE};margin-bottom:20px'>
    """, unsafe_allow_html=True)


    page = st.selectbox("", [
        "🏠 Home",
        "📁 Upload Dataset",
        "📊 Sales Analytics",
        "👥 Customer Segmentation",
        "📈 Demand Forecasting",
        "⚠️ Churn Prediction",
        "📦 Inventory Optimization",
    ], label_visibility="collapsed")

    if "data" in st.session_state:
        df_check = st.session_state["data"]
        st.markdown(f"""
        <div style='margin-top:24px;padding:14px;background:{BG};border-radius:10px;border:1px solid {LINE}'>
            <div style='color:{TEAL};font-size:0.75rem;font-weight:700;margin-bottom:8px'>✅ DATASET LOADED</div>
            <div style='color:{MUTED};font-size:0.78rem'>{df_check.shape[0]:,} rows · {df_check.shape[1]} cols</div>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------
# LOAD & PREPROCESS
# -------------------------------------------------


if "data" in st.session_state:
    df = clean_data(st.session_state["data"].copy())

# -------------------------------------------------
# HOME
# -------------------------------------------------
if page == "🏠 Home":
    st.markdown(f"<div class='hero-badge'>AI POWERED · RETAIL ANALYTICS</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-title'>📊 RetailPulse — AI Retail Analytics</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>Upload your retail dataset and get instant AI-powered insights — sales trends, customer segments, demand forecasting, and churn analysis in one platform.</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    cols = st.columns(3)
    features = [
        ("📊", "Sales Analytics", "Revenue trends, KPIs, top products & daily performance"),
        ("👥", "Customer Segmentation", "RFM model + K-Means clustering into VIP, Loyal, Regular, Lost"),
        ("📈", "Demand Forecasting", "Facebook Prophet — 30-day revenue forecast with confidence bands"),
        ("⚠️", "Churn Prediction", "90-day inactivity detection to identify at-risk customers"),
        ("📦", "Inventory Planning", "Prophet-based stock value recommendations"),
        ("⬇️", "Export Ready", "Download forecast CSV for stakeholder reporting"),
    ]
    for i, (icon, title, desc) in enumerate(features):
        cols[i % 3].markdown(f"""
        <div class='feature-card'>
            <div class='feature-icon'>{icon}</div>
            <div class='feature-title'>{title}</div>
            <div class='feature-desc'>{desc}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='background:{CARD};border:1px solid {LINE};border-radius:14px;padding:20px 24px'>
        <div style='font-weight:800;font-size:0.85rem;color:{TEAL};letter-spacing:0.08em;margin-bottom:10px'>TECH STACK</div>
        <div style='color:{MUTED};font-size:0.88rem;line-height:2'>
        Python &nbsp;·&nbsp; Pandas &nbsp;·&nbsp; NumPy &nbsp;·&nbsp; Scikit-learn &nbsp;·&nbsp; Facebook Prophet &nbsp;·&nbsp; Streamlit &nbsp;·&nbsp; Matplotlib &nbsp;·&nbsp; Seaborn &nbsp;·&nbsp; MySQL
        </div>
    </div>""", unsafe_allow_html=True)

# -------------------------------------------------
# UPLOAD PAGE
# -------------------------------------------------
elif page == "📁 Upload Dataset":
    st.markdown("<div class='section-header'>Upload Dataset</div>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Drop your CSV or Excel retail dataset here", type=["csv", "xlsx"])

    if uploaded_file:
        raw_df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith("csv") else pd.read_excel(uploaded_file)
        st.session_state["data"] = raw_df
        st.success(f"✅ Loaded {raw_df.shape[0]:,} rows × {raw_df.shape[1]} columns")

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<div class='section-header'>Preview</div>", unsafe_allow_html=True)
            st.dataframe(raw_df.head(10), use_container_width=True)
        with c2:
            st.markdown("<div class='section-header'>Summary Stats</div>", unsafe_allow_html=True)
            st.dataframe(raw_df.describe(), use_container_width=True)

        # Download raw data as CSV
        st.markdown("<div class='section-header'>Export</div>", unsafe_allow_html=True)
        csv_raw = raw_df.to_csv(index=False).encode()
        st.download_button("⬇ Download Dataset as CSV", csv_raw, "dataset.csv", "text/csv")

# -------------------------------------------------
# SALES ANALYTICS
# -------------------------------------------------
elif page == "📊 Sales Analytics" and "data" in st.session_state:
    st.markdown("<div class='section-header'>Sales Analytics Dashboard</div>", unsafe_allow_html=True)

    total_revenue = df["TotalPrice"].sum()
    total_orders  = df["InvoiceNo"].nunique()
    total_customers = df["CustomerID"].nunique()
    avg_order = total_revenue / total_orders if total_orders else 0

    c1, c2, c3, c4 = st.columns(4)
    metrics = [
        (f"₹{total_revenue:,.0f}", "Total Revenue", TEAL),
        (f"{total_orders:,}",      "Total Orders",  ORANGE),
        (f"{total_customers:,}",   "Unique Customers", YELLOW),
        (f"₹{avg_order:,.0f}",    "Avg Order Value", GREEN),
    ]
    for col, (val, label, color) in zip([c1,c2,c3,c4], metrics):
        col.markdown(f"""
        <div class='metric-card' style='border-left-color:{color}'>
            <div class='metric-label'>{label}</div>
            <div class='metric-value' style='color:{color}'>{val}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_r = st.columns(2)

    with col_l:
        st.markdown("<div class='section-header'>Daily Revenue Trend</div>", unsafe_allow_html=True)
        daily = df.groupby("InvoiceDate")["TotalPrice"].sum()
        fig, ax = plt.subplots(figsize=(7, 3.5))
        ax.fill_between(daily.index, daily.values, alpha=0.15, color=TEAL)
        ax.plot(daily.index, daily.values, color=TEAL, linewidth=2)
        ax.set_xlabel("Date"); ax.set_ylabel("Revenue (₹)")
        ax.grid(True, axis='y', alpha=0.4)
        ax.spines[['top','right']].set_visible(False)
        fig.tight_layout()
        st.pyplot(fig)

    with col_r:
        st.markdown("<div class='section-header'>Top 10 Products</div>", unsafe_allow_html=True)
        top = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
        fig2, ax2 = plt.subplots(figsize=(7, 3.5))
        bars = ax2.barh(range(len(top)), top.values[::-1],
                        color=[TEAL, ORANGE, YELLOW, GREEN, TEAL, ORANGE, YELLOW, GREEN, TEAL, ORANGE])
        ax2.set_yticks(range(len(top)))
        ax2.set_yticklabels([t[:30] for t in top.index[::-1]], fontsize=8)
        ax2.set_xlabel("Quantity Sold")
        ax2.spines[['top','right']].set_visible(False)
        fig2.tight_layout()
        st.pyplot(fig2)

    # Monthly revenue
    st.markdown("<div class='section-header'>Monthly Revenue Breakdown</div>", unsafe_allow_html=True)
    df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)
    monthly = df.groupby("Month")["TotalPrice"].sum()
    fig3, ax3 = plt.subplots(figsize=(12, 3.5))
    bars = ax3.bar(monthly.index, monthly.values, color=ORANGE, alpha=0.85, width=0.6)
    ax3.set_xlabel("Month"); ax3.set_ylabel("Revenue (₹)")
    ax3.tick_params(axis='x', rotation=45)
    ax3.spines[['top','right']].set_visible(False)
    fig3.tight_layout()
    st.pyplot(fig3)

# -------------------------------------------------
# CUSTOMER SEGMENTATION
# -------------------------------------------------
elif page == "👥 Customer Segmentation" and "data" in st.session_state:
    st.markdown("<div class='section-header'>Customer Segmentation — RFM + K-Means</div>", unsafe_allow_html=True)

    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
    rfm = df.groupby("CustomerID").agg({
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "InvoiceNo":   "count",
        "TotalPrice":  "sum"
    })
    rfm.columns = ["Recency", "Frequency", "Monetary"]

    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm)
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)
    cluster_names = {0: "VIP", 1: "Loyal", 2: "Lost", 3: "Regular"}
    rfm["CustomerSegment"] = rfm["Cluster"].map(cluster_names)

    seg_colors = {"VIP": TEAL, "Loyal": GREEN, "Regular": ORANGE, "Lost": RED}

    # KPI cards
    c1, c2, c3, c4 = st.columns(4)
    for col, seg, color in zip([c1,c2,c3,c4], ["VIP","Loyal","Regular","Lost"], [TEAL,GREEN,ORANGE,RED]):
        count = (rfm["CustomerSegment"] == seg).sum()
        col.markdown(f"""
        <div class='metric-card' style='border-left-color:{color}'>
            <div class='metric-label'>{seg} Customers</div>
            <div class='metric-value' style='color:{color}'>{count}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='section-header'>Segment Distribution</div>", unsafe_allow_html=True)
        seg_count = rfm["CustomerSegment"].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        colors = [seg_colors.get(s, TEAL) for s in seg_count.index]
        ax.bar(seg_count.index, seg_count.values, color=colors, edgecolor="none", width=0.5)
        ax.set_ylabel("Customers")
        ax.spines[['top','right']].set_visible(False)
        fig.tight_layout()
        st.pyplot(fig)

    with col2:
        st.markdown("<div class='section-header'>Revenue by Segment</div>", unsafe_allow_html=True)
        seg_rev = rfm.groupby("CustomerSegment")["Monetary"].sum().sort_values(ascending=False)
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        colors2 = [seg_colors.get(s, TEAL) for s in seg_rev.index]
        ax2.bar(seg_rev.index, seg_rev.values, color=colors2, edgecolor="none", width=0.5)
        ax2.set_ylabel("Revenue (₹)")
        ax2.spines[['top','right']].set_visible(False)
        fig2.tight_layout()
        st.pyplot(fig2)

    st.markdown("<div class='section-header'>Cluster Scatter — Recency vs Monetary</div>", unsafe_allow_html=True)
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    for seg, grp in rfm.groupby("CustomerSegment"):
        ax3.scatter(grp["Recency"], grp["Monetary"], label=seg,
                    color=seg_colors.get(seg, TEAL), alpha=0.7, s=25, edgecolors="none")
    ax3.set_xlabel("Recency (days)"); ax3.set_ylabel("Monetary (₹)")
    ax3.legend(framealpha=0.2)
    ax3.spines[['top','right']].set_visible(False)
    fig3.tight_layout()
    st.pyplot(fig3)

    st.markdown("<div class='section-header'>Segment Table</div>", unsafe_allow_html=True)
    st.dataframe(rfm.head(20), use_container_width=True)

    csv_seg = rfm.to_csv().encode()
    st.download_button("⬇ Download Segmentation CSV", csv_seg, "segments.csv", "text/csv")

# -------------------------------------------------
# DEMAND FORECASTING
# -------------------------------------------------
elif page == "📈 Demand Forecasting" and "data" in st.session_state:
    st.markdown("<div class='section-header'>30-Day Revenue Forecast</div>", unsafe_allow_html=True)

    daily = df.groupby("InvoiceDate")["TotalPrice"].sum().reset_index()
    daily.columns = ["ds", "y"]

    with st.spinner("Training Prophet model..."):
        model = Prophet()
        model.fit(daily)
        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)

    forecast_30 = forecast[["ds","yhat","yhat_lower","yhat_upper"]].tail(30)
    total_projected = forecast_30["yhat"].sum()
    daily_avg = forecast_30["yhat"].mean()

    c1, c2 = st.columns(2)
    c1.markdown(f"""<div class='metric-card' style='border-left-color:{TEAL}'>
        <div class='metric-label'>Projected Revenue (30 Days)</div>
        <div class='metric-value' style='color:{TEAL}'>₹{total_projected:,.0f}</div>
    </div>""", unsafe_allow_html=True)
    c2.markdown(f"""<div class='metric-card' style='border-left-color:{ORANGE}'>
        <div class='metric-label'>Avg Daily Forecast</div>
        <div class='metric-value' style='color:{ORANGE}'>₹{daily_avg:,.0f}</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    fig4 = model.plot(forecast)
    fig4.set_facecolor(CARD)
    st.pyplot(fig4)

    st.markdown("<div class='section-header'>Forecast Components</div>", unsafe_allow_html=True)
    fig5 = model.plot_components(forecast)
    fig5.set_facecolor(CARD)
    st.pyplot(fig5)

    st.markdown("<div class='section-header'>Forecast Table</div>", unsafe_allow_html=True)
    st.dataframe(
        forecast_30.rename(columns={"ds":"Date","yhat":"Forecast ₹","yhat_lower":"Lower","yhat_upper":"Upper"}),
        use_container_width=True
    )
    csv_fc = forecast_30.to_csv(index=False).encode()
    st.download_button("⬇ Download Forecast CSV", csv_fc, "forecast_30days.csv", "text/csv")

# -------------------------------------------------
# CHURN PREDICTION
# -------------------------------------------------
elif page == "⚠️ Churn Prediction" and "data" in st.session_state:
    st.markdown("<div class='section-header'>Customer Churn Analysis</div>", unsafe_allow_html=True)

    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
    last_purchase = df.groupby("CustomerID")["InvoiceDate"].max()
    churn = (snapshot_date - last_purchase).dt.days > 90
    churn_df = churn.reset_index()
    churn_df.columns = ["CustomerID", "Churned"]
    churn_df["Status"] = churn_df["Churned"].map({True: "Churned", False: "Active"})

    churned_n = churn_df["Churned"].sum()
    active_n  = (~churn_df["Churned"]).sum()
    churn_rate = churned_n / len(churn_df) * 100

    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div class='metric-card' style='border-left-color:{RED}'><div class='metric-label'>Churned</div><div class='metric-value' style='color:{RED}'>{churned_n}</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric-card' style='border-left-color:{GREEN}'><div class='metric-label'>Active</div><div class='metric-value' style='color:{GREEN}'>{active_n}</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric-card' style='border-left-color:{ORANGE}'><div class='metric-label'>Churn Rate</div><div class='metric-value' style='color:{ORANGE}'>{churn_rate:.1f}%</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    counts = churn_df["Status"].value_counts()
    fig, ax = plt.subplots(figsize=(5, 3.5))
    ax.bar(counts.index, counts.values, color=[RED, GREEN], width=0.4, edgecolor="none")
    ax.set_ylabel("Customers")
    ax.spines[['top','right']].set_visible(False)
    fig.tight_layout()
    st.pyplot(fig)

    st.dataframe(churn_df.head(20), use_container_width=True)

# -------------------------------------------------
# INVENTORY OPTIMIZATION
# -------------------------------------------------
elif page == "📦 Inventory Optimization" and "data" in st.session_state:
    st.markdown("<div class='section-header'>Inventory Optimization</div>", unsafe_allow_html=True)

    daily = df.groupby("InvoiceDate")["TotalPrice"].sum().reset_index()
    daily.columns = ["ds", "y"]

    with st.spinner("Running forecast..."):
        model = Prophet()
        model.fit(daily)
        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)

    recommended = forecast["yhat"].tail(30).sum()
    daily_avg   = forecast["yhat"].tail(30).mean()
    peak_day    = forecast["yhat"].tail(30).max()

    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div class='metric-card' style='border-left-color:{TEAL}'><div class='metric-label'>Recommended Stock (30 Days)</div><div class='metric-value' style='color:{TEAL}'>₹{recommended:,.0f}</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric-card' style='border-left-color:{ORANGE}'><div class='metric-label'>Avg Daily Demand</div><div class='metric-value' style='color:{ORANGE}'>₹{daily_avg:,.0f}</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric-card' style='border-left-color:{YELLOW}'><div class='metric-label'>Peak Day Demand</div><div class='metric-value' style='color:{YELLOW}'>₹{peak_day:,.0f}</div></div>", unsafe_allow_html=True)

elif "data" not in st.session_state and page not in ["🏠 Home", "📁 Upload Dataset"]:
    st.warning("⚠️ Please upload a dataset first from **📁 Upload Dataset**")