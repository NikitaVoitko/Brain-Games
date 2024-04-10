#!/usr/bin/env python3
# import game_engine and choose is_even as the game
from brain_games.engine.engine import game_engine
from brain_games.games.is_even_game import is_even_game, IS_EVEN_DESCRIPTION


def main():

    game_engine(IS_EVEN_DESCRIPTION, is_even_game)


if __name__ == '__main__':
    main()
