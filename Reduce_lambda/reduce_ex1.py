# # find age_average from dictionary
# data = {{"name":"Abhi","age":21},{"name":"jeet","age": 22},{"name":"abhijit",'age':20}}
# def avg_age(num1,num2):
#     return num1+num2
# def get_avg(num):
#     return num['age']
# age = list(map(get_avg,data))
# print(age)
# ave = reduce(add,age)/len(age)
# print(ave)


###________________________________________________

def add(num1,num2):
    return num1+num2
def mul(num1,num2):
    return num1*num2
from functools import reduce

lst_number=[1,67,89,34]
ans=reduce(add,lst_number)
print(ans)
ans1=reduce(mul,lst_number)
print(f"Multilication {ans1}")

#find age_average from dictionary 
# data={{name:"eee",age:23},{name:"tttt",age:22},
# {name:"ddfdf",age:22}}


# 1+22
# 23+12
 