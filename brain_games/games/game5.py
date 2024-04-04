import prompt
import random


def is_prime(n):
    prime_number = ""
    if n <= 1:
        prime_number = "no"
        return prime_number
    elif n <= 3:
        prime_number = "yes"
        return prime_number
    elif n % 2 == 0 or n % 3 == 0:
        prime_number = "no"
        return prime_number
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            prime_number = "no"
            return prime_number
        i += 6
    prime_number = "yes"
    return prime_number


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
