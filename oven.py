#!/usr/local/bin/python

class Oven:
    def insertSpam(self, spam):
        self.spam = spam

    def getSpam(self):
        return self.spam

class Spam:
    spam = 3; 

myOven = Oven()
mySpam = Spam()
myOven.insertSpam(mySpam)
anotherSpam = myOven.getSpam();
print anotherSpam.spam;
