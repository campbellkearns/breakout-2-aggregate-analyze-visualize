import pandas as pd

df = pd.read_csv("temp_sales_data.csv")

## DataFrame
print(df.head())
# print(df.info())
# print(df.describe())
df.rename(columns={"Amt": "Amount"}, inplace=True) 
print(df.head())

df = df.dropna(subset=["CustomerID"])
print(df)

df["Amount"].fillna(df["Amount"].mean(), inplace=True)

df_cleaned = df
print(df_cleaned)



