import random
num=random.randint(1,30)

while True:
    guess=int(input("Guess number Between 1-30: "))
    if guess == num:
        print("You Guessed the Correct No")
        break
    elif guess>num:
        print("You Guessed the Greater No")
    elif guess<num:
        print("You Guessed the Smaller No")
