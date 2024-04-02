import prompt
import random


def is_even_game():

    number = random.randint(1, 100)
    question = f"Question: {number}"
    print(question)
    answer = prompt.string()

    correct_answer = "yes" if number % 2 == 0 else "no"
    return answer == correct_answer, correct_answer, answer
