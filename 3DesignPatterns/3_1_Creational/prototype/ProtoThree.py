import sys
import copy

class Point:
    __slots__=("x","y")
    def __init__(self,x,y):
        self.x=x
        self.y=y 
    

def create_object(Class,*args,**kwargs):
    return Class(*args,**kwargs)


def main():
    point1=Point(1,2)
    point2 = eval("{}({}, {})".format("Point", 2, 4)) # Risky
    point3 = getattr(sys.modules[__name__], "Point")(3, 6)
    point4 = globals()["Point"](4, 8)
    print("globals", point4)
    point5 = create_object(Point, 5, 10)
    point6 = copy.deepcopy(point5)
    print("after deepcopy", point6.x, point6.y)
    point6.x = 6
    point6.y = 12
    point7 = point1.__class__(7, 14)
    print("point1:",point1.x, point1.y)
    print("point2",point2)
    print("point3",point3)
    print("point4",point4)
    print("point5",point5.x,point5.y)
    print("point6",point6.x, point6.y)
    print("point7",point7.x,point7.y)



if __name__=="__main__":
    main()