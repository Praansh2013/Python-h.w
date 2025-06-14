class fruit:
    def __init__(self,apple,banana):
        self.apple=apple
        self.banana=banana
f=fruit("Apple","Banana")
print("My fruit favourite is ",f.banana)

# Circle
class circle:
    def __init__(self,ra):
        self.ra=ra

    def area(self):
         return 3.14*self.ra**2
    
    def peri(self):
        return 2*3.14*self.ra
# 3.14=pie


ra=int(input("Enter the radius of the circle: "))
r=circle(ra)

print("Area of a rectangle with the radius",r.ra,"cm Is: ",r.area(),"cm square")
print("Perimeter of a rectangle with the radius",r.ra,"cm Is: ",r.peri(),"cm square")