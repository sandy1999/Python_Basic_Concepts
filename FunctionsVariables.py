"""
A py script to showcase some functions and how to pass parameters 
"""

#definig our function 
def cheese_and_crackers(cheese_count,cracker_count):
    print("You have {} amount of cheese".format(cheese_count))
    print("You have {} crackers in your store".format(cracker_count))
    print("This is ample call your gang and get ready to party")
    print("Dont forget to grab a blanket")

#directly passing param values 
print("You can pass direct values")
cheese_and_crackers(10,20)

#using variables to pass the values 
print("You can use some variables to pass the values")
amount_cheese = 20
amount_crackers = 50
cheese_and_crackers(amount_cheese,amount_crackers)

#using a combination of both the types 
print("Or you can combine both and apply maths")
cheese_and_crackers(amount_cheese+10,amount_crackers+20)