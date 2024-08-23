import random

# Quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the chmical symbol for Potassium?",
        "options": ["P", "Po", "K", "Li"],
        "correct_answer": "K"
    },
    {
        "question": "What year was Abraham Lincoln born?",
        "options": ["1909", "1811", "1809", "1776"],
        "correct_answer": "1809"
    },
    {
        "question": "What is the geographical name for a rainforest?",
        "options": ["Taiga", "Badlands", "Selvas", "Hardpan"],
        "correct_answer": "Selvas"
    }
]

#Function for displaying the questions to the screen
def display_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"], 1):
        print(f"{i}. {option}")

#Function for getting user input
def get_user_answer():
    while True:
        try:
            choice = int(input("Enter your answer (1-4): "))
            if 1 <= choice <= 4:
                return choice - 1
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Running the Quiz from start to end
def run_quiz():
    score = 0
    total_questions = len(questions)
    
    random.shuffle(questions)
    
    for question in questions:
        display_question(question)
        user_choice = get_user_answer()
        
        if question["options"][user_choice] == question["correct_answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {question['correct_answer']}")
        
        print()  # Add a blank line for readability
    
    print(f"Quiz complete! You scored {score} out of {total_questions}.")
    percentage = (score / total_questions) * 100
    print(f"Your score: {percentage:.2f}%")
 
#The Main Game Loop
def main():
    while True:
        print("Welcome to the Python Quiz Game!")
        run_quiz()
        
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
