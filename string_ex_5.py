name= "Tops technologies pvt ltd"
#spilt
#join
lst=name.split()
print(lst)
lst1=name.split("t")
print(f"Split by t {lst1}")
sentence= " This is my Python class and it will complete by 10"
print(len(sentence))
# Counting number of words from string
lst2=sentence.split()
print(f"no of words === {len(lst2)}")

lst3=['Apple',"banana","Cherry"]
fruits = " ".join(lst3)
print(fruits)
fruits = "*".join(lst3)
print(fruits)