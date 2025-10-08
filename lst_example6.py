lst_names = ['test','piuyuy','xxcxc']
lst_upper_names=[]
for i in lst_names:
    lst_upper_names.append(i.upper())

print(lst_upper_names)
lst_final_list= lst_upper_names+lst_names
print(lst_final_list)
lst_names[2]='Dharmishtha'
print(lst_names)