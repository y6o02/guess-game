import random

# Game introduction
print("=" * 40)
print("🎯 Welcome to Guess the Number! 🎯")
print("=" * 40)
print("I'm thinking of a number between 1 and 100...")
print()

# Generate a random number
secret_number = random.randint(1, 100)
attempts = 0
min_num, max_num = 1, 100

while True:
    guess = input(f"Take a guess ({min_num}-{max_num}): ")

    # Check if input is a number
    if not guess.isdigit():
        print("⚠️  Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.\n")
    elif guess > secret_number:
        print("Too high! Try again.\n")
    else:
        print()
        print("=" * 40)
        print(f"🎉 You got it! The number was {secret_number}.")
        print(f"👏 It took you {attempts} tries.")
        print("=" * 40)
        break
