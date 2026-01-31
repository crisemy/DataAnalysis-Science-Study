# Integer
x = 46
print(type(x)) # It's an Int class

# Complex numbers
x = 2j + 1
print(type(x))

# String data
x = "Hello, AI Era"
print(type(x))

print('John')
"Hello AI Era".split()
"foo".capitalize()

# List
x = ["ntc", "eth", "xrp"] # Lists are using brackets
print(type(x))

notes = [1, 2, 3, 4]
print(notes[0])

# Dictionary
x = {"name": "Peter", "Age": 36} # Dictionaries have key value pairs
print(type(x))

# Tuples
x = ("Python", "ML", "DS")
print(type(x))

# Sets - Are used for mathematical operations
x = {"python", "ml", "ds"} # Separated by curly brackets

set1 = set([1, 3, 5]) # Using the set function and creating a set from a List
set2 = set([1, 2, 3])

# What elements are in set2 but not in set1
print("Values to differ with:", set2.difference(set1)) # Using the 'difference' function

# Do the differences among each others
set1 - set2