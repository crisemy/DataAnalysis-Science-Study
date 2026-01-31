# When there's a list of Students, even or odd students should be part of different groups
# In this case, John and Vanessa should be in one group and Mark and Marian in another one 

# List of students
students = ['John', 'Mark', 'Vanessa', 'Marian']

def divide_students(students):
    
    # Creating a lists of 2 lists to accumulate those 2 list of students 
    groups = [[], []]

    for index, students in enumerate(students): # Use the index to iterate through the list of students
        if index % 2 == 0:
            groups[0].append(students)
        else:
            groups[1].append(students)
    print(groups)
    return groups

ds = divide_students(students)

# Another way of iterate
print(ds[0])
print(ds[1])