"""
A py script telling how a function can return a value 
"""

# a function to add two values and return it
def add(a,b):
    print("ADDING {} + {}".format(a,b))
    return a+b

# function to subract two values and return difference
def subract(a,b):
    print("SUBRACTING {} - {}".format(a,b))
    return a-b

# function to multplying two values and return product
def multiply(a,b):
    print("MULTIPLYING {} x {}".format(a,b))
    return a*b

# function to divide two numbers and return quotient
def divide(a,b):
    print("DIVIDING {} / {} ".format(a,b))
    return a/b

print("Lets perform some operation and gets it value")
age = add(30,5)
height = subract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

# printing the values of all the variables 
print(f"age : {age}, height : {height}, weight : {weight}, IQ = {iq}")

# creating a handy problem or puzzle
print("Here's a puzzle for you")

what = add(age,subract(height,multiply(weight,divide(iq,2))))

print("Can you do it by Hand ? it becomes {} ".format(what))