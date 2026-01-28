#Numbers
'''
Docstring for python_basics.python_basics.day02_numbers
This script demonstrates the use of numbers in Python, including integers and floating-point numbers, along with basic arithmetic operations.
'''
#Modulo Operator % returns the remainder of a division
print(15%2)
#Exponentiation Operator ** raises a number to the power of another
print(2**3)  # 2 raised to the power of 3
#Floor Division Operator // returns the largest integer less than or equal to the division result   
# Why doesn't 0.1+0.2-0.3 equal 0? Because of floating-point precision issues in binary representation.
print(0.1 + 0.2 - 0.3)  # Outputs a very small number close to 0, not exactly 0
# what's 1/2?
print(1/2)  # Outputs 0.5 why because in Python 3, division of integers results in a float
# what's 1//2?  
print(1//2)  # Outputs 0 because floor division returns the largest integer less than or equal to the division result
#Type Conversion
num_int = 10  # Integer
num_float = float(num_int)  # Convert integer to float
print(num_float)  # Outputs: 10.0
#variable assignment: Python uses dynamic typing, so you can assign different types of values to the same variable

a = int(input("Enter a number: "))
b = 2.5
c = a + b # c will be assigned by adding a and b
print(c)  # Outputs: 7.5
c = "Hello"  # possoible because of dynamic typing.

# Do "Plus one" problem on leetcode.