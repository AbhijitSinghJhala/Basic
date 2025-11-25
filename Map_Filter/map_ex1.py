lst={1,22,3,56,89,12,45,67}
anslst=[]
def square(num):
    return num*num
# for i in lst:
#     anslst.append(square(i))

# print(anslst)
anslst=set(map(square,{23,5,6,7}))
print(anslst)