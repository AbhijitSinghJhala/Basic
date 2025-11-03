# Paramerized function 
def greet(name,grade,age):
    print("Good Morning ",name,"You have ",grade," and age is ",age)
    
for i in range(3):
    n=input("Enter name ")
    g=input("Enter grade ")
    a=int(input("Enter age "))
    greet(n,g,a)