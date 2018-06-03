"""
A py script to understand the concepts of While Loop 
"""

i = 0 # a int initailzed to 0
numbers = [] # an empty list named numbers 

# creating a while loop that runs till i less than 6
while i < 6:
    # print the top most number 
    print("At the top {}".format(i))

    # insert the value of i in numbers 
    numbers.append(i)

    # incrementing the value of i by 1 
    i += 1

    # print numbers list 
    print("The numbers list now : {}".format(numbers))

    # printing the values of i after updation 
    print("The value of i at the bottom : {}".format(i))


# printing the numbers list using a for loop 
for number in numbers:
    print("The number is : {}".format(number))