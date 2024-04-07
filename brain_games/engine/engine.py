from brain_games.cli import welcome_user


def game_engine(game_func):

    name = welcome_user()
    maximum_rounds = 3

    for question_count in range(maximum_rounds):
        correct, correct_answer, user_answer = game_func()
        if correct:
            print("Correct!")
        else:
            print(f"'{user_answer}' is an incorrect answer, {name}! "
                  f"The correct answer was '{correct_answer}'."
                  f" Let's try again, {name}!")
            break

    else:
        print(f"Congratulations, {name}!")
