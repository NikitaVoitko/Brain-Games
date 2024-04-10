import random

PROGRESSION_DESCRIPTION = "What number is missing in the progression?"


def generate_arithmetic_progression():
    start = random.randint(1, 10)
    diff = random.randint(1, 10)
    n = random.randint(5, 10)
    progression = [start + i * diff for i in range(n)]
    missing_index = random.randint(0, n - 1)
    missing_term = progression[missing_index]
    progression[missing_index] = '..'
    return progression, missing_term


def progression_game():
    progression, correct_answer = generate_arithmetic_progression()
    question = " ".join(map(str, progression))
    return correct_answer, question
