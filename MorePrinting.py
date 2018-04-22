print("Mary had a little lamb")
print("Its fleece was as soft as {}".format("snow"))
print("And everywhere that lamb went")
print("." * 10)

end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e' 
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

print(end1+end2+end3+end4+end5+end6,end=' ')
print(end7+end8+end9+end10+end11+end12)

#More Printing, Printing

formatter = '{} {} {} {}'
print(formatter.format(1,2,3,4))
print(formatter.format("one",'two','three','four'))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Try your own",
    "text here",
    "Maybe a poem",
    "Or a song about fear"
))


# Using some tags or blackslash

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food 
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)