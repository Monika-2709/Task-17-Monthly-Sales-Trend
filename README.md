# 📊 Task 17 – Monthly Sales Trend

## 📌 Overview

This project focuses on analyzing retail sales data by month and visualizing the sales trend using a line chart.

The task demonstrates important data analytics concepts including **date handling, monthly aggregation, chronological sorting, and time-series visualization**.

## 🎯 Objective

To summarize sales by month and visualize the monthly sales trend.

## 🛠️ Tools & Technologies

* Microsoft Excel
* Python
* Pandas
* Matplotlib

## 📂 Project Files

| File                               | Description                                                       |
| ---------------------------------- | ----------------------------------------------------------------- |
| `retail_sales_2025.csv`            | Retail sales dataset                                              |
| `monthly_sales_trend.py`           | Python analysis and visualization script                          |
| `monthly_sales_trend.png`          | Monthly sales trend line chart                                    |
| `Task_17_Monthly_Sales_Trend.xlsx` | Excel workbook containing raw data, monthly summary and dashboard |
| `README.md`                        | Project documentation                                             |

## 📊 Dataset

The dataset contains retail sales information including:

* Order ID
* Order Date
* Region
* Segment
* Product
* Category
* Quantity
* Discount
* Sales

The dataset covers **January 2025 to December 2025**.

## 🔎 Analysis Process

1. Loaded the retail sales dataset.
2. Converted `Order_Date` into a proper datetime format.
3. Created a monthly period from the order date.
4. Grouped sales records by month.
5. Calculated total sales for each month.
6. Sorted months chronologically.
7. Created a monthly sales summary.
8. Visualized the trend using a line chart.

## 📈 Visualization

The project uses a **line chart** because it is suitable for showing changes and trends over time.

The visualization helps identify:

* Monthly fluctuations
* High-sales periods
* Low-sales periods
* Overall sales movement throughout the year

## 🐍 Python Code

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "retail_sales_2025.csv",
    parse_dates=["Order_Date"]
)

# Create monthly period
df["Month"] = df["Order_Date"].dt.to_period("M")

# Group sales by month
monthly_sales = (
    df.groupby("Month", as_index=False)["Sales"]
      .sum()
      .sort_values("Month")
)

# Create readable month labels
monthly_sales["Month_Name"] = (
    monthly_sales["Month"].dt.strftime("%b-%Y")
)

# Display monthly sales
print(monthly_sales[["Month_Name", "Sales"]])

# Create line chart
plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales["Month_Name"],
    monthly_sales["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend - 2025")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "monthly_sales_trend.png",
    dpi=150
)

plt.show()
```

## 💡 Key Learning Outcomes

Through this task, I learned:

* Date and datetime handling
* Monthly data grouping
* Sales aggregation
* Chronological sorting
* Time-series analysis
* Line chart visualization
* Excel-based sales analysis
* Python-based data analysis

## ❓ Interview Questions

### 1. What is the best chart for time trends?

A **line chart** is generally suitable because it clearly shows how a value changes over time.

### 2. Why can date formatting cause errors?

If dates are stored as text instead of actual date values, they may be sorted incorrectly or may not group correctly by month.

### 3. Why should months be sorted chronologically?

Chronological sorting ensures that the visualization follows the actual sequence of time rather than alphabetical order.

### 4. Why use monthly aggregation?

Monthly aggregation simplifies transaction-level data and makes it easier to identify trends and fluctuations.

## 📌 Conclusion

This project demonstrates a complete basic workflow for **monthly sales analysis**, from date preprocessing and aggregation to visualization. It combines Excel and Python to provide both spreadsheet-based and programmatic approaches to sales trend analysis.

---

### 🔖 Tags

`Python` `Pandas` `Matplotlib` `Excel` `Data Analytics` `Data Visualization` `Sales Analysis` `Time Series`
