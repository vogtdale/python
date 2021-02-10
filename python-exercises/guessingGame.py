import random

number_to_guess = random.randint(1,100)
guess = 0
count = 0

while guess != number_to_guess and guess != "exit":
    guess = int(input("Guess what number? "))

    if guess == "exit":
        break

    count = count + 1

    if guess < number_to_guess:
        print("Too low")
    elif guess > number_to_guess:
        print("Too High")
    else:
        print("Lucky Guess")
        print("Number of tries ",count)