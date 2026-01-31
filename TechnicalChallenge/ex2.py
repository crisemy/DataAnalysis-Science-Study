from os.path import exists
import csv
from datetime import datetime
from collections import defaultdict

'''------------------------------------------
Technical Challenge: Customers and Orders
Company: AnyoneIA
Author: Cris N.
Date: 05-14-2024
-------------------------------------------'''

# check if file can be found and open the file
datafile = "./sample_data/orders.csv"
if not exists(datafile):
    raise SystemExit("You should run the first code cell and download the dataset files!")

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
    except ValueError:
        return None

def add_order_to_monthly_sales(row, monthly_sales):
    date_str = row[2]
    order_total = float(row[3])
    order_date = parse_date(date_str)
    if order_date:
        month_year = order_date.strftime("%Y-%m")
        monthly_sales[month_year] += order_total

def process_order(row, unique_orders, max_items_per_order, orders_in_october_2021, customer_spending, current_order_id, items_in_current_order):
    order_id = row[1]
    product_name = row[4]
    order_date = parse_date(row[2])
    customer_id = row[0]
    order_total = float(row[3])

    unique_orders.add(order_id)

    if order_id != current_order_id[0]:
        total_orders[0] += 1
        total_items[0] += len(items_in_current_order)
        max_items_per_order[0] = max(max_items_per_order[0], len(items_in_current_order))
        items_in_current_order.clear()
        current_order_id[0] = order_id

    items_in_current_order.add(product_name)

    if order_date and order_date.year == 2021 and order_date.month == 10:
        orders_in_october_2021[0] += 1

    if order_date and order_date.year == 2021:
        customer_spending[customer_id] += order_total

    add_order_to_monthly_sales(row, monthly_sales)

# Initializing variables
unique_orders = set()
total_items = [0]
total_orders = [0]
current_order_id = [None]
items_in_current_order = set()
max_items_per_order = [0]
orders_in_october_2021 = [0]
customer_spending = defaultdict(float)
monthly_sales = defaultdict(float)

with open(datafile, 'r') as fl:
    csvreader = csv.reader(fl, delimiter=',')
    next(csvreader)  # Skip the header row

    for row in csvreader:
        process_order(row, unique_orders, max_items_per_order, orders_in_october_2021, customer_spending, current_order_id, items_in_current_order)

# Add the last order
total_orders[0] += 1
total_items[0] += len(items_in_current_order)
average_items_per_order = round(total_items[0] / total_orders[0], 2)

# Customer spent the best amount of money
max_spending_customer = max(customer_spending, key=customer_spending.get)
max_spending_amount = customer_spending[max_spending_customer]

# Check for the best month for sale
best_month = max(monthly_sales, key=monthly_sales.get)
best_month_sales = monthly_sales[best_month]

print("--------------------------------------")
print("Starting the 2nd Technical Challenge.")
print("--------------------------------------\n")
# Total number of unique orders    
print("Question 1: How many unique orders are in the orders.csv file?")
print(f"The number of unique orders is: {len(unique_orders)} \n")

# Average of items per order
print("Question 2: What is the average number of items per order (rounded to two decimal places)?")
print(f"The average number of items per order is: {average_items_per_order} \n")

# Highest number of items per order
print("Question 3: What is the highest number of items per order?")
print(f"The highest number of items per order is: {max_items_per_order[0]} \n")

# The number of orders placed in October 2021
print("Question 4: What is the number of orders placed in October 2021?")
print(f"The number of orders placed in October 2021 is: {orders_in_october_2021[0]} \n")

# Customer who spent most amount of money in 2021
print("Question 5: Which customer spent the most amount of money in 2021?")
print(f"The customer who spent the most amount of money in 2021 is CustomerID: {max_spending_customer} with a total spend of ${max_spending_amount:.2f} \n")

# The best month for sale
print("Question 6: Historically, what is the best month for sales?")
print(f"The best month for sales historically is {best_month} with total sales of ${best_month_sales:.2f} \n")
print("--------------------------------------")
print("Finishing the 2nd Technical Challenge.")
print("--------------------------------------")