class Singleton:
    __instance=None 

    @staticmethod 
    def getInstance():
        """static access method."""
        if Singleton.__instance==None:
            Singleton()
        return Singleton.__instance 
    
    def __init__(self):
        """virtually private constructor"""
        if Singleton.__instance!=None:
            raise Exception("This class is a Singleton")
        else:
            Singleton.__instance=self
        

if __name__=="__main__":
    bachelor=Singleton()
    #kamel=Singleton()
    print(bachelor)
    #print(kamel)
    print(bachelor.getInstance())