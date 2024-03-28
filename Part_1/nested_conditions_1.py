# Task 1: Code Correction

# Buggy

place = input("Choose a place: forest or cave? ")

if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!")

# Corrected
    
place = input("Choose a place: forest or cave? ")

if place == "forest": # Fix comparison operators
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": # Elif should be here
        print("You found a boat!")
else: # Else should be here / removed unnecessary comparison
    print("You find a hidden treasure!")