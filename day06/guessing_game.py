import random

secret_number = random.randint(1, 100)

guesses = 0

while True:
    guess = int(input("Guess a number betwee 1 and 100: "))

    guesses += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high: Try again.")

    else:
        print("Congratulations! You guessed the number.")
        print(f"It took you {guesses} guesses.")
        break