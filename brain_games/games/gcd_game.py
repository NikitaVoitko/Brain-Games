import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_gcd_game():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = math.gcd(number1, number2)

    return correct_answer, question
