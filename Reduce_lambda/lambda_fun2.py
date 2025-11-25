ans = lambda num:"Even" if num%2==0 else "Odd"
print(ans(21))

lst_num=[3,4,5,6,12,22]
ans1=list(map(lambda num:"Even" if num%2==0 else "Odd",lst_num))
print(ans1)
