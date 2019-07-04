import copy 

class Prototype:
    def __init__(self):
        self._objects={}
    
    def register_object(self,name,obj):
        self._objects[name]=obj
    
    def unregister_object(self,name):
        del self._objects[name]
        
    
    def clone(self,name,**attr):
        obj=copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj 

    

class WashingMachine:
    def __init__(self):
        self.load="10Kg"
        self.waterinput="35L"
        self.runspeed="75"
        print("Full Capacity in the Washing Machine")

    def __str__(self):
         return '{} | {} | {}'.format(self.load,
                                     self.waterinput,
                                     self.runspeed)



def main():
    lg=WashingMachine()
    print("Original Object={}".format(lg))
    #cloning 
    samsung=Prototype()
    samsung.register_object('smsng',lg)
    smfntldr=samsung.clone('smsng')

    #printing clone 
    print("Cloned Object={}".format(smfntldr))


if __name__=="__main__":
    main()