# Lambda is frequently used and important. Is a type of function

# The typical way of calling and generating a function is as follows
def summer(a, b):
    return a + b

print(summer(1,3) * 9)

# Using the 'Lambda' way. 
new_sum = lambda a, b: a + b

print(new_sum(4,5)) # Prints out 9 as a result

# Map example
salaries = [1000, 2000, 3000, 4000, 5000]

# Create a function to get a salary increase of 20%
def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

new_salary(20)

# Without writing a loop and without a for, iterates in the by doing the operation
list(map(new_salary, salaries))

# Doing the map + lambda function
print("Iterates by using the map + lambda function: ", list(map(lambda x: x * 20 / 100 + x, salaries)))

# FILTER: Filter functionality to use filter operations. As the name states, does filters
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Let's exclude some values under certain conditions
print(list(filter(lambda x: x % 2 == 0, list_store))) # Output : [2, 4, 6, 8, 10] -Z Selects even numbers

# REDUCE: Means to condense here
# import the functools function
from functools import reduce

list_store = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, list_store)) # Output: 10