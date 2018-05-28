"""
A py script to play around with files and functions.
"""

from sys import argv

script,input_file = argv

# a function to print all the data from file
def print_all(f):
    print(f.read())

# a function to take file to position 0
def rewind(f):
    f.seek(0)

# a function to read file line  
def print_line(line_number,f):
    print(line_number,f.readline())

# creating a object of input file
current_file = open(input_file)

#printing complete file
print("Lets print a complete line:")
print_all(current_file)

# rewinding the file 
print("Lets rewind our file just like a tape\n")
rewind(current_file)

#printing the file line wise
print("Lets print first 3 lines of file")
for i in range(1,4):
    print_line(i,current_file)