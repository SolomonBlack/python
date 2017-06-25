from sys import exit

"""

The idea for this script is to simulate a typical moment
when you arrive at an atm

Steps for this include:
1. Arriving at the atm as someone with a card
2. Inserting card
3. Having the atm ask for a pin number
4. Entering the pin number
5. Having a series of options to choose from and choosing one
6. picking a number based off that choice
7. changing the persons account based off that number
8. Giving the user the option to quit or star over
9. end script
"""

User_1 = {"name" : "Steve", "Pin": 3489}
User_2 = {"Name" : "Tom", "Pin" : 7287}

#1. Arriving at the atm as someone with a card
print " Hello and welcome to this atm, please insert your card to acess your account"

insert = raw_input("> ")

#2. Inserting card
print "You have inserted your card for account for"

#Insert card name here

print "Is this correct?"

yes/no = raw_input("> ")

#3. Having the atm ask for a pin number

print "Please enter your card pin number to continue"

#4. Entering the pin number

Pin_input = raw_input("> ")

#5. Having a series of options to choose from and choosing one

print "Hello"  #"Please select from one of the following options"

print "Withdraw"
print "Deposit"
print "Transfer"
print "Check account Balance"

#6. picking a number based off that choice

# selection = raw_input("> ")

#7. changing the persons account based off that number

#8. Giving the user the option to quit or star over

#9. end script
print "Thank you for using this atm!"
