# Square of even numbers from list
lst_number = [1,2,4,6,7,9]
ans_lst = [4,16,36]

# first Filter - even - list 
# map square filter list 

def checkEven(num):
    if num%2==0:
        return num
def square(num):
    return num*num
lst_even=list(filter(checkEven,lst_number))
print(lst_even)

lst_ans=list(map(square,lst_even))
print(f"Square of even numbers {lst_ans}")

lst_ans1=list(map(square,list(filter(checkEven,lst_number))))
print(f"Square of even numbers {lst_ans1}")
