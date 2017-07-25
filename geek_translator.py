#geek translator
#demonstrates using dictionaries

geek = { "404" : "clueless. From the web error message 404, meaning page not found.",
"googling" : "searching the internet for background information on a person.",
"Keyboard Plaque" : "the collection of debris found in computer keyboards.",
"Link Rot" : "the process by which web page links become obsolete.",
"Percussive Maintenance" : "the act of shrinking an electronic device to make it work.",
"Uninstalled" : "being fired. Especially popular during the dot-bomb era."
}

choice = None
while choice != "0":

    print \
    """
    Geek translator

    0 - Quit
    1 - Look Up a geek Term
    2 - Add a Geek Term
    3 - Redefine a geek Term
    4 - Delete a Geek Term
    """

    choice = raw_input("Choice: ")
    print

    if choice == "0":
        print "Good-bye."
    elif choice == "1":
        term = raw_input("What term do you want me to translate?: ")
        if term in geek:
            definition = geek[term]
            print "\n", term, "means", definition
        else:
            print "\nSorry, I don't know", term
    elif choice == "2":
        term = raw_input("What term do you want me to add?: ")
        if term not in geek:
            definition = raw_input("What's the definition?: ")
            geek[term] = definition
            print "\n", term, "has been added"
        else:
            print "\nThat term already exist! Try redefining it."
    elif choice == "3":
        term = raw_input("What term do you want me to redefine?: ")
        if term in geek:
            definition = raw_input("Whats the new definition?: ")
            geek[term] = definition
            print "\n", term, "has been redefined"
        else:
            print "\nThat term doesn't exist! Try adding it."
    elif choice == "4":
        term = raw_input("What term do you want me to delete?: ")
        if term in geek:
            del geek[term]
            print "\Okay, I deleted", term
        else:
            print "\nI can't do that!", term, "doesn't exist in the dictionary"
    else:
        print "\nSorry, but", choice, "isn't a valid choice."
