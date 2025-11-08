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

# ## 5) Write a program that takes a list of numbers and returns a tuple containing the sum and product of all the numbers.
# # - Input: `[1, 2, 3, 4]`
# # - Output: `(10, 24)`
# lst_numbers = [1, 2, 3, 4]
# sum = sum(i for i in lst_numbers)
# product = 1
# for i in lst_numbers:
#     product *= i
# print((sum, product))

# # lst_numbers = [1, 2, 3, 4]
# # sum = 0
# # product = 1
# # for i in lst_numbers:
# #     sum += i
# #     product *= i
# # print((sum, product))


# ###________________________________________________________________


# ## 1) "Count frequency of list items and write in into dictionary :input List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
# List1 = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
# count_dict = {}
# for item in List1:
#     if item in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1
# print(count_dict)

# ## 2) Accept a string from the user and print it in uppercase if the length of the string is greater than 5, else print it in lowercase using a function.
# str = input("Enter a string: ")
# def check_string(str):
#     if len(str) > 5:
#         return str.upper()
#     else:
#         return str.lower()
# print(check_string(str))

# ## 3) Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.
# str = input("Enter a string: ")
# def alternate_case(str):
#     result = ""
#     for i in range(len(str)):
#         if i % 2 == 0:
#             result += str[i].upper()
#         else:
#             result += str[i].lower()
#     return result
# print(alternate_case(str))

# ## 4) Write a function that accepts a list of numbers and returns the average of the numbers, excluding any zero values
# lst_numbers = [1, 2, 0, 4, 5]
# def average_excluding_zeros(lst):
#     non_zero_numbers = [num for num in lst if num != 0]
#     if not non_zero_numbers:
#         return 0
#     return sum(non_zero_numbers) / len(non_zero_numbers)
# print(average_excluding_zeros(lst_numbers))

# ## 5) Write a function that accepts a string and returns True if the string is a valid email address (contains "@" and "."), otherwise False.
# email = input("Enter an email address: ")
# def is_valid_email(email):
#     return "@" in email and "." in email
# print(is_valid_email(email))

# # 6) Write a function that accepts a list of integers and returns the second largest number in the list.
# lst_numbers = [1, 2, 3, 4, 5]
# def second_largest(lst):
#     unique_numbers = list(set(lst))
#     if len(unique_numbers) < 2:
#         return None
#     unique_numbers.sort()
#     return unique_numbers[-2]
# print(second_largest(lst_numbers))


# # 7) Write a Python program that uses `map()` to convert a list of strings to uppercase. Input: `['apple', 'banana', 'cherry']` - Output: `['APPLE', 'BANANA', 'CHERRY']`
# name=['apple', 'banana', 'cherry']
# result = list(map(str.upper, name))
# print(result)


# # 8) Write a Python program that uses `map()` to apply a function that converts a list of temperature values in Celsius to Fahrenheit. Input: `[0, 25, 100]` Output: `[32.0, 77.0, 212.0]`
# input = [0, 25, 100]
# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
# lst = list(map(celsius_to_fahrenheit, input))
# print(lst)


# # 9) Find the total income from sales, considering only items that sold more than 100 units sales_data 
# sales_data = [{"product": "Pen", "price": 10, "units_sold": 150},
#     {"product": "Notebook", "price": 50, "units_sold": 90},
#     {"product": "Pencil", "price": 6, "units_sold": 300}
# ]
# total=0
# for i in sales_data:
#     if i["units_sold"] > 100:
#         total = i["price"] * i["units_sold"]
#         print(f'Total income from sales: {total}')



# "Write a prgram to extract unique values from List in dictionary (With Dict/Set comprehension) 
# input dict_city_list = {
#       'cityList1': ['Ahmedabad','Baroda', 'Bhopal', 'Mumbai'], 
#       'cityList2': ['Baroda', 'Mumbai','Delhi', 'Chochi'], 
#       'cityList3': [""Bhopal"",""Banglore"", ""Pune"", ""Mumbai""], 
#       'cityList4': [""Delhi"",""Ahmedabad"", ""Pune"",""Chochi""]}
# Output {'Banglore', 'Delhi', 'Pune', 'Ahmedabad', 'Mumbai', 'Bhopal', 'Baroda', 'Chochi'}
# "


#     "Filter active adults and get their names in uppercase
#     users = [
#     {""name"": ""Alice"", ""age"": 25, ""active"": True},
#     {""name"": ""Bob"", ""age"": 17, ""active"": False},
#     {""name"": ""Charlie"", ""age"": 35, ""active"": True}
#     ]"


#     "Write a program to create a dictionary having data like {
#     Ahemdabad : ((""Ambawadi"", 380006) ,(""Bodakdev"",380054),(""Gandhi Ashram"",380027)),
#     Mumbai : ((""Mandvi"",400003),(""Mumbai Central"",400008),(""Worli"",400018))
#     } 

#     output If user enters Mumbai : then output is area Mandvi -->400003 , Mumbai Central --> 400008, Worli-->400018
#     if user enter 400018 then output  Worli , Mumbai
#     if user enters Mandvi then output is pin code is 400003 and it's in Mumbai"

# Lambda : 
#     find a list with maximum and minimum length using lambda.
#     Python program to sort a list of tuples using Lambda.
#     Fibonacci series up to n using Lambda
#     Rearrange positive and negative numbers in a given array using Lambda. (Use sorted function)

## 00ps Concepts:

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


###____________________________________________________________________________
## Function :

# -  Write a function that accepts a list of numbers and returns the average of the numbers.
list_numbers = [10, 20, 30, 40, 50]
def cal_average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)     
print(cal_average(list_numbers))     

# - Accept a string from the user and print it in uppercase if the length of the string is greater than 5, else print it in lowercase using a function.
def print_str(s):
    if len(s) > 5:
        print(s.upper())
    else:
        print(s.lower())
print_str("abhijit singh")

# - Write a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3.
def filter_divisible_by_3(lst):
    return [num for num in lst if num % 3 == 0]
print(filter_divisible_by_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


# - Write a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list.
def square_numbers(lst):
    return [num ** 2 for num in lst]
print(square_numbers([1, 2, 3, 4, 5]))

# - Write a function that accepts a string and counts how many vowels are in the string.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
print(count_vowels("Hello World"))

# - Write a function that accepts a list of strings and returns the longest string in the list.
def find_longest_string(lst):
    if not lst:
        return ""
    longest = lst[0]
    for s in lst[1:]:
        if len(s) > len(longest):
            longest = s
    return longest
print(find_longest_string(["apple", "banana", "cherry", "date"]))

# - Write a function that accepts a number and checks if it is an Armstrong number.
def is_armstrong_number(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num
print(is_armstrong_number(153))

# - Write a function that accepts a number and returns the sum of its digits.
def sum_of_digits(num):
    return sum(int(d) for d in str(num))
print(sum_of_digits(12345))

# - Write a function that accepts a string and returns the string in alternating uppercase and lowercase characters.
def alternate_case(s):
    result = []
    for i, char in enumerate(s):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    return ''.join(result)
print(alternate_case("hello world"))

# - Write a function that accepts a list of strings and returns a new list with only the strings that have an odd length.
def filter_odd_length_strings(lst):
    return [s for s in lst if len(s) % 2 == 1]
print(filter_odd_length_strings(["apple", "banana", "cherry", "date"]))

# - Write a function that accepts a string and a substring, and returns True if the substring is found in the string, otherwise False.
def contains_substring(string, substring):
    return substring in string
print(contains_substring("Hello, world!", "world"))

# - Write a function that accepts a list of numbers and returns a new list with all the numbers that are divisible by both 2 and 3.
def filter_divisible_by_2_and_3(lst):
    return [num for num in lst if num % 2 == 0 and num % 3 == 0]
print(filter_divisible_by_2_and_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# - Write a function that accepts a string and returns True if the string is a valid email address (contains "@" and "."), otherwise False.
def is_valid_email(email):
    return "@" in email and "." in email
print(is_valid_email("test@example.com"))

# - Write a function that accepts a list of integers and returns the second largest number in the list.
def find_second_largest(lst):
    if len(lst) < 2:
        return None
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None
print(find_second_largest([1, 2, 3, 4, 5]))

# - Write a function that accepts a list of numbers and returns the average of the numbers, excluding any zero values
def average_excluding_zeros(lst):
    non_zero = [num for num in lst if num != 0]
    return sum(non_zero) / len(non_zero) if non_zero else 0
print(average_excluding_zeros([1, 2, 0, 4, 5]))

# - Write a function that accepts two strings and returns the common characters between them
def common_characters(str1, str2):
    return set(str1) & set(str2)
print(common_characters("apple", "banana"))

# - Write a function count_character(string, char) that accepts a string and a character, and returns the number of times the character appears in the string.
def count_character(string, char):
    return string.count(char)
print(count_character("Hello World", "o"))

# - Write a function concatenate_with_separator(lst, separator) that accepts a list of strings and a separator string, then returns a new string where all elements of the list are joined using the separator.
def concatenate_with_separator(lst, separator):
    return separator.join(lst)
print(concatenate_with_separator(["apple", "banana", "cherry"], ", "))

# - Write a function merge_dicts(dict1, dict2) that accepts two dictionaries and returns a single dictionary that contains the merged key-value pairs from both dictionaries.
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged
print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))

# - Write a function longest_word(sentence) that accepts a sentence and returns the longest word in the sentence.
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len) if words else None
print(longest_word("The quick brown fox jumped over the lazy dog"))

# - Write a function create_frequency_dict(lst) that accepts a list and returns a dictionary where the keys are the elements of the list, and the values are the count of how often each element appears.
def create_frequency_dict(lst):
    freq_dict = {}
    for item in lst:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    return freq_dict
print(create_frequency_dict(["apple", "banana", "apple", "orange", "banana", "apple"]))

# - Write a function merge_lists_into_dict(list1, list2) that accepts two lists of equal length and merges them into a dictionary where the keys are the indices (0 to n-1) and the values are the elements from both lists.
def merge_lists_into_dict(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    return {i: (list1[i], list2[i]) for i in range(len(list1))}
print(merge_lists_into_dict(["a", "b", "c"], [1, 2, 3]))


###_______________________________________________________________________________________________
## map():

# # 1) Write a Python program that uses the `map()` function to square each number in a given list of integers. Input: `[1, 2, 3, 4]` , Output: `[1, 4, 9, 16]`
# lst=[1,2,3,4]
# def square(num):
#     return num**2
# anslst = map(square,lst)
# print(list(anslst))

# # 2) Write a Python program that uses `map()` to convert a list of strings to uppercase. Input: `['apple', 'banana', 'cherry']` - Output: `['APPLE', 'BANANA', 'CHERRY']`
# lst = ['apple', 'banana', 'cherry']
# lst_upper = list(map(str.upper, lst))
# print(lst_upper)

# # 3) Write a Python program that uses `map()` to find the length of each string in a list of strings. Input: `['hello', 'world', 'python']` Output: `[5, 5, 6]`
# lst = ['hello', 'world', 'python']
# length = list (map(len, lst))
# print(length)

# # Write a Python program that uses `map()` to add a given number to each element in a list. - Input: `[1, 2, 3, 4]`, `5` Output: `[6, 7, 8, 9]`
# lst = [1, 2, 3, 4]
# def add_num(num):
#     return num + 5
# anslst = map(add_num,lst)
# print(list(anslst))

# # Write a Python program that uses `map()` to apply a function that converts a list of temperature values in Celsius to Fahrenheit. Input: `[0, 25, 100]` Output: `[32.0, 77.0, 212.0]`
# def cel_fah(i):
#     ans = (i * 9/5)+32
#     return ans
# list_ans = [0,25,100]
# lst = list(map(cel_fah,list_ans))
# print(lst)
