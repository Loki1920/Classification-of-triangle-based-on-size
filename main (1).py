# classification  of Triangle based on side
import math
class Triangle():
    def __init__(self,a,b,c):
        self.a =a
        self.b=b
        self.c=c
    def Is_valid(self):
        if a+b>c and a+c>b and b+c>a:
            return "Valid"
        else:
            return "Invalid"
    
    def Side_Classification(self):
        if Triangle.Is_valid(self)=="Valid":
            
            if a==b==c:
                return "Equilateral"
            elif a==b!=c or a==c!=b or b==c!=a:
                return "Isosceles"
            elif a!=b!=c:
                return "Scalene"
        else:
            return "Invalid"
    def Angle_Classification(self):
        if Triangle.Is_valid(self)=="Valid":
            
            if a*a+b*b>c*c:
                return "Acute"
            elif a*a+b*b==c*c:
                return "Right"
            elif a*a+b*b<c*c:
                return "Obtuse"
        else:
            return "Invalid"
    def Area(self):
        if Triangle.Is_valid(self)=="Valid":
            
            s = (a+b+c)/2
            return math.sqrt(s*(s-a)*(s-b)*(s-c))
        else:
            return "Invalid"


a=int(input("enter side1:"))
b=int(input("enter side2:"))
c=int(input("enter side3:"))
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print("Area :",T.Area())