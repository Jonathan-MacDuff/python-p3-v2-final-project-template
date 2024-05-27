# lib/cli.py

from helpers import (
    exit_program,
    list_characters,
    add_character,
    delete_character,
    find_character_by_id,
    find_character_by_name,
    character_battle_count,
    list_battles,
    add_battle,
    delete_battle,
    find_battle_by_id
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
            find_character_by_id()
        elif choice == "5":
            find_character_by_name()
        elif choice == "6":
            character_battle_count()
        elif choice == "7":
            list_battles()
        elif choice == "8":
            add_battle()
        elif choice == "9":
            delete_battle()
        elif choice == "10":
            find_battle_by_id()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all characters")
    print("2. Create a new character")
    print("3. Delete a character")
    print("4. Find a character by id")
    print("5. Find a character by name")
    print("6. Find a character's total battles")
    print("7. List all battles")
    print("8. Create a new battle")
    print("9. Delete a battle")
    print("10. Find a battle by id")


if __name__ == "__main__":
    main()
