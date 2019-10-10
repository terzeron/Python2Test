#!/usr/local/bin/python

print "Please select a shape:"
print "1 Rectangle"
print "2 Circle"

shape = input("> ")

if shape == 1:
    height = input("Please enter the height: ")
    width = input("Please enter the width: ")
    area = height * width
    print "The area is", area
else:
    radius = input("Please enter the radius: ")
    area = 3.14 * (radius ** 2)
    print "The area is", area
    
