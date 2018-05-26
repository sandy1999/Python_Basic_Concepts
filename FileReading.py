"""
A script to read file as in text format
"""

from sys import argv
#unpacking the variables as a arguments
script,filename = argv

#printing the file name that is been asked to read 
print("Reading your file - {} :".format(filename))

# opening the file as specified by the user.
text = open(filename)

#printing all the data that is present in our file 
print(text.read())

#Asking a user to enter a new file name 
filename = input("Enter a name of new file or again\n >")

# again opening the file 
text_again = open(filename)

#printing the contents of file 
print(text_again.read())

#closing the files and destroying the file objects 
text.close()
text_again.close()