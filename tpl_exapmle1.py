# tpl_number=(11,45,67,89)
# print(tpl_number)
# tpl_no1 = 11,
# print(type(tpl_no1))
# lst_names=('ronil','abhijit')
# print(type(lst_names))

# print(f" {lst_names} {lst_names.count('ronil')} {lst_names.index('ronil')}")

###_________________________________________________

#create a new tuple with even numbers, their squares and cubes but sum of the middle values is in new variable

# lst = [2,4,6,12,15,11,18]
# tpl_new = tuple((i,i**2,i**3) for i in lst if i % 2==0)
# print(tpl_new)
# sum_of_squares = sum(i**2 for i in lst if i % 2==0) 
# print("sum_of_squares", sum_of_squares)

###_________________________________________________

lst = [32,46,25,35,15,32,11,18]
sum = 0
for i in lst:
    if i % 2 == 0:
        square = i**2
        cube = i**3
        sum = sum + square
        print((i,square,cube))
print("sum_of_squares", sum)
