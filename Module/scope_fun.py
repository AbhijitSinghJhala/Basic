num = 10
num1=10
def printNum():
    global num
    num = 5
    num1=5
    print(f"{num}-{num1}")
num=15
num1 = 15
print(f"outside function{num}-{num1}")
printNum()
print(f"after calling function{num}-{num1}")