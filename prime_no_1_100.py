temp =1
for i in range(1,101):
    for j in range(2,i):
        if i%j==0:
            #print(f"{num} is not prime number")
            temp=1
            break
        else:
            #print(f"{num} is prime number")
            temp=0

    if temp==1:
        print(f"{i} is not prime number") 
    #else:
    #     print(f"{i} is prime number")
     