
from copy import deepcopy

class Prototype(object):
    def clone(self):
        return deepcopy(self)


class ConcretePrototype1(Prototype):
    def __init__(self):
        self.name="Syed Awase"

class ConcretePrototype2(Prototype):
    def __init__(self):
        self.name="Syed Ameese"

def main():
    sak=ConcretePrototype1()
    sas=ConcretePrototype2()
    aicy=sak.clone()
    munna=sas.clone()
    print("SAK--", sak,aicy)
    print("SAS--",sas,munna)


if __name__=="__main__":
    main()