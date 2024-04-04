from brain_games.engine.engine import game_engine
from brain_games.games.game2 import calculator_game
from brain_games.games.game1 import is_even_game
from brain_games.games.game3 import gcd_game
from brain_games.games.game4 import progression_game
from brain_games.games.game5 import is_prime_game


def game_runner(game_name):
    if game_name == "calculator_game":
        game_engine(calculator_game)
    elif game_name == "is_even_game":
        game_engine(is_even_game)
    elif game_name == "gcd_game":
        game_engine(gcd_game)
    elif game_name == "progression_game":
        game_engine(progression_game)
    else:
        game_engine(is_prime_game)
