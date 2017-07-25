#Critter Caretaker

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __get_mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = "happy"
        elif 5 <= unhappiness <= 10:
            mood = "okay"
        elif 11 <= unhappiness <= 15:
            mood = "frustrated"
        else:
            mood = "mad"
        return mood

    mood = property(__get_mood)

    def talk(self):
        print "I'm", self.name, "and i feel", self.mood, "now.\n"
        self.__pass_time()

    def eat(self, food = 4):
        print "Brrruuuuup. Thank you."
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print "wheee!"
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = raw_input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        """
        Critter Caretaker

        0 - Quit
        1 - Listen to you critter
        2 - Feed your critter
        3 - Play with your critter
        """

        choice = raw_input("Choice: ")
        print

        #exit
        if choice == "0":
            print "Good-bye."
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print "\nSorry, but", choice, "Isn't a valid choice."

main()
("\n\nPress the enter key to exit.")
