# Menu driven program with functions like convert to uppercase, lowercase, find lenth, replace and exit using match case.
# while True:

#     print(" \n1. Convert into Uppercase  \n2. Convert into Lowercase  \n3. Find length  \n4. Replace  \n5. Exit ")
#     choice = int(input("Please enter your choice : "))
#     match choice:
#         case 1:
#             string=input("Pelase enter string that want to convert in upper")
#             print(f"Converted string is {string.upper()}")
#         case 2: 
#             string=input("Pelase enter string that want to convert in lower")
#             print(f"Converted string is {string.lower()}")
#         case 3:
#             string=input("Pelase enter string , find length ")
#             print(f"Converted string is {len(string)}")
#         case 4:
#             string=input("Pelase enter string ")
#             old_str=input("Pelase enter string that you want to replace ")
#             new_str=input("Please enter new string that you want to replace ")
#             print(f"After replace {string.replace(old_str,new_str)}")
#         case 5:
#             break
#         case _:
#             print("Enter valid choice ")

###_________________________________________________________________

# while True:

#     print("convert into uppercase")
#     print("convert into lowercase")
#     print("find length of string")
#     print("replace substring")
#     print("exit")
#     choice = int(input("Enter your choice : "))
#     match choice:
#         case 1:
#             str = input("Enter a string: ")  
#             print(f"Uppercase: {str.upper()}")
#         case 2:
#             str = input("Enter a string: ")
#             print(f"Lowercase: {str.lower()}")      
#         case 3:
#             str = input("Enter a string: ")     
#             print(f"Length of string: {len(str)}")  
#         case 4:
#             str = input("Enter a string: ")  
#             old = input("Enter substring to be replaced: ")     
#             new = input("Enter new substring: ")
#             print(f"Replaced string: {str.replace(old, new)}")
#         case 5:
#             print("Exiting...")       
#             break
#         case _:
#             print("Invalid choice, please try again.")

###_________________________________________________
while True:
    print("Reverse of Number")
    print("Find no of digits")
    print("Count total even/odd digits from number")
    print("check number is palindrom")
    print("exit")
    choice = int(input("Enter your choice (1-5) : "))
    match choice:
        case 1:
            num = int(input("Enter a number: "))
            reversed_num = 0
            temp = num
            while temp > 0:
                digit = temp % 10
                reversed_num = reversed_num * 10 + digit
                temp //= 10
            print(f"Reversed number: {reversed_num}")
        case 2:
            num = int(input("Enter a number: "))
            count = 0
            temp = num
            while temp > 0:
                count += 1
                temp //= 10    
            print(f"Number of digits: {count}")
        case 3:
            start = int(input("Enter a number: "))
            end = int(input("Enter another number: "))
            print(f"Even and odd digits counts between {start} and {end}:")
            even_count = 0
            odd_count = 0
            for num in range(start, end + 1):
                if num % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            print(f"Even digits count: {even_count}")
            print(f"Odd digits count: {odd_count}")
        case 4:
            num = int(input("Enter a number: "))
            temp = num
            reversed_num = 0
            while temp > 0:
                digit = temp % 10
                reversed_num = reversed_num * 10 + digit
                temp //= 10
            if num == reversed_num:
                print(f"{num} is a palindrome.")
            else:
                print(f"{num} is not a palindrome.")
        case 5:
            print("Exiting...")       
            break
        case _:
            print("Invalid choice, please try again.")