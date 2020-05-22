class Language:
    def talk(self,key):
        race = {1:("Common","Draconic"),2:("Common",'Dwarvish'),3:("Common",'Elvish'),4:("Common",'Gnomish'),5:("Common","Elvish",""),6:("Common","Halfling"),7:("Common","Orc"),8:("Common",""),9:("Common","Infernal"),
            10:("Common","Orc",""),11:("Common","Arakocra"),12:("Common","Primordial"),13:("Common","Gol-Kaa",""),14:("Common","Celestial"),15:("Common","Goblin"),16:("Common","Elvish",'Giant'),17:("Common","Goblin"),18:("Common","Goblin"),19:("Common","Auran"),
            20:("Common","Draconic"),21:("Common","Draconic"),22:("Common","Orc",""),23:("Common",""),24:("Aquan","Common","Primordial"),25:("Common","Abyssal","Draconic"),26:("Common","Infernal"),27:("Common","Aquan"),
            28:("Common",""),29:("Common","Quori",""),30:("Common","Orc"),31:("Common"),32:("Common"),33:("Common","Gith"),34:("Sylvan",'Elven'),35:("Common","Loxodon"),36:("Common"),37:("Common","Elven"),38:("Common","Vedalken",""),
            39:("Common","Goblin"),40:("Common","Aquan"),41:("Grung")}
        
        return race.get(key)