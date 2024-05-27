# lib/helpers.py
from models.character import Character
from models.battle import Battle

def list_characters():
    characters = Character.get_all()
    if characters:
        for character in characters:
            print(character)
    else:
        print("No characters found")

def add_character():
    name = input("Enter character name: ")
    location = input("Enter character location: ")
    abilities = [input("Enter character abilities, seperated by commas: ")]
    try:
        character = Character.create(name, location, abilities)
        print(character)
    except Exception as exc:
        print(f'Error creating character: {exc}')

def delete_character():
    id_ = input("Enter character id: ")
    if character := Character.find_by_id(id_):
        character.delete()
        print(f'Character {id_} deleted')
    else:
        print(f'Character {id_} not found')

def find_character_by_id():
    id_ = input("Enter character id: ")
    if character := Character.find_by_id(id_):
        print(character)
    else:
        print(f'Character {id_} not found')

def find_character_by_name():
    name = input("Enter character name: ")
    if character := Character.find_by_name(name):
        print(character)
    else:
        print(f'Character {name} not found')

def character_battle_count():
    id_ = input("Enter character id: ")
    if character := Character.find_by_id(id_):
        battles = character.total_battles()
        print(f'{character.name} has participated in {battles} battle(s)')
    else:
        print(f'Character {id_} not found')

def list_battles():
    battles = Battle.get_all()
    if battles:
        for battle in battles:
            print(battle)
    else:
        print("No battles found")

def add_battle():
    aggressor_id = input("Enter aggressor id: ")
    defender_id = input("Enter defender id: ")
    location = input("Enter battle location: ")
    try:
        battle = Battle.create(aggressor_id, defender_id, location)
        print(battle)
    except Exception as exc:
        print(f'Error creating battle: {exc}')

def delete_battle():
    id_ = input("Enter battle id: ")
    if battle := Battle.find_by_id(id_):
        battle.delete()
        print(f'Battle {id_} deleted')
    else:
        print(f'Battle {id_} not found')

def find_battle_by_id():
    id_ = input("Enter battle id: ")
    if battle := Battle.find_by_id(id_):
        print(battle)
    else:
        print(f'Battle {id_} not found')

def all_victors():
    if victors := Battle.all_battle_victors():
        for victor in victors:
            print(victor)
    else:
        print("No victors found")

def update_character():
    id_ = input("Enter the character's id: ")
    if character := Character.find_by_id(id_):
        print(character)
        try:
            name = input("Enter new character name: ")
            location = input("Enter new character location: ")
            abilities = [(input("Enter new character abilities, seperated by commas: "))]
            character.name = name
            character.location = location
            character.abilities = abilities
            character.update()
            print(f'Success: {character}')
        except Exception as exc:
            print(f'Error updating character: {exc}')
    else:
        print(f'Character {id_} not found')

def update_battle():
    id_ = input("Enter the battle's id: ")
    if battle := Battle.find_by_id(id_):
        print(battle)
        try:
            aggressor_id = input("Enter new aggressor id: ")
            defender_id = input("Enter new defender id: ")
            location = input("Enter new battle location: ")
            victor = input("Enter new battle victor: ")
            battle.aggressor_id = aggressor_id
            battle.defender_id = defender_id
            battle.location = location
            battle.victor = victor
            battle.update()
            print(f'Success: {battle}')
        except Exception as exc:
            print(f'Error updating battle: {exc}')
    else:
        print(f'Battle {id_} not found')
        
def exit_program():
    print("Goodbye!")
    exit()
