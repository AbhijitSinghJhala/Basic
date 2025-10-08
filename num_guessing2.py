import random
number=random.randint(1,100)
while True:
    guess_number=int(input("Please Guess number "))
    if number>guess_number:
        print("Please enter high number ")
    elif number<guess_number:
        print("Please enter lower number ")
    else:
        print("Congratulations you have guessed correct number")
        break
    