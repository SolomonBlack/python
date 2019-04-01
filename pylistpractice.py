"""
print('Enter the name of cat 1 : ')
catname = input()
print('Enter the name of cat 2 : ')
catname2 = input()
print('Enter the name of cat 3 : ')
catname3 = input()
print('Enter the name of cat 4 : ')
catname4 = input()
print('Enter the name of cat 5 : ')
catname5 = input()
print('Enter the name of cat 6 : ')
catname6 = input()

print('The cat names are:')
print(catname + ' ' + catname2 + ' ' + catname3 + ' ' + catname4 + ' ' + catname5 + ' ' + catname6)
"""

catnames = []
while True:
    print('Enter the name of cat ' + str(len(catnames) + 1) + '(Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catnames =  catnames + [name]
print('The cat names are:')
for name in catnames:
    print(' ' + name)
