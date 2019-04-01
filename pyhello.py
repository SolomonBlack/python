import time

class Printer(object):
    def Helloprinter(self):
        print('This is going to print hello 5 times!')
        print("Hello hello hello hello hello")
        print("Now lets save it as a variable!")
        Hello = "Hello"
        print("Now lets print the variable 5 times!")
        Hello5 = Hello * 5
        print(Hello5)
        print("Now lets use a for loop!")
        for i in range(0, 6):
            print(Hello)
        print("Now a while loop!")
        while i <= 5:
            print(Hello)
            i += 1
        print("Done done done!")

    def GoodByeprinter(self):
        print('This is going to print goodbye 5 times!')
        print("Good Good Good Good Bye")
        print("Now lets save it as a variable!")
        goodbye = "Goodbye"
        print("Now lets print the variable 5 times!")
        goodbye5 = goodbye * 5
        print(goodbye)
        print("Now lets use a for loop!")
        for i in range(0, 6):
            print(goodbye)
        print("Now a while loop!")
        while i <= 5:
            print(goodbye)
            i += 1
        print("Done done done!")



Printer = Printer()
#Printer.Helloprinter()
Printer.GoodByeprinter()
