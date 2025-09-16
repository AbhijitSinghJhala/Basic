#---------------lab task
number= int(input("Enter no: "))
digit=0
count_even = 0
count_odd = 0
for i in number:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
print(f"Even no = {count_even} and Odd no = {count_odd}") # error...................