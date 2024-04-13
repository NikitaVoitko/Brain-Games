import random

DESCRIPTION = ('Answer "yes" if given number is prime. '
               'Otherwise answer "no".')


def get_prime_status(n):
    prime_status = "yes"
    if n <= 1:
        prime_status = "no"
    elif n <= 3:
        prime_status = "yes"
    elif n % 2 == 0 or n % 3 == 0:
        prime_status = "no"
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            prime_status = "no"
    return prime_status


def get_is_prime_game():
    number = random.randint(1, 100)
    correct_answer = get_prime_status(number)
    question = f"{number}"
    return correct_answer, question
