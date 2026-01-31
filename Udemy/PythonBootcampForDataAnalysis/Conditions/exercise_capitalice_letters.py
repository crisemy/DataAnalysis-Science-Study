# The objective is to capitalice a string by following the following structure
# Before: "There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."
# After: "ThErE Is No OnE WhO lOvEs PaIn..."

# NOTE: It doesn't matter whether there's spaces in the phrase or not. 
# Whenever a new letter is present, it should be replaced.

# The intent is to create a function by using a loop and if statements on it.

'''
Steps
1. Create a function to get an string like: 
def alternating(string):
2. There should be a new_string variable to get the new string there(The after string I'd say)
3. Loop with a FOR statement and perform the proper changes
4. Get an IF condition which is gonna be in charge of asking for the value of the string
5. Add those new values to the new_string variable
'''

phrase = 'There'
phrase2 = 'is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain'

# To get the lenght of the String
range(len(phrase))
range(0, 5)

def alternating(phrase):
    new_phrase = ''
    for string_index in (range(len(phrase))):
        if string_index % 2 == 0: # We could say that it is an even or odd number
            new_phrase += phrase[string_index].upper() # there should be a concatenation of the new string
        else:
            new_phrase += phrase[string_index].lower()
    
    print(new_phrase)

# Calling the function
alternating(phrase)