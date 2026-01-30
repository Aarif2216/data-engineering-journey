#list
'''
-Docstring for python_basics.day05_lists
-List is a built-in data type in Python that represents an ordered collection of items.
-List are mutable.
-Lists can contain items of different data types, including other lists.
'''
#Creating a list
numbers  = [1,2,3,"four",5.0,True]
numbers2 = list((6,7,8,"nine",10.0,False)) #Using list() constructor
print(numbers)

#Accessing list elements. Works similar to string indexing.
print(numbers[0])  #First element
print(numbers[-1]) #Last element

#concatenating two lists
combined = numbers + numbers2
print(combined)

#Modifying list elements
numbers[3] = 4
print(numbers)

#Adding elements to a list
numbers.append(6) #Adds to the end
print(numbers)
numbers.insert(0, 0) #Inserts at index 0  insert(index, value).
print(numbers)
#Removing elements from a list
numbers.remove(4) #Removes first occurrence of value 4
print(numbers)
popped_value = numbers.pop() #Removes and returns last element
print(f"Popped Value: {popped_value}")
numbers.pop(3) #Removes element at index 3
print(numbers)

#List Slicing. This is also similar to string slicing.
sublist = numbers[1:4] #Elements from index 1 to 3
print(sublist)
sublist2 = numbers[:3] #Elements from start to index 2  
print(sublist2)
sublist3 = numbers[3:] #Elements from index 3 to end    
print(sublist3)
#Sorting a list
num_list = [5, 2, 9, 1, 5, 6]
num_list.sort() #Sorts the list in place    
print(num_list)
num_list.sort(reverse=True) #Sorts in descending order  
print(num_list)
#Using sorted() to return a new sorted list
original_list = [3, 1, 4, 1, 5]     
sorted_list = sorted(original_list)
print(f"Original List: {original_list}")
print(f"Sorted List: {sorted_list}")
#Reversing a list
num_list.reverse()
print(num_list)

#finding the length of a list   
print(f"Length of numbers list: {len(numbers)}")    
#Iterating through a list
for item in numbers:
    print(item)
#List comprehension: Creating a new list by applying an expression to each item in an existing list.[expression for item in iterable if condition]
squared_numbers = [x**2 for x in range(1, 6)]       
print(f"Squared Numbers: {squared_numbers}")
#finding minimum and maximum values in a list manually.
min_value = min(num_list)
max_value = max(num_list)
print(f"Minimum Value: {min_value}, Maximum Value: {max_value}")
man_min_values  = sorted(num_list)[0]
man_max_values = sorted(num_list)[-1]
print(f"Minimum Value: {man_min_values}, Maximum Value: {man_max_values}")