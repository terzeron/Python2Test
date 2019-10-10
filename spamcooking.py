#!/usr/local/bin/python

from time import sleep

print "Please start cooking the spam. (I'll be back in 3 minutes.)"

sleep(180)

print "I'm back :)"

hot_enough = 50

temperature = input("How hot is the spam? ")
while temperature < hot_enough:
    print "Not hot enough... Cook it a bit more..."
    sleep(30)
    temperature = input("OK. How hot is it now? ")

print "It's hot enough - You're done! "
