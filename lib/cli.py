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
    find_battle_by_id,
    all_victors,
    update_character,
    update_battle
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
    print("3. Delete a character")
    print("4. Find a character by id")
    print("5. Find a character by name")
    print("6. Find a character's total battles")
    print("7. List all battles")
    print("8. Create a new battle")
    print("9. Delete a battle")
    print("10. Find a battle by number")
    print("11. List all battle victors")
    print("12. Update a character")
    print("13. Update a battle")

def character_menu():
    while True:
        print("Please select and option:")
        print("0. Return to main menu")
        print("1. View all characters")
        print("2. Create a new character")
        print("3. Delete a character")
        print("4. Update a character")
        choice = input("> ")
        if choice == "0":
            main_menu()
        elif choice == "1":
            character_selection()
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
        print("Please select and option:")
        print("0. Return to main menu")
        print("1. View all battles")
        print("2. Create a new battle")
        print("3. Delete a battle")
        print("4. Update a battle")
        choice = input("> ")
        if choice == "0":
            main_menu()
        elif choice == "1":
            list_battles()
        elif choice == "2":
            add_battle()
        elif choice == "3":
            delete_battle()
        elif choice == "4":
            update_battle()
        else:
            print("Invalid selection")

def character_selection():
    while True:
        list_characters()
        choice = input ("> ")
        if choice == "0":
            character_menu()


if __name__ == "__main__":
    main()
