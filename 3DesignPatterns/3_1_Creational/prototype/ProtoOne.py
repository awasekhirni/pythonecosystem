#Prototype design pattern helps to hide the complexity of the instances created by the class.

import copy 

class Prototype:
    _type=None 
    _value=None 

    def clone(self):
        print("clone rendered")
    def getType(self):
        return self._type 
    
    def getValue(self):
        return self._value 

class Category1(Prototype):
    def __init__(self,number):
        self._type="Category 1"
        self._value=number 
    
    def clone(self):
        return copy.copy(self)


class Category2(Prototype):
    """Concrete Prototype""" 
    def __init__(self,number):
        self._type="Category2"
        self._value= number 
    
    def clone(self):
        return copy.copy(self)
    
class ObjectFactory:
    __type1Value1=None 
    __type2Value2=None 
    __type2Value1=None 
    __type2Value2=None 

    @staticmethod 
    def initialize():
        ObjectFactory.__type1Value1=Category1(1)
        ObjectFactory.__type1Value2=Category1(2)
        ObjectFactory.__type2Value1=Category2(3)
        ObjectFactory.__type2Value2=Category2(4)
    
    @staticmethod 
    def getType1Value1():
        return ObjectFactory.__type1Value1.clone()
    
    @staticmethod 
    def getType1Value2():
        return ObjectFactory.__type1Value2.clone()
    
    @staticmethod 
    def getType2Value1():
        return ObjectFactory.__type2Value1.clone()
    
    @staticmethod 
    def getType2Value2():
        return ObjectFactory.__type2Value2.clone()


def main():
    ObjectFactory.initialize()

    instance=ObjectFactory.getType1Value1()
    print("%s:%s" % (instance.getType(),instance.getValue()))

    instance2=ObjectFactory.getType1Value2()
    print("%s:%s" % (instance2.getType(),instance2.getValue()))

    instance3=ObjectFactory.getType2Value1()
    print("%s:%s" % (instance3.getType(),instance3.getValue()))

    instance4=ObjectFactory.getType2Value2()
    print("%s:%s" % (instance4.getType(),instance4.getValue()))



if __name__=="__main__":
    main()
