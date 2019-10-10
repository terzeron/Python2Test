#!/usr/local/bin/python

age = 0
def setAge(a):
    global age # comment this line
    age = a

setAge(100)
print age
