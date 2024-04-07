#!/usr/bin/env python3
def main():

    # import game_engine and choose is_even as the game
    from brain_games.engine.engine import game_engine
    from brain_games.games.is_prime_game import is_prime_game

    game_engine(is_prime_game)


if __name__ == '__main__':
    main()
