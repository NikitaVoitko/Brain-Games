import prompt
import random
import math


def gcd_game():
    
    print("Find the greatest common divisor of given numbers.")
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    correct_answer = 0
    question = f"Question: {number1} {number2}"
    print(question)
    answer = prompt.integer()
    correct_answer = math.gcd(number1, number2)
    print(correct_answer)

    return answer == correct_answer, correct_answer, answer
