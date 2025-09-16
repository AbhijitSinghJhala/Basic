num = int(input("Enter number "))
prev= 0
next=1
sum=0
for i in range(num):
    if i==0:
        sum = 0        
        #sum=prev+next
    else:
        prev=next
        next=sum
        sum=prev+next
    print(sum,sep="\t")