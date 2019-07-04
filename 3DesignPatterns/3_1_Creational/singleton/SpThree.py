
def singleton(cls):
    instances={}
    def getInstance(anyArgs=None):
        if cls not in instances:
            instances[cls]=cls(anyArgs)
        return instances[cls]
    return getInstance


@singleton 
class MyClass:
    def __init__(self,count=None):
        print("print argument if any exists",count)
    
    def test(self,counter):
        print("--->",counter)
        return counter 
    

if __name__=="__main__":
    one = MyClass(12381322)
    one.test(1)
    two=MyClass(137467367)
    two.test(2)
    if one!=two:
        print("this is not a singleton object")
    else: 
        print("this is a singleton object")