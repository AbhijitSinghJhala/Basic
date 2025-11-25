# add 2 list elements using map
def add(num1,num2):
    return num1+num2
lst_num1=[2,3,4,5]
lst_num2=[3,9,0]
lst_ans=list(map(add,lst_num1,lst_num2))
print(lst_ans)