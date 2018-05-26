"""
A py script for writing into a file and then reading the stuff 
"""
#import lib to read argument variables 
from sys import argv 

#unpacing the variables 

script,filename = argv

#printing some questional statements for users

print(f"I am going to erase all the contents of {filename}")
print("If you want to stop operation press CLT-C (^C)")
print("If not then press enter")

#taking a user input
input("?")

#creating an object of file
target = open(filename,'w')

#erasing all the data of files
target.truncate()

#taking user input for writing in the file 
line1 = input("Enter line 1 to be saved: ")
line2 = input("Enter line 2 to be saved: ") 
line3 = input("Enter line 3 to be saved: ") 

#writing all the lines 
target.write("{}\n{}\n{}\n".format(line1,line2,line3))

#printing the file contents
print("The contents of file you wrote are been written ")

#closing and deleting file object

