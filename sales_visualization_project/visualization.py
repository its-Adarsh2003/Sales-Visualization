import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset
df = pd.read_csv("sales_data.csv")

# Create images folder if not exists
os.makedirs("images", exist_ok=True)

# 1. Line Chart (Sales vs Expenses)
plt.figure(figsize=(8,5))
plt.plot(df["Month"], df["Sales"], marker='o', label="Sales")
plt.plot(df["Month"], df["Expenses"], marker='o', label="Expenses")
plt.title("Sales vs Expenses Over Time")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.savefig("images/line_chart.png")
plt.close()

# 2. Bar Chart (Monthly Sales)
plt.figure(figsize=(8,5))
sns.barplot(x="Month", y="Sales", data=df)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("images/bar_chart.png")
plt.close()

# 3. Pie Chart (Sales Distribution)
plt.figure(figsize=(6,6))
plt.pie(df["Sales"], labels=df["Month"], autopct='%1.1f%%', startangle=140)
plt.title("Sales Distribution by Month")
plt.savefig("images/pie_chart.png")
plt.close()

print("✅ All charts saved in 'images/' folder")
