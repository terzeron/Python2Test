#!/usr/local/bin/python

def floor(number):
    result = 0
    while result < number:
        result = result + 1
    result = result - 1
    return result

number = input("What is the number? ")
result = floor(number)
print "The floor of", number, "is", result



