# Basic CLI Battler


## Introduction

This system is designed to generate characters and battles between them. It does so by adding data to tables via CLI user input.


## How to Run

1. download this repo
2. cd into this repo file in your terminal
3. run pipenv install
4. cd into the lib folder of this repo
5. run python seed
6. run python battler


## CLI Overview

I've designed my CLI with non-technical user comfort in mind. Upon opening the CLI, the user is prompted with 2 options; a character menu and a battle menu.

The character menu allows the user to either view a list of all characters or generate a new one. If the former option is selected, the user will receive a numbered list of characters, from which they can select one by name or number. Upon doing so, they are given a set of new options to interact with that character. They can view that character's details, update them, or delete them completely. The latter option will also delete any battles the character has participated in.

The battle menu is similar, but doesn't include a sub-menu for each battle. The user has the option of viewing all battles, viewing all battle victors, adding a battle, deleting a battle, updating a battle, or viewing all battles that have taken place at a particular location.


## CLI Helper Functions

`helpers.py` is where the magic happens. I'll explain each function here in the order they appear.

1. `find_victor` This takes a battle instance as an argument to determine who wins. It does so by comparing each battle participant's quantity of abilities, by splitting the abilities string of each character into a list of strings, and comparing their lengths.
2. `display_character` This takes a character instance as an argument, and prints a description of the data contained in that instance.
3. `diaplay_battle` This takes a battle instance as an argument, and prints a description of the data contained in that instance.
4. `character_choice` This prints a numbered list of all character instances, and prompts the user to select one by name or number, returning the chosen instance.
5. `update_character` This takes a character instance as an argument, and prompts the user to redefine the instance attributes, displaying the updated character.
6. `delete_character` This takes a character instance as an argument, and prompts the user to confirm before deleting that instance and all related battle instances.
7. `add_character` This prompts the user for each character instance attribute, then creates a new character instance with the chosen attributes, and displays the new character.
8. `list_battles` This displays all battle instances.
9. `all_victors` This prints a numbered list of all battle victors.
10. `add_battle` This prompts the user for each battle instance attribute, then creates a new battle instance with the chosen attributes, and displays the new battle.
11. `delete_battle` This displays all battle instances, then prompts the user to select one. It then deletes the selected instance.
12. `update_battle` This displays all battle instances, then prompts the user to select one. It then prompts the user to redefine the instance attributes, displaying the updated battle.
13. `location_battles` This prompts the user for a location, then displays all battles with that location attribute.
14. `exit_program` This exits the battler program.


## Character Class

My character class takes three strings as arguments, with an additional id argument to be set by sql methods. Each string is validated before being set as a name, location, or abilities property attribute. This class also has methods to create and drop the characters table, and a method to create an instance of the class and add it to the characters table. It has a reuseable method to convert table rows back to character instances, which is used in methods to find a character instance by name or id, and get all character instances. Lastly, it has update and delete methods, and a method to find all related battle instances. 


## Battle Class

My battle class takes three arguments, with an additional id argument to be set by sql methods. The first two arguments are foreign keys referring to an instance of the character class, and the third is a location that must be a tring. Each argument is validated before being set as an aggressor_id, defender_id, or location property attribute. This class also has methods to create and drop the battles table, and a method to create an instance of the class and add it to the battles table. It has a reuseable method to convert table rows back to battle instances, which is used in methods to find a battle instance by id, and get all battle instances. Lastly, it has update and delete methods, and a method to find related aggressor and defender character instances. 
