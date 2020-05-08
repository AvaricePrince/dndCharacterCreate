"""

"""

import linecache as line
import sys
thismodule = sys.modules[__name__]


#==========DICTIONARIES==========#
_Character = {"pname":"", "fname":"", "lname":"","level":"", "race":"", "class":"", "alignment":"","background":""}
Items = {}
abilityScore = {"Strength":"", "Dexterity":"", "Constitution":"", "Intelligence":"", "Wisdom":"", "Charisma":"", "Proficiency Bonus":""}
savingThrows = {"Saving Strength":"", "Saving Dexterity":"", "Saving Constitution":"", "Saving Intelligence":"", "Saving Wisdom":"", "Saving Charisma":""}
#==========DICTIONARIES==========#

#-----------GLOBAL VARIABLES--------#
thismodule.save = "",""
thismodule.sMod = ""
thismodule.dMod = ""
thismodule.cMod = ""
thismodule.iMod = ""
thismodule.wMod = ""
thismodule.chMod = ""
#-----------GLOBAL VARIABLES--------#

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
    # race = input("What is your race? ").capitalize()
    # _Character["race"] = race
    # print("You are a " + race)
    print("""
    --Select a Race--\n
    1: Dragonborn\n
    2: Dwarf\n
    3: Elf\n
    4: Gnome\n
    5: Half-Elf\n
    6: Halfling\n
    7: Half-Orc\n
    8: Human\n
    9: Tiefling\n
    """)
    print("*Explorer's Guide to Wildemount*\n")
    print("""
    0: Orc of Exandria\n""")
    print("*Elemental Evil Player's Companion*\n")
    print("""
    11: Aarakocra\n
    12: Genasi\n
    13: Goliath\n
    """)
    print("*Volo's Guide to Monsters*")
    print("""
    14: Aasimar\n
    15: Bugbear\n
    16: Firblog\n
    17: Goblin\n
    18: Hobgoblin\n
    19: Kenku\n
    20: Kobold\n
    21: Lizardfolk\n
    22: Orc\n
    23: Tabaxi\n
    24: Triton\n
    25: Yuan-ti Pureblood\n
    """)
    print("*Sword Coast Adventurer's Guide*\n")
    print("""
    26: Feral Tiefling\n
    """)
    print("""
    **The Tortle Package**\n
    27: Tortle\n
    *Eberron: Rising from the Last War*\n
    28: Changeling\n
    29: Kalashtar\n
    30: Orc of Eberron\n
    31: Shifter\n
    32: Warforged\n
    **Mordenkainen's Tome of Foes**\n
    33: Gith\n
    **Guildmasters' Guide to Ravnica**\n
    34: Centaur\n
    35: Loxodon\n
    36: Minotaur\n
    37: Simic Hybrid\n
    38: Vedalken\n
    **Acquisitions Incorporated**\n
    39: Verdan\n
    **Locathah Rising**\n
    40: Locathah\n
    **One Grung Above**\n
    41: Grung\n
    """)
    while True:
        try:
            choice = int(input("Choose your race: "))
            if choice == 1:
                _Character["race"] = "Dragonborn"
                print("You are a Dragonborn\n")
                break
            elif choice == 2:
                _Character["race"] = "Dwarf"
                print("You are a Dwarf\n")
                break
            elif choice == 3:
                _Character["race"] = "Elf"
                print("You are a Elf\n")
                break
            elif choice == 4:
                _Character["race"] = "Gnome"
                print("You are a Gnome\n")
                break
            elif choice == 5:
                _Character["race"] = "Half-Elf"
                print("You are a Half-Elf\n")
                break
            elif choice == 6:
                _Character["race"] = "Halfling"
                print("You are a Halfling\n")
                break
            elif choice == 7:
                _Character["race"] = "Half-Orc"
                print("You are a Half-Orc\n")
                break
            elif choice == 8:
                _Character["race"] = "Human"
                print("You are a Human\n")
                break
            elif choice == 9:
                _Character["race"] = "Tiefling"
                print("You are a Tiefling\n")
                break
            elif choice == 0:
                _Character["race"] = "Orc of Exandria"
                print("You are an Orc of Exandria\n")
                break
            elif choice == 11:
                _Character["race"] = "Aarakocra"
                print("You are a Aarakocra\n")
                break
            elif choice == 12:
                _Character["race"] = "Genasi"
                print("You are a Genasi\n")
                break
            elif choice == 13:
                _Character["race"] = "Goliath"
                print("You are a Goliath\n")
                break
            elif choice == 14:
                _Character["race"] = "Aasimar"
                print("You are a Aasimar\n")
                break
            elif choice == 15:
                _Character["race"] = "Bugbear"
                print("You are a Bugbear\n")
                break
            elif choice == 16:
                _Character["race"] = "Firblog"
                print("You are a Firblog\n")
                break
            elif choice == 17:
                _Character["race"] = "Goblin"
                print("You are a Goblin\n")
                break
            elif choice == 18:
                _Character["race"] = "Hobgoblin"
                print("You are a Hobgoblin\n")
                break
            elif choice == 19:
                _Character["race"] = "Kenku"
                print("You are a Kenku\n")
                break
            elif choice == 20:
                _Character["race"] = "Kobold"
                print("You are a Kobold\n")
                break
            elif choice == 21:
                _Character["race"] = "Lizardfolk"
                print("You are a Lizardfolk\n")
                break
            elif choice == 22:
                _Character["race"] = "Orc"
                print("You are a Orc\n")
                break
            elif choice == 23:
                _Character["race"] = "Tabaxi"
                print("You are a Tabaxi\n")
                break
            elif choice == 24:
                _Character["race"] = "Triton"
                print("You are a Triton\n")
                break
            elif choice == 25:
                _Character["race"] = "Yuan-ti Pureblood"
                print("You are a Yuan-ti Pureblood\n")
                break
            elif choice == 26:
                _Character["race"] = "Feral Tiefling"
                print("You are a Feral Tiefling\n")
                break
            elif choice == 27:
                _Character["race"] = "Tortle"
                print("You are a Tortle\n")
                break
            elif choice == 28:
                _Character["race"] = "Changeling"
                print("You are a Changeling\n")
                break
            elif choice == 29:
                _Character["race"] = "Kalashtar"
                print("You are a Kalashtar\n")
                break
            elif choice == 30:
                _Character["race"] = "Orc of Eberron"
                print("You are an Orc of Eberron\n")
                break
            elif choice == 31:
                _Character["race"] = "Shifter"
                print("You are a Shifter\n")
                break
            elif choice == 32:
                _Character["race"] = "Warforged"
                print("You are a Warforged\n")
                break
            elif choice == 33:
                _Character["race"] = "Gith"
                print("You are a Gith\n")
                break
            elif choice == 34:
                _Character["race"] = "Centaur"
                print("You are a Centaur\n")
                break
            elif choice == 35:
                _Character["race"] = "Loxodon"
                print("You are a Loxodon\n")
                break
            elif choice == 36:
                _Character["race"] = "Minotaur"
                print("You are a Minotaur\n")
                break
            elif choice == 37:
                _Character["race"] = "Simic Hybrid"
                print("You are a Simic Hybrid\n")
                break
            elif choice == 38:
                _Character["race"] = "Vedalken"
                print("You are a Vedalken\n")
                break
            elif choice == 39:
                _Character["race"] = "Verdan"
                print("You are a Verdan\n")
                break
            elif choice == 40:
                _Character["race"] = "Locathah"
                print("You are a Locathah\n")
                break
            elif choice == 41:
                _Character["race"] = "Grung"
                print("You are a Grung\n")
                break
            else:
                print("No race selected\n")
                continue
        except ValueError:
            print("Invalid, must be a number\n")
            continue

def updateClass():
    _class = {"\n-----SELECT A CLASS-----":"", 1:"Barbarian", 2:"Bard",3:"Cleric",4: "Druid",5: "Fighter",
    6: "Monk",7:"Paladin",8:"Ranger",9:"Rogue",10:"Sorcerer",11:"Warlock",12:"Wizard",
    "***Eberron: Rising from the Last War***":"",13:"Artificer","***Critical Role***":"",14:"Blood Hunter"}
    for key in _class:
        print(str(key) + ":", _class[key],"\n")
    # for i in critClss:
    #     print(i)
    # print("""---SELECT A CLASS---
    # 1: Barbarian\n
    # 2: Bard\n
    # 3: Cleric\n
    # 4: Druid\n
    # 5: Fighter\n
    # 6: Monk\n
    # 7: Paladin\n
    # 8: Ranger\n
    # 9: Rogue\n
    # 0: Sorcerer\n
    # 11: Warlock\n
    # 12: Wizard\n
    # ***Eberron: Rising from the Last War***\n
    # 13: Artificer\n 
    # ***Critical Role***\n
    # 14: Blood Hunter\n
    # """)
    while True:
        try:
            choice = int(input("Pick a Class: "))
            _Character["class"] = _class.get(choice,"Invalid\n")
            print("\nYou are a:",_Character.get("class"))
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




            # if _class[choice]:
            #     _Character["class"] = "Barbarian"
            #     print("\n" + "You are a Barbarian\n")
            #     thismodule.save = "s","c"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Bard"
            #     print("You are a Bard\n")
            #     thismodule.save = "d","c"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Cleric"
            #     print("You are a Cleric\n")
            #     thismodule.save = "w","c"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Druid"
            #     print("You are a Druid\n")
            #     thismodule.save = "i","w"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Fighter"
            #     print("You are a Fighter\n")
            #     thismodule.save = "s","c"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Monk"
            #     print("You are a Monk\n")
            #     thismodule.save = "s","d"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Paladin"
            #     print("You are a Paladin\n")
            #     thismodule.save = "w","c"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Ranger"
            #     print("You are a Ranger\n")
            #     thismodule.save = "s","d"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Rogue"
            #     print("You are a Rogue\n")
            #     thismodule.save = "d","i"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Sorcerer"
            #     print("You are a Sorcerer\n")
            #     thismodule.save = "c","c"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Warlock"
            #     print("You are a Warlock\n")
            #     thismodule.save = "w","c"
            #     break
            # elif _class[choice]:
            #     _Character["class"] = "Wizard"
            #     print("You are a Wizard\n")
            #     thismodule.save = "i","w"
            #     break
            # elif _class[choice+1]:
            #     _Character["class"] = "Artificer"
            #     print("You are a Artificer\n")
            #     thismodule.save = "c","i"
            #     break
            # elif choice == 14:
            #     _Character["class"] = "Blood Hunter"
            #     print("You are a Artificer\n")
            #     thismodule.save = "d","i"
            #     break
            # else:
            #     print("Class does not exist\n")
            #     continue

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
    # align = input("What is your alignment? ").capitalize()
    # _Character["alignment"] = align
    # print("Okay, your alignment is: " + align)
    while True:
        print("---Select your alignment--- \n")
        print("1: Lawful Good \n")
        print("2: Neutral Good \n")
        print("3: Chaotic Good \n")
        print("4: Lawful Neutral \n")
        print("5: True Neutral \n")
        print("6: Chaotic Neutral \n")
        print("7: Lawful Evil \n")
        print("8: Neutral Evil \n")
        print("9: Chaotic Evil \n")
        print("0: Unaligned \n")
        align = int(input("Choose your alignment: "))
        if align == 1:
            _Character["alignment"] = "Lawful good"
            print("Okay, you're Lawful good \n")
            break
        elif align == 2:
            _Character["alignment"] = "Neutral Good"
            print("Okay, you're Neutral good \n")
            break
        elif align == 3:
            _Character["alignment"] = "Chaotic Good"
            print("Okay, you're Chaotic good \n")
            break
        elif align == 4:
            _Character["alignment"] = "Lawful Neutral"
            print("Okay, you're Lawful Neutral \n")
            break
        elif align == 5:
            _Character["alignment"] = "True Neutral"
            print("Okay, you're True Neutral \n")
            break
        elif align == 6:
            _Character["alignment"] = "Chaotic Neutral"
            print("Okay, you're Chaotic Neutral \n")
            break
        elif align == 7:
            _Character["alignment"] = "Lawful Evil"
            print("Okay, you're Lawful Evil \n")
            break
        elif align == 8:
            _Character["alignment"] = "Neutral Evil"
            print("Okay, you're Neutral Evil \n")
            break
        elif align == 9:
            _Character["alignment"] = "Chaotic Evil"
            print("Okay, you're Chaotic Evil \n")
            break
        elif align == 0:
            _Character["alignment"] = "Unaligned"
            print("Okay, you're Unaligned \n")
            break
        else:
            print("Invalid choice, try again\n")
            continue

#allows user to input their characters background
def updateBackground():
    bg = input("What is your background? ").capitalize()
    _Character["background"] = bg
    print("Your background is: " + bg + "\n")

#allows user to input their ability scores
def updateAbilityScore():
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
def calcSaveThrow():
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
#==========FUNCTIONS==========#

#==========RUN PROGRAM==========#
# _MakeACharacter()
#==========RUN PROGRAM==========#
updateClass()