from app.utils.preprocess import load_data, clean_data, save_clean_data


# -------------------------------
# LOAD RAW DATASET
# -------------------------------
df = load_data("data/raw/Online Retail.xlsx")


# -------------------------------
# CLEAN DATA
# -------------------------------
df = clean_data(df)


# -------------------------------
# SAVE CLEAN DATASET
# -------------------------------
save_clean_data(df, "data/processed/cleaned_retail.csv")


# -------------------------------
# PREVIEW
# -------------------------------
print(df.head())
print(df.shape)