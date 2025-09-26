# str1 = "Tops"
# str2 = "12345"
# str3 = "Tops@123"
# str4 = " Tops tech "

# str1.isdigit()
# # print("str1 is digit:", str1.isdigit())
# print(f" {str1 :} str1 is digit: {str1.isdigit()}, str1 is alpha: {str1.isalpha()}, str1 is alnum: {str1.isalnum()}")
# print(f" {str2 :} str2 is digit: {str2.isdigit()}, str2 is alpha: {str2.isalpha()}, str2 is alnum: {str2.isalnum()}")
# print(f" {str3 :} str3 is digit: {str3.isdigit()}, str3 is alpha: {str3.isalpha()}, str3 is alnum: {str3.isalnum()}")
# print(f" {str4 :} str4 is digit: {str4.isdigit()}, str4 is alpha: {str4.isalpha()}, str4 is alnum: {str4.isalnum()}")

###______________________________________________________

# string = input("Enter name:")
# print(string.isdigit(),string.isalpha(),string.isalnum())


###_______________________________________________________

# write a python program to check weather the given email is valid or not.

# email = input("Enter email:")
# if "@" i email and "." in email:
#     print(f"{email} is a Valid email")
# else:
#     print(f"{email} is an Invalid email")

##______________________________________________________

# email = input("Enter email:")
# if email.endswith(".com") or email .endswith(".in"):
#     print("Valid email")
# else:
#     print("Invalid email")

##______________________________________________________

# email = input("Enter email:")
# if email.endswith(".com"):
#     print(f"{email} is a Valid email")
# else:
#     print(f"{email} is an Invalid email")
 
###______________________________________________________

# email = "abhijit@gmail.com"
# if email.endswith("gmail.com"):
#     print(f"{email} is a Valid email")
# else:
#     print(f"{email} is an Invalid email")

####________________________________________________________

msg="Have a good day!!!"
print(msg.endswith("test"))
email = input("Enter email id ")
ans=email.endswith(".com")
#if email.endswith(".com"):
if ans:    
    print(f"{email} is valid email address")
else:
    print(f"{email} is invalid email address")