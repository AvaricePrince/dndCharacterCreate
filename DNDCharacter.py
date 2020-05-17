"""
Copyright 2020, Raul Mendez, All rights reserved
"""

import linecache as line
import sys
thismodule = sys.modules[__name__]

#-----------GLOBAL VARIABLES--------#
thismodule.save = "",""
thismodule.saveBg = "",""
thismodule.sMod = ""
thismodule.dMod = ""
thismodule.cMod = ""
thismodule.iMod = ""
thismodule.wMod = ""
thismodule.chMod = ""
#-----------GLOBAL VARIABLES--------#

#==========DICTIONARIES==========#
_Character = {"pname":"", "fname":"", "lname":"","level":"", "race":"", "class":"", "alignment":"","background":""}
Items = {}
abilityScore = {"Strength":"", "Dexterity":"", "Constitution":"", "Intelligence":"", "Wisdom":"", "Charisma":"", "Proficiency Bonus":""}
savingThrows = {"Saving Strength":"", "Saving Dexterity":"", "Saving Constitution":"", "Saving Intelligence":"", "Saving Wisdom":"", "Saving Charisma":""}
# skillz = {"Acrobatics(Dex)":"","Animal Handling(Wis)":"","Arcana(Int)":"","Athletics(Str)":"","Deception(Cha)":"","History(Int)":"","Insight(Wis)":"",
# "Intimidation(Cha)":"","Investigation(Int)":"","Medicine(Wis)":"","Nature(Int)":"","Perception(Wis)":"","Persuasion(Cha)":"","Religion(Int)":"",
# "Sleight of Hand(Dex)":"","Stealth(Dex)":"","Survival(Wis)":""}
#==========DICTIONARIES==========#

#==========MAIN FUNCTION==========#
def _MakeACharacter():
    _Logo()
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
            calcSaveThrow()
            saveCharacter()
            saveAbilityScore()
            saveSaveThrows()
            print("Character created succesfully\n")
            addStuff()
        elif newCharacter == "N":
            lookUp = input("Would you like to look up a character? Y/N ")
            if lookUp.capitalize() == "Y":
                lookUpCharacter()
            elif lookUp.capitalize() == "N":
                dele = input("Delete Everything? Y/N ")
                if dele.capitalize() == "Y":
                    clearAllCharacters()
                    print("All characters have been deleted!\n")
                elif dele.capitalize() == "N":
                    print("Have a good day Adventurer!\n ")
                    break
            else:
                print("Invalid entry\n")
                continue
        else:
            print("Try again\n")
            continue
#==========MAIN FUNCTION==========#

#==========FUNCTIONS==========#
def lookUpCharacter():
    while True:
        num = input("Which character do you want to see? ")
        if str.isdigit(num):
            #checks to see if the line the user typed in is populated, .strip() finds the empty space
            if line.getline("Character.txt", int(num)).strip():
                print(line.getline("Character.txt", int(num)))
                print(line.getline("stuff.txt", int(num)))
                print(line.getline("ability.txt", int(num)))
                print(line.getline("Saving Throws.txt", int(num)))
                break
            else:
                print("Character does not exit! \n")
                break

        else:
            print("Please enter a row number\n")
            continue

def updatePName():
    name = input("What is your irl name? ").capitalize()
    _Character["pname"]=name
    print("Okay, your name is: " + name + "\n")

def updateCName():
    fname = input("Character's First name: ").capitalize()
    lname = input("Character's Last name: ").capitalize()
    _Character["fname"] = fname
    _Character["lname"] = lname
    print("Your name is: " + fname, lname + "\n")

def updateRace():
    race = {"\n-----SELECT A CLASS-----":"",1:"Dragonborn",2:"Dwarf",3:"Elf",4:"Gnome",5:"Half-Elf",6:"Halfling",7:"Half-Orc",8:"Human",9:"Tiefling",
    "**Explorer's Guide to Wildemount**":"",10:"Orc of Exandria","**Elemental Evil Player's Companion**":"",11:"Aarakocra",
    12:"Genasi",13:"Goliath","**Volo's Guide to Monsters**":"",14:"Aasimar",15:"Bugbear",16:"Firblog",17:"Goblin",18:"Hobgoblin",19:"Kenku",
    20:"Kobold",21:"Lizardfolk",22:"Orc",23:"Tabaxi",24:"Triton",25:"Yuan-ti Pureblood","**Sword Coast Adventurer's Guide**":"",
    26:"Feral Tiefling","**The Tortle Package**":"",27:"Tortle","**Eberron: Rising from the Last War**":"",28:"Changeling",29:"Kalashtar",30:"Orc of Eberron",31:"Shifter",32:"Warforged",
    "**Mordenkainen's Tome of Foes**":"",33:"Gith","**Guildmasters' Guide to Ravnica**":"",34:"Centaur",35:"Loxodon",36:"Minotaur",37:"Simic Hybrid",38:"Vedalken","**Acquisitions Incorporated**":"",
    39:"Verdan","**Locathah Rising**":"",40:"Locathah","**One Grung Above**":"",41:"Grung\n"}
    for key in race:
        print("\n" + str(key)+":",race.get(key))

    while True:
        try:
            choice = int(input("Choose your race: "))
            if choice not in range(1,42):
                print("\nRace does not exist!\n")
            else:
                _Character["race"] = race.get(choice)
                print("\nYou are a: " + _Character.get("race") + "\n")
                break
        except ValueError:
            print("Invalid, must be a number\n")
            continue

def updateClass():#TODO go back and specify constitution or charisma with c and co or c and ch!
    _class = {"\n-----SELECT A CLASS-----":"", 1:"Barbarian", 2:"Bard",3:"Cleric",4: "Druid",5: "Fighter",
    6: "Monk",7:"Paladin",8:"Ranger",9:"Rogue",10:"Sorcerer",11:"Warlock",12:"Wizard",
    "***Eberron: Rising from the Last War***":"",13:"Artificer","***Critical Role***":"",14:"Blood Hunter"}
    for key in _class:
        print(str(key) + ":", _class[key],"\n")
    while True:
        try:
            choice = int(input("Pick a Class: "))
            if choice not in range(1,15):
                print("\nRace does not exist\n")
            else:
                _Character["class"] = _class.get(choice)
                print("\nYou are a:",_Character.get("class"),"\n")

                if _class.get(choice) == "Barbarian":
                    thismodule.save = "s","c"
                    break
                elif _class.get(choice) == "Bard":
                    thismodule.save = "d","c"
                    break
                elif _class.get(choice) == "Cleric":
                    thismodule.save = "w","c"
                    break
                elif _class.get(choice) == "Druid":
                    thismodule.save = "i","w"
                    break
                elif _class.get(choice) == "Fighter":
                    thismodule.save = "s","c"
                    break
                elif _class.get(choice) == "Monk":
                    thismodule.save = "s","d"
                    break
                elif _class.get(choice) == "Paladin":
                    thismodule.save = "w","c"
                    break
                elif _class.get(choice) == "Ranger":
                    thismodule.save = "s","d"
                    break
                elif _class.get(choice) == "Rogue":
                    thismodule.save = "d","i"
                    break
                elif _class.get(choice) == "Sorcerer":
                    thismodule.save = "c","c"
                    break
                elif _class.get(choice) == "Warlock":
                    thismodule.save = "w","c"
                    break
                elif _class.get(choice) == "Wizard":
                    thismodule.save = "i","w"
                    break
                elif _class.get(choice) == "Artificer":
                    thismodule.save = "c","i"
                    break
                elif _class.get(choice) == "Blood Hunter":
                    thismodule.save = "d","i"
                    break
        except ValueError:
            print("\nMust be a number!\n")
            continue 
        except IndexError:
            print("there was an error")

def updateLevel():
    while True:
        try:
            level = int(input("What level are you? Level: "))
            if level > 20:
                print("Your level is too high!\n")
                continue
            elif level < 1:
                print("You cant be a negative level!\n")
                continue
            proBo(level)
        except ValueError:
            print("Invalid number\n")
            continue
        _Character["level"] = level
        print("You're level " + str(level) + "\n")
        break

#allows user to input their characters alignment
def updateAlignment():
    alignment = {"\n ---SELECT YOUR ALIGNMENT---":"",1:"Lawful Good",2:"Neutral Good",3:"Chaotic Good",4:"Lawful Neutral",
    5:"True Neutral",6:"Chaotic Neutral",7:"Lawful Evil",8:"Neutral Evil",9:"Chaotic Evil",0:"Unaligned"}
    for key in alignment:
        print( str(key) + ":", alignment[key],"\n")
    while True:
        try:
            align = int(input("Choose your Alignment: "))
            if align not in range(0,10):
                print("\nError: Out of range, try again\n")
            else:
                _Character["alignment"] = alignment.get(align)
                print("\nYou are a: " + _Character.get("alignment") + "\n")
                break
        except ValueError:
            print("\nInvalid, must be a number\n")
            continue

#allows user to input their characters background
def updateBackground():
    # bg = input("What is your background? ").capitalize()
    # _Character["background"] = bg
    # print("Your background is: " + bg + "\n")
    bg = {}

#allows user to input their ability scores
def updateAbilityScore(): #modifiers are here
    while True:
        try:
            st = int(input("What did you roll for strength? "))
            if st < 2:
                abilityScore["Strength"] = (st, "Modifier: ", -5)
                thismodule.sMod = -5
            elif st <= 3: 
                abilityScore["Strength"] = (st, "Modifier: ", -4)
                thismodule.sMod = -4
            elif st <= 5:
                abilityScore["Strength"] = (st, "Modifer: ", -3)
                thismodule.sMod = -3
            elif st <= 7:
                abilityScore["Strength"] = (st, "Modifier: ", -2)
                thismodule.sMod = -2
            elif st <= 9:
                abilityScore["Strength"] = (st, "Modifier: ", -1)
                thismodule.sMod = -1
            elif st <= 11:
                abilityScore["Strength"] = (st, "Modifier: ", 0)
                thismodule.sMod = 0
            elif st <= 13:
                abilityScore["Strength"] = (st, "Modifier: ", 1)
                thismodule.sMod = 1
            elif st <= 15:
                abilityScore["Strength"] = (st, "Modifier: ", 2)
                thismodule.sMod = 2
            elif st <= 17:
                abilityScore["Strength"] = (st, "Modifier: ", 3)
                thismodule.sMod = 3
            else:
                print("Invalid entry")
                continue

            dex = int(input("What did you roll for Dexterity? "))
            if dex < 2:
                abilityScore["Dexterity"] = (dex, "Modifier: ", -5)
                thismodule.dMod = -5
            elif dex <= 3: 
                abilityScore["Dexterity"] = (dex, "Modifier: ", -4)
                thismodule.dMod = -4
            elif dex <= 5:
                abilityScore["Dexterity"] = (dex, "Modifer: ", -3)
                thismodule.dMod = -3
            elif dex <= 7:
                abilityScore["Dexterity"] = (dex, "Modifier: ", -2)
                thismodule.dMod = -2
            elif dex <= 9:
                abilityScore["Dexterity"] = (dex, "Modifier: ", -1)
                thismodule.dMod = -1
            elif dex <= 11:
                abilityScore["Dexterity"] = (dex, "Modifier: ", 0)
                thismodule.dMod = 0
            elif dex <= 13:
                abilityScore["Dexterity"] = (dex, "Modifier: ", 1)
                thismodule.dMod = 1
            elif dex <= 15:
                abilityScore["Dexterity"] = (dex, "Modifier: ", 2)
                thismodule.dMod = 2
            elif dex <= 17:
                abilityScore["Dexterity"] = (dex, "Modifier: ", 3)
                thismodule.dMod = 3
            else:
                print("Invalid entry")
                continue

            con = int(input("What did you roll for Constitution? "))
            if con < 2:
                abilityScore["Constitution"] = (con, "Modifier: ",-5)
                thismodule.cMod = -5
            elif con <= 3: 
                abilityScore["Constitution"] = (con, "Modifier: ",-4)
                thismodule.cMod = -4
            elif con <= 5:
                abilityScore["Constitution"] = (con, "Modifer: ",-3)
                thismodule.cMod = -3
            elif con <= 7:
                abilityScore["Constitution"] = (con, "Modifier: ",-2)
                thismodule.cMod = -2
            elif con <= 9:
                abilityScore["Constitution"] = (con, "Modifier: ",-1)
                thismodule.cMod = -1
            elif con <= 11:
                abilityScore["Constitution"] = (con, "Modifier: ",0)
                thismodule.cMod = 0
            elif con <= 13:
                abilityScore["Constitution"] = (con, "Modifier: ",1)
                thismodule.cMod = 1
            elif con <= 15:
                abilityScore["Constitution"] = (con, "Modifier: ",2)
                thismodule.cMod = 2
            elif con <= 17:
                abilityScore["Constitution"] = (con, "Modifier: ",3)
                thismodule.cMod = 3
            else:
                print("Invalid entry")
                continue

            intel = int(input("What did you roll for Intelligence? "))
            if intel < 2:
                abilityScore["Intelligence"] = (intel, "Modifier: ",-5)
                thismodule.iMod = -5
            elif intel <= 3: 
                abilityScore["Intelligence"] = (intel, "Modifier: ",-4)
                thismodule.iMod = -4
            elif intel <= 5:
                abilityScore["Intelligence"] = (intel, "Modifer: ",-3)
                thismodule.iMod = -3
            elif intel <= 7:
                abilityScore["Intelligence"] = (intel, "Modifier: ",-2)
                thismodule.iMod = -2
            elif intel <= 9:
                abilityScore["Intelligence"] = (intel, "Modifier: ",-1)
                thismodule.iMod = -1
            elif intel <= 11:
                abilityScore["Intelligence"] = (intel, "Modifier: ",0)
                thismodule.iMod = 0
            elif intel <= 13:
                abilityScore["Intelligence"] = (intel, "Modifier: ",1)
                thismodule.iMod = 1
            elif intel <= 15:
                abilityScore["Intelligence"] = (intel, "Modifier: ",2)
                thismodule.iMod = 2
            elif intel <= 17:
                abilityScore["Intelligence"] = (intel, "Modifier: ",3)
                thismodule.iMod = 3
            else:
                print("Invalid entry")
                continue

            wis = int(input("What did you roll for Wisdom? "))
            if wis < 2:
                abilityScore["Wisdom"] = (wis, "Modifier: ",-5)
                thismodule.wMod = -5
            elif wis <= 3: 
                abilityScore["Wisdom"] = (wis, "Modifier: ",-4)
                thismodule.wMod = -4
            elif wis <= 5:
                abilityScore["Wisdom"] = (wis, "Modifer: ",-3)
                thismodule.wMod = -3
            elif wis <= 7:
                abilityScore["Wisdom"] = (wis, "Modifier: ",-2)
                thismodule.wMod = -2
            elif wis <= 9:
                abilityScore["Wisdom"] = (wis, "Modifier: ",-1)
                thismodule.wMod = -1
            elif wis <= 11:
                abilityScore["Wisdom"] = (wis, "Modifier: ",0)
                thismodule.wMod = 0
            elif wis <= 13:
                abilityScore["Wisdom"] = (wis, "Modifier: ",1)
                thismodule.wMod = 1
            elif wis <= 15:
                abilityScore["Wisdom"] = (wis, "Modifier: ",2)
                thismodule.wMod = 2
            elif wis <= 17:
                abilityScore["Wisdom"] = (wis, "Modifier: ",3)
                thismodule.wMod = 3
            else:
                print("Invalid entry")
                continue

            cha = int(input("What did you roll for Charisma? "))
            if cha < 2:
                abilityScore["Charisma"] = (cha, "Modifier: ",-5)
                thismodule.chMod = -5
            elif cha <= 3: 
                abilityScore["Charisma"] = (cha, "Modifier: ",-4)
                thismodule.chMod = -4
            elif cha <= 5:
                abilityScore["Charisma"] = (cha, "Modifer: ",-3)
                thismodule.chMod = -3
            elif cha <= 7:
                abilityScore["Charisma"] = (cha, "Modifier: ",-2)
                thismodule.chMod = -2
            elif cha <= 9:
                abilityScore["Charisma"] = (cha, "Modifier: ",-1)
                thismodule.chMod = -1
            elif cha <= 11:
                abilityScore["Charisma"] = (cha, "Modifier: ",0)
                thismodule.chMod = 0
            elif cha <= 13:
                abilityScore["Charisma"] = (cha, "Modifier: ",1)
                thismodule.chMod = 1
            elif cha <= 15:
                abilityScore["Charisma"] = (cha, "Modifier: ",2)
                thismodule.chMod = 2
            elif cha <= 17:
                abilityScore["Charisma"] = (cha, "Modifier: ",3)
                thismodule.chMod = 3
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

#adds items to the Items dictionary
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
        print("No items added \n")
        saveStuff()
        for key, val in Items.items():
            print("You have " + val + " " + key +"\n")
    else:
        print("invalid")
        addStuff()

#saves the character the user created when invoked      
def saveCharacter():
    f = open("Character.txt", "a")
    f.write( str(_Character) + "\n" )
    f.close()

#reads the Character.txt file 
def readSavedCharacter():
    f = open("Character.txt", "r")
    print(f.read())

#saves items to the Items dictionary
def saveStuff():
      f = open("stuff.txt", "a")
      f.write( str(Items) + "\n")
      f.close()

#self explanitory
def saveAbilityScore():
    f = open("ability.txt","a")
    f.write( str(abilityScore) + "\n")
    f.close()


def saveSaveThrows():
    f = open("Saving Throws.txt","a")
    f.write( str(savingThrows) + "\n")
    f.close()


def readSaveThrows():
    f.open("Saving Throws.txt", "r")
    print(f.read())
 
#deletes all information on every text file when invoked!!
def clearAllCharacters():
    f = open("Character.txt", "w").close()
    f = open("stuff.txt", "w").close()
    f = open("ability.txt", "w").close()
    f = open("Saving Throws.txt", "w").close()

#calculates the proficiency bonus based on inputed level
def proBo(level):
    if 1 <  level <= 4:
        abilityScore["Proficiency Bonus"] = 2
    elif 5 < level <=9:
        abilityScore["Proficiency Bonus"] = 3
    elif 9 < level <=13:
        abilityScore["Proficiency Bonus"] = 4
    elif 13 < level <=17:
        abilityScore["Proficiency Bonus"] = 5
    elif 17 < level <=21:
        abilityScore["Proficiency Bonus"] = 6


def _Logo():
    print("""
    ██████╗ ███╗   ██╗██████╗                                                
    ██╔══██╗████╗  ██║██╔══██╗                                               
    ██║  ██║██╔██╗ ██║██║  ██║                                               
    ██║  ██║██║╚██╗██║██║  ██║                                               
    ██████╔╝██║ ╚████║██████╔╝                                               
    ╚═════╝ ╚═╝  ╚═══╝╚═════╝                                                
     ██████╗██╗  ██╗ █████╗ ██████╗  █████╗  ██████╗████████╗███████╗██████╗ 
    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
    ██║     ███████║███████║██████╔╝███████║██║        ██║   █████╗  ██████╔╝
    ██║     ██╔══██║██╔══██║██╔══██╗██╔══██║██║        ██║   ██╔══╝  ██╔══██╗
    ╚██████╗██║  ██║██║  ██║██║  ██║██║  ██║╚██████╗   ██║   ███████╗██║  ██║
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
     ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗                
    ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗               
    ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝               
    ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗               
    ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║               
     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝               
    """)

#calculates what your saving throw will be based off of ur level and class
def calcSaveThrow(): #TODO update the if statements when constitution and charisma are updated in updateClass()
    savingThrows["Saving Strength"] = sMod
    savingThrows["Saving Dexterity"] = dMod
    savingThrows["Saving Constitution"] = cMod
    savingThrows["Saving Intelligence"] = iMod
    savingThrows["Saving Wisdom"] = wMod
    savingThrows["Saving Charisma"] = chMod

    if save == ("s","c"):
        savingThrows["Saving Strength"] = sMod + abilityScore.get("Proficiency Bonus")
        savingThrows["Saving Constitution"] = cMod + abilityScore.get("Proficiency Bonus")
    elif save == ("d","c"):
        savingThrows["Saving Dexterity"] = dMod + abilityScore.get("Proficiency Bonus")
        savingThrows["Saving Charisma"] = chMod + abilityScore.get("Proficiency Bonus")
    elif save == ("w","c"):
        savingThrows["Saving Wisdom"] = wMod + abilityScore.get("Proficiency Bonus")
        savingThrows["Saving Charisma"] = chMod + abilityScore.get("Proficiency Bonus")
    elif save == ("i","w"):
        savingThrows["Saving Intelligence"] = iMod + abilityScore.get("Proficiency Bonus")
        savingThrows["Saving Wisdom"] = wMod + abilityScore.get("Proficiency Bonus")
    elif save == ("s","d"):
        savingThrows["Saving Strength"] = sMod + abilityScore.get("Proficiency Bonus")
        savingThrows["Saving Dexterity"] = dMod + abilityScore.get("Proficiency Bonus")
    elif save == ("d","i"):
        savingThrows["Saving Dexterity"] = dMod + abilityScore.get("Proficiency Bonus")
        savingThrows["Saving Intelligence"] = iMod + abilityScore.get("Proficiency Bonus")
    elif save == ("c","c"):
        savingThrows["Saving Constitution"] = cMod + abilityScore.get("Proficiency Bonus")
        savingThrows["Saving Charisma"] = chMod + abilityScore.get("Proficiency Bonus")
    elif save == ("c","i"):
        savingThrows["Saving Constitution"] = cMod + abilityScore.get("Proficiency Bonus")
        savingThrows["Saving Intelligence"] = iMod + abilityScore.get("Proficiency Bonus")

def calcSkills(): #calculates the skill table
    skillz = {"Acrobatics(Dex)":dMod,"Animal Handling(Wis)":wMod,"Arcana(Int)":iMod,"Athletics(Str)":sMod,"Deception(Cha)":chMod,"History(Int)":iMod,"Insight(Wis)":wMod,
    "Intimidation(Cha)":chMod,"Investigation(Int)":iMod,"Medicine(Wis)":wMod,"Nature(Int)":iMod,"Perception(Wis)":wMod,"Persuasion(Cha)":chMod,"Religion(Int)":iMod,
    "Sleight of Hand(Dex)":dMod,"Stealth(Dex)":dMod,"Survival(Wis)":wMod}

    if save == ("s","ch"):
        skillz.update({"Athletics(Str)":sMod + abilityScore.get("Proficiency Bonus"),"Deception(Cha)":chMod + abilityScore.get("Proficiency Bonus"),"Intimidation(Cha)":chMod + abilityScore.get("Proficiency Bonus"),"Persuasion(Cha)":chMod + abilityScore.get("Proficiency Bonus")})
    elif save == ("d","ch"):
        skillz.update({"Acrobatics(Dex)":dMod + abilityScore.get("Proficiency Bonus"),"Sleight of Hand(Dex)":dMod + abilityScore.get("Proficiency Bonus"),"Stealth(Dex)":dMod + abilityScore.get("Proficiency Bonus"),"Deception(Cha)":chMod + abilityScore.get("Proficiency Bonus"),
        "Intimidation(Cha)":chMod + abilityScore.get("Proficiency Bonus"),"Persuasion(Cha)":chMod + abilityScore.get("Proficiency Bonus")})
    elif save == ("w","ch"):
        #TODO finish calcSkills after save has been udated to specify between constitution and charisma
#==========FUNCTIONS==========#

#==========RUN PROGRAM==========#
# _MakeACharacter()
#==========RUN PROGRAM==========#

#++++++++++TEST SPACE++++++++++#
# updateAlignment()
# print(skillz)
calcSkills()
#++++++++++TEST SPACE++++++++++#

