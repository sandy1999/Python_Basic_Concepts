"""
A py script to deal with functions and its branches in a ternary way 
"""

# importing exit form sys 
from sys import exit

# a fucntion to define gold room 
def gold_room():
    print("The room is full of Gold. How much did you take ?")
    choice = input('> ')
    # check if choice is int or noe
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        # if not int pass it in dead function 
        dead("Man, learn to type a number ")
    
    # check if how_much less than 50
    if how_much < 50:
        print("Nice you are not greedy, Congratulations you win")
        # exit with status 0
        exit(0)
    else:
        dead("You greed bastard !")

# bear room function goes here 
def bear_room():
    print("There is a bear in the room")
    print("The bear has bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you going to move a fat bear.")

    bear_moved = False # declaring bear moved to false

    # a while loop to iterate untill bear moves 
    while True:
        # taking an input from user
        choice = input("> ")

        # if choice is take honey
        if choice == 'take honey':
            dead("The bear looks at you then slaps your face off")
        # if bear not moved and taunt bear
        elif choice == 'taunt bear' and not bear_moved:
            bear_moved = True # assign bear moved to true
            print("The bear has moved form the door.")
            print("You can go through it now")
        # if bear moved and taunt bear 
        elif bear_moved and choice == 'taunt bear':
            dead("The bear gets pissed of and chews your legs off")
        # if bear moved and open door 
        elif bear_moved and choice == 'open door':
            # run gold room function
            gold_room()
        # finally else part
        else:
            print("I have no idea what it does")

# cthutlu room function 
def cthutlu_room():
    print("Here you see great evil Cthutlu.")
    print("Who ever stares into his eyes goes mad and insane")
    print("Do you flee for your life of eat your head off")

    # take user input 
    choice = input("> ")

    # if choice is flee
    if choice is 'flee':
        start()
    # if choice is head
    elif choice == 'head':
        dead("Well that was tasty")
    else:
        cthutlu_room()

# dead function 
def dead(why):
    print(why," Good Job!")
    exit(0)

# a start function 
def start():
    print("There is a dark room")
    print("There are two doors right and one to your left")
    print("Which one would you take")

    # taking user input 
    choice = input("> ")

    # if choice is right 
    if choice == 'right':
        cthutlu_room()
    # if choice is left
    elif choice == 'left':
        bear_room()
    else:
        dead("You stubmle upond and get stabbed by a knife")

def main():
    start()

if __name__ == '__main__':
    main()