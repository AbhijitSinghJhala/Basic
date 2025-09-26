# c_name= "Tops Technologies"
# s= c_name.upper()
# print(s)

# ###

# s2= c_name.lower()
# print(s2)

# ##

# s3= c_name.title()
# print("Title ",s3)

# ##

# s4= c_name.capitalize() 
# print("Capitalize ",s4)

#_____________________________________________________________________

#ex.

# c_name = "tops tachnologies"
# print(c_name.upper())
# print(c_name.lower())
# print(c_name.title())
# print(c_name.capitalize())

#______________________________________________________________

# string =   "abhi jeet"
# print(f"original string: '{string}'")
# print(f"lenth of string: '{len(string)}'")
# print(f"lowercase: '{string.lower()}'")
# print(f"uppercase: '{string.upper()}'")
# print(f"Title case: '{string.title()}'")
# print(f"capitalized: '{string.capitalize()}'")
# print(f"stripped: '{string.strip()}'")

#___________________________________________________________

#accept 5 string user and perform all 4 operations/methods on each string

# for i in range(5):
#     user_input = input(f"Enter string {i+1}: ")
#     print(user_input.upper())
#     print(user_input.lower())
#     print(user_input.title())
#     print(user_input.capitalize())

#_______________________________________________________

num = int(input("Enter number "))
i=1
while i<=num:
    user_input = input("Enter the string :")
    print(user_input.upper())
    print(user_input.lower())           
    print(user_input.title())
    print(user_input.capitalize())
    i+=1 
