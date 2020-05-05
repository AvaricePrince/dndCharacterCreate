import linecache as line

_Character = {"pname":"", "fname":"", "lname":"","level":"", "race":"", "class":"", "alignment":""}
Items = {}


def _MakeACharacter():
    newCharacter = input("Hello Adventurer, would you like to create a new character? Y/N ").capitalize()
    if newCharacter == "Y":
        updatePName()
        updateCName()
        updateLevel()
        updateRace()
        updateClass()
        updateAlignment()
        updateBackground()
        saveCharacter()
        print("Character created succesfully ")
        addStuff()
    elif newCharacter == "N":
        lookUp = input("Would you like to look up a character? Y/N ")
        if lookUp.capitalize() == "Y":
            lookUpCharacter()
        elif lookUp.capitalize() == "N":
            print("Have a good day adventurer!")
    else:
        print("Try again")
        _MakeACharacter()

def lookUpCharacter():
    num = input("Which character do you want to see? ")
    print(line.getline("Character.txt", int(num)))
    print(line.getline("stuff.txt", int(num)))

def updatePName():
    name = input("What is your irl name? ")
    _Character["pname"]=name
    print("Okay, your name is: " + name)

def updateCName():
    fname = input("First name: ").capitalize()
    lname = input("Last name: ").capitalize()
    _Character["fname"] = fname
    _Character["lname"] = lname
    print("Your name is: " + fname, lname)

def updateRace():
    race = input("What is your race? ").capitalize()
    _Character["race"] = race
    print("You are a " + race)

def updateClass():
    _class = input("What is your class? ").capitalize()
    _Character["class"] = _class
    print("Your class is " + _class)

def updateLevel():
    level = input("What level are you? Level: ")
    _Character["level"] = level
    print("You're level " + level)

def updateAlignment():
    align = input("What is your alignment?")
    _Character["alignment"] = align
    print("Okay, your alignment is: " + align)

def updateBackground():
    bg = input("What is your background? ")
    _Character["background"] = bg
    print("Your background is: " + bg)

def saveCharacter():
    f = open("Character.txt", "a")
    f.write( str(_Character) + "\n" )
    f.close()

def readSavedCharacter():
    f = open("Character.txt", "r")
    print(f.read())

def addStuff():
    stuff = input("Do you have any items? Y/N ")
    if stuff.capitalize() == "Y":
        item = input("What item do you have? ")
        amount = input("How much of the item do you have? ")
        if amount.isdigit() is False:
            print("Amount has to be a number")
            addStuff()
        Items[item] = amount
        addStuff()
    elif stuff.capitalize() == "N":
        print("no items added")
        saveStuff()
        for key, val in Items.items():
            print("You have " + val + " " + key)
    else:
        print("invalid")
        addStuff()

def saveStuff():
      f = open("stuff.txt", "a")
      f.write( str(Items) + "\n")
      f.close()

_MakeACharacter()