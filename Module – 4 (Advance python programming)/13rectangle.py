#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def rect(self,length,width):
        self.l=length
        self.w=width
    def area(self):
        print("Area of rectangle is: ",self.l*self.w)

a=Rectangle()
a.rect(30,40)
a.area()
