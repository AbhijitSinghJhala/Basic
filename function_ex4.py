#function with return 
def checkNumber(num):
    if num%2==0:
        return "EVEN"
    else:
        return "ODD"

ans=checkNumber(23)
print(ans)
ans=checkNumber(922222)
print(ans)
for i in range(100):
    print(f"{i} - {checkNumber(i)}")