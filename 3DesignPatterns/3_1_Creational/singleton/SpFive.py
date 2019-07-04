#decorator, modyfies new_cls
def _singleton(new_cls):
    instance = new_cls()                                              #2
    def new(cls):
        if isinstance(instance, cls):                                 #5
            return instance
        else:
            raise TypeError("I can only return instance of {}, caller wanted {}".format(new_cls, cls))
    new_cls.__new__  = new                                            #3
    new_cls.__init__ = lambda self: None                              #4
    return new_cls


#decorator, creates new class
def singleton(cls):
    new_cls = type('singleton({})'.format(cls.__name__), (cls,), {} ) #1
    return _singleton(new_cls)


#metaclass
def meta_singleton(name, bases, attrs):
    new_cls = type(name, bases, attrs)        #1
    return _singleton(new_cls)


#tests
if __name__=='__main__':
    def val(expr):
        print('{}: {}'.format(expr, eval(expr)))
    class Base:
        def __init__(self):
            print("{}'s instance created".format(type(self).__name__))
    @singleton
    class Singleton(Base):
        print("Singleton base")
    val('Singleton() is Singleton()')
    class MetaSingleton(Base, metaclass=meta_singleton):
        print("MetaSingleton")
    val('MetaSingleton() is MetaSingleton()')
    class Derived(Singleton):
        print("Derived Singleton ")
    #Derived() #fails
    class MetaDerived(Singleton):
        print("MetaDerived Singleton ")
    #MetaDerived() #fails