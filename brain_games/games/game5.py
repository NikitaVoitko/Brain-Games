import prompt
import random


def is_prime(n):
    if n <= 1:
        return "no"
    elif n <= 3:
        return "yes"
    elif n % 2 == 0 or n % 3 == 0:
        return "no"

    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return "no"

    return "yes"


def is_prime_game():
    number = random.randint(1, 100)
    prime_number = is_prime(number)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answer = ""
    question = f"Question: {number}"
    print(question)
    answer = prompt.string()
    correct_answer = prime_number
    print(correct_answer)
    return answer == correct_answer, correct_answer, answer
