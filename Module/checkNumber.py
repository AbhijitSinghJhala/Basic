def check_even(num):
    if num % 2==0:
        print("even")
    else:
        print("odd")

def check_pos_neg(num):
    if num>0:
        print("positive")
    else:
        print("negative")

def isprime(num):
    for i in range(2,num):
        if num%i==0:
             return False
    return True

