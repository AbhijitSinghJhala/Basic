# 5) Write a Python program to get the Factorial number of given numbers. 
# Ans:-
#   Factorial of a number n means multiplying all numbers from 1 to n.
#   Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

# Here’s a simple Python program to find the factorial of a number:

# Program to find factorial of a given number

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)
