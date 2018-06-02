"""
A py script to understand concepts and working of if else statements 
"""

people = 30
cars = 40
trucks = 15

# check if cars < people 
if people > cars:   
    print("Let's take a car")
    # if not check wether people > cars 
elif people < cars:
    print("We Should not take cars")
# if every thing fails print this
else:
    print("We cant decide.")

# check conditions betwen trucks and cars 
# check if truk more than cars 
if trucks > cars:
    print("There are too many trucks")
elif trucks < cars: # check truck less than cars
    print("Lets take trucks")
else: # when every condition fails
    print("We Still can't decide")

# check between people and truck 
# if people more than truck
if people > trucks:
    print("Finally lets take trucks")
else: # last condition if every thing fails
    print("Fine, lets cancel the plan")