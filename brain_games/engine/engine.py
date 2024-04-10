from brain_games.cli import welcome_user
import prompt

ROUND_COUNT = 3


def game_engine(description, game_func):
    name = welcome_user()
    print(description)
    for _ in range(ROUND_COUNT):
        correct_answer, question = game_func()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')
        if str(correct_answer) != user_answer:
            print(f"'{user_answer}' is an incorrect answer, {name}! "
                  f"The correct answer was '{correct_answer}'."
                  f" Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f"Congratulations, {name}!")
