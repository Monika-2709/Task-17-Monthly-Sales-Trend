import pandas as pd
import matplotlib.pyplot as plt

# Load data and convert dates correctly
df = pd.read_csv("retail_sales_2025.csv", parse_dates=["Order_Date"])

# Group sales by month and sort chronologically
df["Month"] = df["Order_Date"].dt.to_period("M")
monthly_sales = (
    df.groupby("Month", as_index=False)["Sales"]
      .sum()
      .sort_values("Month")
)
monthly_sales["Month_Name"] = monthly_sales["Month"].dt.strftime("%b-%Y")

print("\nMONTHLY SALES TABLE")
print(monthly_sales[["Month_Name", "Sales"]].to_string(index=False))

# Line chart for the time trend
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales["Month_Name"], monthly_sales["Sales"], marker="o")
plt.title("Monthly Sales Trend - 2025")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=150)
plt.show()
