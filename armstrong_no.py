# # Armstrong Number Check

# num = int(input("Enter a number: "))

# # Count digits
# n = len(str(num))

# # Calculate sum of powers of digits
# sum_of_powers = sum(int(digit) ** n for digit in str(num))

# # Check condition
# if sum_of_powers == num:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")




###
#simple and self--->


#Armstrong number
num = int(input("Enter the number: "))
digit = 0
sum = 0
rem = 0
temp = num
copy = num

# count digits
while num !=0:
    num = num//10     #integer division
    digit +=1

# Armstrong check
while temp != 0:
    rem = temp % 10 #145
    sum += rem ** digit
    temp //= 10

if sum == copy:
    print(copy, "is an Armstrong number")
else:
    print(copy, "is Not an Armstrong number") 
    