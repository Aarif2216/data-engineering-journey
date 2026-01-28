#Strings
''' String are sequences of characters enclosed in quotes(single/ double).
    Strings are ordered and immutable (cannot be changed after creation).
    uses [] to access characters by index. Indexing starts at 0.
    Reverse indexing starts at -1 for the last character. 0 ... -4 -3 -2 -1
    Slicing: str[start:end:step] extracts substring from start index to end-1 index.
    Escape Characters: Use backslash (\) for special characters like \n (newline), \t (tab), \\ (backslash), \' (single quote), \" (double quote).
    'I'm learning Python' -> 'I\'m learning Python' or "I'm learning Python".
'''
Journey = "I'm learning Python"
print(Journey)
# Accessing characters by index
print(Journey[0], Journey[-1]) 
# Slicing
print(Journey[0:5])
print(Journey[0:len(Journey): 2])
print(Journey[: : -1])
text = "Data Engineering"

print(f"Length: {len(text)}")
print(f"First char: {text[0]}")
print(f"Last char: {text[-1]}")
print(f"Slice (0–4): {text[0:4]}")
print(f"Reversed: {text[::-1]}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Count of 'e': {text.count('e')}")
print(f"Index of 'E': {text.index('E')}")
print(f"Replace 'Data' with 'Big Data': {text.replace('Data', 'Big Data')}") 

# String Properties and Methods
'''#Immutability: 
s = 'Arif'
s[0] = 'B'  # This will raise an error because strings are immutable.
What is real meaning of immutability? It means once a string is created, its characters cannot be changed or modified. Any operation that seems to modify a string actually creates a new string.

'''
#concatenation
first_name  = "Arif"
last_name = "Hussain"
full_name = first_name + " " + last_name
print(full_name)

print(first_name * 3)  # Repeats the string 3 times
#f-strings (formatted string literals)
age = 22
intro = f"My name is {full_name} and I am {age} years old."
print(intro)
#String Methods
print(full_name.upper())  # Converts to uppercase
print(full_name.lower())  # Converts to lowercase
print(full_name.split()) # Splits into a list of words
print(full_name.split('u')) # Splits at 'u'

