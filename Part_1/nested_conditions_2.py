# Task 2 Setting the Scene

#  If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", 
#and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest": 
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": 
        print("You found a boat!")
elif place == "cave": 
    action = input("Do you want to light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Good idea, this cave is very dark, and now you can see.")
    elif action == "proceed in the dark":
        print("You might want to reconsider, as you'll probably need a torch!")
    else:
        print("You must choose between the torch and the dark!")
else:
    pass