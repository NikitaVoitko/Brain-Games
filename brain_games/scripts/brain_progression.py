#!/usr/bin/env python3
# import game_engine and choose is_even as the game
from brain_games.engine.engine import game_engine
from brain_games.games.progression_game import progression_game


def main():

    game_engine(progression_game)


if __name__ == '__main__':
    main()
