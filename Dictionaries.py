"""
A py script demonstrating the cocepts of dictonaries in py 
"""
# create a mapping of a state abbreveation 
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

# adding some cities to the state 
cities = {
    'CA': 'San Fransisco',
    'MI': 'Detorite',
    'FL': 'Jacksonvillie'
}

# adding some more cities 
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities 
print('-'*10)
print("NY state has city : {}".format(cities['NY']))
print("OR state has city : {}".format(cities['OR']))

# print some states 
print('-'*10)
print("Michigan's abbrevation is : {}".format(states['Michigan']))
print("Florida's abrevation is : {}".format(states['Florida']))

# using states dict to print city 
print('-'*10)
print("Michigan has {}".format(cities[states['Michigan']]))
print("Florida has ",cities[states['Florida']])

# print every abrevation of the states  
print('-'*10)
for state, abbrev in list(states.items()):
    print("{} is abbrevated as {} ".format(state,abbrev))

# print every city of a state 
print("-"*10)
for abbrev, city in list(cities.items()):
    print("{} has {}".format(abbrev,city))

# print state and its cities 
for state, abbrev in list(states.items()):
    print("{} is abbrevated as {} \n has city {}".format(state,abbrev,cities[abbrev]))

# safely get state value 
print('-'*10)
state = states.get('Texas')
if not state:
    print("Sorry Texas doesn't exsist")

# using a default argument to print in case list element not found 
print('-'*10)
city = cities.get('TX','Does not exsist')
print("The city for 'TX' is {}".format(city))