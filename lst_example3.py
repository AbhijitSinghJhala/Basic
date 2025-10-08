lst=['ahmedbad',345,567,345,345,67567,34234]
print(lst.count('test'))
print(lst.index(345,2))
lst.insert(2,'Saturday')
print(lst)

# lst1=[23,34,54,23,45,56,89,23,56,23]
# print(lst1.index(23,4,8))

# print("Before pop ",lst)
# lst.pop()
# lst.pop()
# lst.pop()
# lst.pop(2)

# print("After pop ",lst)
print(f"before remove ",lst)
lst.remove(345)
print(f"after remove ",lst)
lst.reverse()
print(f"Reverse  ",lst)
lst1=[12,4,6,120,78,456]
# lst1=['ahmedbabd','ajmer','Jaipur']
lst1.sort(reverse=True)
print(f"Sort  ",lst1)