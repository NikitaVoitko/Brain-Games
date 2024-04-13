#!/usr/bin/env python3
# import game_engine and choose gcd as the game
from brain_games.engine.engine import run_game
import brain_games.games.gcd_game


def main():
    run_game(brain_games.games.gcd_game.DESCRIPTION, 
             brain_games.games.gcd_game.get_gcd_game)


if __name__ == '__main__':
    main()
