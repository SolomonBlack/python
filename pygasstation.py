"""
This is a Gas Station simulation using object oriented programming

The scenario is that a guy has a car,
needs Gas
has money
and needs to pay either a cashier or a machine
"""

import os, time

class Car(object):
    def __init__(self, cartank=0, fulltank=0):
        print("This car class is now built")
        Car.cartank = cartank
        Car.fulltank = fulltank
        print("This tank has", self.cartank, "gallons of fuel")
        print("This tanks max is", self.fulltank, "gallons of fuel")

    def update_tank(self):
        if Person.selection > 3:
            print("Your car tank is still the same.")
        elif Person.selection == 0:
            print("Your car tank is still the same.")
        elif Person.selection < 0:
            print("Your car tank is still the same.")
        elif Person.useramount <= 0 and Person.selection == 1 or 2 or 3:
            print("You need to pay before you can pump gas to car")
        elif Person.selection == 1 or 2 or 3 and Person.useramount > 0:
            print("Car tank filling up...")
            Car.cartank += 1 * Person.useramount
            print(Car.cartank)

class GasStation(object):
    def __init__(self, gastationtank=0, unleaded=0, super=0, premium=0):
        print("This gasstation class is now built")
        GasStation.gastationtank = gastationtank
        GasStation.unleaded = unleaded
        GasStation.super = super
        GasStation.premium = premium
        print("This tank has", self.gastationtank, "gallons of fuel")
        print("Hello and welcome to your local gas station, what can i get for you today?")
        print("The prices for gas are as followed:")
        print(self.unleaded, "/Gallon for unleaded")
        print(self.super, "/Gallon for super")
        print(self.premium, "/Gallon for premium")

    def update_gasstationtank(self):
        if Person.selection == 0:
            print("This Gas station is still full")
        elif Person.selection > 3:
            print("This Gas station is still full")
        elif Person.selection < 0:
            print("This Gas station is still full")
        elif Person.useramount <= 0 and Person.selection == 1 or 2 or 3:
            print("You need to pay before you can get gas from pump")
        elif Person.selection == 1 or 2 or 3 and Person.useramount > 0:
            print("Filling tank from main tank...")
            GasStation.gastationtank -= 1 * Person.useramount
            print(GasStation.gastationtank)

class Person(object):
    def __init__(self, money=0):
        self.money = int(money)
        print("This person class is now built")
        print("This guy has", self.money, "bucks on him")

    def givemoney(self):
        self.useramount = int(input("Enter the desired amount of money you want to pay for gas: "))
        self.selection =  int(input("Select the type of gas you want(1, 2, or 3)"))
        if self.useramount > 0:
            print("Giving", int(self.useramount) ,"to requested person")
            while self.useramount and self.selection != "0":
                if self.selection == 1:
                    print("You have selected Unleaded")
                    print("Total comes out too", self.useramount * GasStation.unleaded)
                    self.unleadedtotal = self.useramount * GasStation.unleaded
                    break
                elif self.selection == 2:
                    print("You have selected super")
                    print("Total comes out too", self.useramount * GasStation.super)
                    self.supertotal = self.useramount * GasStation.super
                    break
                elif self.selection == 3:
                    print("You have selected premium")
                    print("Total comes out too", self.useramount * GasStation.premium)
                    self.premiumtotal = self.useramount * GasStation.premium
                    break
                elif self.selection <= 0:
                    print("You need to make a proper selection")
                    print("Wallet is still the same")
                    break
                elif self.selection > 3:
                    print("You need to make a proper selection")
                    print("Wallet is still the same")
                    break
        elif self.selection == 1 or 2 or 3 and self.useramount <= 0:
            print("I need your money")
            print("Wallet is still the same")
        elif self.useramount <= 0:
            print("This Gas station does not give away free gas")
            print("Your wallet is still the same")

    def update_wallet(self):
        if self.selection == 1 or 2 or 3:
            if self.selection == 1:
                self.unleadedtotal = self.useramount * GasStation.unleaded
                self.money = self.money - self.unleadedtotal
                print("person now has...", self.money, "in his pocket")
            elif self.selection == 2:
                self.supertotal = self.useramount * GasStation.super
                self.money = self.money - self.supertotal
                print("person now has...", self.money, "in his pocket")
            elif self.selection == 3:
                self.premiumtotal = self.useramount * GasStation.premium
                self.money = self.money - self.premiumtotal
                print("person now has...", self.money, "in his pocket")
        elif self.selection <= 0:
            print("Sorry, please try again")
        elif self.selection >= 3:
            print("Sorry, please try again")

#main code

Person = Person(100)
Car = Car(10, 40)
Gasstation = GasStation(5000, 3.87, 4.87, 5.87)

Person.givemoney()
Person.update_wallet()
Gasstation.update_gasstationtank()
Car.update_tank()

input("Thank you. \nPress any key to exit")
