# 4)	Write a Python program to check if a number is positive, negative or zero. 
# Ans:-
#   A Python program to check if a number is positive, negative, or zero can be implemented 
#   using conditional statements. The program will prompt the user for input, convert it to 
#   a numerical type, and then evaluate its value.

# Prompt the user to input a number
try:
    num = float(input("Enter a number: "))

    # Check if the number is positive, negative, or zero
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:  # This condition implies num == 0
        print("The number is zero.")

except ValueError:
    print("Invalid input. Please enter a valid number.")


