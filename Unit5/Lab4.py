
# To develop a retail sales analysis dashboard using CSV files and Matplotlib to visualize sales data through graphs.

import csv
import matplotlib.pyplot as plt

# Sample retail sales data
sales_data = [
    ["Product", "Quantity", "Price"],
    ["Laptop", 5, 50000],
    ["Mobile", 10, 20000],
    ["Headphones", 15, 2000],
    ["Keyboard", 8, 1500],
    ["Mouse", 12, 800]
]

# Create CSV file
with open("sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sales_data)

# Read CSV file
products = []
sales = []

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["Product"]
        quantity = int(row["Quantity"])
        price = float(row["Price"])

        total = quantity * price

        products.append(product)
        sales.append(total)

# Calculate total revenue
total_revenue = sum(sales)

print("RETAIL SALES DASHBOARD")
print("----------------------")

for i in range(len(products)):
    print(products[i], "Sales:", sales[i])

print("\nTotal Revenue: Rs.", total_revenue)

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(products, sales)
plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(sales, labels=products, autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.show()
