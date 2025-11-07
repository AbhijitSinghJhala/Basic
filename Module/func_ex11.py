# lst=[1,2,3]
# def square_list():
#     list1=[]
#     for i in lst:
#         list1.append(i**2)
#     return list1
# print(square_list())

#____________________________________________________

def square(num):
    return num**num
lst=[1,2,3]
anslst=[]
anslst = map(square,lst)
print(list(anslst))
