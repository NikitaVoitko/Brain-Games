import prompt
import random

# import welcome user from cli

from brain_games.cli import welcome_user


def is_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_count = 0
    incorrect_answer = False

    while question_count < 3:
        number = random.randint(1, 100)
        question = f"Question: {number}"
        print(question)
        answer = prompt.string()

        if (number % 2 == 0 and answer == "yes") or (number % 2 != 0 and answer == "no"):
            print("Correct!")
            question_count += 1
        else:
            print(f"'{answer}' is the wrong answer ;(. Let's try again, {name}!")
            incorrect_answer = True
            break
    if not incorrect_answer:
        print(f"Congratulations, {name}!")
