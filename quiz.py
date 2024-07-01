import random

# Questions and answers database
quiz_data = {
    'mathematics': {
        'simple': [
            ('What is 2 + 2?', '4'),
            ('What is 5 - 3?', '2'),
            ('What is 3 * 1?', '3')
        ],
        'medium': [
            ('What is 12 / 4?', '3'),
            ('What is 15 % 4?', '3'),
            ('What is 5 * 6?', '30')
        ],
        'complex': [
            ('What is 25 * 3?', '75'),
            ('What is 100 / 4?', '25'),
            ('What is 9 ** 2?', '81')
        ]
    },
    'science': {
        'simple': [
            ('What planet is known as the Red Planet?', 'Mars'),
            ('What is the chemical symbol for water?', 'H2O'),
            ('What gas do plants absorb from the atmosphere?', 'Carbon Dioxide')
        ],
        'medium': [
            ('What is the speed of light?', '299792458'),
            ('What is the main gas found in the air we breathe?', 'Nitrogen'),
            ('What force keeps us on the ground?', 'Gravity')
        ],
        'complex': [
            ('What is the powerhouse of the cell?', 'Mitochondria'),
            ('What is the chemical formula for methane?', 'CH4'),
            ('What planet is closest to the sun?', 'Mercury')
        ]
    }
}

def ask_question(question, correct_answer):
    user_answer = input(f"{question} ").strip().lower()
    return user_answer == correct_answer.lower()

def conduct_quiz(subject, difficulty):
    selected_questions = quiz_data[subject][difficulty]
    random.shuffle(selected_questions)
    score = 0

    for question, answer in selected_questions:
        if ask_question(question, answer):
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {answer}.")

    print(f"Your final score: {score}/{len(selected_questions)}")

def start_quiz():
    print("Welcome to the Quiz Game!")
    subject = input("Choose a subject (mathematics/science): ").strip().lower()
    while subject not in quiz_data:
        subject = input("Invalid subject. Please choose again (mathematics/science): ").strip().lower()

    difficulty = input("Choose a difficulty (simple/medium/complex): ").strip().lower()
    while difficulty not in quiz_data[subject]:
        difficulty = input("Invalid difficulty. Please choose again (simple/medium/complex): ").strip().lower()

    conduct_quiz(subject, difficulty)

if name == "main":
    start_quiz()