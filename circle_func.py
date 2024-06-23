import math as m

class circle:
    def area(r):
        return m.pi*r**2
    def perimeter(r):
        return 2*m.pi*r
    
obj = circle
print("area : ",obj.area(4))
print("perimeter : ",obj.perimeter(2))