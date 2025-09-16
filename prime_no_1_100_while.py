temp = 0
i=1
while i<=100:
    j=2
    while j<i:
        if i%j==0:
            temp=1
            break
        else:
            temp=0
        j+=1
    if temp==1:
        print(i,"No is not prime ")
    else:
        print(i,"No is prime ")
    i+=1





# temp=0
# for i in range(1,101):
#     for j in range(2,i):
#         if i%j==0:
#             #print(f"{num} is not prime number")
#             temp=1
#             break
#         else:
#             #print(f"{num} is prime number")
#             temp=0

#     if temp==0:
#         print(f"{i} is prime number")
#     # else:
#     #       print(f"{i} is prime number")