#Private Critter

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, mood):
        print "A new critter has been born!"
        self.name = name
        self.__mood = mood

    def talk(self):
        print "\nI'm", self.name
        print "Right now i feel", self.__mood, "\n"

    def __private_method(self):
        print "This is a private method."

    def public_method(self):
        print "This a public_method"
        self.__private_method()

#main

crit = Critter(name = "Poochie", mood = "Happy")
crit.talk()
crit.public_method()

raw_input("\n\nPress the enter key to exit.")
