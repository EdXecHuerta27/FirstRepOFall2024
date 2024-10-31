import random

# Define color functions with ANSI escape codes
def red_text(text):
    return f"\033[31m{text}\033[0m"

def blue_text(text):
    return f"\033[34m{text}\033[0m"

def green_text(text):
    return f"\033[32m{text}\033[0m"

def yellow_text(text):
    return f"\033[33m{text}\033[0m"

def purple_text(text):
    return f"\033[35m{text}\033[0m"

# Function to pick a random color
def random_color_text(text):
    color_functions = [red_text, blue_text, green_text, yellow_text, purple_text]
    return random.choice(color_functions)(text)

# Main program loop
def main():
    print("Welcome to the Text Color Changer Program!")

    while True:
        # Prompt user for a color choice
        color_choice = input("Choose a color (red, blue, green, yellow, purple, random, or custom): ").strip().lower()
        text = input("Enter the text you want to display: ")

        # Display the text in the selected color
        if color_choice == "red":
            print(red_text(text))
        elif color_choice == "blue":
            print(blue_text(text))
        elif color_choice == "green":
            print(green_text(text))
        elif color_choice == "yellow":
            print(yellow_text(text))
        elif color_choice == "purple":
            print(purple_text(text))
        elif color_choice == "random":
            print(random_color_text(text))
        elif color_choice == "custom":
            custom_code = input("Enter a custom ANSI color code (e.g., 31 for red): ").strip()
            print(f"\033[{custom_code}m{text}\033[0m")
        else:
            print("Invalid choice. Please try again.")

        # Ask if the user wants to continue
        continue_choice = input("Do you want to color another text? (yes or no): ").strip().lower()
        if continue_choice != "yes":
            print("Thank you for using the Text Color Changer Program!")
            break

# Run the main program
main()
