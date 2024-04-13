import random
import operator

DESCRIPTION = "What is the result of the expression?"


def get_calculator_game():
    number1 = random.randint(50, 100)
    number2 = random.randint(1, 50)
    operator_functions = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul)
    ]

    operator_symbol, operation_function = random.choice(operator_functions)
    correct_answer = operation_function(number1, number2)
    question = f"{number1} {operator_symbol} {number2}"

    return correct_answer, question
