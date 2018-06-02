"""
A py script to make a more use of if else to take some decisions
"""

print(""" You Entered a dark room with two doors.
Do you go through door #1 or #2 """)

door = input("> ")

# check which door picked 
if door == "1":
    print("There is a giant bear eating a cheese cake")
    print("What do you do?")
    print("1. Eat his cake")
    print("2. Scream at bear")

    bear = input("> ") 
    # conditions based on input after door 1 
    if bear == "1":
        print("The Bear eat's your face off. Good Job")
    elif bear =="2":
        print("The bear eat's your legs off. Good Job")
    else:
        print("Well, Doing {} bear is better ".format(bear))
        print("Bear runs away")

# if door two selected
elif door == "2":
    print("You stare into endless abyss of chutlu's retina")
    print("1. Blueberries")
    print("2. yellow jacket clothespins")
    print("3. understanding revolvers yelling melodies")

    # conditions based after door selection 2 
    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives by the mind of jello.")
        print("Good Job")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good Job")
# if none of the two doors selected.
else:
    print("You stumble around and fall on knife. Good Job.")