import copy 

class ICloneable:
    def shallowClone(self):
        return copy.copy(self)
    
    def deepClone(self):
        return copy.deepcopy(self)
    

class WorkExperience(ICloneable):
    workData=""
    company=""

class Resume(ICloneable):
    name=""
    sex=""
    age=0
    work=None 

    def __init__(self,name):
        self.name=name 
        self.work=WorkExperience()

    
    def setPersonInfo(self,sex,age):
        self.sex=sex 
        self.age=age 
    
    def setWorkExperience(self,workData,company):
        self.work.workData=workData 
        self.work.company=company 
    
    def display(self):
        print('%s, %s, %d' % (self.name,self.sex,self.age)) 
        print('%s, %s' % (self.work.workData, self.work.company))


def main():
    sak=Resume("SyedAwase")
    sak.setPersonInfo("m",36)
    sak.setWorkExperience("2000-2015","tpri.com")

    aicy=sak.shallowClone()
    aicy.setWorkExperience("2000-2013","sycliq.com")

    rayyan=sak.deepClone()
    rayyan.setWorkExperience("2000-2016","cliniqone.com")

    sak.display()
    aicy.display()
    rayyan.display()
    return

if __name__=="__main__":
    main()

