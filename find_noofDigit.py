num = int(input("Enter no "))
count=0
while num!=0:
    rem = num % 10
    num = num//10
    count+=1
    print(f"Num = {num} Rem = {rem}")

print(f"NO of digit {count}")
