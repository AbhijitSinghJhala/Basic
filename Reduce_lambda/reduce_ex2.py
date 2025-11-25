from functools import reduce

def add(num1,num2):
    return num1+num2

data=[{"name":"eee","age":23},{"name":"tttt","age":22},
{"name":"ddfdf","age":22}]

lst_ages=[]
for i in data:
    lst_ages.append(i["age"])

print(lst_ages)
ans=reduce(add,lst_ages)
print(ans/len(lst_ages))

