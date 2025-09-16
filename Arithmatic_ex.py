# Example of all arithmatic operator
number1 = 120
number2 = 110
number1 = int(input("Enter number 1 "))
number2 = int(input("Enter number 2 "))
Ans = number1 + number2
#print("Addition is ", ans)

print("Addition is ", number1 + number2)
print("addition of ", number1, "and", number2, "is", number1 + number2)
print("Addition of {} and {} is {}" .format(number1,number2,number1+number2))

print("substraction is ", number1-number2)
print(f"substraction of {number1} and {number2} is {number1-number2}")
print("Multiplication is ", number1*number2)
# '/' gives float value
print("Division is",number1/number2)
# '//' gives int value
print("Floor division",number1//number2)
print("Modules",number1%number2)
print("Exponent", number1**number2)