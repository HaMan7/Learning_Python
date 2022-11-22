#Hauwa
# Create the Rock, Paper, Scissors game with python.
#The rules of the game are:
#1. Rock wins Scissors
#2. Paper wins Rock
#3. Scissors wins Paper
import random


selection_list = ["r", "p", "s"]
print(f"Please use the first letter to Make a selection from the list:",selection_list)
com_choice = random.choice(selection_list)
user_choice = input("Choice:")

win = True

if user_choice in com_choice:
    print(f"You chose: {user_choice}, Computer Chose: {com_choice}")
    if user_choice == com_choice:
        print("You made same selection, Try again")
    elif user_choice == "r":
        if com_choice == "s":
            print("Rock crushes Scissors, You win")
        else:
            print("Paper covers rock, You Loose!")
    elif user_choice == "p":
        if com_choice == "r":
            print("Paper covers rock, You win!!")
        else:
            print("Scissors Cuts paper, You Loose!!")
    elif user_choice == "s":
        if com_choice == "p":
            print("Scissors cuts Paper, you Win!!")
        else:
            print("Rock Smashes Paper, You Loose!!")
else:
    print("Invalid Input!!")
        
    