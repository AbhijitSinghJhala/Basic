# short way / readable way/consice way

lst_number=[1,2,9]
# lst_new_number=[]
# # copy into another list 
# for i in lst_number:
#     lst_new_number.append(i)
# print(lst_new_number)
lst_new_numbers = [i**5 for i in lst_number]
print(lst_new_numbers)

#want to convert all string into upper case 
lst_city=['baroda','surat','ahmedabad']
lst_upper_city=[i.upper() for i in lst_city if len(i)>5]
print(lst_upper_city)

lst_num = [1,2,3]
#output = [(1,1,1),(2,4,8),(3,9,27)]
lst_num_ans = [(i,i**2,i**3) for i in lst_num]
print(lst_num_ans)

lst_num_sq=(i*i for i in lst_num)
print(list(lst_num_sq))

###________________________________________________

# lst1=[1,23,34,56]
# lst2 = [i for i in lst1]
# print(lst2)
# #square each element 
# lst2 = [i**2 for i in lst1]
# print(lst2)

##_________________________________________________

# lst = [2,4,6,12,15,11,18]
# lst1 = tuple(i**2 for i in lst if i % 2==0)
# print(lst1)

###_________________________________________________

