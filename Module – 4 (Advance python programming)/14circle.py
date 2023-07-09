#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

class Circle:
    
    def cir(self,radius):
        self.r=radius
    def area(self):
        print("Area of circle: ",self.r**2*3.14)
    def perimeter(self):
        print("Perimeter of circle: ",2*3.14*self.r)


a=Circle()
a.cir(4)
a.area()
a.perimeter()


