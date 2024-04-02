from brain_games.cli import welcome_user


def game_engine(game_func):

    name = welcome_user()
    question_count = 0
    incorrect_answer = False
    while question_count < 3:
        correct, correct_answer, user_answer = game_func()
        if correct:
            print("Correct!")
            question_count += 1
        else:
            if isinstance(correct_answer, int):
                print(f"'{user_answer}' is an incorrect answer, {name}!"
                      f"The correct answer was '{correct_answer}'."
                      f"  Let's try again.")
                incorrect_answer = True
            else:
                print(f"'{user_answer}' is an incorrect answer, {name}!"
                      f" Let's try again.")
                incorrect_answer = True
            break
    if not incorrect_answer:
        print(f"Congratulations, {name}!")
