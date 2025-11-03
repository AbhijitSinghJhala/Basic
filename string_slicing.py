# name = "Tops technologies"
# print(name[0:4])  # 0 to 3
# print(name[5:])   # 5 to end


###______________________________________________________

# name= "Tops Technologies"
# # 0-5 letter
# print(name[0:5]) # 5 letter
# # 4 to 10 
# print(name[4:10]) # 6 letter

# # upto 10 letter
# print(f"Upto 10 letter {name[:10]}")
# # from 5th letter to end
# print(f"From 5th Letter to end {name[5:]}")

# # alternate letter 
# print(f"printing alternate letter from string {name[::2]}")

# # from letter 5th to alternate of whole string
# print(f"From 5th letter to end alternate letter {name[5::2]}")

# print(name[10::1])

####______________________________________________________

# print the last half string and other half
str1 = input("Enter your name: ")
length = len(str1)
half = length // 2


####______________________________________________________

#Example for join method
word_list = ['This', 'is', 'Python']
joined_string = ' '.join(word_list)
print(f"list of words: {word_list}")
print(f"joined string: {joined_string}")

###______________________________________________________   

# Example of strip method
str1 = "   Tops Technologies   "
print(f"original string: '{str1}'")
print(f"string after strip: '{str1.strip()}'")

