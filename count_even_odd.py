start = int(input("Etner start number "))
end = int(input("Enter end number "))
count_even = 0
count_odd = 0
for i in range(start,end):
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1
# total_num=count_even+count_odd
# print(f" Total numbers {total_num} ::: Even no  = {count_even} and odd no = {count_odd}")

print(f" Even no  = {count_even} and odd no = {count_odd}")
