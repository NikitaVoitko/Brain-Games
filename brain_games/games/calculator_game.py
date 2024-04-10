import random

CALC_DESCRIPTION = "What is the result of the expression?"


def calculator_game():

    number1 = random.randint(50, 100)
    number2 = random.randint(1, 50)
    correct_answer = 0
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    question = f"{number1} {random_operator} {number2}"

    if random_operator == '+':
        correct_answer = number1 + number2
    elif random_operator == '-':
        correct_answer = number1 - number2
    else:
        correct_answer = number1 * number2

    return correct_answer, question
