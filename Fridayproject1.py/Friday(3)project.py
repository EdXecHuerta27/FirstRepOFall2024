import random

# Greeting message and asking the user if they want to play
print("Welcome to the Number Guessing Game!")
play_game = input("Do you want to play? (yes or no): ").strip().lower()

if play_game == "yes":
    # Generate a random secret number between 1 and 10
    secret_number = random.randint(1, 10)
    print("Great! I'm thinking of a number between 1 and 10.")

    while True:
        # Ask the user to guess the number
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check the guess and give feedback
        if guess == secret_number:
            print("Congratulations! You've guessed the number!")
            break
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

    # Farewell message after correct guess
    print("Thanks for playing! Goodbye!")

elif play_game == "no":
    # If the user doesn't want to play
    print("Maybe next time! Have a great day!")
else:
    print("Invalid input. Please enter 'yes' or 'no' next time.")
