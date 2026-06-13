import pandas as pd


# -------------------------------
# LOAD DATA
# -------------------------------
def load_data(filepath):

    # Load CSV or Excel
    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath, encoding="ISO-8859-1")
    else:
        df = pd.read_excel(filepath)

    return df


# -------------------------------
# CLEAN DATA
# -------------------------------
def clean_data(df):

    # Remove missing Customer IDs
    df = df.dropna(subset=["CustomerID"])

    # Remove cancelled orders
    df = df[df["Quantity"] > 0]

    # Remove invalid prices
    df = df[df["UnitPrice"] > 0]

    # Convert InvoiceDate
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Create TotalPrice
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    # Feature Engineering
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["Day"] = df["InvoiceDate"].dt.day
    df["Hour"] = df["InvoiceDate"].dt.hour
    df["DayName"] = df["InvoiceDate"].dt.day_name()

    return df


# -------------------------------
# SAVE CLEAN DATA
# -------------------------------
def save_clean_data(df, output_path):

    df.to_csv(output_path, index=False)

    print(f"✅ Cleaned dataset saved at: {output_path}")