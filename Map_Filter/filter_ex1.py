def checkEven(num):
    if num%2==0:
        return num
lst_numbers=[1,33,21,55,67,81]
lst_even_numbers=list(filter(checkEven,lst_numbers))
print(lst_even_numbers)
