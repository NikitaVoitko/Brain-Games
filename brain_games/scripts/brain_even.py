#!/usr/bin/env python3
def main():

    # import game1 and engine
    from brain_games.games.game1 import is_even_game
    from brain_games.engine.game_runner import game_runner
    game_runner(is_even_game)


if __name__ == '__main__':
    main()
