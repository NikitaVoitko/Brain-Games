import random


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
    progression, missing_term = generate_arithmetic_progression()
    print("What number is missing in the progression?")
    print("Question: " + " ".join(map(str, progression)))
    user_answer = input("Your answer: ")
    user_answer = int(user_answer)
    if user_answer == missing_term:
        return True, missing_term, user_answer
    else:
        return False, missing_term, user_answer
