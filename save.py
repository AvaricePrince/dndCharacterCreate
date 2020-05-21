class Save:
    def saveThing(self,name,dict):
        f = open(name + ".txt","a")
        f.write( str(dict) + "\n")
        f.close()