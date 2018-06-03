"""
A py script demonstarating loops and lists 
"""

# creating a new list named count 
count = [1,2,3,4,5]

# list of fruits
fruits = ['apples','oranges','pears','appricots']

# list of changes
the_change = [1,'pennies',2,'dimes',3,'quaters']

# a for loop to traverse lists
for number in count:
    print("This is count {}".format(number))

# a loop to traverse fruits 
for fruit in fruits:
    print("We have {}".format(fruit))

# we can also traverse mixed arrays 
for change in the_change:
    print("I got {}".format(change))

# we can also build list 
elements = [] # an var name element with empty list

# for loop in range of 0-6
for i in range(0,6):
    
    # adding into list using appned method 
    elements.append(i)

# printing the elements list
for element in elements:
    print("Element: {}".format(element))