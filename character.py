import linecache as line

class Character:
    def lookUpCharacter(self):
        while True:
            num = input("Which character do you want to see? ")
            if num.isdigit():
                if line.getline("Character.txt", int(num)).strip():
                    print(line.getline("Character.txt", int(num)))
                    print(line.getline("stuff.txt", int(num)))
                    print(line.getline("ability.txt", int(num)))
                    print(line.getline("Saving Throws.txt", int(num)))
                    print(line.getline("skills.txt",int(num)))
                    break
                else:
                    stop = input("\nCharacter does not exist! Continue? Y/N ")
                    if stop.capitalize() == 'Y':
                        continue
                    elif stop.capitalize() == 'N':
                        break
                    else:
                        print("Invalid choice")
                        break
            else:
                print("\nMust be a number!\n")
                continue

    def playerName(self):
        name = input("What is your IRL name? ").capitalize()
        return name
    
    def fName(self):
        fname = input("\nWhat is your character's first name? ")
        return fname
    
    def lName(self):
        lname = input("\nWhat is you character's last name? ")
        return lname


