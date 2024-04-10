#!/usr/bin/env python3
# import game_engine and choose is_even as the game
from brain_games.engine.engine import game_engine
from brain_games.games.calculator_game import calculator_game, CALC_DESCRIPTION


def main():

    game_engine(CALC_DESCRIPTION, calculator_game)


if __name__ == '__main__':
    main()
