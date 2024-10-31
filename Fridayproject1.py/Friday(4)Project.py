# Trivia Study Program

# Define a dictionary with questions as keys and answers as values
questions_and_answers = {
    "What is the capital of France?": "Paris",
    "What planet is known as the Red Planet?": "Mars",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the smallest ocean in the world?": "Arctic",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}

# Greeting message
print("Welcome to the Trivia Study Program!")
print("Let's see how many questions you can answer correctly!\n")

# Loop through the dictionary to ask each question
for question, correct_answer in questions_and_answers.items():
    # Display the question to the user and get their answer
    user_answer = input(question + " ").strip()

    # Check if the user's answer is correct and provide feedback
    if user_answer.lower() == correct_answer.lower():
        print("Correct!\n")
    else:
        print(f"Incorrect. The correct answer is '{correct_answer}'.\n")

# Farewell message
print("Thanks for studying! Good luck on your test!")
