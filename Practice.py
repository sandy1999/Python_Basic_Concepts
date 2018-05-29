"""
A python script to brush all the above concepts
"""

print("Let's Practice everything that you know.")
print("You'd need to know \'bout escapes with \\ that do:")
print('\n new lines and \t tabs.')

poem = """
\t Lovely World
with logic so firmly planted
cannot discern \n the needs of love
nor compherend passion from intution 
and requires an explanation
\n\t\n where there is none
"""
print("-----------------------")
print(poem)
print("-----------------------")

# a variable 
five = 10 - 2 + 3 -6
print(f'This should be five {five}')

# function example 
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 10

    # returning the values 
    return jelly_beans , jars, crates

# start_point for function 
start_point = 1000
beans, jars, crates  = secret_formula(start_point)

# printing the values using a formatted values 
print('With a starting point of {}'.format(start_point))
print("'We'd have {0} beans, {1} jars and {2} crates".format(beans,jars,crates))

# new start point and invoking 
formula = secret_formula(start_point/10)

# using a multipe arguments method to print using *  
print("We'd like to have {} beans, {} jars and {} crates".format(*formula))