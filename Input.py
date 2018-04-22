# This module is intented to get insights of how to take input in python

print("How old are you ? ",end=" ")
age = input()
print("How tall are you ? ",end=' ')
height = input()
print("How much do you weigh ? ", end= ' ')
weight = input()

print(f"So you're {age} old, {height} tall and {weight} heavy.")

# Prompting the people 

age = int(input("How old are you? "))
height = input("How tall are you? ")
weight = float(input("How much do you weigh? "))

print("So you're {} old, {} tall and {} heavy.".format(age,height,weight))