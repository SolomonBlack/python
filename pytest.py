#Trust Fund Buddy
#Demonstrates a logical error
print /

"""
Trust Fund Buddy

Blah Blah Blah
Blah Blah Blah

"""

car = raw_input("Lamborghini Tune-Ups: ")
car = int(car)

rent = int(raw_input("Manhattan Apartment: "))
jet = int(raw_input("Private Jet Rental: "))
gifts = int(raw_input("Gifts: "))
food = int(raw_input("Dining Out: "))
staff = int(raw_input("Staff (butlers, chef, driver, assistant): "))
guru = int(raw_input("Personal Guru and Coach: "))
games = int(raw_input("Computer Games: "))

total = rent + jet + gifts + food + staff + guru + games + car

print "\nGrand Total: ", total

raw_input("Press any key to exit.")
