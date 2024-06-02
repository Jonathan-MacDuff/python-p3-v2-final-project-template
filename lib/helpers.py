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
    
def print_character(character):
    print(f'{character.name} lives in/on {character.location}. Their abilities include: {character.abilities}.')

def print_battle(battle):
    print(f'Battle number {battle.id}: {name_from_id(battle.aggressor_id)} attacked {name_from_id(battle.defender_id)} in/on {battle.location}. {find_victor(battle.aggressor_id, battle.defender_id)} was the victor.')

def list_characters():
    characters = Character.get_all()
    if characters:
        for character in characters:
            print_character(character)
    else:
        print("No characters found")

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

def delete_character():
    name = input("Enter character name: ")
    if character := Character.find_by_name(name):
        character.delete()
        print(f'{name} deleted')
    else:
        print(f'{name} not found')

def find_character_by_id():
    id_ = input("Enter character id: ")
    if character := Character.find_by_id(id_):
        print_character(character)
    else:
        print(f'Character not found')

def find_character_by_name():
    name = input("Enter character name: ")
    if character := Character.find_by_name(name):
        print_character(character)
    else:
        print(f'{name} not found')

def character_battle_count():
    name = input("Enter character name: ")
    if character := Character.find_by_name(name):
        battles = 0
        for battle in Battle.get_all():
            if battle.aggressor_id == character.id or battle.defender_id == character.id:
                battles += 1
        print(f'{name} has participated in {battles} battle(s)')
    else:
        print(f'{name} not found')

def list_battles():
    battles = Battle.get_all()
    if battles:
        for battle in battles:
            print_battle(battle)
    else:
        print("No battles found")

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
    n = input("Enter the battle number: ")
    if battle := Battle.find_by_id(n):
        battle.delete()
        print(f'Battle number {n} deleted')
    else:
        print(f'Battle number {n} not found')

def find_battle_by_id():
    n = input("Enter the battle number: ")
    if battle := Battle.find_by_id(n):
        print_battle(battle)
    else:
        print(f'Battle number {n} not found')

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

def update_character():
    name = input("Enter the character's name: ")
    if character := Character.find_by_name(name):
        print_character(character)
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
    else:
        print(f'{name} not found')

def update_battle():
    n = input("Enter the battle number: ")
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
        
def exit_program():
    print("Goodbye!")
    exit()
