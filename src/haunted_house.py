import random
from data import data

# Global lists to track choices and outcomes
choices_made = []  # List to store user's choices during the game
outcomes = data.outcomes
help_text = """
Help Information:
-----------------
1. If you are getting 'Invalid Choice' error, please ensure there are no spelling mistakes in your input.
2. If you would like to quit the game mid-way, please provide the input as 'stop'.
3. If you would like to report a bug, please send an email to 2012029@apps.nsd.org with as much details as you can and I'll be happy to fix it.
4. If you have critical feedback or enhancement request, please send email to 2012029@apps.nsd.org and I'll be happy to work on it.

"""

def start_story():
    """Initial greeting and starting point of the game."""
    print("#"*100 + "\n")
    print("Welcome to the Haunted House Adventure!\n".upper())
    print("#"*100 + "\n")
    print("You stand before an eerie mansion. The door creaks open as if inviting you inside.")
    print("Type 'stop' at any time to quit the game.")
    print("Type 'help' at any time if you need help with the game.\n")
    
    while True:
        user_choice = input("What would you like to do? You can 'enter' the house or 'leave'. Type your choice: ").lower().strip()
        choices_made.append("Start Story: " + user_choice)
        
        if user_choice == "stop":
            print("Thanks for playing! Goodbye.")
            break
        elif user_choice == "help":
            print(help_text)
        elif user_choice == "enter":
            enter_house()
            summary()
            break
        elif user_choice == "leave":
            leave_house()
            break
        else:
            print("Invalid choice. Please type 'enter' or 'leave'.")

def enter_house():
    """Handles the logic and choices for entering the haunted house."""
    print("\nYou step inside the mansion. The air is cold, and the floors creak beneath your feet.")
    print("You see a staircase leading upstairs, a hallway that seems to stretch endlessly, and a door to your left with a strange glowing symbol on it.")
    
    while True:
        user_choice = input("Do you want to go 'upstairs', 'explore' the hallway, or 'open' the strange door? Type your choice: ").lower().strip()
        choices_made.append("Enter House: " + user_choice)
        
        if user_choice == "stop":
            print("Thanks for playing! Goodbye.")
            break
        elif user_choice == "help":
            print(help_text)
        elif user_choice == "upstairs":
            upstairs()
            break
        elif user_choice == "explore":
            explore_hallway()
            break
        elif user_choice == "open":
            open_strange_door()
            break
        else:
            print("Invalid choice. Please type 'upstairs', 'explore', or 'open'.")

def upstairs():
    """Handles the upstairs encounter with a ghost and possible vampire encounter."""
    print("\nYou climb the stairs and enter a dimly lit room. The air feels thick, and there's an old rocking chair that moves by itself.")
    print("The room feels haunted. Suddenly, a ghostly figure appears!")

    while True:
        user_choice = input("Do you 'talk' to the ghost, 'run' out of the room, or 'investigate' the mirror on the wall? Type your choice: ").lower().strip()
        choices_made.append("Upstairs: " + user_choice)
        
        if user_choice == "stop":
            print("Thanks for playing! Goodbye.")
            break
        elif user_choice == "help":
            print(help_text)
        elif user_choice == "talk":
            print("\nThe ghost tells you a tragic tale of how it was once a resident of the mansion and asks for your help.")
            print("You decide to help the ghost, and it grants you a treasure as a token of thanks. You escape safely!")
            break
        elif user_choice == "run":
            print("\nYou run back down the stairs and out of the house, heart racing.")
            break
        elif user_choice == "investigate":
            print("\nYou walk towards the mirror and touch it. Suddenly, you're transported into another dimension!")
            print("This new world is full of strange creatures. You see a Vampire approaching...")
            vampire_encounter()
            break
        else:
            print("Invalid choice. Please type 'talk', 'run', or 'investigate'.")

def explore_hallway():
    """Handles the hallway encounter with a werewolf."""
    print("\nYou walk down the long hallway. The walls are covered in old portraits, their eyes seemingly following you.")
    print("At the end of the hallway, you see a door slightly ajar. There's a faint growl coming from inside.")

    while True:
        user_choice = input("Do you want to 'enter' the room with the growl or 'turn back' and leave the house? Type your choice: ").lower().strip()
        choices_made.append("Explore Hallway: " + user_choice)
        
        if user_choice == "stop":
            print("Thanks for playing! Goodbye.")
            break
        elif user_choice == "help":
            print(help_text)
        elif user_choice == "enter":
            print("\nYou step into the room and come face to face with a huge, snarling werewolf!")
            werewolf_encounter()
            break
        elif user_choice == "turn back":
            print("\nYou turn back and leave the mansion, deciding it’s not worth the risk. Maybe another time.")
            break
        else:
            print("Invalid choice. Please type 'enter' or 'turn back'.")

def open_strange_door():
    """Handles the encounter with the witch."""
    print("\nYou open the door to find a dimly lit room full of strange symbols and a glowing cauldron in the center.")
    print("As you approach the cauldron, a figure appears behind you. It's a witch!")

    while True:
        user_choice = input("Do you 'talk' to the witch, 'run' away, or 'inspect' the cauldron? Type your choice: ").lower().strip()
        choices_made.append("Open Strange Door: " + user_choice)
        
        if user_choice == "stop":
            print("Thanks for playing! Goodbye.")
            break
        elif user_choice == "help":
            print(help_text)
        elif user_choice == "talk":
            print("\nThe witch offers you a potion and asks if you wish to gain power in exchange for a dangerous quest.")
            print("You accept, and the witch teleports you to the heart of the forest where strange things are afoot!")
            break
        elif user_choice == "run":
            print("\nYou run out of the room, heart racing, and the door slams shut behind you. Maybe it's best not to anger a witch.")
            break
        elif user_choice == "inspect":
            print("\nYou inspect the cauldron, and suddenly, a vision appears—vampires, werewolves, and witches are all part of a secret society.")
            print("Before you can react, the cauldron bubbles over, and you are pulled into a dark underground lair!")
            underground_lair()
            break
        else:
            print("Invalid choice. Please type 'talk', 'run', or 'inspect'.")

def vampire_encounter():
    """Handles the vampire encounter logic."""
    print("\nThe Vampire approaches, his eyes glowing red. He speaks in a low, haunting voice.")
    print("'You have entered my domain, mortal. Will you join us, or will you die like the rest?'")
    
    while True:
        user_choice = input("Do you 'join' the vampire, 'fight' him, or 'run' away? Type your choice: ").lower().strip()
        choices_made.append("Vampire Encounter: " + user_choice)
        
        if user_choice == "stop":
            print("Thanks for playing! Goodbye.")
            break
        elif user_choice == "help":
            print(help_text)
        elif user_choice == "join":
            outcome = "You join the vampire and become immortal!"
            print(f"\n{outcome}")
            choices_made.append("Vampire outcome: " + outcome)
            break
        elif user_choice == "fight":
            outcome = random.choice(outcomes['vampire'])
            print(f"\n{outcome}")
            choices_made.append("Vampire outcome: " + outcome)
            break
        elif user_choice == "run":
            outcome = "You run away, barely escaping with your life!"
            print(f"\n{outcome}")
            choices_made.append("Vampire outcome: " + outcome)
            break
        else:
            print("Invalid choice. Please type 'join', 'fight', or 'run'.")

def werewolf_encounter():
    """Handles the werewolf encounter logic."""
    print("\nThe werewolf lunges at you with a vicious growl! Its claws are sharp and its eyes full of rage.")
    
    while True:
        user_choice = input("Do you 'fight' the werewolf, 'run' for the door, or 'try' to reason with it? Type your choice: ").lower().strip()
        choices_made.append("Werewolf Encounter: " + user_choice)
        
        if user_choice == "stop":
            print("Thanks for playing! Goodbye.")
            break
        elif user_choice == "help":
            print(help_text)
        elif user_choice == "fight":
            outcome = random.choice(outcomes['werewolf'])
            print(f"\n{outcome}")
            choices_made.append("Werewolf outcome: " + outcome)
            break
        elif user_choice == "run":
            outcome = "You run away, leaving the werewolf howling in the distance."
            print(f"\n{outcome}")
            choices_made.append("Werewolf outcome: " + outcome)
            break
        elif user_choice == "try":
            outcome = "You try to reason with the werewolf but it attacks you and kills you!"
            print(f"\n{outcome}")
            choices_made.append("Werewolf outcome: " + outcome)
            break
        else:
            print("Invalid choice. Please type 'fight', 'run', or 'try'.")

def underground_lair():
    """Handles the final encounter in the underground lair with all three creatures."""
    print("\nYou find yourself in an underground lair, surrounded by ancient symbols and dark figures.")
    print("The vampire, werewolf, and witch stand before you. They speak in unison: 'You are caught in our web.'")

    while True:
        user_choice = input("Do you 'fight' them all, 'try to escape' the lair, or 'join' their secret society? Type your choice: ").lower().strip()
        choices_made.append("Underground Lair Encounter: " + user_choice)
        
        if user_choice == "stop":
            print("Thanks for playing! Goodbye.")
            break
        elif user_choice == "help":
            print(help_text)
        elif user_choice == "fight":
            outcome = random.choice(outcomes['witch'])
            print(f"\n{outcome}")
            choices_made.append("Underground Lair outcome: " + outcome)
            break
        elif user_choice == "try to escape":
            print("\nYou attempt to escape, but the lair is filled with traps. You're caught in a net, helpless.")
            break
        elif user_choice == "join":
            print("\nYou join the secret society, becoming one of the most powerful beings in the world. Your journey ends here...")
            break
        else:
            print("Invalid choice. Please type 'fight', 'try to escape', or 'join'.")

def leave_house():
    """Handles the scenario where the user chooses to leave the haunted house."""
    print("\nYou decide to leave the haunted house. The door slams shut behind you as if it never wanted you inside.")
    print("As you walk away, you feel a chill run down your spine. Perhaps you’ll be brave enough to return one day.")
    print("\nThanks for playing! Goodbye.")
    
def summary():
    print("\n--- Game Summary ---\n")
    print("Choices made by you during the game:")
    for choice in choices_made:
        print(f"- {choice}")
    print("\nThanks for playing! Goodbye.")


if __name__ == "__main__":
    start_story()
