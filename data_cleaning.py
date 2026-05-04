import os
import pandas as pd

# Data Loading
# This script loads the raw e-commerce dataset, combines both sheets,
# cleans invalid records, creates revenue/time-based features,
# and exports a cleaned CSV for Tableau dashboarding.

RAW_FILE = "online_retail_II.xlsx"
OUTPUT_FILE = "cleaned_retail.csv"

print("Current files:", os.listdir())

# Load Excel workbook
xls = pd.ExcelFile(RAW_FILE)
print("Sheets:", xls.sheet_names)

# Load both sheets
df1 = pd.read_excel(RAW_FILE, sheet_name=0)
df2 = pd.read_excel(RAW_FILE, sheet_name=1)

# Combine into one dataset
df = pd.concat([df1, df2], ignore_index=True)

print("Initial shape:", df.shape)
print("Columns:", df.columns.tolist())

# Data Cleaning
# Remove rows without Customer ID so customer-level analysis is possible.
df = df[df["Customer ID"].notna()]

# Remove invalid transactions with non-positive quantity or price.
df = df[df["Quantity"] > 0]
df = df[df["Price"] > 0]

# Feature Engineering
# Create revenue and time-based fields for dashboarding.
df["Revenue"] = df["Quantity"] * df["Price"]

df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

print("Cleaned shape:", df.shape)
print(df.head())

# Export cleaned data
df.to_csv(OUTPUT_FILE, index=False)

print(f"Cleaned dataset saved to {OUTPUT_FILE}")
