import random
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def play_game():
    # Game introduction
    print(Fore.CYAN + "=" * 50)
    print(Fore.MAGENTA + "🎯 Welcome to Guess the Number! 🎯".center(50))
    print(Fore.CYAN + "=" * 50)
    print()

    # Choose difficulty
    print("Choose your difficulty level:")
    print(Fore.GREEN + "🟢 Easy   (1–50)")
    print(Fore.YELLOW + "🟡 Medium (1–100)")
    print(Fore.RED + "🔴 Hard   (1–500)")
    print()

    difficulty = input("Enter difficulty (easy/medium/hard): ").lower()

    if difficulty == "easy":
        max_num = 50
    elif difficulty == "hard":
        max_num = 500
    else:
        max_num = 100  # Default medium

    # Load best score
    score_file = "score.txt"
    best_score = None
    if os.path.exists(score_file):
        with open(score_file, "r") as f:
            content = f.read().strip()
            if content.isdigit():
                best_score = int(content)

    if best_score:
        print(Fore.YELLOW + f"🏆 Current best score: {best_score} attempts")
    else:
        print(Fore.YELLOW + "🏆 No best score yet — be the first!")

    secret_number = random.randint(1, max_num)
    attempts = 0
    min_num = 1

    print()
    print(f"I'm thinking of a number between {min_num} and {max_num}...")
    print()

    # Main game loop
    while True:
        guess = input(f"Take a guess ({min_num}-{max_num}): ")

        if not guess.isdigit():
            print(Fore.RED + "⚠️  Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print(Fore.BLUE + "Too low! Try again.\n")
        elif guess > secret_number:
            print(Fore.BLUE + "Too high! Try again.\n")
        else:
            print()
            print(Fore.CYAN + "=" * 50)
            print(Fore.GREEN + f"🎉 You got it! The number was {secret_number}.")
            print(Fore.GREEN + f"👏 It took you {attempts} tries.")
            print(Fore.CYAN + "=" * 50)

            # Update best score
            if best_score is None or attempts < best_score:
                print(Fore.MAGENTA + "🏅 New best score! Saving to file...")
                with open(score_file, "w") as f:
                    f.write(str(attempts))
            else:
                print(Fore.YELLOW + f"Your best score remains {best_score} attempts.")
            break

# Play again loop
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print(Fore.CYAN + "Thanks for playing! Goodbye! 👋")
        break
