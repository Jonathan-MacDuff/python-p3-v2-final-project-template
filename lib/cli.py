# lib/cli.py

from helpers import (
    exit_program,
    list_characters,
    add_character
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_characters()
        elif choice == "2":
            add_character()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all heroes")
    print("2. Create a hero")


if __name__ == "__main__":
    main()
