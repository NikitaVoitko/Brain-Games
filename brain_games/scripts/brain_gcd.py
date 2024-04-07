#!/usr/bin/env python3
def main():

    # import game_engine and choose is_even as the game
    from brain_games.engine.engine import game_engine
    from brain_games.games.gcd_game import gcd_game

    game_engine(gcd_game)


if __name__ == '__main__':
    main()
