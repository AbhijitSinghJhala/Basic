#stirp
#sort
name = "  Tops Technologies"
print(len(name))
name=name.strip()
print(len(name))

print(sorted(name))

#words to be sorted from sentence 
sentense = "This is Tuesday "
lst = sentense.split()
sort_lst=sorted(lst)
print(f"Original list {lst} and sorted list {sort_lst}")

sort_lst_len=sorted(lst,key=len)
print(f"Original list {lst} and sorted list {sort_lst_len}")

###______________________________________________________

# # print the string in which the first and last character is exchanged
# str1 = input("Enter your name: ")
# modified_str = str1[-1] + str1[1:-1] + str1[0]
# print(f"Modified string: {modified_str}")

###______________________________________________________

# Example of sorted() function
str1 = " Tops Technologies "
print(f"original string: '{str1}'")
print(f"sorted characters: {sorted(str1)}")
print(f" Joined sorted string: '{' '.join(sorted(str1.split()))}'")

###______________________________________________________

#Example of sorted() funtion through length of string
str1 = input("Enter your name: ")
print(f"original string: '{str1}'")
len_str = sorted(str1.split(), key=len)
print(f"sorted characters by length: {len_str}")

###______________________________________________________

#example of sorted() function through length of string in reverse order
str1 = input("Enter your name: ")
print(f"original string: '{str1}'")
len_str = sorted(str1.split(), key=len, reverse=True)
print(f"sorted characters by length in reverse order: {len_str}")