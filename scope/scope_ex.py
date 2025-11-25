num=10
num1=10
def printNum():
    global num 
    num=200
    num1=200
    print(f"{num} - {num1}")

num=300
num1=300
print(f"Outside function {num} - {num1}")
printNum()
print(f"After calling function Outside function {num} - {num1}")