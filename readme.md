# Haunted House Adventure Game

Welcome to the **Haunted House Adventure** game! This is a text-based interactive story where you explore a mysterious haunted mansion and make choices that affect the outcome of your journey. You will encounter a variety of creatures, including vampires, werewolves, and witches. Your decisions will lead to different outcomes, making each playthrough unique and exciting.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation Instructions](#installation-instructions)
- [How to Play](#how-to-play)
- [Code Overview](#code-overview)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

In this game, you step into the shoes of a brave adventurer who enters a haunted mansion. As you explore different rooms, you will encounter strange beings, including **vampires**, **werewolves**, and **witches**. Your choices will determine the fate of your character, leading to multiple potential endings based on your decisions.

This program was developed using Python, ensuring a lightweight and straightforward game that runs in any Python environment without needing additional libraries or installation dependencies.

## Features

- **Interactive Story**: Engage in an exciting narrative where every decision you make impacts the story's direction.
- **Randomized Encounters**: Vampires, werewolves, and witches present different outcomes every time you play.
- **Multiple Endings**: Depending on your choices, you can become part of the dark forces or escape the mansion.
- **Replayable**: With multiple paths and outcomes, the game offers a new experience on each playthrough.
- **Simple Text-Based Interface**: The game is designed to be intuitive and easy to navigate with simple text inputs.
- **Input Validation**: Invalid inputs are caught and the player is asked to enter a valid option.

## Installation Instructions

### Requirements:
- Python 3.x installed on your computer.
- No external libraries or dependencies are required.

### Steps to Run:

1. Clone or download the repository to your local machine.
2. Navigate to the project directory via the terminal or command prompt.
3. Ensure Python 3 is installed by running the command:
   ```bash
   python --version
   ```
4. Run the game script using Python:
   ```bash
   python haunted_house_adventure.py
   ```

5. Follow the on-screen prompts to play the game!

## How to Play

1. **Starting the Game**: When you run the program, you will be greeted with an introduction to the haunted mansion. You’ll be given the option to either **enter** the mansion or **leave**.
   
2. **Make Decisions**: As you progress through the game, you’ll face various encounters. You can choose between different actions like "fight", "talk", "run", or "join". Your choices will determine the path you take and the outcome of the story.

3. **Quit the Game**: At any time, you can type **`stop`** to exit the game.

4. **Endings**: There are multiple possible endings based on your choices, such as becoming a vampire, escaping the mansion, or succumbing to the forces inside.

## Code Overview

### Structure:
- **Modular Functions**: The game is divided into functions based on different scenes and encounters (e.g., `enter_house()`, `vampire_encounter()`, `werewolf_encounter()`).
- **Randomized Outcomes**: The encounters with creatures like vampires, werewolves, and witches use randomization to give different results each time, creating replayability.
- **Lists for Choices**: The game tracks player decisions using lists (`choices_made`), which allows for flexible outcome generation and summary reporting.

### Code Features:
- **Input Validation**: Ensures players enter valid options such as "enter", "fight", "run", etc.
- **User Interaction**: Clear instructions and feedback are provided at each decision point to guide the player.
- **No External Libraries**: Only standard Python functions are used, making the game lightweight and easy to run in any Python environment.

### Code Example:

```python
def enter_house():
    """Handles the logic and choices for entering the haunted house."""
    print("\nYou step inside the mansion. The air is cold, and the floors creak beneath your feet.")
    print("You see a staircase leading upstairs, a hallway that seems to stretch endlessly, and a door to your left with a strange glowing symbol on it.")
    
    while True:
        user_choice = input("Do you want to go 'upstairs', 'explore' the hallway, or 'open' the strange door? Type your choice: ").lower()
        if user_choice == "stop":
            print("Thanks for playing! Goodbye.")
            break
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
```

### Major Sections:
- **Story Logic**: Each encounter in the mansion is designed to give the player multiple choices, which are then validated before proceeding.
- **Outcome Randomization**: When encountering vampires, werewolves, and witches, outcomes are randomly selected from a list to keep gameplay fresh.

## License

This project is open-source and free to use. You can modify and distribute it under the terms of the **MIT License**.

## Acknowledgements

- **Python**: The game is built using Python, an excellent programming language for text-based applications.
- No external libraries or frameworks were used, making it lightweight and easy to execute without dependencies.

---

### **Additional Resources**
- If you're interested in contributing, feel free to submit pull requests to improve the game’s logic, add new features, or fix bugs.
- You can explore additional Python libraries like **`curses`** or **`tkinter`** for adding graphical interfaces or more complex gameplay mechanics in future versions.

---

### **Game Credits**
- **Developer**: Tanisha Shankpal
- **Version**: 1.0
- **Release Date**: 16-Nov-2024

---

This **`README.md`** file provides all the necessary information for users to run the game, understand its functionality, and get a brief overview of the development process. It also includes instructions, code examples, and highlights the key features of the game.
