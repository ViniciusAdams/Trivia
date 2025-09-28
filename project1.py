#List of questions
# store the answers
# randomly pick questions
# ask the questions to the user
# see if they are correct 
#keep the socre 
# tell the user their score

import random

questions = {
     "What keyword is used to define a function in Python?": "def",
     "What is the output of len(\"hello\")?": "5",
     "Which data type is used to store a sequence of items in a specific order and is mutable?": "list",
     "What symbol is used to start a comment in Python?": "#",
     "What will type(3.14) return?": "<class 'float'>",
     "What keyword is used to handle exceptions in Python?": "try",
     "Which built-in function is used to get user input from the console?": "input()",
     "What is the boolean value of bool([])?": "False",
     "What is the output of print(2 ** 3)?": "8",
     "Which module is commonly used for working with regular expressions in Python?": "re ",
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    print(selected_questions)

python_trivia_game()    
python_trivia_game()  