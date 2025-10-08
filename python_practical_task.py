# Write a program to remove all items from a list that are less then 5 e.g [12,3,4,5,67,0] output [12,5,67]

# Write a program to find common among 2 lists. eg. lst_numbers = [1,2,34,33,21] lst_numbers2=[11,2,33,45] output [2,33]

# Write a program to sort a list of strings by their length e.g ['apple', 'banana', 'kiwi', 'orange'] output : ['kiwi', 'apple', 'orange', 'banana']

# Write a program to accepts a list of integers and returns a tuple with the sum of all positive numbers and the sum of all negative numbers

# Write a program that takes a list of numbers and returns a tuple containing the sum and product of all the numbers.
# - Input: `[1, 2, 3, 4]`
# - Output: `(10, 24)`

###__________________________________________________


# ## 1) Write a program to remove all items from a list that are less then 5 e.g [12,3,4,5,67,0] output [12,5,67]
# lst_numbers = [12,3,4,5,67,0]
# lst1 = [i for i in lst_numbers if i >= 5]
# print(lst1)
# # for i in lst_numbers:
# #     if i < 5:
# #         lst_numbers.remove(i)
# # print(lst_numbers)

# ## 2) Write a program to find common among 2 lists. eg. lst_numbers = [1,2,34,33,21] lst_numbers2=[11,2,33,45] output [2,33]
# lst_numbers = [1,2,34,33,21]
# lst_numbers2=[11,2,33,45]
# common = set(lst_numbers).intersection(set(lst_numbers2))
# print(common)
# # common = [i for i in lst_numbers if i in lst_numbers2]
# # print(common)

# ## 3) Write a program to sort a list of strings by their length e.g ['apple', 'banana', 'kiwi', 'orange'] output : ['kiwi', 'apple', 'orange', 'banana']
# lst_strings = ['apple', 'banana', 'kiwi', 'orange']
# lst_strings.sort(key=len)
# print(lst_strings)

# # lst_strings = ['apple', 'banana', 'kiwi', 'orange']
# # lst_strings.sort()
# # print(lst_strings)
# # lst_strings = ['apple', 'banana', 'kiwi', 'orange']
# # lst_strings1 = sorted(lst_strings, key=len)
# # print(lst_strings1)
# # lst_strings1 = sorted(lst_strings)
# # print(lst_strings1)

# ## 4) Write a program to accepts a list of integers and returns a tuple with the sum of all positive numbers and the sum of all negative numbers
# lst_numbers = [1, -2, 3, -4, 5]
# sum_positive = sum(i for i in lst_numbers if i > 0)
# sum_negative = sum(i for i in lst_numbers if i < 0)
# print((sum_positive, sum_negative))

# # lst_numbers = [1, -2, 3, -4, 5]
# # sum_positive = 0
# # sum_negative = 0
# # for i in lst_numbers:
# #     if i > 0:
# #         sum_positive += i
# #     elif i < 0:
# #         sum_negative += i
# # print((sum_positive, sum_negative))

## 5) Write a program that takes a list of numbers and returns a tuple containing the sum and product of all the numbers.
# - Input: `[1, 2, 3, 4]`
# - Output: `(10, 24)`
lst_numbers = [1, 2, 3, 4]
sum = sum(i for i in lst_numbers)
product = 1
for i in lst_numbers:
    product *= i
print((sum, product))

# lst_numbers = [1, 2, 3, 4]
# sum = 0
# product = 1
# for i in lst_numbers:
#     sum += i
#     product *= i
# print((sum, product))



#######_________________________________________________________________________________
##tasks for practice---------->


# "Count frequency of list items and write in into dictionary :input List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
# output : {1: 2, 2: 2, 3: 1, 4: 2, 5: 2, 6: 1, 7: 2}"

# Accept a string from the user and print it in uppercase if the length of the string is greater than 5, else print it in lowercase using a function.

# Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.

# Write a function that accepts a list of numbers and returns the average of the numbers, excluding any zero values

# Write a function that accepts a string and returns True if the string is a valid email address (contains "@" and "."), otherwise False.

# Write a function that accepts a list of integers and returns the second largest number in the list.

# Write a Python program that uses `map()` to convert a list of strings to uppercase. Input: `['apple', 'banana', 'cherry']` - Output: `['APPLE', 'BANANA', 'CHERRY']`

# Write a Python program that uses `map()` to apply a function that converts a list of temperature values in Celsius to Fahrenheit. Input: `[0, 25, 100]` Output: `[32.0, 77.0, 212.0]`


# "Find the total income from sales, considering only items that sold more than 100 units sales_data = [
#     {""product"": ""Pen"", ""price"": 10, ""units_sold"": 150},
#     {""product"": ""Notebook"", ""price"": 50, ""units_sold"": 90},
#     {""product"": ""Pencil"", ""price"": 5, ""units_sold"": 300},
# ]"

# "Write a prgram to extract unique values from List in dictionary (With Dict/Set comprehension) input dict_city_list = {'cityList1': ['Ahmedabad','Baroda', 'Bhopal', 'Mumbai'], 
#       'cityList2': ['Baroda', 'Mumbai','Delhi', 'Chochi'], 
#       'cityList3': [""Bhopal"",""Banglore"", ""Pune"", ""Mumbai""], 
#       'cityList4': [""Delhi"",""Ahmedabad"", ""Pune"",""Chochi""]}
# Output {'Banglore', 'Delhi', 'Pune', 'Ahmedabad', 'Mumbai', 'Bhopal', 'Baroda', 'Chochi'}
# "

# create a class called "Book" with attributes for title, author, and ISBN, and methods to display book details.


# Write a program to create a class called "Employee" with a name, salary, and hire date attributes, and a method to calculate years of service.


# Write a program to create a class called "Reservation" with attributes for reservation ID, customer name, and date. Create subclasses "ResortReservation" and "RailwayReservation" that add specific attributes like room number for hotels and seat number for flights. Implement methods to check reservation status and modify reservation details.


# Write a python program to add two distances using class and object concepts (km,m) (Use Operator Oveloading)


# Write a python program to manage a phone store (mobile shop) record using class
# Phone (brand, model, price) and PhoneInventory(add_phone,find_phone,remove_phone,display_phone) class
# 1. Add Phone to Inventory
# 2. Remove Phone from Inventory
# 3. Find Phone in Inventory
# 4. Display Inventory
# 5. Quit