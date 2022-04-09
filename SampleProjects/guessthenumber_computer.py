import random

def guess(x):
    random_number = random.randint(1, x)
    guessed_number = 0
    while guessed_number != random_number:
        guessed_number = int(input(f"Guess a number between 1 and {x}: "))

        if guessed_number < random_number:
            print("Guess again, Too low")
        elif guessed_number > random_number:
            print("Guess again, Too High")

    print(f"You guessed it right, number is, {guessed_number}")


guess(9)


