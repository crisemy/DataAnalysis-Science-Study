from os.path import exists
import csv
from collections import defaultdict

'''------------------------------------------
Technical Challenge: Customers and Orders
Company: AnyoneIA
Author: Cris N.
Date: 05-14-2024
-------------------------------------------'''

# check if file can be found and opened up
datafile = "./sample_data/customers.csv"
if not exists(datafile):
    raise SystemExit("You should run the first code cell and download the dataset file!")

# Defining Functions
def count_customers(customersQuantity):
    return customersQuantity + 1

def count_states(states, statesQuantity, state):
    if state not in states:
        states.append(state)
        statesQuantity += 1
    return states, statesQuantity

def count_customers_by_state(customersByState, state):
    customersByState[state] = customersByState.get(state, 0) + 1
    return customersByState

def find_least_customers(customersByState):
    least_customers_state = min(customersByState, key=customersByState.get)
    least_customers_count = customersByState[least_customers_state]
    return least_customers_state, least_customers_count

def find_most_common_last_name(last_names):
    most_common_last_name = max(last_names, key=last_names.get)
    most_common_last_name_count = last_names[most_common_last_name]
    return most_common_last_name, most_common_last_name_count

with open(datafile, 'r') as fl:
    csvreader = csv.reader(fl, delimiter=',')
    next(csvreader)
    
    # Initializing variables
    customersQuantity = 0
    states = []
    statesQuantity = 0
    customersByState = {}
    last_names = defaultdict(int)

    for row in csvreader:
        # Question 1
        customersQuantity = count_customers(customersQuantity)
        
        # Question 2
        state = row[4].strip().upper()
        states, statesQuantity = count_states(states, statesQuantity, state)

        # Question 3
        customersByState = count_customers_by_state(customersByState, state)
        
        # Question 4
        customersByState = count_customers_by_state(customersByState, state)
        
        # Question 5    
        last_name = row[2].strip()
        last_names[last_name] += 1

    # Find the state with the most customers
    most_customers_state = max(customersByState, key=customersByState.get)
    most_customers_count = customersByState[most_customers_state]
    
    # Find the state with the least customers
    least_customers_state, least_customers_count = find_least_customers(customersByState)
    
    # Find the most common last name
    most_common_last_name, most_common_last_name_count = find_most_common_last_name(last_names)

print("--------------------------------------")
print("Starting the 1st Technical Challenge.")
print("--------------------------------------\n")
# Total Quantity of Customers
print("Question 1: How many customers are in the file?")
print(f"The quantity of Customers is: {customersQuantity}\n")

# Total Quantity of States
print("Question 2: In how many different states do the customers live in?")
print(f"Total Quantity of States: {statesQuantity}\n")

# State with the most Customers
print("Question 3: What is the state with most customers?")
print(f"The state with the most customers is {most_customers_state} with {most_customers_count} customers.\n")

# State with the least Customers
print("Question 4: What is the state with the least customers?")
print(f"The state with the least customers is {least_customers_state} with {least_customers_count} customers.\n")
    
# Most common last name
print("Question 5: What is the most common last name?")
print(f"The most common last name is {most_common_last_name} with {most_common_last_name_count} occurrences.\n")
print("--------------------------------------")
print("Finishing the 1st Technical Challenge.")
print("--------------------------------------")