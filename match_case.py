# print("\n1. Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Floor Division") 
# ch=int(input("Enter your choice "))
# number1=int(input("Enter number "))
# number2=int(input("Enter number "))
# match ch:
#     case 1:print(f"Addition is {number1+number2}")
#     case 2:print(f"subtraction is {number1-number2}")
#     case 3:print(f"multiplication is {number1*number2}")
#     case 4:print(f"Division is {number1/number2}")
#     case 5:print(f"Floor Division is {number1//number2}")
#     case _:print("INvalid choice ")

###----------------------.>


print("\n1. Addition : +  \n2. Subtraction : - \n3. Multiplication : * \n4. Division : / \n5. Floor-Division : //") 
number1=int(input("Enter number1 "))
number2=int(input("Enter number2 "))
ch=(input("Enter your choice "))
match ch:
    case "+":print(f"Addition is {number1+number2}")
    case "-":print(f"subtraction is {number1-number2}")
    case "*":print(f"multiplication is {number1*number2}")
    case "/":print(f"Division is {number1/number2}")
    case "//":print(f"Floor Division is {number1//number2}")
    case _:print("INvalid choice ")