# def greet(name,grade,age):
#     print("good morning",name,"you have",grade, "and age is ",age)
# for i in range(3):
#     name=input("name: ")
#     grade=input("grade: ")
#     age=input("age: ")
#     print()
#     greet(name ,grade, age)

#________________________________________________
# def check_number(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
# # number=int(input("enter number: ")) 
# # result=check_number(number)
# # print(f"The number {number} is {result}")
# ans=check_number(7)
# print(ans)

#___________________________________-

# # create function which accept a number and return "Prime" or "Not Prime"
# def check_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 return "Not Prime"
#         return "Prime"
#     else:
#         return "Not Prime"
# number = int(input("Enter number: "))
# result = check_prime(number)
# print(f"The number {number} is {result}")
# # for i in range(1, 21):
# #     print(f"{i} - {check_prime(i)}")

#___________________________________

# create function to check string is palindrome or not

def palindrome(s):
    if s == s[::-1]:
        print(f'"{s}" is a palindrome.')
    else:
       print(f'"{s}" is not a palindrome.')
s = input("Enter a string: ")
print(palindrome(s))
# for i in range(5):
#     str_input = input("Enter a string: ")
#     palindrome(str_input)
