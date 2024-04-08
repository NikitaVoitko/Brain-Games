import prompt
import random


def calculator_game():
    # to-do: docstring missing
    print('What is the result of the expression?')
    number1 = random.randint(50, 100)
    number2 = random.randint(1, 50)
    correct_answer = 0
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    question = f"Question: {number1} {random_operator} {number2}"
    print(question)
    answer = prompt.integer()
    # to-do: error handling if no proper number provided
    # e.g. print(f"Provided input \"{answer}\" is not an number. Please provide a new answer.")

    if random_operator == '+':
        correct_answer = number1 + number2
    elif random_operator == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2
    # to-do define readable variable before returning
    return answer == correct_answer, correct_answer, answer
