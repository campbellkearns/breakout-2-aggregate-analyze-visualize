import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("original data:")
print(df.head())

## identify missing values
print("Missing Values:")
print(df.isnull().sum())

print("\n" + "="*50 + "\n")

# cleaning data (drop rows with missing CustomerID, fill missing Amounts with mean)
df = df.dropna(subset=["CustomerID"])
df["Amount"].fillna(df["Amount"].mean(), inplace=True)
print(df)

# aggregate total sales by region
sales_by_region = df.groupby("Region")["Amount"].sum()
print("\nSales by Region:")
print(sales_by_region)

# visualize sales by region
plt.bar(sales_by_region.index, sales_by_region.values)
plt.show()

# enhanced visualization
plt.figure(figsize=(10,6))
plt.bar(sales_by_region.index, sales_by_region.values, color='green')
plt.xlabel('Sales Region')
plt.ylabel('Total Sales in Region')
plt.savefig("sales_by_region.png")
plt.show()

# sales trend over time (monthly)
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Amount'].sum()

# visualize sales over time in a line chart
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind="line", title="Sales by Month", marker='o', color='green')
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("sales_by_month.png")
print("Line chart saved as 'sales_by_month.png'")
plt.show()

## cleaned data saved to new csv file
df.to_csv("cleaned_sales_data.csv", index=False)
print("Cleaned data saved to 'cleaned_sales_data.csv'")
