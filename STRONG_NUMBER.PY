#STRONG NUMBER 
#What is a Strong Number?
'''
A Strong Number is a number such that the sum of the 
factorials of its digits equals the number itself.
EXAMPLE : (145) 1 * 4 * 5
'''
num = int(input("Enter the Number: ")) #145
temp = num
total = 0

while num > 0:
    rem = num % 10
    fact = 1
    for i in range(1, rem + 1):
        fact *= i
    total += fact
    num //= 10  # integer division to drop last digit

if total == temp:
    print(f"{temp} is a Strong Number.")
else:
    print(f"{temp} is NOT a Strong Number.")
