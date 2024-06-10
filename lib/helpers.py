# lib/helpers.py
from models.character import Character
from models.battle import Battle

def find_victor(battle):
    if len(battle.aggressor().abilities.split(', ')) < len(battle.defender().abilities.split(', ')):
        return battle.defender().name
    elif len(battle.aggressor().abilities.split(', ')) > len(battle.defender().abilities.split(', ')):
        return battle.aggressor().name
    else:
        return "Draw"

def print_character(character):
    print(f'{character.name} lives in/on {character.location}. Their abilities include: {character.abilities}.')

def print_battle(battle):
    print(f'Battle number {battle.id}: {battle.aggressor().name} attacked {battle.defender().name} in/on {battle.location}. {find_victor(battle)} was the victor.')

def character_choice():
    characters = Character.get_all()
    if characters:
        for i, character in enumerate(characters, start = 1):
            print(f'{i}.', character.name)
        choice = input("Select a character: ")
        try:
            chosen = characters[int(choice) - 1]
            return chosen
        except:
            chosen = Character.find_by_name(choice)
            if chosen:
                return chosen
            else:
                return None
    else:
        return None

def display_character(character):
        print(character.name)
        print(f'Location: {character.location}')
        print(f'Abilities: {character.abilities}')
        print(f'Total battles: {len(character.battles())}')

def update_character(character):
    try:
        name = input("Enter new character name: ")
        location = input("Enter new character location: ")
        abilities = (input("Enter new character abilities, seperated by commas: "))
        character.name = name
        character.location = location
        character.abilities = abilities
        character.update()
        print('Success:')
        print_character(character)
    except Exception as exc:
        print(f'Error updating character: {exc}')
#
def delete_character(character):
    confirm = input("This will also delete all battles involving this character. Please enter \"delete\" to confirm: ")
    if confirm.lower() == "delete":
        for battle in character.battles():
            battle.delete()
        character.delete()
        print(f'Success: {character.name} deleted')
    else:
        print("Deletion canceled")
#
def add_character():
    name = input("Enter character name: ")
    location = input("Enter character location: ")
    abilities = input("Enter character abilities, seperated by commas: ")
    try:
        character = Character.create(name, location, abilities)
        print('Success:')
        print_character(character)
    except Exception as exc:
        print(f'Error creating character: {exc}')

def list_battles():
    battles = Battle.get_all()
    if battles:
        for battle in battles:
            print_battle(battle)
    else:
        print("No battles found")

def all_victors():
        victors = []
        for battle in Battle.get_all():
            victor = find_victor(battle.aggressor_id, battle.defender_id)
            if not victors.__contains__(victor):
                victors.append(victor)
        if victors:
            for victor in victors:
                print(victor)
        else:
            print("No victors found")

def add_battle():
    aggressor = input("Enter aggressor name: ")
    defender = input("Enter defender name: ")
    location = input("Enter battle location: ")
    try:
        battle = Battle.create(Character.find_by_name(aggressor).id, Character.find_by_name(defender).id, location)
        print_battle(battle)
    except Exception as exc:
        print(f'Error creating battle: {exc}')

def delete_battle():
    list_battles()
    n = input("Enter the battle number to delete: ")
    if battle := Battle.find_by_id(n):
        battle.delete()
        print(f'Battle number {n} deleted')
    else:
        print(f'Battle number {n} not found')

def update_battle():
    list_battles()
    n = input("Enter the battle number to update: ")
    if battle := Battle.find_by_id(n):
        print_battle(battle)
        try:
            aggressor = input("Enter new aggressor name: ")
            defender = input("Enter new defender name: ")
            location = input("Enter new battle location: ")
            battle.aggressor_id = Character.find_by_name(aggressor).id
            battle.defender_id = Character.find_by_name(defender).id
            battle.location = location
            battle.update()
            print('Success:')
            print_battle(battle)
        except Exception as exc:
            print(f'Error updating battle: {exc}')
    else:
        print(f'Battle number {n} not found')

def location_battles():
    location = input("Enter location: ")
    battles = Battle.get_all()
    battle_list = []
    for battle in battles:
        if battle.location == location:
            battle_list.append(battle)
    if battle_list:
        for battle in battle_list:
            print_battle(battle)
    else:
        print("No battles found")
        
def exit_program():
    print("Goodbye!")
    exit()
