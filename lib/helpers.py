# lib/helpers.py
from models.character import Character
from models.battle import Battle

def name_from_id(id_):
    return Character.find_by_id(id_).name

def id_from_name(name):
    return Character.find_by_name(name).id

def find_victor(id_1, id_2):
    aggressor = Character.find_by_id(id_1)
    defender = Character.find_by_id(id_2)
    if len(aggressor.abilities.split(', ')) < len(defender.abilities.split(', ')):
        return defender.name
    elif len(aggressor.abilities.split(', ')) > len(defender.abilities.split(', ')):
        return aggressor.name
    else:
        return "Draw"
    
def all_character_battles(character):
        battles = []
        for battle in Battle.get_all():
            if battle.aggressor_id == character.id or battle.defender_id == character.id:
                battles.append(battle)
        return battles
    
def character_battle_count(character):
    return len(all_character_battles(character))
    
def print_character(character):
    print(f'{character.name} lives in/on {character.location}. Their abilities include: {character.abilities}.')

def print_battle(battle):
    print(f'Battle number {battle.id}: {name_from_id(battle.aggressor_id)} attacked {name_from_id(battle.defender_id)} in/on {battle.location}. {find_victor(battle.aggressor_id, battle.defender_id)} was the victor.')

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
        print(f'Total battles: {character_battle_count(character)}')

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

def delete_character(character):
    confirm = input("This will also delete all battles involving this character. Please enter \"delete\" to confirm: ")
    if confirm.lower() == "delete":
        character_battles = all_character_battles(character)
        for battle in character_battles:
            battle.delete()
        character.delete()
        print(f'Success: {character.name} deleted')
    else:
        print("Deletion canceled")

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
        battle = Battle.create(id_from_name(aggressor), id_from_name(defender), location)
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
            battle.aggressor_id = id_from_name(aggressor)
            battle.defender_id = id_from_name(defender)
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
