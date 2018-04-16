# A script to give you some examples of variables in python 

# cars we have
cars = 100
#space in each car
space_in_a_car = 4.0
#no of drivers available today
drivers  = 30
# No passengers to be carpooled
passengers = 90
# No of cars not driven today
cars_not_driven = cars - drivers
# No of cars driven
cars_driven = drivers
# Carpooling capacity of driven cars
carpool_capacity = cars_driven * space_in_a_car
# Average passengers that can be accomodated in a car 
average_passenger_per_car = passengers / cars_driven

print("There are ",cars,"cars available")
print("There are only ",drivers,"drivers available") 
print("There will be ",cars_not_driven," empty cars today")
print("We can transport ",carpool_capacity," passengers today")
print("We have ",passengers," passengers to car pool today")
print("We need to put about ", average_passenger_per_car," in each car")

# some more variable and printing 

my_name = "Sanidhya"
my_age = 20
my_height = 1.76 #cm
my_weight = 178 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Black'

print(f"Lets talk about {my_name}")
print(f"He is {my_height} inches tall")
print(f"He is {my_weight} pounds heavy")
print("Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"He's teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_weight}, {my_height} I get {total}") 