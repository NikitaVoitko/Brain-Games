from brain_games.engine.engine import game_engine
from brain_games.games.game2 import calculator_game
from brain_games.games.game1 import is_even_game


def game_runner(game_name):
    if game_name == "calculator_game":
        game_engine(calculator_game)
    elif game_name == "is_even_game":
        game_engine(is_even_game)
    else:
        print("No game found")
