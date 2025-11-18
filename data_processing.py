import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("original data:")
print(df.head())

## cleaning data

print("Missing Values:")
print(df.isnull().sum())

print("\n" + "="*50 + "\n")

df = df.dropna(subset=["CustomerID"])

df["Amount"].fillna(df["Amount"].mean(), inplace=True)

print(df)
sales_by_region = df.groupby("Region")["Amount"].sum()
print("\nSales by Region:")
print(sales_by_region)

plt.bar(sales_by_region.index, sales_by_region.values)
plt.show()
