import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("monthly_sales_full_report.csv")

print("---- Monthly Sales Data ----")
print(df.head(), "\n")


plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Sales"], marker='o', linewidth=2)

plt.title("Company Sales Trend Over 12 Months")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
plt.bar(df["Month"], df["Quantity_Sold"])

plt.title("Product Quantity Sold Per Month")
plt.xlabel("Month")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.show()


print("---- Summary Statistics ----")
print(df.describe(), "\n")


best_month = df.loc[df["Sales"].idxmax()]
worst_month = df.loc[df["Sales"].idxmin()]

print(f"📌 Best Month: {best_month['Month']} - Sales: {best_month['Sales']}")
print(f"📌 Worst Month: {worst_month['Month']} - Sales: {worst_month['Sales']}")
