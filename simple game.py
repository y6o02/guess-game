import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100...")

# Generate a random number
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Take a guess: ")

    # Check if input is a number
    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 You got it! The number was {secret_number}.")
        print(f"It took you {attempts} tries.")
        break
