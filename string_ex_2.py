# c_name = "tops technologies"
# i=c_name.find("s t")
# print(i)
# i=c_name.find("s" , 4,10)
# print("After 4th position ",i)

# #find function is return the position of sub string

# print(len(c_name))

# c=c_name.count("tops technologies")
# print(c)

###________________________________________________

# sentence = "cat is animal and dog is animal"
# c=sentence.count("animal")
# print("count animal is :",c)

###______________________________________________________

# # String indexing with Positive indexing

# str1 = "Abhijit singh"
# print(str1[0]) # print A
# print(str1[1]) # print b
# print(str1[2]) # h
# print(str1[3]) # i
# print(str1[4]) # j
# print(str1[5]) # i
# print(str1[6]) # t
# print(str1[7]) #
# print(str1[8]) # s
# print(str1[9]) # i
# print(str1[10]) # n
# print(str1[11]) # g
# print(str1[12]) # h

###______________________________________________________

# # Negative indexing

# str1 = "Abhijit"
# print(str1[-1])
# print(str1[-2])
# print(str1[-3])
# print(str1[-4])
# print(str1[-5])
# print(str1[-6])
# print(str1[-7])


###______________________________________________________

## Accessing string through indexing

# # Check vowels  in a given string 

# str1 = input("Enter string: ")
# vowels = "aeiouAEIOU"
# count = 0 
# for i in range(len(str1)):
#     if str1[i] in vowels:
#         count += 1
# print("Vowels in a given string is :",count)  

###______________________________________________________

str = "This is Python class"
print(str[-4])
print(len(str))

name=input("Enter name ")
for i in name:
    print(i)

#accessing thru index
for i in range(len(name)):
    print(f"{i} ---> {name[i]}")
