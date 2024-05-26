# lib/cli.py

from helpers import (
    exit_program,
    list_characters,
    add_character,
    delete_character,
    find_character
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
        elif choice == "3":
            delete_character()
        elif choice == "4":
            find_character()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all characters")
    print("2. Create a character")
    print("3. Delete a character")
    print("4. Find a character")


if __name__ == "__main__":
    main()
