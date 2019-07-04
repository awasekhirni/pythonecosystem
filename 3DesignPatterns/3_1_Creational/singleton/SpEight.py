#thread safe implementation of singleton
import threading

class MySingletonClass(object):
    
    __lockObj=threading.Lock() #thread locking
    __instance=None #the unique instance

    def __new__(cls,*args,**kwargs):
        return cls.getInstance(cls,*args,**kwargs)

    
    def __init__(self):
        print("initialization method called")

    
    def getInstance(cls,*args,**kwargs):
        """static method to have a reference to the unique identifier"""
        cls.__lockObj.acquire()
        try:
            if cls.__instance is None: 
                cls.__instance=object.__new__(cls,*args,**kwargs)

        finally:
            cls.__lockObj.release()
    
        return cls.__instance 



if __name__=="__main__":
    print("singleton object demo")