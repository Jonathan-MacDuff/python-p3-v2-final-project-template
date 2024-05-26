# lib/helpers.py
from models.character import Character

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

def find_character():
    id_ = input("Enter character id: ")
    if character := Character.find_by_id(id_):
        print(character)
    else:
        print(f'Character {id_} not found')
        
def exit_program():
    print("Goodbye!")
    exit()
