# Dictionary creation - There are tuples to gain access to the dictionary
dictionary = {'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

# ways to handle data from a dictionary
dictionary.keys()
dictionary.values()
dictionary.items()

# Examples of data manipulation
{k: v ** 2 for (k, v) in dictionary.items()}
{k.upper(): v for (k, v) in dictionary.items()}
{k.upper(): v*2 for (k, v) in dictionary.items()}

# 1. Exercise
# List made up with numbers. Find the even numbers in the list. Search for even numbers and square them.
# The intent is to add them to a dictionary

numbers = range(10)
new_dict = {} # Creating a dictionary to save squared even numbers

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

print(new_dict)

# This FOR statement is the same of the above one but quite reduced. Notice how the order of the struncture changes
{n: n ** 2 for n in numbers if n % 2 == 0}

print(new_dict)

# 2. Excercise: Change a dictionary structure to get uppercase words. For instance:
# Before: 
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']
# After:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSESS, 'ABBREV']
#  

import seaborn as sns

car_crashes = ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']
df = sns.load_dataset("car_crashes")
print(df.columns)

# Traditional way
for col in df.columns:
    print(col.upper())

# Adding the Uppercase phrases to a new dictionary
new_dictionary = []

for col in df.columns:
    new_dictionary.append(col.upper())
print(new_dictionary)

# Python Way
df.columns = new_dictionary
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

# 3. For variables in the dictionary that contains the 'ins', there should be a "FLAG_", otherwise a "NO_FLAG_"
# Let's use the new_dictionary option

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

