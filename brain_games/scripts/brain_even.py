#!/usr/bin/env python3
from brain_games.games.game1 import is_even_game
from brain_games.engine.game_runner import run_game


def main():
    run_game(is_even_game)


if __name__ == '__main__':
    main()
