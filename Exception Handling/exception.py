no=int(input("Enter num "))
print(no)
ans=no/2

#ans=no/0

print(f"After division {ans}")
dic1={"name":"Abhijit","age":30}
print(f"Dictionary value {dic1['name']}")
with open('abhi',"r") as file:
    data =file.read()


##____________________________________________________________________

try:
    no=input("enter a num: ")
    no1 = int(no)
    print(f"value is {no1}")
     
    ans=no1/0
    print(f"Ans {ans}")
except:
    print("There is an error ")


##____________________________________________________________________

try:
    no=input("enter num ")
    no1=int(no)
    print(f"value is {no1}")

    ans=no1/2

    print(f"Ans {ans}")
except ZeroDivisionError:
    print("There is an ZeroDivisionError ")
except ValueError:
    print("There is ValueError")
finally:
    print("have a greate day !1")


##____________________________________________________________________

import traceback
try:
    no=input("enter num ")
    no1=int(no)
    print(f"value is {no1}")
    ans=no1/0
    print(f"Ans  {ans}")
except ZeroDivisionError:
    #print("There is an ZeroDivisionError ")  
    traceback.print_exc()
except ValueError:
    print("There is ValueError")
finally:
    print("have a greate day !")


##____________________________________________________________________

import traceback
try:
    no=int(input("enter num "))
    print(f"here is no {no}")
except:
    traceback.print_exc()
else:
    print("In Else ")
finally:
    print("In Finally ")

##____________________________________________________________________

import traceback
class lengthException(Exception):
    pass
try:
    name=input("enter name ")
    # if len(name)<5:
    #     raise lengthException("Address is too short ")
    if len(name)>20:
        raise lengthException("Name must be upto 20 character long")
    
    address=input("enter address ")
    if len(address)<5:
        raise lengthException("Address is too short ")
    
    age=int(input("enter age "))
    if age<18:
        raise ValueError("Age must be > 18 ")

except lengthException as e:
    print(f"Length Exception {e}")
    traceback.print_exc()
except ValueError as ve:
    print(f"{ve}")

