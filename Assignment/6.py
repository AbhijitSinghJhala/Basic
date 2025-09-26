# 6) Write a Python program to get the Fibonacci series of given range.

# Fibonacci series is a sequence where:
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# Each number after the first two is the sum of the previous two numbers.
 

# Python Program for Fibonacci Series (using loop)

n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci series up to", n, "term:")
    print(a)
else:
    print("Fibonacci series:")
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1
