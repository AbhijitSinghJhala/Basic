# lst=[1,2,3]
# def square_list():
#     list1=[]
#     for i in lst:
#         list1.append(i**2)
#     return list1
# print(square_list())

#____________________________________________________

# def square(num):
#     return num**num
# lst=[1,2,3]
# anslst=[]
# anslst = map(square,lst)
# print(list(anslst))

#____________________________________________________

# lst = {1,22,3,56,89,12,45,67}
# anslst=[]
# def square(num):
#     return num**2
# #for i in lst:
# #    anslst.append(square(i))
# #print(anslst)
# anslst = set(map(square,{23,5,6,7}))
# print(anslst)

#________________________________________________________
# length find , upper case

# city = ['bangalore', 'mysore', 'mangalore', 'hubli']
# # length = list (map(len, city))
# # print(length)
# length = list(map(str.upper, city))
# print(length)

#________________________________________________________

# city = ['bangalore', 'mysore', 'mangalore', 'hubli']
# def length(city):
#     if len(city)>7:
#         return len(city)
# len_city = list(filter(length, city))
# # print(list(len_city))

# upper_lst = list(map(str.upper,len_city))
# print(upper_lst)
#______________________________________________________
# square of even number from list

# lst_num = [1,2,4,6,7,9]
# def even_num(num):
#     if num%2==0:
#         return num
# def square(num):
#     return num**2

# even = list(filter(even_num,lst_num))
# print(even)
# square_lst = list(map(square,even))
# print(square_lst)

#_____________________________________________________________

# celsius to fahrenite

def cel_fah(i):
    ans = (i * 9/5)+32
    return ans
list_ans = [0,23,22,7,11]
lst = list(map(cel_fah,list_ans))
print(lst)