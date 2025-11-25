# def greet(name,grade,age):
#     print("good morning",name,"you have",grade, "and age is ",age)
# for i in range(3):
#     name=input("name: ")
#     grade=input("grade: ")
#     age=input("age: ")
#     print()
#     greet(name ,grade, age)

#___________________________________
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

#___________________________________

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


##_____________________________________________________________________________

def f1():
    print("Good Morning Vishwarj ")
def close():
    print("Bye..")
    print("This is example of function ")
f1()

close()
close()


##_____________________________________________________________________________

# Paramerized function 
def greet(name,grade,age):
    print("Good Morning ",name,"You have ",grade," and age is ",age)
    

greet("vishwaraj","Grade A",23)
greet("Romil","Grade A+",23)
#loop , input 


##_____________________________________________________________________________

# Paramerized function 
def greet(name,grade,age):
    print("Good Morning ",name,"You have ",grade," and age is ",age)
    
for i in range(3):
    n=input("Enter name ")
    g=input("Enter grade ")
    a=int(input("Enter age "))
    greet(n,g,a)


##_____________________________________________________________________________

#function with return 
def checkNumber(num):
    if num%2==0:
        return "EVEN"
    else:
        return "ODD"

ans=checkNumber(23)
print(ans)
ans=checkNumber(922222)
print(ans)
for i in range(100):
    print(f"{i} - {checkNumber(i)}")


##_____________________________________________________________________________

def greet(name,age=20):
    print("Good Morning ",name,age)

greet("Dharmishtha",30)
greet("Vishwraj")
greet("Dhruv")
greet("Abhijit",22)


##_____________________________________________________________________________

def greet(name,msg):
    print(name,msg)
greet("Good morning","Dharmishtha")
greet(msg="Good morning",name="Dharmishtha") 


##_____________________________________________________________________________

def personDetails(*abhi):
    print(abhi)
    # print(len(abhi))
    # for i in abhi:
        # print(i)

print("Person1 ")
personDetails(101,"Dharmishtha",30)
print("Person2 ")
personDetails(201,"Abhijit","BTech","Ahemedabad")
print("Person 3 ")
personDetails("Dhruv","BTech","dhruv@gmail.com",1213134)
    

##_____________________________________________________________________________

def addition(*args):
    sum=0
    for i in args:
        if type(i)==int:
            sum+=i
    return sum
ans=addition(12,23)
print(ans)
print(addition(23,657,5656))
print(addition(23,345,567567,13123,34.5656))
print(addition(23,345,"anshu",567567,13123))

#_________________________________


# # def addition(*args):
# #     return sum(args)

def addition(*args):
    sum=0 
    for i in args:
        if type(i)== int:
            sum+=i
        print(sum)
        

print(addition(12,23))
print(addition(23,657,5656))
print(addition(23,345,5656,6789,"oooo"))


##______________________________________________________________________________

def personDetails(**kwargs):
    #print(kwargs)
    if kwargs['age']>=30:
        # print(kwargs['name'])
        print(kwargs)
def details():
    return 1,"Dharmishtha",30,"Python"
personDetails(name="Dharmishtha",age=30)
personDetails(city="Ahedmbad",name="Dhruv",age=20)
personDetails(name="Abhijit",age=22)
personDetails(name="etets",age=30)
print(details())

# #________________________________
# def persondetails(**kwargs):
#     if kwargs['age']>=55:
#         print(kwargs)
# persondetails(name="mahendra",age=60)
# persondetails(name="Abhijit",age=45)
# persondetails(name="piyush",city="neemuch",age=70)
# persondetails(name="anshu",age=30)
