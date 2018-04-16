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