# lib/helpers.py
from models.hero import Hero
from models.villain import Villain

def list_heroes():
    heroes = Hero.get_all()
    if heroes:
        for hero in heroes:
            print(hero)
    else:
        print("No heroes found")

def add_hero():
    name = input("Enter hero name: ")
    location = input("Enter hero location: ")
    abilities = [input("Enter hero abilities, seperated by commas: ")]
    try:
        hero = Hero.create(name, location, abilities)
        print(hero)
    except Exception as exc:
        print(f'Error creating hero: {exc}')
        
def exit_program():
    print("Goodbye!")
    exit()
