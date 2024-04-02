#!/usr/bin/env python3
def main():

    # import game1 and engine
    from brain_games.games.game2 import calculator_game
    from brain_games.engine.engine import game_engine
    game_engine(calculator_game)


if __name__ == '__main__':
    main()
