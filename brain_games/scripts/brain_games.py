#!/usr/bin/env python3
def main():
    print("Welcome to the Brain Games!")

    # import welcome user from cli
    from brain_games.cli import welcome_user
    welcome_user()


if __name__ == '__main__':
    main()
