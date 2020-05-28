class Save:
    def saveDict(self,name,dict):
        f = open(name + ".txt","a")
        f.write( str(dict) + "\n")
        f.close()
    def saveList(self,name,list):
        f = open(name + ".txt","a")
        f.write( str(list) + "\n")
        f.close()

