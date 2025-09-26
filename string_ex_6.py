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

