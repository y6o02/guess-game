import random

# Game introduction
print("=" * 40)
print("🎯 Welcome to Guess the Number! 🎯")
print("=" * 40)
print()

# Choose difficulty
print("Choose your difficulty level:")
print("🟢 Easy   (1–50)")
print("🟡 Medium (1–100)")
print("🔴 Hard   (1–200)")
print()

difficulty = input("Enter difficulty (easy/medium/hard): ").lower()

if difficulty == "easy":
    max_num = 50
elif difficulty == "hard":
    max_num = 200
else:
    max_num = 100  # Default is medium

# Generate random number based on difficulty
secret_number = random.randint(1, max_num)
attempts = 0
min_num = 1

print()
print(f"I'm thinking of a number between {min_num} and {max_num}...")
print()

# Main game loop
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

