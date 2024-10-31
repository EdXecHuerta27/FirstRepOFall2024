# Mad Lib Game in Python

# Prompting the user for input
large_object = input("Enter a large object: ")
large_objects_plural = input("Enter large objects (plural): ")
adjective = input("Enter an adjective: ")
body_part = input("Enter a body part: ")
restaurant = input("Enter a restaurant: ")
first_food = input("Enter a food: ")
second_food = input("Enter another food: ")

# Constructing the story with user input
story = f"""
I've had a very {adjective} day.
This morning, I dropped a box of {large_objects_plural} on my {body_part}.
Then, at lunch, I went to {restaurant} for their delicious {first_food},
but the waiter brought me {second_food}, which I was not hungry for.
Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof.
"""

# Printing the completed story
print("\nHere is your Mad Lib story:")
print(story)