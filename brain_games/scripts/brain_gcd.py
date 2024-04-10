#!/usr/bin/env python3
# import game_engine and choose gcd as the game
from brain_games.engine.engine import game_engine
from brain_games.games.gcd_game import gcd_game, GCD_DESCRIPTION


def main():
    game_engine(GCD_DESCRIPTION, gcd_game)


if __name__ == '__main__':
    main()
