"""
A script to copy and paste contents of a file.
"""

#importing arv function
from sys import argv
from os.path import exists

#unpacking argv variables.
script,in_file,out_file = argv

#reading input data form input file
in_data = open(in_file).read()

#prompting if the user wants to continue this op or not 
print("Does the output file exsist ? {}".format(exists(out_file)))
print("Hit Enter to continue and CLT-C to stop this operation")
input()

#writing data in the file
open(out_file,'w').write(in_data)

#final output of the script.
print("Data written sucessfully in the file")