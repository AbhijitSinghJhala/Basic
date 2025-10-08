# lst= ['abhijit','singh','jhala','rajasthan']
# lst1=len(lst)
# for i in range(lst1):
#     print(f"Uppercase: {lst[i].upper()}")

##_________________________________________________
#find length of each string in list

# lst= ['abhijit','singh','jhala','rajasthan']
# lst1=len(lst)
# for i in range(lst1):
#     print(len(lst[i]))

##_________________________________________________
#find largest string in list

# lst= ['abhijit','singh','jhala','rajasthan']
# lst1=len(lst)
# largest=0
# for i in range(lst1):
#     if len(lst[i])>largest:
#         largest=len(lst[i])
#         largest_str=lst[i]
# print(f"Largest string is: {largest_str} and length is: {largest}")

###_________________________________________________
#reverse a list

lst_name=['Roumil','Abhijit','Dhruti']

#print(lst_name)
#want ot access items from index position
total_name=len(lst_name)
# for i in range(total_name):
#     print(lst_name[i])

# #-ve indexing
# print(lst_name[-2])


for i in range(total_name-1,-1,-1):
    print(lst_name[i])
