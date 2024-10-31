# PowerBall Lottery Number Generator

import random

# Greeting message
print("Welcome to the PowerBall Lottery Number Generator!")
print("Your lucky numbers for today are:")

# Generate five random numbers for white balls (1-69)
white_ball1 = random.randint(1, 69)
white_ball2 = random.randint(1, 69)
white_ball3 = random.randint(1, 69)
white_ball4 = random.randint(1, 69)
white_ball5 = random.randint(1, 69)

# Generate one random number for the red ball (1-26)
red_ball = random.randint(1, 26)

# Print the lottery numbers with required spacing
print(f"{white_ball1} {white_ball2} {white_ball3} {white_ball4} {white_ball5}   {red_ball}")

# Farewell message
print("Good luck! Remember to play responsibly.")
