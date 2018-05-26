"""
A script to show all the kinds of arguments in py
"""

# with multiple paramaters list
def print_two(*args):
    arg1,arg2 = args
    print("arg1 : {} and arg2 : {}".format(arg1,arg2))
#with only one param
def print_two_again(arg1,arg2):
    print("arg1 : {} and arg2 : {}".format(arg1,arg2))

#only one param 
def print_one(arg1):
    print("arg1 : {}".format(arg1))

#with an optional param 
def print_optional(arg1 = "Arg1"):
    print("arg1 : {}".format(arg1))

#with none param 
def print_noparam():
    print("I Have nothing")

print_two("Foo","Bar")
print_two_again("Foo","Bar")
print_one("Foo")
print_optional()
print_optional("Bar")
print_noparam()
