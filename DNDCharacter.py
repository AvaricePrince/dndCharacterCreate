import linecache as line

_Character = {"pname":"", "fname":"", "lname":"","level":"", "race":"", "class":"", "alignment":""}
Items = {}
abilityScore = {"Strength":"", "Dexterity":"", "Constitution":"", "Intelligence":"", "Wisdom":"", "Charisma":""}


def _MakeACharacter():
    while True:
        newCharacter = input("Hello Adventurer, would you like to create a new character? Y/N ").capitalize()
        if newCharacter == "Y":
            updatePName()
            updateCName()
            updateLevel()
            updateRace()
            updateClass()
            updateAlignment()
            updateBackground()
            updateAbilityScore()
            saveCharacter()
            saveAbilityScore()
            print("Character created succesfully ")
            addStuff()
        elif newCharacter == "N":
            lookUp = input("Would you like to look up a character? Y/N ")
            if lookUp.capitalize() == "Y":
                lookUpCharacter()
            elif lookUp.capitalize() == "N":
                dele = input("Delete Everything? Y/N ")
                if dele.capitalize() == "Y":
                    clearAllCharacters()
                    print("All characters have been deleted!")
                elif dele.capitalize() == "N":
                    print("Have a good day Adventurer! ")
                    break
        else:
            print("Try again")
            continue

def lookUpCharacter():
    while True:
        num = input("Which character do you want to see? ")
        if str.isdigit(num):
            if line.getline("Character.txt", int(num)) != '\n':
                print(line.getline("Character.txt", int(num)))
                print(line.getline("stuff.txt", int(num)))
                print(line.getline("ability.txt", int(num)))
                break
            else:
                print("Character does not exit, please try again ")
                continue
        else:
            print("Please enter a row number")
            continue

def updatePName():
    name = input("What is your irl name? ").capitalize()
    _Character["pname"]=name
    print("Okay, your name is: " + name)

def updateCName():
    fname = input("Character's First name: ").capitalize()
    lname = input("Character's Last name: ").capitalize()
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
    while True:
        try:
            level = int(input("What level are you? Level: "))
        except ValueError:
            print("Invalid number")
            continue
        _Character["level"] = str(level)
        print("You're level " + str(level))
        break

def updateAlignment():
    align = input("What is your alignment? ").capitalize()
    _Character["alignment"] = align
    print("Okay, your alignment is: " + align)

def updateBackground():
    bg = input("What is your background? ").capitalize()
    _Character["background"] = bg
    print("Your background is: " + bg)

def updateAbilityScore():
    # mod = 0
    while True:
        try:
            st = int(input("What did you roll for strength? "))
            if st < 2:
                abilityScore["Strength"] = (st, "Modifier: -5")
            elif st <= 3: 
                abilityScore["Strength"] = (st, "Modifier: -4")
            elif st <= 5:
                abilityScore["Strength"] = (st, "Modifer: -3")
            elif st <= 7:
                abilityScore["Strength"] = (st, "Modifier: -2")
            elif st <= 9:
                abilityScore["Strength"] = (st, "Modifier: -1")
            elif st <= 11:
                abilityScore["Strength"] = (st, "Modifier: 0")
            elif st <= 13:
                abilityScore["Strength"] = (st, "Modifier: +1")
            elif st <= 15:
                abilityScore["Strength"] = (st, "Modifier: +2")
            elif st <= 17:
                abilityScore["Strength"] = (st, "Modifier: +3")
            else:
                print("Invalid entry")
                continue

            dex = int(input("What did you roll for Dexterity? "))
            if dex < 2:
                abilityScore["Dexterity"] = (dex, "Modifier: -5")

            elif dex <= 3: 
                abilityScore["Dexterity"] = (dex, "Modifier: -4")

            elif dex <= 5:
                abilityScore["Dexterity"] = (dex, "Modifer: -3")

            elif dex <= 7:
                abilityScore["Dexterity"] = (dex, "Modifier: -2")

            elif dex <= 9:
                abilityScore["Dexterity"] = (dex, "Modifier: -1")

            elif dex <= 11:
                abilityScore["Dexterity"] = (dex, "Modifier: 0")
 
            elif dex <= 13:
                abilityScore["Dexterity"] = (dex, "Modifier: +1")

            elif dex <= 15:
                abilityScore["Dexterity"] = (dex, "Modifier: +2")

            elif dex <= 17:
                abilityScore["Dexterity"] = (dex, "Modifier: +3")

            else:
                print("Invalid entry")
                continue

            con = int(input("What did you roll for Constitution? "))
            if con < 2:
                abilityScore["Constitution"] = (con, "Modifier: -5")

            elif con <= 3: 
                abilityScore["Constitution"] = (con, "Modifier: -4")

            elif con <= 5:
                abilityScore["Constitution"] = (con, "Modifer: -3")

            elif con <= 7:
                abilityScore["Constitution"] = (con, "Modifier: -2")

            elif con <= 9:
                abilityScore["Constitution"] = (con, "Modifier: -1")

            elif con <= 11:
                abilityScore["Constitution"] = (con, "Modifier: 0")
              
            elif con <= 13:
                abilityScore["Constitution"] = (con, "Modifier: +1")
               
            elif con <= 15:
                abilityScore["Constitution"] = (con, "Modifier: +2")
              
            elif con <= 17:
                abilityScore["Constitution"] = (con, "Modifier: +3")
               
            else:
                print("Invalid entry")
                continue

            intel = int(input("What did you roll for Intelligence? "))
            if intel < 2:
                abilityScore["Intelligence"] = (intel, "Modifier: -5")
               
            elif intel <= 3: 
                abilityScore["Intelligence"] = (intel, "Modifier: -4")
           
            elif intel <= 5:
                abilityScore["Intelligence"] = (intel, "Modifer: -3")
                
            elif intel <= 7:
                abilityScore["Intelligence"] = (intel, "Modifier: -2")
               
            elif intel <= 9:
                abilityScore["Intelligence"] = (intel, "Modifier: -1")
             
            elif intel <= 11:
                abilityScore["Intelligence"] = (intel, "Modifier: 0")
             
            elif intel <= 13:
                abilityScore["Intelligence"] = (intel, "Modifier: +1")
       
            elif intel <= 15:
                abilityScore["Intelligence"] = (intel, "Modifier: +2")
              
            elif intel <= 17:
                abilityScore["Intelligence"] = (intel, "Modifier: +3")
    
            else:
                print("Invalid entry")
                continue

            wis = int(input("What did you roll for Wisdom? "))
            if wis < 2:
                abilityScore["Wisdom"] = (wis, "Modifier: -5")
        
            elif wis <= 3: 
                abilityScore["Wisdom"] = (wis, "Modifier: -4")
             
            elif wis <= 5:
                abilityScore["Wisdom"] = (wis, "Modifer: -3")
             
            elif wis <= 7:
                abilityScore["Wisdom"] = (wis, "Modifier: -2")
              
            elif wis <= 9:
                abilityScore["Wisdom"] = (wis, "Modifier: -1")
        
            elif wis <= 11:
                abilityScore["Wisdom"] = (wis, "Modifier: 0")
        
            elif wis <= 13:
                abilityScore["Wisdom"] = (wis, "Modifier: +1")
         
            elif wis <= 15:
                abilityScore["Wisdom"] = (wis, "Modifier: +2")
               
            elif wis <= 17:
                abilityScore["Wisdom"] = (wis, "Modifier: +3")
           
            else:
                print("Invalid entry")
                continue

            cha = int(input("What did you roll for Charisma? "))
            if cha < 2:
                abilityScore["Charisma"] = (cha, "Modifier: -5")
              
            elif cha <= 3: 
                abilityScore["Charisma"] = (cha, "Modifier: -4")
              
            elif cha <= 5:
                abilityScore["Charisma"] = (cha, "Modifer: -3")
             
            elif cha <= 7:
                abilityScore["Charisma"] = (cha, "Modifier: -2")
                
            elif cha <= 9:
                abilityScore["Charisma"] = (cha, "Modifier: -1")
               
            elif cha <= 11:
                abilityScore["Charisma"] = (cha, "Modifier: 0")
                
            elif cha <= 13:
                abilityScore["Charisma"] = (cha, "Modifier: +1")
                
            elif cha <= 15:
                abilityScore["Charisma"] = (cha, "Modifier: +2")
                
            elif cha <= 17:
                abilityScore["Charisma"] = (cha, "Modifier: +3")
               
            else:
                print("Invalid entry")
                continue

        except ValueError:
            print("Not a valid number")
            continue
        else:
            return st,dex,con,intel,wis,cha
            break
    saveAbilityScore()
      
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

def saveAbilityScore():
    f = open("ability.txt","a")
    f.write( str(abilityScore) + "\n")
    f.close()

def clearAllCharacters():
    f = open("Character.txt", "w").close()
    f = open("stuff.txt", "w").close()
    f = open("ability.txt", "w").close()

_MakeACharacter()