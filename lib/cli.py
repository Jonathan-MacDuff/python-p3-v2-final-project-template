# lib/cli.py

from helpers import (
    exit_program,
    character_choice,
    add_character,
    delete_character,
    list_battles,
    add_battle,
    delete_battle,
    all_victors,
    update_character,
    update_battle,
    display_character
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            character_menu()
        elif choice == "2":
            battle_menu()
        else:
            print("Invalid selection")


def main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Character menu")
    print("2. Battle menu")

def character_menu():
    while True:
        print("Please select an option:")
        print("0. Return to main menu")
        print("1. View all characters")
        print("2. Create a new character")
        print("3. Delete a character")
        print("4. Update a character")
        choice = input("> ")
        if choice == "0":
            main_menu()
        elif choice == "1":
            chosen = character_choice()
            single_character_menu(chosen)
        elif choice == "2":
            add_character()
        elif choice == "3":
            delete_character()
        elif choice == "4":
            update_character()
        else:
            print("Invalid selection")

def battle_menu():
    while True:
        print("Please select an option:")
        print("0. Return to main menu")
        print("1. View all battles")
        print("2. View all battle victors")
        print("3. Create a new battle")
        print("4. Delete a battle")
        print("5. Update a battle")
        choice = input("> ")
        if choice == "0":
            main_menu()
        elif choice == "1":
            list_battles()
        elif choice == "2":
            all_victors()
        elif choice == "3":
            add_battle()
        elif choice == "4":
            delete_battle()
        elif choice == "5":
            update_battle()
        else:
            print("Invalid selection")

def single_character_menu(chosen):
    while True:
        print(f'Please select an option for {chosen.name}: ')
        print("0. Return to character menu")
        print("1. View character details")
        print("2. Update character")
        print("3. Delete character")
        choice = input("> ")
        if choice == "0":
            character_menu()
        elif choice == "1":
            display_character(chosen)
        elif choice == "2":
            update_character(chosen)
        elif choice == "3":
            delete_character(chosen)
            character_menu()
        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()
