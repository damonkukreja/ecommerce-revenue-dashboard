import os
os.listdir()

## Data Loading

In this step, I load the raw e-commerce dataset and inspect its structure, including available sheets and columns. This helps ensure the data is correctly imported before cleaning and analysis.

import pandas as pd
xls = pd.ExcelFile("E-commerce/online_retail_ii.xlsx")
xls.sheet_names

df1 = pd.read_excel("E-commerce/online_retail_ii.xlsx", sheet_name=0)
df2 = pd.read_excel("E-commerce/online_retail_ii.xlsx", sheet_name=1)

df = pd.concat([df1, df2], ignore_index=True)

After combining the datasets, I inspect the structure to verify column names, data types, and identify any missing or inconsistent values.

df.shape

df.info()

df.head()

df.columns.tolist()

## Data Cleaning

I prepared the dataset for analysis by removing incomplete and invalid records. Transactions without customer IDs were excluded to enable customer-level analysis, and entries with non-positive quantities or prices were filtered out to ensure accurate revenue calculations and avoid distortion from returns or data errors.

df = df[df["Customer ID"].notna()]
df.shape

df = df[df["Quantity"] > 0]
df = df[df["Price"] > 0]

I created additional features to support analysis, including revenue and time-based attributes.

df["Revenue"] = df["Quantity"] * df["Price"]

df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)

df.head()

df.info()

df.shape

df.to_csv("E-commerce/cleaned_retail.csv", index=False)

os.listdir("E-Commerce")

## Visualization & Dashboard

The following dashboard presents revenue trends, top-performing products, and geographic distribution of sales.

![Dashboard.png](attachment:0296921a-1236-4d66-bbdc-273a3661503d.png)

## Key Insights

- Revenue exhibits strong seasonality, with significant peaks during November–December, likely driven by holiday purchasing behavior.

- A small number of products contribute a disproportionate share of total revenue, indicating reliance on top-performing items.

- Revenue is heavily concentrated in the United Kingdom, suggesting strong geographic dependence and limited international diversification.

- The final period shows a sharp decline, likely due to incomplete data rather than a true drop in performance, highlighting the need to account for partial time periods.