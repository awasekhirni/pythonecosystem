class TestSingleton:
    """create a class variable that will hold a reference """
    instance=None 

    #define a helper class that will override the __calll__ 
    class TestSingletonHelper:
        def __call__(self,*args,**kwargs):
            if TestSingleton.instance is None:
                object =TestSingleton()
                TestSingleton.instance=object

                return TestSingleton.instance 
    
    getInstance=TestSingletonHelper()

    def __init__(self):
        if not TestSingleton.instance==None:
            raise RuntimeError



if __name__=="__main__":
    for i in range(10):
        print(TestSingleton.getInstance())