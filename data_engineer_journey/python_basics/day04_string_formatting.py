# String Formatting in Python
''' .format() method and f-strings (formatted string literals) are two ways to format strings in Python.
1. .format() Method:
   - Use curly braces {} as placeholders in the string.
   - Call the .format() method on the string and pass the values to be inserted.
   - You can use positional or keyword arguments.

'''

print("My name is {} and I am {} years old." .format("Md Arif Hussain", 22))
#Using positional arguments.
print("My name is {0} and I am {1} years old. {0} is learning Python." .format("Md Arif Hussain", 22))

#Using Keyword arguments.
print("My naem is {name} and I am {age} years old {}.".format(name  = 'Md Arif Hussain', age  = 22))

