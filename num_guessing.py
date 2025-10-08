import random
number=random.randint(100,110)
while True:
    guess_number=int(input("Please Guess number "))
    if guess_number==number:
        print("Congratulations you have guessed correct number")
        break